/*
 * Calendly tells this address when a consult is booked, moved or cancelled, so the reminder
 * texts always match the calendar:
 *   booked    -> schedule the day-before and 2-hours-before reminders
 *   moved     -> cancel the old reminders, text the new time, schedule new reminders
 *   cancelled -> cancel the reminders
 * The inbox page's "Connect Calendly" button creates the subscription, with a secret key in
 * the address (?k=...) so nobody else can call it.
 */
"use strict";
const crypto = require("crypto");
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
    if (req.method !== "POST" || !sms.configured() || !process.env.INBOX_PASSWORD) return done(res, 404, "not found");
    const k = new URL(req.url, "http://x").searchParams.get("k") || "";
    const a = Buffer.from(k), b = Buffer.from(sms.hookKey());
    if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) return done(res, 403, "forbidden");

    const body = await json(req);
    const p = body.payload || {};
    // The website stores the client's mobile in Calendly's "utm_term" tracking field at booking time.
    const phone = sms.usPhone((p.tracking || {}).utm_term) || sms.usPhone(p.text_reminder_number);
    const start = (p.scheduled_event || {}).start_time;
    if (!phone) return done(res, 200, "no phone");            // booked some other way (not the website)

    if (body.event === "invitee.canceled") {
      await sms.cancelScheduled(phone);
    } else if (body.event === "invitee.created" && start && Date.parse(start) > Date.now()) {
      if (p.old_invitee) {                                     // a reschedule: new time, new reminders
        await sms.cancelScheduled(phone);
        await sms.sendText(phone, sms.confirmationText(p.name, start, true));
      }
      await sms.scheduleReminders(phone, p.name, start);
    }
    return done(res, 200);
  } catch (e) {
    console.error("calendly hook error", e && e.message);
    return done(res, 200);                                     // don't make Calendly retry forever
  }
};
