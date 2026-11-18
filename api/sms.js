/*
 * Incoming texts. Twilio calls this address every time a client texts the gym's number.
 * The message itself is already saved in Twilio (the inbox page reads it from there), so all
 * this does is check the call is really from Twilio and nudge Dan's own phone.
 * Set as the Messaging Service's "incoming message" webhook: https://www.figperformance.com/api/sms
 */
"use strict";
const sms = require("./_sms.js");

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
    // Opt-out words are handled by Twilio itself; don't forward those.
    if (from && dan && from !== dan && !/^(stop|stopall|unsubscribe|cancel|end|quit|start|unstop|help|info)$/i.test(body)) {
      await sms.sendText(dan, "Fig inbox: " + from.replace(/^\+1(\d{3})(\d{3})(\d{4})$/, "($1) $2-$3") + " replied: \"" +
        body.slice(0, 200) + "\". Answer at figperformance.com/inbox");
    }
    return twiml(res);
  } catch (e) {
    console.error("sms webhook error", e && e.message);
    return twiml(res);
  }
};
