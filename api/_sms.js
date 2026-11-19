/*
 * Fig Performance texting helper (shared by the booking, inbox and webhook functions).
 * Twilio is the phone company here and also keeps the text history: the inbox page reads
 * conversations from Twilio. Bookings, leads and settings live in the database (api/_db.js).
 *
 * Settings (Vercel > Project > Settings > Environment Variables). Never put these in site files:
 *   TWILIO_ACCOUNT_SID            starts with AC
 *   TWILIO_AUTH_TOKEN             the account's secret
 *   TWILIO_MESSAGING_SERVICE_SID  starts with MG (the Messaging Service that holds the gym's number)
 *   INBOX_PASSWORD                the password Dan types to open /inbox (12+ characters)
 *   DAN_MOBILE                    optional. Dan's own cell: gets a short text when a client replies
 *   SESSION_SECRET                optional. 32+ random characters. If unset, a secret is derived from
 *                                 the Twilio auth token or the database token (never from the inbox
 *                                 password, which is guessable).
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

/* +1 numbers outside the US, Canada and US territories, and premium codes: common toll-fraud targets. */
const BLOCKED_AREA = new Set(["242", "246", "264", "268", "284", "345", "441", "473", "649", "658", "664", "721", "758", "767", "784",
  "809", "829", "849", "868", "869", "876", "900", "976"]);
function usPhone(v) {
  let d = String(v || "").replace(/\D/g, "");
  if (d.length === 11 && d[0] === "1") d = d.slice(1);
  if (d.length !== 10 || /^[01]/.test(d) || /^[01]/.test(d.slice(3)) || BLOCKED_AREA.has(d.slice(0, 3))) return null;
  return "+1" + d;
}

/* One strong secret for sign-in cookies, the Calendly hook address and booking signatures. */
function secret(purpose) {
  // Any one of these long random secrets works; the database token is there as soon as the database is connected.
  const base = (process.env.SESSION_SECRET || "").length >= 32 ? process.env.SESSION_SECRET
    : String(process.env.TWILIO_AUTH_TOKEN || process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN || "");
  return crypto.createHmac("sha256", base).update("fig:" + purpose).digest();
}
function safeEqual(x, y) { const a = Buffer.from(String(x)), b = Buffer.from(String(y)); return a.length === b.length && crypto.timingSafeEqual(a, b); }

/* Best-effort limiter (per server instance). The real limit is a Vercel Firewall rule; this is a backstop. */
const hits = new Map();
function tooMany(key, max, windowMs) {
  const now = Date.now(), arr = (hits.get(key) || []).filter(t => now - t < windowMs);
  arr.push(now); hits.set(key, arr);
  if (hits.size > 5000) hits.clear();
  return arr.length > max;
}
function clientIp(req) { return String(req.headers["x-forwarded-for"] || "").split(",")[0].trim() || "unknown"; }

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
  if (!r.ok) {
    console.error("twilio send failed", r.status, r.j && r.j.code);                           // no message bodies or numbers in logs
    try { const db = require("./_db.js"); if (db.configured()) await db.pipeline([["INCR", "health:sendfail"], ["EXPIRE", "health:sendfail", "21600"]]); } catch (e) { /* counting failures is best-effort */ }
    return null;
  }
  return r.j;
}

async function listMessages(query, maxPages) {
  const sid = process.env.TWILIO_ACCOUNT_SID;
  const qs = new URLSearchParams(Object.assign({ PageSize: "400" }, query || {})).toString();
  let path = "/Messages.json?" + qs, out = [];
  for (let i = 0; i < (maxPages || 1) && path; i++) {
    const r = await twilio(path);
    if (!r.ok) break;
    out = out.concat(r.j.messages || []);
    const next = r.j.next_page_uri;                           // e.g. /2010-04-01/Accounts/AC.../Messages.json?Page=1...
    path = next && next.indexOf("/Accounts/" + sid + "/") > 0 ? next.slice(next.indexOf("/Accounts/" + sid) + ("/Accounts/" + sid).length) : null;
  }
  return out;
}

/* Has this number been texted by us in the last `hours`, or does it have a reminder waiting? */
async function recentlyTexted(to, hours) {
  const msgs = await listMessages({ To: to, PageSize: "30" });
  const since = Date.now() - hours * 3600 * 1000;
  return msgs.some(m => m.status === "scheduled" || (m.status !== "canceled" && Date.parse(m.date_created) > since));
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
function first(name) { return String(name || "there").trim().split(/\s+/)[0].replace(/[^\p{L}\p{N}'-]/gu, "").slice(0, 30) || "there"; }   // no dots: a name must never become a link

/* The three texts every consult gets. Wording lives here so it's easy to change in one place. */
function confirmationText(name, startIso, moved, manageUrl) {
  const w = when(startIso);
  return "Hi " + first(name) + ", it's Coach Dan at Fig Performance. " +
    (moved ? "Your free consult is now " : "You're confirmed for your free consult ") + w.day + " at " + w.time +
    ", " + ADDRESS + ". Questions? Just reply here." + (manageUrl ? " Change or cancel: " + manageUrl : "") +
    " Msg & data rates may apply. Reply STOP to opt out, HELP for help.";
}
function cancelledText(name, startIso) {
  const w = when(startIso);
  return "Hi " + first(name) + ", your free consult at Fig Performance on " + w.day + " at " + w.time +
    " is cancelled. To pick a new time: figperformance.com/#consult or reply here. Reply STOP to opt out.";
}
function prettyPhone(p) { return String(p).replace(/^\+1(\d{3})(\d{3})(\d{4})$/, "($1) $2-$3"); }
/* A heads-up to Dan's own phone. Never throws. */
async function tellDan(text) {
  try { const dan = usPhone(process.env.DAN_MOBILE); if (dan) await sendText(dan, text); } catch (e) { /* not critical */ }
}
/* Marketing texts may only go out 9 AM to 8 PM Pacific (federal rule is 8 AM to 9 PM local; this stays inside it). */
function quietHours(now) {
  const h = +new Intl.DateTimeFormat("en-US", { timeZone: TZ, hourCycle: "h23", hour: "2-digit" }).format(now || new Date());
  return h < 9 || h >= 20;
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

/* Heads-ups to Dan's own phone before a consult: one early (5 AM that day, or 8 PM the night before for
   a consult before 7 AM) and one an hour before. Returns the scheduled message IDs so a cancel or move can
   pull exactly these two, never anything else queued for Dan. */
function pacificClock(iso) {
  const parts = new Intl.DateTimeFormat("en-US", { timeZone: TZ, hourCycle: "h23", hour: "2-digit", minute: "2-digit" }).formatToParts(new Date(iso));
  const get = t => +parts.find(x => x.type === t).value;
  return get("hour") * 60 + get("minute");
}
async function scheduleDanReminders(b) {
  const dan = usPhone(process.env.DAN_MOBILE);
  if (!dan || !configured()) return [];
  const start = Date.parse(b.start), w = when(b.start), mins = pacificClock(b.start);
  const who = String(b.name || "").slice(0, 40) + ", " + prettyPhone(b.phone);
  const early = mins >= 7 * 60
    ? new Date(start - (mins - 5 * 60) * 60000)                 // 5:00 AM the same day
    : new Date(start - (mins + 4 * 60) * 60000);               // 8:00 PM the night before
  const out = [];
  const a = await sendText(dan, "Fig: consult " + (mins >= 7 * 60 ? "today" : "tomorrow") + " at " + w.time + " with " + who + ". 90-min block.", early);
  if (a && a.sid) out.push(a.sid);
  const c = await sendText(dan, "Fig: consult in 1 hour (" + w.time + ") with " + who + ".", new Date(start - 3600 * 1000));
  if (c && c.sid) out.push(c.sid);
  return out;
}
async function cancelSids(sids) {
  let n = 0;
  for (const sid of sids || []) { try { const r = await twilio("/Messages/" + sid + ".json", { Status: "canceled" }); if (r.ok) n++; } catch (e) { /* already sent or gone */ } }
  return n;
}

/* Carrier approval of the texting registration (A2P 10DLC campaign). Until it says VERIFIED, carriers block our texts.
   Returns "approved", "in_review", "failed" or "unknown". */
async function carrierStatus() {
  const mg = process.env.TWILIO_MESSAGING_SERVICE_SID;
  if (!configured() || !mg) return "unknown";
  try {
    const sid = process.env.TWILIO_ACCOUNT_SID;
    const r = await fetch("https://messaging.twilio.com/v1/Services/" + mg + "/Compliance/Usa2p",
      { headers: { Authorization: "Basic " + Buffer.from(sid + ":" + process.env.TWILIO_AUTH_TOKEN).toString("base64") } });
    if (!r.ok) return "unknown";
    const j = await r.json(), list = (j && j.compliance) || [];
    const st = list.map(c => String(c.campaign_status || "").toUpperCase());
    if (st.includes("VERIFIED")) return "approved";
    if (st.includes("FAILED")) return "failed";
    return st.length ? "in_review" : "unknown";
  } catch (e) { return "unknown"; }
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

/* The private key in Dan's calendar-feed address. */
function feedKey() { return secret("calendar-feed").toString("hex").slice(0, 40); }

module.exports = { configured, twilio, usPhone, sendText, listMessages, recentlyTexted, cancelScheduled, confirmationText, scheduleReminders, validTwilioSignature, feedKey, secret, safeEqual, tooMany, clientIp, first, when, cancelledText, prettyPhone, tellDan, quietHours, scheduleDanReminders, cancelSids, carrierStatus, ADDRESS };
