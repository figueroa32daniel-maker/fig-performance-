/*
 * Fig Performance data store: bookings, leads, settings.
 * Uses the Redis database that Vercel adds from its Storage tab (Upstash). Vercel puts the two
 * settings below into the project by itself when the database is connected; nobody pastes keys.
 *   KV_REST_API_URL / KV_REST_API_TOKEN   (or UPSTASH_REDIS_REST_URL / UPSTASH_REDIS_REST_TOKEN)
 *
 * Keys:
 *   settings            JSON  consult hours, blocked dates, notice, follow-up texts
 *   bk:<id>             JSON  one booking (id doubles as the private "manage my booking" code)
 *   bk:byStart          ZSET  booking ids scored by start time
 *   slot:<startISO>     the booking id holding that time (SET NX = no double bookings)
 *   lead:<+1phone>      JSON  one person: name, status, consent record, follow-up position
 *   clients             JSON  Dan's training clients (his contact list): [{phone, name, note}]
 *   ses:<id>            JSON  one client training session {id, phone, name, start}
 *   ses:byStart         ZSET  session ids scored by start time
 *                       A session holds slot:<startISO> exactly like a consult does, so the
 *                       website can never offer a consult at a time Dan is training someone.
 *   fu:due              ZSET  phones scored by when their next follow-up text is due
 */
"use strict";
const crypto = require("crypto");

const TZ = "America/Los_Angeles";
function url() { return process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL || ""; }
function token() { return process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN || ""; }
function configured() { return !!(url() && token()); }

async function pipeline(cmds) {
  const r = await fetch(url().replace(/\/$/, "") + "/pipeline", {
    method: "POST", headers: { Authorization: "Bearer " + token(), "Content-Type": "application/json" }, body: JSON.stringify(cmds)
  });
  if (!r.ok) throw Object.assign(new Error("db " + r.status), { code: 503 });
  const j = await r.json();
  return j.map(x => { if (x.error) throw Object.assign(new Error("db command failed"), { code: 503 }); return x.result; });
}
async function cmd() { return (await pipeline([Array.prototype.slice.call(arguments)]))[0]; }
async function getJSON(key) { const v = await cmd("GET", key); if (!v) return null; try { return JSON.parse(v); } catch (e) { return null; } }
async function setJSON(key, val) { return cmd("SET", key, JSON.stringify(val)); }
async function getMany(keys) {
  if (!keys.length) return [];
  const v = await cmd.apply(null, ["MGET"].concat(keys));
  return v.map(x => { try { return x ? JSON.parse(x) : null; } catch (e) { return null; } });
}

/* ---------- settings ---------- */
const DAYS = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"];
const DEFAULTS = {
  // No open times until Dan sets them on the inbox Settings tab: better no slots than wrong slots.
  hours: { sun: null, mon: null, tue: null, wed: null, thu: null, fri: null, sat: null },   // e.g. { from: "16:00", to: "19:00" }
  blocked: [],                 // dates off, "YYYY-MM-DD"
  noticeHours: 3,              // earliest bookable time from now
  daysAhead: 14,
  followups: [                 // sent only to people who ticked the optional marketing box
    { day: 2, text: "Hi {first}, Coach Dan at Fig Performance. Good meeting you. Any questions about the plan we talked through? Just reply here. Reply STOP to opt out." },
    { day: 7, text: "Hi {first}, Coach Dan here. Most people I work with say the hardest part is starting. Want me to hold a first session time for you this week? Reply STOP to opt out." },
    { day: 21, text: "Hi {first}, it's Coach Dan at Fig Performance. Still thinking about getting stronger? I have a couple of training spots open. Reply here and I'll set it up. Reply STOP to opt out." },
    { day: 45, text: "Hi {first}, Coach Dan at Fig Performance. Last note from me: if the timing is better now, reply and we'll pick up where we left off. Reply STOP to opt out." }
  ],
  noShowText: "Hi {first}, Coach Dan at Fig Performance. Sorry we missed each other today. Want to pick a new time? Reply here or book at figperformance.com. Reply STOP to opt out."
};
function cleanSettings(s) {
  s = s || {};
  const out = JSON.parse(JSON.stringify(DEFAULTS));
  DAYS.forEach(d => {
    const h = (s.hours || {})[d];
    if (h && /^\d{2}:00$/.test(h.from) && /^\d{2}:00$/.test(h.to) && h.from < h.to) out.hours[d] = { from: h.from, to: h.to };
  });
  if (Array.isArray(s.blocked)) out.blocked = s.blocked.filter(x => /^\d{4}-\d{2}-\d{2}$/.test(x)).slice(0, 200);
  if (Number.isFinite(+s.noticeHours)) out.noticeHours = Math.max(0, Math.min(72, Math.round(+s.noticeHours)));
  if (Number.isFinite(+s.daysAhead)) out.daysAhead = Math.max(1, Math.min(30, Math.round(+s.daysAhead)));
  if (Array.isArray(s.followups)) {
    const f = s.followups.map(x => ({ day: Math.max(1, Math.min(120, Math.round(+x.day || 0))), text: String(x.text || "").trim().slice(0, 600) }))
      .filter(x => x.text).sort((a, b) => a.day - b.day).slice(0, 6);
    out.followups = f.map(withStop);
  }
  if (typeof s.noShowText === "string" && s.noShowText.trim()) out.noShowText = withStop({ text: s.noShowText.trim().slice(0, 600) }).text;
  return out;
}
/* Every marketing text must say who it's from and how to stop. Added back if someone edits it out. */
function withStop(x) {
  let t = x.text;
  if (!/fig performance|coach dan/i.test(t)) t = "Fig Performance: " + t;
  if (!/reply stop/i.test(t)) t = t.replace(/\s*$/, "") + " Reply STOP to opt out.";
  return Object.assign({}, x, { text: t });
}
async function settings() { return cleanSettings(await getJSON("settings")); }

/* ---------- time helpers (Pacific time, daylight saving safe) ---------- */
function dateKey(d) { return new Intl.DateTimeFormat("en-CA", { timeZone: TZ, year: "numeric", month: "2-digit", day: "2-digit" }).format(d); }
function pacificParts(d) {
  const p = {}; new Intl.DateTimeFormat("en-US", { timeZone: TZ, hourCycle: "h23", weekday: "short", hour: "2-digit", minute: "2-digit" }).formatToParts(d).forEach(x => { p[x.type] = x.value; });
  return { dow: p.weekday.toLowerCase().slice(0, 3), hour: +p.hour, minute: +p.minute };
}
function zonedToUtc(dateStr, hhmm) {                 // "2026-11-21", "17:00" in Pacific -> Date
  const guess = new Date(dateStr + "T" + hhmm + ":00Z");
  for (const off of [8, 7]) {
    const d = new Date(guess.getTime() + off * 3600 * 1000), pp = pacificParts(d);
    if (dateKey(d) === dateStr && pp.hour === +hhmm.slice(0, 2)) return d;
  }
  return null;                                       // a time that doesn't exist (spring-forward hour)
}

/* Every time the settings allow from now through daysAhead, before removing taken ones. */
function candidateSlots(s, now) {
  const out = [], earliest = now + s.noticeHours * 3600 * 1000;
  for (let i = 0; i <= s.daysAhead; i++) {
    const day = dateKey(new Date(now + i * 864e5));
    if (s.blocked.indexOf(day) >= 0) continue;
    const dow = pacificParts(new Date(day + "T20:00:00Z")).dow;      // noon-ish Pacific on that date
    const h = s.hours[dow]; if (!h) continue;
    for (let hr = +h.from.slice(0, 2); hr < +h.to.slice(0, 2); hr++) {
      const d = zonedToUtc(day, String(hr).padStart(2, "0") + ":00");
      if (d && d.getTime() >= earliest) out.push(d.toISOString().replace(".000Z", "Z"));
    }
  }
  return out;
}
async function openSlots(now) {
  const s = await settings(), all = candidateSlots(s, now || Date.now());
  if (!all.length) return [];
  const taken = await cmd.apply(null, ["MGET"].concat(all.map(x => "slot:" + x)));
  return all.filter((x, i) => !taken[i]);
}

/* ---------- bookings ---------- */
function newId() { return crypto.randomBytes(18).toString("base64url"); }
async function createBooking(b) {                    // returns the booking, or null if the time was just taken
  const id = newId(), ttl = Math.max(3600, Math.round((Date.parse(b.start) - Date.now()) / 1000) + 86400);
  const got = await cmd("SET", "slot:" + b.start, id, "NX", "EX", String(ttl));
  if (got !== "OK") return null;
  const rec = Object.assign({ id, status: "booked", created: new Date().toISOString() }, b);
  await pipeline([["SET", "bk:" + id, JSON.stringify(rec)], ["ZADD", "bk:byStart", String(Date.parse(b.start)), id]]);
  return rec;
}
async function getBooking(id) { return /^[A-Za-z0-9_-]{20,40}$/.test(String(id || "")) ? getJSON("bk:" + id) : null; }
async function saveBooking(rec) { return setJSON("bk:" + rec.id, rec); }
async function cancelBooking(rec, by) {
  if (rec.status === "cancelled") return rec;
  rec.status = "cancelled"; rec.cancelledBy = by; rec.cancelledAt = new Date().toISOString();
  await pipeline([["SET", "bk:" + rec.id, JSON.stringify(rec)], ["DEL", "slot:" + rec.start]]);
  return rec;
}
async function moveBooking(rec, newStart) {          // returns false if the new time is taken
  const ttl = Math.max(3600, Math.round((Date.parse(newStart) - Date.now()) / 1000) + 86400);
  if ((await cmd("SET", "slot:" + newStart, rec.id, "NX", "EX", String(ttl))) !== "OK") return false;
  const old = rec.start; rec.start = newStart; rec.moved = (rec.moved || 0) + 1;
  await pipeline([["SET", "bk:" + rec.id, JSON.stringify(rec)], ["DEL", "slot:" + old], ["ZADD", "bk:byStart", String(Date.parse(newStart)), rec.id]]);
  return true;
}
async function bookingsBetween(fromMs, toMs) {
  const ids = await cmd("ZRANGEBYSCORE", "bk:byStart", String(fromMs), String(toMs), "LIMIT", "0", "300");
  return (await getMany((ids || []).map(i => "bk:" + i))).filter(Boolean).sort((a, b) => Date.parse(a.start) - Date.parse(b.start));
}

/* ---------- training clients and their sessions ---------- */
async function clients() { return ((await getJSON("clients")) || []).sort((a, b) => a.name.localeCompare(b.name)); }
async function saveClients(list) { return setJSON("clients", list.slice(0, 400)); }
function validHourStart(iso) { return /^\d{4}-\d{2}-\d{2}T\d{2}:00:00Z$/.test(String(iso)) && !isNaN(Date.parse(iso)); }
/* Returns the session, or null when that hour is already taken (by a session or a consult). */
async function addSession(c, startIso) {
  if (!validHourStart(startIso)) return null;
  const id = "s_" + newId(), ttl = Math.max(3600, Math.round((Date.parse(startIso) - Date.now()) / 1000) + 86400);
  if ((await cmd("SET", "slot:" + startIso, id, "NX", "EX", String(ttl))) !== "OK") return null;
  const rec = { id, phone: c.phone, name: c.name, start: startIso, created: new Date().toISOString() };
  await pipeline([["SET", "ses:" + id, JSON.stringify(rec), "EX", String(ttl + 60 * 86400)], ["ZADD", "ses:byStart", String(Date.parse(startIso)), id]]);
  return rec;
}
async function removeSession(id) {
  if (!/^s_[A-Za-z0-9_-]{20,40}$/.test(String(id || ""))) return false;
  const rec = await getJSON("ses:" + id); if (!rec) return false;
  const holder = await cmd("GET", "slot:" + rec.start);
  const cmds = [["DEL", "ses:" + id], ["ZREM", "ses:byStart", id]];
  if (holder === id) cmds.push(["DEL", "slot:" + rec.start]);
  await pipeline(cmds); return true;
}
async function sessionsBetween(fromMs, toMs) {
  const ids = await cmd("ZRANGEBYSCORE", "ses:byStart", String(fromMs), String(toMs), "LIMIT", "0", "500");
  return (await getMany((ids || []).map(i => "ses:" + i))).filter(Boolean).sort((a, b) => Date.parse(a.start) - Date.parse(b.start));
}
/* Monday 00:00 Pacific of the week containing `d`, as a Date. */
function weekStart(d) {
  const key = dateKey(d), dow = DAYS.indexOf(pacificParts(new Date(key + "T20:00:00Z")).dow);     // 0 = Sunday
  const back = (dow + 6) % 7, monday = dateKey(new Date(Date.parse(key + "T20:00:00Z") - back * 864e5));
  return zonedToUtc(monday, "00:00");
}

/* ---------- leads ---------- */
const LEAD_STATUSES = ["new", "booked", "showed", "no_show", "signed_up", "not_interested"];
async function getLead(phone) { return getJSON("lead:" + phone); }
async function saveLead(l) { l.updated = new Date().toISOString(); return setJSON("lead:" + l.phone, l); }
async function getLeads(phones) { return getMany(phones.map(p => "lead:" + p)); }
/* Put someone on (or take them off) the follow-up schedule. */
async function scheduleFollowup(phone, atMs) { return cmd("ZADD", "fu:due", String(atMs), phone); }
async function stopFollowups(phone) { return cmd("ZREM", "fu:due", phone); }
async function dueFollowups(nowMs) { return (await cmd("ZRANGEBYSCORE", "fu:due", "0", String(nowMs), "LIMIT", "0", "40")) || []; }

module.exports = { TZ, DAYS, DEFAULTS, LEAD_STATUSES, configured, cmd, pipeline, getJSON, setJSON, settings, cleanSettings, dateKey, pacificParts, zonedToUtc,
  candidateSlots, openSlots, createBooking, getBooking, saveBooking, cancelBooking, moveBooking, bookingsBetween,
  getLead, saveLead, getLeads, scheduleFollowup, stopFollowups, dueFollowups,
  clients, saveClients, addSession, removeSession, sessionsBetween, weekStart, validHourStart };
