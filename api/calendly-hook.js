/*
 * Calendly tells this address when a consult is booked, moved or cancelled, so the reminder
 * texts always match the calendar:
 *   booked    -> schedule the day-before and 2-hours-before reminders
 *   moved     -> cancel the old reminders, text the new time, schedule new reminders
 *   cancelled -> cancel the reminders
 * The inbox page's "Connect Calendly" button creates the subscription, with a secret key in
 * the address (?k=...) so nobody else can call it. On top of that, a booking only gets texts if
 * it is the consult event AND carries the signature our own booking form attaches to the phone,
 * so a booking made on Calendly's public page with someone else's number is ignored.
 */
"use strict";
const sms = require("./_sms.js");

async function json(req) {
  if (req.body && typeof req.body === "object") return req.body;
  const chunks = []; let size = 0;
  for await (const c of req) { size += c.length; if (size > 200000) break; chunks.push(c); }
  try { return JSON.parse(Buffer.concat(chunks).toString("utf8") || "{}"); } catch (e) { return {}; }
}
function done(res, code, msg) { res.statusCode = code; res.setHeader("Cache-Control", "no-store"); res.end(msg || "ok"); }

module.exports = async function handler(req, res) {
  try {
    if (req.method !== "POST" || !sms.configured()) return done(res, 404, "not found");
    const k = new URL(req.url, "http://x").searchParams.get("k") || "";
    if (!sms.safeEqual(k, sms.hookKey())) return done(res, 403, "forbidden");

    const body = await json(req);
    const p = body.payload || {};
    // The website stores the client's mobile in Calendly's "utm_term" tracking field at booking time.
    const t = p.tracking || {};
    const phone = sms.usPhone(t.utm_term);
    const start = (p.scheduled_event || {}).start_time;
    if (!phone || !sms.safeEqual(t.utm_content || "", sms.phoneSig(phone))) return done(res, 200, "not from the website form");
    const consult = await require("./booking.js").eventType();
    if ((p.scheduled_event || {}).event_type !== consult.uri) return done(res, 200, "other event type");

    if (body.event === "invitee.canceled") {
      // A reschedule arrives as "canceled" (old time) plus "created" (new time), in either order.
      // The "created" side replaces the reminders, so the "canceled" side must not wipe them.
      if (p.rescheduled) return done(res, 200, "rescheduled");
      await sms.cancelScheduled(phone);
    } else if (body.event === "invitee.created" && start && Date.parse(start) > Date.now()) {
      await sms.cancelScheduled(phone);                        // always clear first: no doubles if Calendly repeats itself
      if (p.old_invitee) await sms.sendText(phone, sms.confirmationText(p.name, start, true));
      await sms.scheduleReminders(phone, p.name, start);
    }
    return done(res, 200);
  } catch (e) {
    console.error("calendly hook error", e && e.message);
    return done(res, 500, "try again");                        // Calendly retries, so a hiccup doesn't lose the reminders
  }
};
