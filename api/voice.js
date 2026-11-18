/*
 * Phone calls to the gym's texting number, and the missed-call text-back.
 * Twilio calls this address when someone phones the number (set as the number's "A call comes in" webhook:
 * https://www.figperformance.com/api/voice).
 *   1. If "ring my cell first" is on, the call rings Dan's own phone for 18 seconds.
 *   2. If Dan doesn't pick up (or ringing is off because his carrier already tried him), the caller hears a
 *      short message and gets ONE text so the conversation carries on in the inbox.
 * A caller gets at most one of these texts in 12 hours, and never if they have replied STOP.
 */
"use strict";
const sms = require("./_sms.js");
const db = require("./_db.js");

function xml(res, inner) {
  res.statusCode = 200; res.setHeader("Content-Type", "text/xml; charset=utf-8"); res.setHeader("Cache-Control", "no-store");
  res.end("<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response>" + inner + "</Response>");
}
async function form(req) {
  if (req.body && typeof req.body === "object") return req.body;
  const chunks = []; let size = 0;
  for await (const c of req) { size += c.length; if (size > 20000) break; chunks.push(c); }
  return Object.fromEntries(new URLSearchParams(Buffer.concat(chunks).toString("utf8")));
}
const SORRY = "<Say voice=\"alice\">Thanks for calling Fig Performance. Coach Dan is with a client right now. We just sent you a text message, so you can reply there and he will get right back to you.</Say><Hangup/>";
const PLAIN = "<Say voice=\"alice\">Thanks for calling Fig Performance. Coach Dan is with a client right now. Please send a text to this number and he will get right back to you.</Say><Hangup/>";

async function textBack(from, s) {
  const dan = sms.usPhone(process.env.DAN_MOBILE);
  if (!from || from === dan || !s.missedCall.on) return false;
  if ((await db.cmd("SET", "missed:" + from, "1", "NX", "EX", String(12 * 3600))) !== "OK") return false;      // one per caller per 12 hours
  const lead = (await db.getLead(from)) || { phone: from, created: new Date().toISOString(), status: "new", source: "phone call" };
  if (lead.optedOut) return false;
  const ok = await sms.sendText(from, s.missedCall.text);
  lead.missedCallAt = new Date().toISOString(); await db.saveLead(lead);
  await sms.tellDan("Fig inbox: missed call from " + (lead.name ? lead.name + " " : "") + sms.prettyPhone(from) + (ok ? ". They got your missed-call text." : ". The auto-text could not be sent.") + " figperformance.com/inbox");
  return !!ok;
}

module.exports = async function handler(req, res) {
  try {
    if (req.method !== "POST" || !sms.configured()) { res.statusCode = 404; return res.end("not found"); }
    const p = await form(req);
    if (!sms.validTwilioSignature(req, p)) { res.statusCode = 403; return res.end("forbidden"); }
    const after = /[?&]step=after(&|$)/.test(req.url || "");
    const from = sms.usPhone(p.From), dan = sms.usPhone(process.env.DAN_MOBILE);
    const s = db.configured() ? await db.settings() : db.cleanSettings({});
    if (!after && s.missedCall.ring && dan && from !== dan) {
      return xml(res, "<Dial timeout=\"18\" answerOnBridge=\"true\" action=\"/api/voice?step=after\" method=\"POST\"><Number>" + dan + "</Number></Dial>");
    }
    if (after && p.DialCallStatus === "completed") return xml(res, "<Hangup/>");          // Dan answered
    const sent = db.configured() ? await textBack(from, s) : false;
    return xml(res, sent ? SORRY : PLAIN);
  } catch (e) {
    console.error("voice webhook error", e && e.message);
    return xml(res, PLAIN);
  }
};
