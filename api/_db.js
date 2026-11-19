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
 *   slot:<cellISO>      who holds one 30-minute cell of the calendar (SET NX = no double bookings).
 *                       A consult holds 3 cells (90 minutes); a client session holds 2 (60 minutes).
 *   skip:<phone>:<iso>  "don't re-add this fixed weekly session" (Dan removed that one week)
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
const CELL = 30 * 60 * 1000;      // the calendar grid
const CONSULT_MIN = 90;            // Dan: consult runs about 1 h 10, blocked as 1 h 30
const SESSION_MIN = 60;
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
  // Consults can be booked any time the gym is open that a client session doesn't already take (Dan, Nov 18 2026).
  hours: { sun: null, mon: { from: "05:00", to: "20:00" }, tue: { from: "05:00", to: "20:00" }, wed: { from: "05:00", to: "20:00" },
           thu: { from: "05:00", to: "20:00" }, fri: { from: "05:00", to: "20:00" }, sat: { from: "05:00", to: "12:00" } },
  blocked: [],                 // dates off, "YYYY-MM-DD"
  noticeHours: 3,              // earliest bookable time from now
  daysAhead: 14,
  followups: [                 // sent only to people who ticked the optional marketing box
    { day: 2, text: "Hi {first}, Coach Dan at Fig Performance. Good meeting you. Any questions about the plan we talked through? Just reply here. Reply STOP to opt out." },
    { day: 7, text: "Hi {first}, Coach Dan here. Most people I work with say the hardest part is starting. Want me to hold a first session time for you this week? Reply STOP to opt out." },
    { day: 21, text: "Hi {first}, it's Coach Dan at Fig Performance. Still thinking about getting stronger? I have a couple of training spots open. Reply here and I'll set it up. Reply STOP to opt out." },
    { day: 45, text: "Hi {first}, Coach Dan at Fig Performance. Last note from me: if the timing is better now, reply and we'll pick up where we left off. Reply STOP to opt out." }
  ],
  // The texting assistant. Off until Dan turns it on. "facts" is the only information it may give out.
  ai: { on: false, weeklyAsk: false, alerts: "urgent", facts: "Fig Performance is Coach Dan Figueroa's private personal-training gym at 1284 E. Yorba Linda Blvd, Placentia, CA. Gym hours: Mon-Fri 5 AM to 8 PM, Saturday 5 AM to 12 PM, closed Sunday. Training is by appointment only. Phone: (714) 396-7178. Website: figperformance.com." },
  // Missed-call text-back: a caller Dan couldn't answer gets one text so the lead isn't lost.
  // ring: true = calls to the gym number ring Dan's cell first; false = his carrier already tried him (call forwarding).
  missedCall: { on: true, ring: true, text: "Hi, this is Coach Dan at Fig Performance. Sorry I missed your call, I'm probably coaching. Text me here and I'll get right back to you, or book a free consult at figperformance.com. Reply STOP to opt out." },
  sessionReminders: true,      // text each client the morning before a training session
  // Google review request. Sent only when Dan presses "Ask for a review" on a client. No link, no button.
  review: { link: "", text: "Hi {first}, Coach Dan at Fig Performance. If training here has helped you, would you leave a quick Google review? It means a lot: {link} Reply STOP to opt out." },
  noShowText: "Hi {first}, Coach Dan at Fig Performance. Sorry we missed each other today. Want to pick a new time? Reply here or book at figperformance.com. Reply STOP to opt out."
};
function cleanSettings(s) {
  s = s || {};
  const out = JSON.parse(JSON.stringify(DEFAULTS));
  DAYS.forEach(d => {
    if (!s.hours || !(d in s.hours)) return;                  // not saved yet: keep the gym-hours default
    const h = s.hours[d];                                      // saved as closed (null) stays closed
    out.hours[d] = h && /^\d{2}:00$/.test(h.from) && /^\d{2}:00$/.test(h.to) && h.from < h.to ? { from: h.from, to: h.to } : null;
  });
  if (Array.isArray(s.blocked)) out.blocked = s.blocked.filter(x => /^\d{4}-\d{2}-\d{2}$/.test(x)).slice(0, 200);
  if (Number.isFinite(+s.noticeHours)) out.noticeHours = Math.max(0, Math.min(72, Math.round(+s.noticeHours)));
  if (Number.isFinite(+s.daysAhead)) out.daysAhead = Math.max(1, Math.min(30, Math.round(+s.daysAhead)));
  if (Array.isArray(s.followups)) {
    const f = s.followups.map(x => ({ day: Math.max(1, Math.min(120, Math.round(+x.day || 0))), text: String(x.text || "").trim().slice(0, 600) }))
      .filter(x => x.text).sort((a, b) => a.day - b.day).slice(0, 6);
    out.followups = f.map(withStop);
  }
  if (s.ai && typeof s.ai === "object") {
    out.ai.on = s.ai.on === true;
    out.ai.weeklyAsk = s.ai.weeklyAsk === true;
    out.ai.alerts = s.ai.alerts === "all" ? "all" : "urgent";
    if (typeof s.ai.facts === "string" && s.ai.facts.trim()) out.ai.facts = s.ai.facts.trim().slice(0, 3000);
  }
  if (s.missedCall && typeof s.missedCall === "object") {
    out.missedCall.on = s.missedCall.on !== false; out.missedCall.ring = s.missedCall.ring !== false;
    if (typeof s.missedCall.text === "string" && s.missedCall.text.trim()) out.missedCall.text = withStop({ text: s.missedCall.text.trim().slice(0, 480) }).text;
  }
  if (typeof s.sessionReminders === "boolean") out.sessionReminders = s.sessionReminders;
  if (s.review && typeof s.review === "object") {
    const link = String(s.review.link || "").trim();
    if (/^https:\/\/[a-z0-9.-]+\.[a-z]{2,}\/[^\s<>"']{0,300}$/i.test(link)) out.review.link = link;
    if (typeof s.review.text === "string" && s.review.text.trim()) {
      let t = withStop({ text: s.review.text.trim().slice(0, 480) }).text;
      if (t.indexOf("{link}") < 0) t = t.replace(/\s*Reply STOP to opt out\.\s*$/i, "") + " {link} Reply STOP to opt out.";
      out.review.text = t;
    }
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

/* Every consult start the settings allow from now through daysAhead (every 30 minutes; the consult
   must finish by the day's end time), before removing taken ones. */
function candidateSlots(s, now) {
  const out = [], earliest = now + s.noticeHours * 3600 * 1000;
  for (let i = 0; i <= s.daysAhead; i++) {
    const day = dateKey(new Date(now + i * 864e5));
    if (s.blocked.indexOf(day) >= 0) continue;
    const dow = pacificParts(new Date(day + "T20:00:00Z")).dow;      // noon-ish Pacific on that date
    const h = s.hours[dow]; if (!h) continue;
    const open = zonedToUtc(day, h.from), close = zonedToUtc(day, h.to);
    if (!open || !close) continue;
    for (let t = open.getTime(); t + CONSULT_MIN * 60000 <= close.getTime(); t += CELL) {
      if (t >= earliest) out.push(iso(t));
    }
  }
  return out;
}
function iso(ms) { return new Date(ms).toISOString().replace(".000Z", "Z"); }
function cellsFor(startIso, minutes) {
  const out = [], t0 = Date.parse(startIso);
  for (let t = t0; t < t0 + minutes * 60000; t += CELL) out.push(iso(t));
  return out;
}
/* Take every cell or none. */
async function lockCells(cells, id) {
  const ttl = String(Math.max(3600, Math.round((Date.parse(cells[cells.length - 1]) - Date.now()) / 1000) + 86400));
  const got = await pipeline(cells.map(c => ["SET", "slot:" + c, id, "NX", "EX", ttl]));
  if (got.every(x => x === "OK")) return true;
  const mine = cells.filter((c, i) => got[i] === "OK");
  if (mine.length) await pipeline(mine.map(c => ["DEL", "slot:" + c]));
  return false;
}
async function freeCells(cells, id) {
  const held = await cmd.apply(null, ["MGET"].concat(cells.map(c => "slot:" + c)));
  const mine = cells.filter((c, i) => held[i] === id);
  if (mine.length) await pipeline(mine.map(c => ["DEL", "slot:" + c]));
}
async function openSlots(now, ignoreId) {             // ignoreId: a booking being moved doesn't block itself
  const s = await settings(), all = candidateSlots(s, now || Date.now());
  if (!all.length) return [];
  const cells = Array.from(new Set(all.flatMap(x => cellsFor(x, CONSULT_MIN))));
  const held = await cmd.apply(null, ["MGET"].concat(cells.map(c => "slot:" + c)));
  const busy = new Set(cells.filter((c, i) => held[i] && held[i] !== ignoreId));
  return all.filter(x => cellsFor(x, CONSULT_MIN).every(c => !busy.has(c)));
}

/* ---------- bookings ---------- */
function newId() { return crypto.randomBytes(18).toString("base64url"); }
async function createBooking(b) {                    // returns the booking, or null if the time was just taken
  const id = newId();
  if (!(await lockCells(cellsFor(b.start, CONSULT_MIN), id))) return null;
  const rec = Object.assign({ id, status: "booked", minutes: CONSULT_MIN, created: new Date().toISOString() }, b);
  await pipeline([["SET", "bk:" + id, JSON.stringify(rec)], ["ZADD", "bk:byStart", String(Date.parse(b.start)), id]]);
  return rec;
}
async function getBooking(id) { return /^[A-Za-z0-9_-]{20,40}$/.test(String(id || "")) ? getJSON("bk:" + id) : null; }
async function saveBooking(rec) { return setJSON("bk:" + rec.id, rec); }
async function cancelBooking(rec, by) {
  if (rec.status === "cancelled") return rec;
  rec.status = "cancelled"; rec.cancelledBy = by; rec.cancelledAt = new Date().toISOString();
  await setJSON("bk:" + rec.id, rec);
  await freeCells(cellsFor(rec.start, rec.minutes || CONSULT_MIN), rec.id);
  await freed(rec.start, rec.minutes || CONSULT_MIN);
  return rec;
}
async function moveBooking(rec, newStart) {          // returns false if the new time is taken
  const mins = rec.minutes || CONSULT_MIN, oldCells = cellsFor(rec.start, mins), newCells = cellsFor(newStart, mins);
  // Cells the booking already holds stay held; only the new ones need taking.
  const need = newCells.filter(c => oldCells.indexOf(c) < 0);
  if (need.length && !(await lockCells(need, rec.id))) return false;
  await freeCells(oldCells.filter(c => newCells.indexOf(c) < 0), rec.id);
  const was = rec.start;
  rec.start = newStart; rec.moved = (rec.moved || 0) + 1;
  await pipeline([["SET", "bk:" + rec.id, JSON.stringify(rec)], ["ZADD", "bk:byStart", String(Date.parse(newStart)), rec.id]]);
  await freed(was, mins);
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
async function addSession(c, startIso, fixed, by) {
  if (!validHourStart(startIso)) return null;
  const id = "s_" + newId();
  if (!(await lockCells(cellsFor(startIso, SESSION_MIN), id))) return null;
  const rec = { id, phone: c.phone, name: c.name, start: startIso, fixed: !!fixed, created: new Date().toISOString() };
  if (by) rec.by = by;
  const ttl = String(Math.max(3600, Math.round((Date.parse(startIso) - Date.now()) / 1000)) + 90 * 86400);
  await pipeline([["SET", "ses:" + id, JSON.stringify(rec), "EX", ttl], ["ZADD", "ses:byStart", String(Date.parse(startIso)), id]]);
  return rec;
}
/* charge = a late cancel or no-show: the client loses that session from their count. */
async function removeSession(id, charge) {
  if (!/^s_[A-Za-z0-9_-]{20,40}$/.test(String(id || ""))) return false;
  const rec = await getJSON("ses:" + id); if (!rec) return false;
  if (charge && !rec.counted) await useCredit(rec.phone, 1);
  await freeCells(cellsFor(rec.start, SESSION_MIN), id);
  const cmds = [["DEL", "ses:" + id], ["ZREM", "ses:byStart", id]];
  // A fixed weekly session removed for one week must not be put straight back by the weekly fill.
  if (rec.fixed && Date.parse(rec.start) > Date.now()) cmds.push(["SET", "skip:" + rec.phone + ":" + rec.start, "1", "EX", String(Math.round((Date.parse(rec.start) - Date.now()) / 1000) + 86400)]);
  await pipeline(cmds);
  await freed(rec.start, SESSION_MIN);
  return true;
}
/* Time came free: let the waitlist know. (Loaded here, not at the top, because the assistant file loads this one.) */
async function freed(startIso, minutes) { try { await require("./_ai.js").offerFreed(startIso, minutes); } catch (e) { /* never block a cancel */ } }
/*
 * Session count. A client can have "sessions left" (credits). It goes down by one for every session that
 * has happened, and for a late cancel or no-show Dan marks. Clients with no count set are not tracked.
 * Returns the client after the change, or null if they are not being counted.
 */
async function useCredit(phone, n) {
  const list = await clients(), c = list.find(x => x.phone === phone);
  if (!c || !Number.isFinite(c.credits)) return null;
  c.credits = c.credits - n; await saveClients(list); return c;
}
/* Called by the daily job: count every session that has finished and hasn't been counted yet. */
async function tallySessions(now) {
  const done = (await sessionsBetween(now - 10 * 864e5, now - SESSION_MIN * 60000)).filter(x => !x.counted), low = [];
  for (const rec of done) {
    rec.counted = true;
    await cmd("SET", "ses:" + rec.id, JSON.stringify(rec), "KEEPTTL");
    await useCredit(rec.phone, 1);
  }
  // Tell Dan about anyone this run brought down to 2 or fewer, using where they ended up.
  const touched = new Set(done.map(x => x.phone));
  (await clients()).forEach(c => { if (touched.has(c.phone) && Number.isFinite(c.credits) && c.credits <= 2) low.push({ name: c.name, credits: c.credits }); });
  return { counted: done.length, low };
}
/* Clients with fixed weekly times ("Tuesday 5 AM, never changes"): keep the next few weeks filled in. */
async function ensureFixed(weeksAhead) {
  const list = (await clients()).filter(c => Array.isArray(c.fixed) && c.fixed.length), now = Date.now();
  let added = 0;
  for (const c of list) {
    for (let i = 0; i < (weeksAhead || 3) * 7; i++) {
      const day = dateKey(new Date(now + i * 864e5)), dow = pacificParts(new Date(day + "T20:00:00Z")).dow;
      for (const f of c.fixed.filter(x => x.dow === dow)) {
        const at = zonedToUtc(day, String(f.hour).padStart(2, "0") + ":00");
        if (!at || at.getTime() < now) continue;
        const startIso = iso(at.getTime());
        if (await cmd("GET", "skip:" + c.phone + ":" + startIso)) continue;
        if (await addSession(c, startIso, true)) added++;
      }
    }
  }
  return added;
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

/* "Needs you": things the assistant handed to Dan. Newest first, kept 30 days, at most 100. */
async function addNeed(n) {
  const rec = Object.assign({ id: newId(), at: new Date().toISOString(), done: false }, n);
  await pipeline([["LPUSH", "needs", JSON.stringify(rec)], ["LTRIM", "needs", "0", "99"]]);
  return rec;
}
async function needs() {
  const raw = (await cmd("LRANGE", "needs", "0", "99")) || [], cut = Date.now() - 30 * 864e5;
  return raw.map(x => { try { return JSON.parse(x); } catch (e) { return null; } }).filter(x => x && Date.parse(x.at) > cut);
}
async function resolveNeed(id) {
  const list = await needs(), hit = list.find(x => x.id === id);
  if (!hit) return false;
  hit.done = true; hit.doneAt = new Date().toISOString();
  await pipeline([["DEL", "needs"]].concat(list.length ? [["RPUSH", "needs"].concat(list.map(x => JSON.stringify(x)))] : []));
  return true;
}

/* What the assistant did, newest first (last 50), for the Today page. */
async function logActivity(a) {
  await pipeline([["LPUSH", "activity", JSON.stringify(Object.assign({ at: new Date().toISOString() }, a))], ["LTRIM", "activity", "0", "49"]]);
}
async function activity() {
  return ((await cmd("LRANGE", "activity", "0", "49")) || []).map(x => { try { return JSON.parse(x); } catch (e) { return null; } }).filter(Boolean);
}

module.exports = { TZ, addNeed, needs, resolveNeed, logActivity, activity, DAYS, DEFAULTS, LEAD_STATUSES, configured, cmd, pipeline, getJSON, setJSON, settings, cleanSettings, dateKey, pacificParts, zonedToUtc,
  candidateSlots, openSlots, createBooking, getBooking, saveBooking, cancelBooking, moveBooking, bookingsBetween,
  getLead, saveLead, getLeads, scheduleFollowup, stopFollowups, dueFollowups,
  clients, saveClients, addSession, removeSession, sessionsBetween, weekStart, validHourStart, ensureFixed, useCredit, tallySessions, cellsFor, CONSULT_MIN, SESSION_MIN };
