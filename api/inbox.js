/*
 * The staff side of the system, behind figperformance.com/inbox (Dan only).
 *   POST {action:"login", password} / {action:"logout"}
 *   GET  ?view=list                         -> text conversations, newest first, with each lead's status
 *   GET  ?view=thread&with=+1714...         -> every text with one person, pending reminders, their lead card
 *   GET  ?view=schedule                     -> consults: last 7 days through the next 30
 *   GET  ?view=settings                     -> consult hours, days off, follow-up texts, calendar feed link
 *   POST {action:"send", to, body}          -> text someone from the gym's number
 *   POST {action:"cancel", sid}             -> cancel one pending reminder
 *   POST {action:"booking", id, set}        -> showed | no_show | cancel
 *   POST {action:"lead", phone, status}     -> new | booked | showed | no_show | signed_up | not_interested
 *   POST {action:"settings", settings}      -> save hours, days off, follow-up texts
 * Texts are read live from Twilio; bookings, leads and settings come from the database.
 */
"use strict";
const crypto = require("crypto");
const sms = require("./_sms.js");
const db = require("./_db.js");

const COOKIE = "__Host-fig_inbox";
const DAYS = 30;

function send(res, status, body) {
  res.statusCode = status;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  res.setHeader("X-Robots-Tag", "noindex");
  res.end(JSON.stringify(body));
}
function secret() { return sms.secret("inbox-session"); }
function sign(exp) { return exp + "." + crypto.createHmac("sha256", secret()).update(String(exp)).digest("hex"); }
function signedIn(req) {
  const m = /(?:^|;\s*)__Host-fig_inbox=([^;]+)/.exec(String(req.headers.cookie || ""));
  if (!m) return false;
  const parts = decodeURIComponent(m[1]).split(".");
  const exp = Number(parts[0]);
  if (!exp || exp < Date.now()) return false;
  const a = Buffer.from(sign(exp)), b = Buffer.from(parts.join("."));
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}
function sameSite(req) {                       // block other websites from posting here with Dan's cookie
  const o = req.headers.origin;
  if (!o) return true;
  try { return new URL(o).host === (req.headers["x-forwarded-host"] || req.headers.host); } catch (e) { return false; }
}
async function body(req) {
  if (req.body && typeof req.body === "object") return req.body;
  const chunks = []; let size = 0;
  for await (const c of req) { size += c.length; if (size > 10000) break; chunks.push(c); }
  try { return JSON.parse(Buffer.concat(chunks).toString("utf8") || "{}"); } catch (e) { return {}; }
}
const sleep = ms => new Promise(r => setTimeout(r, ms));

function slim(m) {
  const inbound = m.direction === "inbound";
  return {
    sid: m.sid, inbound, body: m.body || "", status: m.status,
    at: m.status === "scheduled" ? null : (m.date_sent || m.date_created),
    with: inbound ? m.from : m.to
  };
}
function nameFrom(msgs) {                      // our own texts start "Hi Maria, ..."
  for (let i = msgs.length - 1; i >= 0; i--) {
    const m = /^Hi ([^,]{1,30}),/.exec(msgs[i].inbound ? "" : msgs[i].body);
    if (m && m[1] !== "there") return m[1];
  }
  return null;
}

async function list() {
  const dan = sms.usPhone(process.env.DAN_MOBILE);
  const all = (await sms.listMessages(null, 6)).map(slim).filter(m => m.with && m.with !== dan);   // up to 2,400 texts back
  const by = {};
  all.forEach(m => { (by[m.with] = by[m.with] || []).push(m); });   // Twilio returns newest first
  const convos = Object.keys(by).map(num => {
    const msgs = by[num];
    const sent = msgs.filter(m => m.status !== "scheduled" && m.status !== "canceled");
    const last = sent[0] || msgs[0];
    return {
      with: num, name: nameFrom(msgs.slice().reverse()),
      last: last.body.slice(0, 140), lastInbound: last.inbound, at: last.at,
      needsReply: !!(sent[0] && sent[0].inbound),
      pending: msgs.filter(m => m.status === "scheduled").length
    };
  }).filter(c => c.at).sort((a, b) => Date.parse(b.at) - Date.parse(a.at)).slice(0, 150);
  if (db.configured() && convos.length) {
    const leads = await db.getLeads(convos.map(c => c.with));
    convos.forEach((c, i) => { const l = leads[i]; if (l) { c.name = l.name ? sms.first(l.name) : c.name; c.status = l.status; c.optedOut = !!l.optedOut; } });
  }
  return convos;
}

async function thread(num) {
  const [to, from] = await Promise.all([sms.listMessages({ To: num, PageSize: "200" }), sms.listMessages({ From: num, PageSize: "200" })]);
  const msgs = to.concat(from).map(slim).filter(m => m.status !== "canceled");
  const sent = msgs.filter(m => m.at).sort((a, b) => Date.parse(a.at) - Date.parse(b.at));
  const pending = to.filter(m => m.status === "scheduled").reverse().map(m => ({ sid: m.sid, body: m.body, status: "scheduled" }));
  const out = { with: num, name: nameFrom(sent), messages: sent, pending, lead: null };
  if (db.configured()) {
    const l = await db.getLead(num);
    if (l) {
      const bk = l.bookingId ? await db.getBooking(l.bookingId) : null;
      out.name = l.name || out.name;
      out.lead = { name: l.name, status: l.status, goal: l.goal || "", optedOut: !!l.optedOut, marketing: !!(l.consent && l.consent.marketingTexts),
        consentAt: l.consent ? l.consent.at : null, followStep: l.followStep || 0,
        booking: bk ? { id: bk.id, start: bk.start, status: bk.status, confirmed: !!bk.confirmed } : null };
    }
  }
  return out;
}

async function schedule() {
  const now = Date.now(), list = await db.bookingsBetween(now - 7 * 864e5, now + 30 * 864e5);
  const leads = await db.getLeads(list.map(b => b.phone));
  return list.map((b, i) => ({ id: b.id, name: b.name, phone: b.phone, goal: b.goal || "", start: b.start, status: b.status, confirmed: !!b.confirmed,
    source: b.source || "", leadStatus: leads[i] ? leads[i].status : null, optedOut: !!(leads[i] && leads[i].optedOut),
    marketing: !!(leads[i] && leads[i].consent && leads[i].consent.marketingTexts) }));
}

/* Dan marks what happened. "Showed" and "no-show" start the follow-up plan (marketing texts only with consent). */
async function setLeadStatus(lead, status, baseIso) {
  const s = await db.settings();
  lead.status = status;
  await db.stopFollowups(lead.phone);
  if ((status === "showed" || status === "no_show") && lead.consent && lead.consent.marketingTexts && !lead.optedOut && s.followups.length) {
    lead.followBase = baseIso || new Date().toISOString(); lead.followStep = 0;
    await db.scheduleFollowup(lead.phone, Math.max(Date.now() + 3600 * 1000, Date.parse(lead.followBase) + s.followups[0].day * 864e5));
  }
  await db.saveLead(lead);
}
async function markBooking(id, set) {
  const bk = await db.getBooking(id);
  if (!bk) return { ok: false, error: "not_found" };
  const lead = (await db.getLead(bk.phone)) || { phone: bk.phone, name: bk.name, created: new Date().toISOString() };
  if (set === "cancel") {
    if (bk.status !== "booked") return { ok: false, error: "closed" };
    const oldStart = bk.start;
    await db.cancelBooking(bk, "dan");
    if (sms.configured() && !lead.optedOut) { await sms.cancelScheduled(bk.phone); await sms.sendText(bk.phone, sms.cancelledText(bk.name, oldStart)); }
    lead.status = "new"; await db.saveLead(lead);
    return { ok: true };
  }
  if (set !== "showed" && set !== "no_show") return { ok: false, error: "set" };
  if (bk.status === "cancelled") return { ok: false, error: "closed" };
  const first = bk.status === "booked";
  bk.status = set; await db.saveBooking(bk);
  if (sms.configured()) await sms.cancelScheduled(bk.phone);
  // One "sorry we missed you" text about their own appointment (not marketing), unless they opted out.
  if (set === "no_show" && first && sms.configured() && !lead.optedOut && !sms.quietHours()) {
    const s = await db.settings();
    await sms.sendText(bk.phone, s.noShowText.replace(/\{first\}/g, sms.first(bk.name)));
  }
  await setLeadStatus(lead, set, bk.start);
  return { ok: true };
}

module.exports = async function handler(req, res) {
  try {
    const pw = process.env.INBOX_PASSWORD || "";
    if (pw.length < 12) return send(res, 503, { error: "not_configured", need: "INBOX_PASSWORD" });
    if (!process.env.TWILIO_AUTH_TOKEN && (process.env.SESSION_SECRET || "").length < 32) return send(res, 503, { error: "not_configured", need: "TWILIO" });
    if (!sameSite(req)) return send(res, 403, { error: "forbidden" });

    if (req.method === "POST") {
      const ct = String(req.headers["content-type"] || "");
      if (!ct.includes("application/json")) return send(res, 415, { error: "json_only" });
      const b = await body(req);
      if (b.action === "login") {
        if (sms.tooMany("login:" + sms.clientIp(req), 8, 10 * 60 * 1000)) return send(res, 429, { error: "slow_down" });
        await sleep(700);                                    // slows password guessing
        const a = crypto.createHash("sha256").update(String(b.password || "")).digest();
        const want = crypto.createHash("sha256").update(pw).digest();
        if (!crypto.timingSafeEqual(a, want)) return send(res, 401, { error: "wrong_password" });
        const exp = Date.now() + DAYS * 864e5;
        res.setHeader("Set-Cookie", COOKIE + "=" + encodeURIComponent(sign(exp)) + "; Path=/; Max-Age=" + DAYS * 86400 + "; HttpOnly; Secure; SameSite=Strict");
        return send(res, 200, { ok: true });
      }
      if (b.action === "logout") {
        res.setHeader("Set-Cookie", COOKIE + "=; Path=/; Max-Age=0; HttpOnly; Secure; SameSite=Strict");
        return send(res, 200, { ok: true });
      }
      if (!signedIn(req)) return send(res, 401, { error: "sign_in" });
      if ((b.action === "send" || b.action === "cancel") && !sms.configured()) return send(res, 503, { error: "not_configured", need: "TWILIO" });
      if (b.action === "send") {
        const to = sms.usPhone(b.to), text = String(b.body || "").trim();
        if (!to) return send(res, 400, { error: "phone" });
        if (!text || text.length > 1200) return send(res, 400, { error: "body" });
        if (db.configured()) { const l = await db.getLead(to); if (l && l.optedOut) return send(res, 409, { error: "opted_out" }); }
        const m = await sms.sendText(to, text);
        return m ? send(res, 200, { ok: true }) : send(res, 502, { error: "send_failed" });
      }
      if (b.action === "cancel") {
        if (!/^(SM|MM)[0-9a-f]{32}$/i.test(String(b.sid || ""))) return send(res, 400, { error: "sid" });
        const r = await sms.twilio("/Messages/" + b.sid + ".json", { Status: "canceled" });
        return send(res, r.ok ? 200 : 502, { ok: r.ok });
      }
      if (!db.configured()) return send(res, 503, { error: "not_configured", need: "DATABASE" });
      if (b.action === "booking") return send(res, 200, await markBooking(b.id, b.set));
      if (b.action === "lead") {
        const phone = sms.usPhone(b.phone);
        if (!phone || db.LEAD_STATUSES.indexOf(b.status) < 0) return send(res, 400, { error: "lead" });
        const lead = (await db.getLead(phone)) || { phone, created: new Date().toISOString() };
        await setLeadStatus(lead, b.status);
        return send(res, 200, { ok: true });
      }
      if (b.action === "settings") {
        const clean = db.cleanSettings(b.settings);
        await db.setJSON("settings", clean);
        return send(res, 200, { ok: true, settings: clean });
      }
      return send(res, 400, { error: "action" });
    }

    if (req.method === "GET") {
      if (!signedIn(req)) return send(res, 401, { error: "sign_in" });
      const q = new URL(req.url, "http://x").searchParams;
      if (q.get("view") === "schedule" || q.get("view") === "settings") {
        if (!db.configured()) return send(res, 503, { error: "not_configured", need: "DATABASE" });
        if (q.get("view") === "schedule") return send(res, 200, { bookings: await schedule(), texting: sms.configured() });
        const host = req.headers["x-forwarded-host"] || req.headers.host;
        return send(res, 200, { settings: await db.settings(), texting: sms.configured(), feed: "https://" + host + "/api/cal?k=" + sms.feedKey() });
      }
      if (!sms.configured()) return send(res, 503, { error: "not_configured", need: "TWILIO" });
      if (q.get("view") === "thread") {
        const num = sms.usPhone(q.get("with"));
        if (!num) return send(res, 400, { error: "phone" });
        return send(res, 200, await thread(num));
      }
      return send(res, 200, { conversations: await list() });
    }
    res.setHeader("Allow", "GET, POST");
    return send(res, 405, { error: "method" });
  } catch (e) {
    console.error("inbox error", e && e.message);
    return send(res, 500, { error: "server" });
  }
};
