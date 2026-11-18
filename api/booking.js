/*
 * Fig Performance booking engine (Vercel serverless function). No Calendly: the site keeps its
 * own calendar in the database (api/_db.js) and sends its own texts (api/_sms.js).
 *
 *   GET  /api/booking                          -> open consult times (from Dan's hours in Settings)
 *   POST /api/booking {name, phone, start,...} -> books it: holds the time, texts the client, texts Dan
 *   POST /api/booking {action:"manage", t}     -> the booking behind a private "manage" link
 *   POST /api/booking {action:"cancel", t}     -> client cancels
 *   POST /api/booking {action:"move", t, start}-> client picks a new time
 */
"use strict";
const sms = require("./_sms.js");
const db = require("./_db.js");

const SITE = "https://www.figperformance.com";
const CONSENT_VERSION = "2026-11-17.2";      // bump when the wording next to the booking button changes

function send(res, status, body, cache) {
  res.statusCode = status;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", cache || "no-store");
  res.end(JSON.stringify(body));
}
function clean(v, max) { return String(v == null ? "" : v).replace(/[\u0000-\u001F\u007F<>]/g, "").replace(/\s+/g, " ").trim().slice(0, max); }
async function readBody(req) {
  if (req.body && typeof req.body === "object") return req.body;
  const chunks = []; let size = 0;
  for await (const c of req) { size += c.length; if (size > 10000) throw Object.assign(new Error("too big"), { code: 413 }); chunks.push(c); }
  try { return JSON.parse(Buffer.concat(chunks).toString("utf8") || "{}"); } catch (e) { return {}; }
}
function manageUrl(id) { return SITE + "/manage?t=" + id; }
function pub(b) { return { start: b.start, status: b.status, first: sms.first(b.name), canChange: b.status === "booked" && Date.parse(b.start) > Date.now() }; }

/* Confirmation now, reminders the day before and 2 hours before. Old reminders are cleared first. */
async function sendBookingTexts(b, moved) {
  if (!sms.configured()) return false;
  try {
    await sms.cancelScheduled(b.phone);
    const ok = await sms.sendText(b.phone, sms.confirmationText(b.name, b.start, moved, manageUrl(b.id)));
    await sms.scheduleReminders(b.phone, b.name, b.start);
    return !!ok;
  } catch (e) { console.error("booking texts failed", e && e.message); return false; }
}

async function book(req, res, b) {
  if (clean(b.website, 200)) return send(res, 200, { ok: true });            // honeypot: bots get a fake success
  if (sms.tooMany("book:" + sms.clientIp(req), 6, 3600 * 1000)) return send(res, 429, { error: "slow_down" });
  const name = clean(b.name, 80), email = clean(b.email, 254).toLowerCase(), phone = sms.usPhone(b.phone);
  const goal = clean(b.goal, 500), start = clean(b.start, 40);
  if (name.length < 2) return send(res, 400, { error: "name" });
  if (!phone) return send(res, 400, { error: "phone" });
  if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return send(res, 400, { error: "email" });
  if (b.consent !== true) return send(res, 400, { error: "consent" });

  // The time must be one the site is offering right now (Dan's hours, notice period, not taken).
  if ((await db.openSlots()).indexOf(start) < 0) return send(res, 409, { error: "taken" });

  // One upcoming consult per mobile: stops scripts booking (and texting) the same number repeatedly.
  let lead = await db.getLead(phone);
  if (lead && lead.optedOut && sms.configured()) { /* still allowed to book; we just won't text them */ }
  if (lead && lead.bookingId) {
    const cur = await db.getBooking(lead.bookingId);
    if (cur && cur.status === "booked" && Date.parse(cur.start) > Date.now()) return send(res, 409, { error: "already_booked" });
  }

  const rec = await db.createBooking({
    name, phone, email, goal, start,
    source: [clean(b.utm_source, 60), clean(b.utm_medium, 60), clean(b.utm_campaign, 60)].filter(Boolean).join(" / ") || "website"
  });
  if (!rec) return send(res, 409, { error: "taken" });

  // The consent record: what they agreed to, when, and from where. Kept with the lead.
  const now = new Date().toISOString();
  lead = Object.assign({ phone, created: now, status: "new" }, lead || {}, {
    name, email: email || (lead && lead.email) || "", goal: goal || (lead && lead.goal) || "",
    status: "booked", bookingId: rec.id, lastStart: start, followStep: 0,
    consent: {
      at: now, ip: sms.clientIp(req), version: CONSENT_VERSION, page: clean(b.page, 120) || "/",
      appointmentTexts: true,                               // agreed by booking with the notice shown at the button
      marketingTexts: b.marketing === true                  // only if they ticked the separate, optional box
    }
  });
  await db.saveLead(lead);
  await db.stopFollowups(phone);

  const texted = lead.optedOut ? false : await sendBookingTexts(rec, false);
  const w = sms.when(start);
  await sms.tellDan("New consult booked: " + name + ", " + w.day + " " + w.time + ", " + sms.prettyPhone(phone) + (goal ? ". Goal: " + goal.slice(0, 80) : ""));
  return send(res, 200, { ok: true, start, texting: texted, manage_url: "/manage?t=" + rec.id });
}

async function manage(req, res, b) {
  if (sms.tooMany("manage:" + sms.clientIp(req), 30, 3600 * 1000)) return send(res, 429, { error: "slow_down" });
  const rec = await db.getBooking(b.t);
  if (!rec) return send(res, 404, { error: "not_found" });
  if (b.action === "manage") return send(res, 200, { ok: true, booking: pub(rec) });
  if (rec.status !== "booked" || Date.parse(rec.start) < Date.now()) return send(res, 409, { error: "closed", booking: pub(rec) });
  const lead = (await db.getLead(rec.phone)) || {};
  const was = sms.when(rec.start);

  if (b.action === "cancel") {
    const oldStart = rec.start;
    await db.cancelBooking(rec, "client");
    if (sms.configured() && !lead.optedOut) { try { await sms.cancelScheduled(rec.phone); await sms.sendText(rec.phone, sms.cancelledText(rec.name, oldStart)); } catch (e) { /* booking is cancelled either way */ } }
    await sms.tellDan("Cancelled by client: " + rec.name + ", " + was.day + " " + was.time + ", " + sms.prettyPhone(rec.phone));
    return send(res, 200, { ok: true, booking: pub(rec) });
  }
  if (b.action === "move") {
    const start = clean(b.start, 40);
    if ((rec.moved || 0) >= 3) return send(res, 409, { error: "too_many_moves" });
    if (start === rec.start) return send(res, 200, { ok: true, texting: false, booking: pub(rec) });
    if ((await db.openSlots(null, rec.id)).indexOf(start) < 0 || !(await db.moveBooking(rec, start))) return send(res, 409, { error: "taken" });
    if (lead.phone) { lead.lastStart = start; await db.saveLead(lead); }
    const texted = lead.optedOut ? false : await sendBookingTexts(rec, true);
    const w = sms.when(start);
    await sms.tellDan("Rescheduled: " + rec.name + ", was " + was.day + " " + was.time + ", now " + w.day + " " + w.time);
    return send(res, 200, { ok: true, texting: texted, booking: pub(rec) });
  }
  return send(res, 400, { error: "action" });
}

module.exports = async function handler(req, res) {
  try {
    if (!db.configured()) return send(res, 503, { error: "not_configured" });
    if (req.method === "GET") {
      const slots = await db.openSlots();
      return send(res, 200, { duration: db.CONSULT_MIN, slots }, "public, max-age=0, s-maxage=30, stale-while-revalidate=30");
    }
    if (req.method === "POST") {
      if (!String(req.headers["content-type"] || "").includes("application/json")) return send(res, 415, { error: "json_only" });
      const b = await readBody(req);
      if (b.action === "manage" || b.action === "cancel" || b.action === "move") return await manage(req, res, b);
      return await book(req, res, b);
    }
    res.setHeader("Allow", "GET, POST");
    return send(res, 405, { error: "method" });
  } catch (e) {
    console.error("booking error", e && e.message);
    return send(res, e && e.code ? e.code : 500, { error: "server" });
  }
};
