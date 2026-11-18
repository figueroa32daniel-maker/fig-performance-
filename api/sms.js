/*
 * Incoming texts. Twilio calls this address every time a client texts the gym's number.
 * The message itself is already saved in Twilio (the inbox page reads it from there), so all
 * this does is check the call is really from Twilio and nudge Dan's own phone.
 * Set as the Messaging Service's "incoming message" webhook: https://www.figperformance.com/api/sms
 */
"use strict";
const sms = require("./_sms.js");
const db = require("./_db.js");

function twiml(res) {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/xml; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  res.end("<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response></Response>");
}

async function form(req) {
  if (req.body && typeof req.body === "object") return req.body;
  const chunks = []; let size = 0;
  for await (const c of req) { size += c.length; if (size > 20000) break; chunks.push(c); }
  return Object.fromEntries(new URLSearchParams(Buffer.concat(chunks).toString("utf8")));
}

module.exports = async function handler(req, res) {
  try {
    if (req.method !== "POST" || !sms.configured()) { res.statusCode = 404; return res.end("not found"); }
    const p = await form(req);
    if (!sms.validTwilioSignature(req, p)) { res.statusCode = 403; return res.end("forbidden"); }
    const from = sms.usPhone(p.From), body = String(p.Body || "").trim();
    const dan = sms.usPhone(process.env.DAN_MOBILE);
    const word = body.toLowerCase().replace(/[^a-z]/g, "");
    const stop = /^(stop|stopall|unsubscribe|cancel|end|quit|optout|revoke)$/.test(word);
    const start = /^(start|unstop|yes)$/.test(word) && false;      // "YES" is a confirmation here, never a re-subscribe
    const resub = /^(start|unstop)$/.test(word);
    // Twilio itself blocks texts to anyone who sent STOP. We also record it, cancel their reminders
    // and take them off every follow-up, so nothing is even attempted.
    if (from && db.configured()) {
      try {
        const lead = (await db.getLead(from)) || { phone: from, created: new Date().toISOString(), status: "new" };
        if (stop) { lead.optedOut = true; lead.optedOutAt = new Date().toISOString(); await db.stopFollowups(from); await sms.cancelScheduled(from); }
        else if (resub) { lead.optedOut = false; lead.optedInAt = new Date().toISOString(); }
        else {
          lead.repliedAt = new Date().toISOString(); await db.stopFollowups(from);          // a real reply: Dan takes it from here
          if (/^(yes|y|yep|yeah|confirm|confirmed|c)$/.test(word) && lead.bookingId) {    // "YES" to the reminder = confirmed
            const bk = await db.getBooking(lead.bookingId);
            if (bk && bk.status === "booked" && !bk.confirmed && Date.parse(bk.start) > Date.now()) {
              bk.confirmed = true; bk.confirmedAt = new Date().toISOString(); await db.saveBooking(bk);
              const w = sms.when(bk.start);
              await sms.sendText(from, "Confirmed. See you " + w.day + " at " + w.time + ". - Coach Dan, Fig Performance");
            }
          }
        }
        await db.saveLead(lead);
      } catch (e) { console.error("lead update failed", e && e.message); }
    }
    void start;
    if (from && dan && from !== dan && !stop && !resub && !/^(help|info)$/.test(word)) {
      await sms.sendText(dan, "Fig inbox: " + sms.prettyPhone(from) + " replied: \"" +
        body.slice(0, 200) + "\". Answer at figperformance.com/inbox");
    }
    return twiml(res);
  } catch (e) {
    console.error("sms webhook error", e && e.message);
    return twiml(res);
  }
};
