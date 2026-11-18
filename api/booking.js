/*
 * Fig Performance booking API (Vercel serverless function).
 * The website's own day/time picker talks to this; this talks to Calendly.
 *
 *   GET  /api/booking?from=YYYY-MM-DD   -> open consult times for 7 days from that date
 *   POST /api/booking                    -> books a time (name + mobile required, email optional)
 *
 * Settings (Vercel > Project > Settings > Environment Variables):
 *   CALENDLY_TOKEN       required. Calendly personal access token. Never put it in the site files.
 *   CALENDLY_EVENT_SLUG  optional. The end of the consult booking link. Default: free-consult-inbody-scan
 *   BOOKING_INBOX        optional. Calendly needs an email on every booking; when a visitor skips email,
 *                        the booking uses this address instead. Default: trainat@figperformance.com
 */
"use strict";
const sms = require("./_sms.js");

const API = "https://api.calendly.com";
const TZ = "America/Los_Angeles";
const DEFAULT_SLUG = "free-consult-inbody-scan";

let cachedEventType = null; // { uri, name, duration, at }

function send(res, status, body, cache) {
  res.statusCode = status;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", cache || "no-store");
  res.end(JSON.stringify(body));
}

async function calendly(path, opts) {
  const r = await fetch(API + path, Object.assign({}, opts, {
    headers: {
      Authorization: "Bearer " + process.env.CALENDLY_TOKEN,
      "Content-Type": "application/json",
      Accept: "application/json"
    }
  }));
  let j = {};
  try { j = await r.json(); } catch (e) { /* empty body */ }
  return { ok: r.ok, status: r.status, j };
}

async function eventType() {
  if (cachedEventType && Date.now() - cachedEventType.at < 10 * 60 * 1000) return cachedEventType;
  const me = await calendly("/users/me");
  if (!me.ok) throw Object.assign(new Error("calendly auth failed"), { code: 503 });
  const user = me.j.resource.uri;
  const list = await calendly("/event_types?active=true&count=100&user=" + encodeURIComponent(user));
  if (!list.ok) throw Object.assign(new Error("event types failed"), { code: 503 });
  const slug = (process.env.CALENDLY_EVENT_SLUG || DEFAULT_SLUG).trim().toLowerCase();
  const all = list.j.collection || [];
  const et = all.find(e => (e.scheduling_url || "").toLowerCase().endsWith("/" + slug)) || all[0];
  if (!et) throw Object.assign(new Error("no event type"), { code: 503 });
  cachedEventType = { uri: et.uri, name: et.name, duration: et.duration, at: Date.now() };
  return cachedEventType;
}

function clean(v, max) {
  return String(v == null ? "" : v).replace(/[\u0000-\u001F\u007F<>]/g, "").replace(/\s+/g, " ").trim().slice(0, max);
}

const usPhone = sms.usPhone;

async function getSlots(req, res) {
  const q = new URL(req.url, "http://x").searchParams;
  const from = /^\d{4}-\d{2}-\d{2}$/.test(q.get("from") || "") ? q.get("from") : null;
  const now = Date.now();
  let start = from ? Date.parse(from + "T00:00:00-08:00") : now;
  if (!(start > now)) start = now + 60 * 1000;         // Calendly wants a start in the future
  if (start > now + 60 * 24 * 3600 * 1000) return send(res, 400, { error: "too_far" });
  const end = start + 7 * 24 * 3600 * 1000 - 60 * 1000;  // Calendly allows at most 7 days per request
  const et = await eventType();
  const r = await calendly("/event_type_available_times?event_type=" + encodeURIComponent(et.uri) +
    "&start_time=" + new Date(start).toISOString() + "&end_time=" + new Date(end).toISOString());
  if (!r.ok) return send(res, 502, { error: "slots_failed" });
  const slots = (r.j.collection || [])
    .filter(s => s.status === "available")
    .map(s => s.start_time);
  return send(res, 200, { duration: et.duration, slots }, "public, max-age=0, s-maxage=60, stale-while-revalidate=60");
}

async function readBody(req) {
  if (req.body && typeof req.body === "object") return req.body;
  const chunks = [];
  let size = 0;
  for await (const c of req) { size += c.length; if (size > 10000) throw Object.assign(new Error("too big"), { code: 413 }); chunks.push(c); }
  try { return JSON.parse(Buffer.concat(chunks).toString("utf8") || "{}"); } catch (e) { return {}; }
}

async function book(req, res) {
  const b = await readBody(req);
  if (clean(b.website, 200)) return send(res, 200, { ok: true });   // honeypot: bots get a fake success
  if (sms.tooMany("book:" + sms.clientIp(req), 6, 3600 * 1000)) return send(res, 429, { error: "slow_down" });
  const name = clean(b.name, 80);
  const email = clean(b.email, 254).toLowerCase();
  const phone = usPhone(b.phone);
  const goal = clean(b.goal, 500);
  const start = clean(b.start, 40);
  if (name.length < 2) return send(res, 400, { error: "name" });
  if (!phone) return send(res, 400, { error: "phone" });
  if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return send(res, 400, { error: "email" });
  if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$/.test(start) || Date.parse(start) < Date.now()) return send(res, 400, { error: "start" });

  // One active booking per mobile: stops scripts from booking (and texting) the same number over and over.
  let alreadyTexted = false;
  if (sms.configured()) {
    try { alreadyTexted = await sms.recentlyTexted(phone, 24); } catch (e) { alreadyTexted = true; }
    if (alreadyTexted) return send(res, 409, { error: "already_booked" });
  }

  const et = await eventType();
  // Like Train With Dave: only name + mobile are required. Calendly still needs an email, so a
  // booking without one uses the gym's inbox (Dan then also gets Calendly's emails for it).
  const inbox = (process.env.BOOKING_INBOX || "trainat@figperformance.com").trim();
  const invitee = { name, email: email || inbox, timezone: TZ };
  if (!sms.configured()) invitee.text_reminder_number = phone;   // Calendly texts only when our own texting is off
  const payload = {
    event_type: et.uri,
    start_time: start,
    invitee,
    tracking: {
      utm_source: clean(b.utm_source, 100) || "figperformance.com",
      utm_medium: clean(b.utm_medium, 100) || "website",
      utm_campaign: clean(b.utm_campaign, 100) || "native-booking",
      // Signature proving this phone came from our own form (checked by api/calendly-hook.js).
      utm_content: sms.configured() ? sms.phoneSig(phone) : (clean(b.utm_content, 100) || undefined),
      // The mobile rides along here so api/calendly-hook.js can match reminders to this booking.
      utm_term: phone
    }
  };
  let r = await calendly("/invitees", { method: "POST", body: JSON.stringify(payload) });
  // If text reminders aren't switched on for this event yet, Calendly can reject the number: book without it.
  // The phone still reaches Dan in the lead email the website sends.
  if (!r.ok && r.status === 400 && /text_reminder|phone/i.test(JSON.stringify(r.j))) {
    delete invitee.text_reminder_number;
    r = await calendly("/invitees", { method: "POST", body: JSON.stringify(payload) });
  }
  if (!r.ok) {
    const msg = JSON.stringify(r.j);
    if (r.status === 409 || /not available|unavailable|already|taken|no longer/i.test(msg)) return send(res, 409, { error: "taken" });
    console.error("calendly booking failed", r.status);
    return send(res, 502, { error: "book_failed" });
  }
  const v = r.j.resource || {};
  // Our own texting (Twilio), when it's set up: confirmation now. The reminders are scheduled by
  // api/calendly-hook.js when Calendly reports the booking, so moves and cancels stay in step.
  let texted = false;
  try { texted = !!(await sms.sendText(phone, sms.confirmationText(name, start, false))); } catch (e) { console.error("confirm text failed", e && e.message); }
  return send(res, 200, {
    ok: true,
    start,
    reschedule_url: v.reschedule_url || null,
    cancel_url: v.cancel_url || null,
    texting: texted || !!invitee.text_reminder_number
  });
}

async function handler(req, res) {
  try {
    if (!process.env.CALENDLY_TOKEN) return send(res, 503, { error: "not_configured" });
    if (req.method === "GET") return await getSlots(req, res);
    if (req.method === "POST") {
      const ct = String(req.headers["content-type"] || "");
      if (!ct.includes("application/json")) return send(res, 415, { error: "json_only" });
      return await book(req, res);
    }
    res.setHeader("Allow", "GET, POST");
    return send(res, 405, { error: "method" });
  } catch (e) {
    console.error("booking error", e && e.message);
    return send(res, e && e.code ? e.code : 500, { error: "server" });
  }
}
handler.eventType = eventType;
module.exports = handler;
