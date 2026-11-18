/*
 * Fig Performance texting helper (shared by the booking, inbox and webhook functions).
 * Twilio is the phone company here AND the message store: there is no separate database.
 * Every text sent or received lives in the Twilio account and the inbox page reads it from there.
 *
 * Settings (Vercel > Project > Settings > Environment Variables). Never put these in site files:
 *   TWILIO_ACCOUNT_SID            starts with AC
 *   TWILIO_AUTH_TOKEN             the account's secret
 *   TWILIO_MESSAGING_SERVICE_SID  starts with MG (the Messaging Service that holds the gym's number)
 *   INBOX_PASSWORD                the password Dan types to open /inbox (12+ characters)
 *   DAN_MOBILE                    optional. Dan's own cell: gets a short text when a client replies
 */
"use strict";
const crypto = require("crypto");

const TZ = "America/Los_Angeles";
const ADDRESS = "1284 E. Yorba Linda Blvd, Placentia";
const MIN_AHEAD = 16 * 60 * 1000;            // Twilio schedules 15 minutes to 35 days ahead
const MAX_AHEAD = 34 * 24 * 3600 * 1000;

function configured() {
  return !!(process.env.TWILIO_ACCOUNT_SID && process.env.TWILIO_AUTH_TOKEN && process.env.TWILIO_MESSAGING_SERVICE_SID);
}

async function twilio(path, params, method) {
  const sid = process.env.TWILIO_ACCOUNT_SID;
  const url = "https://api.twilio.com/2010-04-01/Accounts/" + sid + path;
  const opts = {
    method: method || (params ? "POST" : "GET"),
    headers: { Authorization: "Basic " + Buffer.from(sid + ":" + process.env.TWILIO_AUTH_TOKEN).toString("base64") }
  };
  if (params && opts.method === "POST") {
    opts.headers["Content-Type"] = "application/x-www-form-urlencoded";
    opts.body = new URLSearchParams(params).toString();
  }
  const r = await fetch(url, opts);
  let j = {};
  try { j = await r.json(); } catch (e) { /* empty */ }
  return { ok: r.ok, status: r.status, j };
}

function usPhone(v) {
  let d = String(v || "").replace(/\D/g, "");
  if (d.length === 11 && d[0] === "1") d = d.slice(1);
  if (d.length !== 10 || /^[01]/.test(d)) return null;
  return "+1" + d;
}

/* Send a text now, or at `sendAt` (a Date) if given. Returns the Twilio message or null. */
async function sendText(to, body, sendAt) {
  if (!configured()) return null;
  const p = { To: to, Body: String(body).slice(0, 1200), MessagingServiceSid: process.env.TWILIO_MESSAGING_SERVICE_SID };
  if (sendAt) {
    const ahead = sendAt.getTime() - Date.now();
    if (ahead < MIN_AHEAD || ahead > MAX_AHEAD) return null;
    p.ScheduleType = "fixed";
    p.SendAt = sendAt.toISOString();
  }
  const r = await twilio("/Messages.json", p);
  if (!r.ok) { console.error("twilio send failed", r.status, JSON.stringify(r.j).slice(0, 300)); return null; }
  return r.j;
}

async function listMessages(query) {
  const qs = new URLSearchParams(Object.assign({ PageSize: "400" }, query || {})).toString();
  const r = await twilio("/Messages.json?" + qs);
  return r.ok ? (r.j.messages || []) : [];
}

/* Cancel every not-yet-sent reminder to one number (used when a consult is cancelled or moved). */
async function cancelScheduled(to) {
  const msgs = await listMessages({ To: to, PageSize: "100" });
  let n = 0;
  for (const m of msgs) {
    if (m.status !== "scheduled") continue;
    const r = await twilio("/Messages/" + m.sid + ".json", { Status: "canceled" });
    if (r.ok) n++;
  }
  return n;
}

function when(iso) {
  const d = new Date(iso);
  const day = new Intl.DateTimeFormat("en-US", { timeZone: TZ, weekday: "short", month: "short", day: "numeric" }).format(d);
  const time = new Intl.DateTimeFormat("en-US", { timeZone: TZ, hour: "numeric", minute: "2-digit" }).format(d);
  return { day, time };
}
function first(name) { return String(name || "there").trim().split(/\s+/)[0].replace(/[^\p{L}\p{N}'.-]/gu, "").slice(0, 30) || "there"; }

/* The three texts every consult gets. Wording lives here so it's easy to change in one place. */
function confirmationText(name, startIso, moved) {
  const w = when(startIso);
  return "Hi " + first(name) + ", it's Coach Dan at Fig Performance. " +
    (moved ? "Your free consult is now " : "You're confirmed for your free consult ") + w.day + " at " + w.time +
    ", " + ADDRESS + ". Questions or need to change it? Just reply here. Reply STOP to opt out.";
}
async function scheduleReminders(phone, name, startIso) {
  const start = Date.parse(startIso), w = when(startIso);
  const out = [];
  out.push(await sendText(phone,
    "Hi " + first(name) + ", Coach Dan here. Your free consult at Fig Performance is tomorrow at " + w.time +
    ". Reply YES to confirm, or tell me if you need a different time.", new Date(start - 24 * 3600 * 1000)));
  out.push(await sendText(phone,
    "See you at " + w.time + " today at Fig Performance, " + ADDRESS + ". Wear workout clothes. We'll start with your InBody scan.",
    new Date(start - 2 * 3600 * 1000)));
  return out.filter(Boolean).length;
}

/* Twilio signs every webhook it sends. Reject anything that isn't really from Twilio. */
function validTwilioSignature(req, params) {
  const sig = String(req.headers["x-twilio-signature"] || "");
  if (!sig || !process.env.TWILIO_AUTH_TOKEN) return false;
  const host = req.headers["x-forwarded-host"] || req.headers.host;
  let data = "https://" + host + req.url;
  Object.keys(params).sort().forEach(function (k) { data += k + params[k]; });
  const want = crypto.createHmac("sha1", process.env.TWILIO_AUTH_TOKEN).update(Buffer.from(data, "utf8")).digest("base64");
  const a = Buffer.from(sig), b = Buffer.from(want);
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

/* A secret only this site can compute, used to protect the Calendly webhook address. */
function hookKey() {
  return crypto.createHmac("sha256", String(process.env.INBOX_PASSWORD || "")).update("calendly-hook").digest("hex").slice(0, 40);
}

module.exports = { configured, twilio, usPhone, sendText, listMessages, cancelScheduled, confirmationText, scheduleReminders, validTwilioSignature, hookKey, first, when };
