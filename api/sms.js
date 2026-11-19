/*
 * Incoming texts. Twilio calls this address every time a client texts the gym's number.
 * The message itself is already saved in Twilio (the inbox page reads it from there), so all
 * this does is check the call is really from Twilio and nudge Dan's own phone.
 * Set as the Messaging Service's "incoming message" webhook: https://www.figperformance.com/api/sms
 */
"use strict";
const sms = require("./_sms.js");
const db = require("./_db.js");
const ai = require("./_ai.js");

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

// Words that mean "Dan should see this now", whatever the assistant decides.
const EMERGENCY = /\b(emergency|911|ambulance|hospital|hurt|injur(ed|y)|bleeding|faint(ed)?|dizzy|chest pain|can'?t breathe|fell|locked out|can'?t get in|door('?s)? locked|fire|police)\b/i;

module.exports = async function handler(req, res) {
  try {
    if (req.method !== "POST" || !sms.configured()) { res.statusCode = 404; return res.end("not found"); }
    const p = await form(req);
    if (!sms.validTwilioSignature(req, p)) { res.statusCode = 403; return res.end("forbidden"); }
    const from = sms.usPhone(p.From), body = String(p.Body || "").trim();
    const dan = sms.usPhone(process.env.DAN_MOBILE);
    // Keywords count only when they are the whole message ("Cancel", "STOP."), the way carriers treat them.
    // "Cancel 11/24 at 5" is a scheduling request, not an opt-out.
    const word = /^[\s"'.!]*[a-z]+[\s"'.!]*$/i.test(body) ? body.toLowerCase().replace(/[^a-z]/g, "") : "";
    const stop = /^(stop|stopall|unsubscribe|cancel|end|quit|optout|revoke)$/.test(word);
    const start = /^(start|unstop|yes)$/.test(word) && false;      // "YES" is a confirmation here, never a re-subscribe
    const resub = /^(start|unstop)$/.test(word);
    // Twilio itself blocks texts to anyone who sent STOP. We also record it, cancel their reminders
    // and take them off every follow-up, so nothing is even attempted.
    let optedOut = false;
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
        optedOut = !!lead.optedOut;
        await db.saveLead(lead);
      } catch (e) { console.error("lead update failed", e && e.message); }
    }
    void start;
    if (from && from !== dan && !stop && !resub && !/^(help|info)$/.test(word)) {
      // The assistant answers clients (and books what they ask for) when Dan has it switched on.
      // Anything it can't do, or any error, falls through to the plain "someone replied" nudge.
      let done = null;
      if (!optedOut && body) { try { done = await ai.handle(from, body); } catch (e) { console.error("assistant error", e && e.message); } }
      if (done) await sms.sendText(from, done.reply);
      // Dan's phone stays quiet unless it matters. An emergency, or a text the assistant could not handle
      // (it is off, or it failed), reaches him right away. Everything else waits on the inbox's Today page
      // and in his one daily summary, unless he chose "text me everything" in Settings.
      const s = await db.settings();
      const emergency = EMERGENCY.test(body);
      const urgent = emergency || !!(done && done.urgent) || !done;
      const who = done ? done.who : sms.prettyPhone(from);
      if (done && done.did.length) await db.logActivity({ phone: from, who: done.who, did: done.did });
      if (done && (done.handoff || emergency)) await db.addNeed({ phone: from, who, text: body.slice(0, 300), reason: done.handoff || "possible emergency", urgent });
      if (dan && (urgent || s.ai.alerts === "all")) {
        const head = (urgent && done ? "URGENT. " : "") + "Fig: " + who + ": \"" + body.slice(0, 160) + "\". ";
        await sms.sendText(dan, head + (done
          ? "Assistant " + (done.did.length ? done.did.join(", ") : "answered") + (done.handoff ? ". Needs you: " + done.handoff : "") + ". figperformance.com/inbox"
          : "Answer at figperformance.com/inbox"));
      }
    }
    return twiml(res);
  } catch (e) {
    console.error("sms webhook error", e && e.message);
    return twiml(res);
  }
};
