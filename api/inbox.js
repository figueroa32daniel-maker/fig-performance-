/*
 * The texting inbox behind figperformance.com/inbox (Dan only).
 *   POST {action:"login", password}            -> sets a 30-day sign-in cookie
 *   POST {action:"logout"}
 *   GET  ?view=list                             -> conversations, newest first
 *   GET  ?view=thread&with=+1714...             -> every text with one person (and pending reminders)
 *   POST {action:"send", to, body}              -> text someone from the gym's number
 *   POST {action:"cancel", sid}                 -> cancel one pending reminder
 *   POST {action:"connect"}                     -> subscribe to Calendly so reminders follow the calendar
 * Messages are read live from Twilio; nothing is stored on the website.
 */
"use strict";
const crypto = require("crypto");
const sms = require("./_sms.js");

const COOKIE = "fig_inbox";
const DAYS = 30;

function send(res, status, body) {
  res.statusCode = status;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  res.setHeader("X-Robots-Tag", "noindex");
  res.end(JSON.stringify(body));
}
function secret() { return crypto.createHmac("sha256", String(process.env.INBOX_PASSWORD)).update("inbox-session").digest(); }
function sign(exp) { return exp + "." + crypto.createHmac("sha256", secret()).update(String(exp)).digest("hex"); }
function signedIn(req) {
  const m = /(?:^|;\s*)fig_inbox=([^;]+)/.exec(String(req.headers.cookie || ""));
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
  const all = (await sms.listMessages()).map(slim).filter(m => m.with && m.with !== dan);
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
  }).filter(c => c.at).sort((a, b) => Date.parse(b.at) - Date.parse(a.at));
  return convos;
}

async function thread(num) {
  const [to, from] = await Promise.all([sms.listMessages({ To: num, PageSize: "200" }), sms.listMessages({ From: num, PageSize: "200" })]);
  const msgs = to.concat(from).map(slim).filter(m => m.status !== "canceled");
  const sent = msgs.filter(m => m.at).sort((a, b) => Date.parse(a.at) - Date.parse(b.at));
  const pending = to.filter(m => m.status === "scheduled").reverse().map(m => ({ sid: m.sid, body: m.body, status: "scheduled" }));
  return { with: num, name: nameFrom(sent), messages: sent, pending };
}

async function connectCalendly(req) {
  const tok = process.env.CALENDLY_TOKEN;
  if (!tok) return { ok: false, error: "Add the Calendly key first." };
  const h = { Authorization: "Bearer " + tok, "Content-Type": "application/json" };
  const me = await (await fetch("https://api.calendly.com/users/me", { headers: h })).json();
  if (!me.resource) return { ok: false, error: "Calendly didn't accept the key." };
  const host = req.headers["x-forwarded-host"] || req.headers.host;
  const url = "https://" + host + "/api/calendly-hook?k=" + sms.hookKey();
  const q = "organization=" + encodeURIComponent(me.resource.current_organization) + "&user=" + encodeURIComponent(me.resource.uri) + "&scope=user";
  const existing = await (await fetch("https://api.calendly.com/webhook_subscriptions?" + q, { headers: h })).json();
  if ((existing.collection || []).some(w => w.callback_url === url && w.state === "active")) return { ok: true, already: true };
  const r = await fetch("https://api.calendly.com/webhook_subscriptions", {
    method: "POST", headers: h,
    body: JSON.stringify({ url, events: ["invitee.created", "invitee.canceled"], organization: me.resource.current_organization, user: me.resource.uri, scope: "user" })
  });
  if (r.ok) return { ok: true };
  const j = await r.json().catch(() => ({}));
  return { ok: false, error: (j.message || j.title || "Calendly refused the connection.").slice(0, 200) };
}

module.exports = async function handler(req, res) {
  try {
    const pw = process.env.INBOX_PASSWORD || "";
    if (pw.length < 12) return send(res, 503, { error: "not_configured", need: "INBOX_PASSWORD" });
    if (!sameSite(req)) return send(res, 403, { error: "forbidden" });

    if (req.method === "POST") {
      const ct = String(req.headers["content-type"] || "");
      if (!ct.includes("application/json")) return send(res, 415, { error: "json_only" });
      const b = await body(req);
      if (b.action === "login") {
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
      if (!sms.configured()) return send(res, 503, { error: "not_configured", need: "TWILIO" });
      if (b.action === "send") {
        const to = sms.usPhone(b.to), text = String(b.body || "").trim();
        if (!to) return send(res, 400, { error: "phone" });
        if (!text || text.length > 1200) return send(res, 400, { error: "body" });
        const m = await sms.sendText(to, text);
        return m ? send(res, 200, { ok: true }) : send(res, 502, { error: "send_failed" });
      }
      if (b.action === "cancel") {
        if (!/^(SM|MM)[0-9a-f]{32}$/i.test(String(b.sid || ""))) return send(res, 400, { error: "sid" });
        const r = await sms.twilio("/Messages/" + b.sid + ".json", { Status: "canceled" });
        return send(res, r.ok ? 200 : 502, { ok: r.ok });
      }
      if (b.action === "connect") return send(res, 200, await connectCalendly(req));
      return send(res, 400, { error: "action" });
    }

    if (req.method === "GET") {
      if (!signedIn(req)) return send(res, 401, { error: "sign_in" });
      if (!sms.configured()) return send(res, 503, { error: "not_configured", need: "TWILIO" });
      const q = new URL(req.url, "http://x").searchParams;
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
