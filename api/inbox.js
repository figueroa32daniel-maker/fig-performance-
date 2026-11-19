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
 *   GET  ?view=week&start=YYYY-MM-DD        -> one week: client sessions + consults, and the client list
 *   POST {action:"client", phone, name, note, remove?}   -> add, rename or remove a training client
 *   POST {action:"session", phone, date, hour}           -> put a client on the schedule (one hour)
 *   POST {action:"session_remove", id}                   -> take a session off
 *   POST {action:"copy_week", from, to}                  -> repeat one week's client sessions in another week
 * Texts are read live from Twilio; bookings, leads and settings come from the database.
 */
"use strict";
const crypto = require("crypto");
const sms = require("./_sms.js");
const db = require("./_db.js");
const ai = require("./_ai.js");

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
// The signature includes a fingerprint of the current password, so changing the password signs out every device.
function pwPrint() { return crypto.createHash("sha256").update("fig-pw:" + (process.env.INBOX_PASSWORD || "")).digest("hex").slice(0, 16); }
function sign(exp) { return exp + "." + crypto.createHmac("sha256", secret()).update(String(exp) + ":" + pwPrint()).digest("hex"); }
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
    const cl = await db.clients();
    convos.forEach((c, i) => { const l = leads[i]; if (l) { c.name = l.name ? sms.first(l.name) : c.name; c.status = l.status; c.optedOut = !!l.optedOut; }
      const k = cl.find(x => x.phone === c.with); if (k) { c.name = k.name; c.client = true; } });
  }
  return convos;
}

async function thread(num) {
  const [to, from] = await Promise.all([sms.listMessages({ To: num, PageSize: "200" }), sms.listMessages({ From: num, PageSize: "200" })]);
  const msgs = to.concat(from).map(slim).filter(m => m.status !== "canceled");
  const sent = msgs.filter(m => m.at).sort((a, b) => Date.parse(a.at) - Date.parse(b.at));
  const pending = to.filter(m => m.status === "scheduled").reverse().map(m => ({ sid: m.sid, body: m.body, status: "scheduled" }));
  const out = { with: num, name: nameFrom(sent), messages: sent, pending, lead: null };
  const k = db.configured() ? (await db.clients()).find(x => x.phone === num) : null;
  if (k) out.name = k.name;
  if (db.configured()) {
    const l = await db.getLead(num);
    if (l) {
      const bk = l.bookingId ? await db.getBooking(l.bookingId) : null;
      out.name = (k && k.name) || l.name || out.name;
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
  return list.map((b, i) => ({ id: b.id, name: b.name, phone: b.phone, goal: b.goal || "", start: b.start, status: b.status, confirmed: !!b.confirmed, autoShowed: !!b.autoShowed,
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
    if (bk.danSids && bk.danSids.length) { await sms.cancelSids(bk.danSids); bk.danSids = []; await db.saveBooking(bk); }
    if (sms.configured() && !lead.optedOut) { await sms.cancelScheduled(bk.phone); await sms.sendText(bk.phone, sms.cancelledText(bk.name, oldStart)); }
    lead.status = "new"; await db.saveLead(lead);
    return { ok: true };
  }
  if (set !== "showed" && set !== "no_show") return { ok: false, error: "set" };
  if (bk.status === "cancelled") return { ok: false, error: "closed" };
  const first = bk.status === "booked" || (bk.autoShowed && set === "no_show" && bk.status === "showed");   // Dan correcting an automatic "showed"
  if (set === "no_show") bk.autoShowed = false;
  if (bk.danSids && bk.danSids.length) { await sms.cancelSids(bk.danSids); bk.danSids = []; }
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

/* The daily job marks consults Dan didn't mark by the next morning as "showed", so follow-ups start without him.
   A consult with someone already on the Clients list counts as signed up (no sales follow-ups to a client). */
async function autoMark(now) {
  const list = (await db.bookingsBetween(now - 7 * 864e5, now - 12 * 3600e3)).filter(b => b.status === "booked");
  const cl = await db.clients(), out = { showed: [], signed: [] };
  for (const b of list) {
    if (cl.some(c => c.phone === b.phone)) {
      b.status = "showed"; await db.saveBooking(b);
      const lead = (await db.getLead(b.phone)) || { phone: b.phone, name: b.name, created: new Date().toISOString() };
      lead.status = "signed_up"; await db.stopFollowups(b.phone); await db.saveLead(lead);
      out.signed.push(b.name); continue;
    }
    const r = await markBooking(b.id, "showed");
    if (r.ok) { const fresh = await db.getBooking(b.id); fresh.autoShowed = true; await db.saveBooking(fresh); out.showed.push(b.name); }
  }
  return out;
}

module.exports = async function handler(req, res) {
  try {
    const pw = process.env.INBOX_PASSWORD || "";
    if (pw.length < 12) return send(res, 503, { error: "not_configured", need: "INBOX_PASSWORD" });
    if (!process.env.TWILIO_AUTH_TOKEN && !db.configured() && (process.env.SESSION_SECRET || "").length < 32) return send(res, 503, { error: "not_configured", need: "DATABASE" });
    if (!sameSite(req)) return send(res, 403, { error: "forbidden" });

    if (req.method === "POST") {
      const ct = String(req.headers["content-type"] || "");
      if (!ct.includes("application/json")) return send(res, 415, { error: "json_only" });
      const b = await body(req);
      if (b.action === "login") {
        // Password guessing: 8 tries per 10 minutes per address, and 30 wrong tries an hour from everywhere
        // combined locks the login for the rest of that hour (and texts Dan once). Counted in the database,
        // so it holds across servers.
        const ip = sms.clientIp(req);
        if (sms.tooMany("login:" + ip, 8, 10 * 60 * 1000) || await db.over("login:" + ip, 8, 600, true)) return send(res, 429, { error: "slow_down" });
        if (db.configured() && +(await db.cmd("GET", "rl:loginfail:" + Math.floor(Date.now() / 3600000)) || 0) >= 30) return send(res, 429, { error: "slow_down" });
        await sleep(700);                                    // slows password guessing
        const a = crypto.createHash("sha256").update(String(b.password || "")).digest();
        const want = crypto.createHash("sha256").update(pw).digest();
        if (!crypto.timingSafeEqual(a, want)) {
          if (db.configured()) {
            const hk = "rl:loginfail:" + Math.floor(Date.now() / 3600000);
            const n = (await db.pipeline([["INCR", hk], ["EXPIRE", hk, "3700"]]))[0];
            if (+n === 30) await sms.tellDan("URGENT. Fig inbox: 30 wrong password tries in the last hour. The login is locked until the hour is up. If this wasn't you, change INBOX_PASSWORD in Vercel (Claude can walk you through it).");
          }
          return send(res, 401, { error: "wrong_password" });
        }
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
        if (m && db.configured()) await ai.note(to, "d", text);          // the assistant stays quiet while Dan is in the conversation
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
      if (b.action === "client") {
        const phone = sms.usPhone(b.phone), name = String(b.name || "").replace(/[<>\u0000-\u001F]/g, "").trim().slice(0, 60);
        if (!phone) return send(res, 400, { error: "phone" });
        let list = (await db.clients()).filter(c => c.phone !== phone);
        if (!b.remove) {
          if (name.length < 2) return send(res, 400, { error: "name" });
          const fixed = (Array.isArray(b.fixed) ? b.fixed : []).filter(f => db.DAYS.indexOf(f.dow) >= 0 && +f.hour >= 4 && +f.hour <= 21)
            .map(f => ({ dow: f.dow, hour: +f.hour })).slice(0, 14);
          const old = (await db.clients()).find(c => c.phone === phone) || {};
          const next = Object.assign({}, old, { phone, name, note: String(b.note || "").replace(/[<>]/g, "").trim().slice(0, 200), fixed });
          // Sessions left: a number starts or corrects the count, "" or null stops counting, add: N tops it up.
          if (b.credits === null || b.credits === "") delete next.credits;
          else if (b.credits !== undefined && Number.isFinite(+b.credits)) next.credits = Math.max(-50, Math.min(500, Math.round(+b.credits)));
          if (Number.isFinite(+b.add) && +b.add > 0) next.credits = Math.min(500, (Number.isFinite(next.credits) ? next.credits : 0) + Math.round(+b.add));
          list.push(next);
        }
        await db.saveClients(list);
        if (!b.remove) await db.ensureFixed(3);
        return send(res, 200, { ok: true, clients: await db.clients() });
      }
      if (b.action === "session") {
        const phone = sms.usPhone(b.phone), c = (await db.clients()).find(x => x.phone === phone);
        if (!c) return send(res, 400, { error: "client" });
        if (!/^\d{4}-\d{2}-\d{2}$/.test(String(b.date)) || !(+b.hour >= 4 && +b.hour <= 21)) return send(res, 400, { error: "time" });
        const at = db.zonedToUtc(b.date, String(+b.hour).padStart(2, "0") + ":00");
        if (!at) return send(res, 400, { error: "time" });
        const rec = await db.addSession(c, at.toISOString().replace(".000Z", "Z"));
        return rec ? send(res, 200, { ok: true, session: rec }) : send(res, 409, { error: "taken" });
      }
      if (b.action === "session_remove") return send(res, 200, { ok: await db.removeSession(b.id, b.charge === true) });
      if (b.action === "review") {                         // one Google review request, only when Dan presses the button
        if (!sms.configured()) return send(res, 503, { error: "not_configured", need: "TWILIO" });
        const phone = sms.usPhone(b.phone), list = await db.clients(), c = list.find(x => x.phone === phone), s = await db.settings();
        if (!c) return send(res, 400, { error: "client" });
        if (!s.review.link) return send(res, 400, { error: "no_link" });
        const l = await db.getLead(phone); if (l && l.optedOut) return send(res, 409, { error: "opted_out" });
        if (c.reviewAsked && Date.now() - Date.parse(c.reviewAsked) < 180 * 864e5) return send(res, 409, { error: "already_asked" });
        const m = await sms.sendText(phone, s.review.text.replace(/\{first\}/g, sms.first(c.name)).replace(/\{link\}/g, s.review.link));
        if (!m) return send(res, 502, { error: "send_failed" });
        c.reviewAsked = new Date().toISOString(); await db.saveClients(list);
        return send(res, 200, { ok: true, clients: await db.clients() });
      }
      if (b.action === "need_done") return send(res, 200, { ok: await db.resolveNeed(String(b.id || "")) });
      if (b.action === "assistant_try") {                  // Settings tab: see what the assistant would say. Nothing is booked or sent.
        if (!ai.configured()) return send(res, 503, { error: "not_configured", need: "AI_KEY" });
        const phone = sms.usPhone(b.phone), text = String(b.text || "").trim().slice(0, 600);
        if (!phone || !text) return send(res, 400, { error: "input" });
        const out = await ai.handle(phone, text, { dry: true, timeoutMs: 20000 });
        return send(res, 200, out ? (out.error ? { ok: false, error: out.error } : { ok: true, reply: out.reply, did: out.did, handoff: out.handoff }) : { ok: false, error: "no_reply" });
      }
      if (b.action === "copy_week") {
        const from = db.zonedToUtc(String(b.from), "00:00"), to = db.zonedToUtc(String(b.to), "00:00");
        if (!from || !to) return send(res, 400, { error: "week" });
        const src = await db.sessionsBetween(from.getTime(), from.getTime() + 7 * 864e5 - 1), known = await db.clients();
        let added = 0, skipped = 0;
        for (const s of src) {
          const c = known.find(x => x.phone === s.phone); if (!c) { skipped++; continue; }
          const pp = db.pacificParts(new Date(s.start)), dayOffset = Math.round((Date.parse(db.dateKey(new Date(s.start)) + "T12:00:00Z") - Date.parse(db.dateKey(from) + "T12:00:00Z")) / 864e5);
          const date = db.dateKey(new Date(Date.parse(db.dateKey(to) + "T12:00:00Z") + dayOffset * 864e5));
          const at = db.zonedToUtc(date, String(pp.hour).padStart(2, "0") + ":00");
          if (at && at.getTime() > Date.now() && await db.addSession(c, at.toISOString().replace(".000Z", "Z"))) added++; else skipped++;
        }
        return send(res, 200, { ok: true, added, skipped });
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
      if (q.get("view") === "week") {
        if (!db.configured()) return send(res, 503, { error: "not_configured", need: "DATABASE" });
        const want = /^\d{4}-\d{2}-\d{2}$/.test(q.get("start") || "") ? new Date(q.get("start") + "T20:00:00Z") : new Date();
        const ws = db.weekStart(want), from = ws.getTime(), to = from + 7 * 864e5 - 1;
        const [ses, bks, cl] = await Promise.all([db.sessionsBetween(from, to), db.bookingsBetween(from, to), db.clients()]);
        // How many sessions each client has on the calendar this month (done and still to come).
        const ym = db.dateKey(new Date()).slice(0, 7), m0 = db.zonedToUtc(ym + "-01", "00:00").getTime(), month = {};
        (await db.sessionsBetween(m0, m0 + 32 * 864e5)).forEach(x => { if (db.dateKey(new Date(x.start)).slice(0, 7) === ym) month[x.phone] = (month[x.phone] || 0) + 1; });
        return send(res, 200, { weekStart: db.dateKey(ws), clients: cl, texting: sms.configured(), month, reviewLink: !!(await db.settings()).review.link,
          sessions: ses.map(s => ({ id: s.id, name: s.name, phone: s.phone, start: s.start, fixed: !!s.fixed, by: s.by || "", counted: !!s.counted })),
          consults: bks.filter(b => b.status !== "cancelled").map(b => ({ id: b.id, name: b.name, phone: b.phone, start: b.start, status: b.status, confirmed: !!b.confirmed })) });
      }
      if (q.get("view") === "today") {                       // the home page: what needs Dan, today's schedule, what the assistant did
        if (!db.configured()) return send(res, 503, { error: "not_configured", need: "DATABASE" });
        const now = Date.now(), today = db.dateKey(new Date(now)), d0 = db.zonedToUtc(today, "00:00").getTime();
        let carrier = "unknown"; try { carrier = await db.carrierWatch(); } catch (e) { /* shown as unknown */ }
        const [ses, bks, nd, act, st] = await Promise.all([db.sessionsBetween(d0, d0 + 864e5 - 1), db.bookingsBetween(d0, d0 + 2 * 864e5 - 1), db.needs(), db.activity(), db.settings()]);
        const tomorrowStart = d0 + 864e5;
        const items = ses.map(x => ({ kind: "session", id: x.id, name: x.name, phone: x.phone, start: x.start, by: x.by || "" }))
          .concat(bks.filter(b => b.status !== "cancelled" && Date.parse(b.start) < tomorrowStart).map(b => ({ kind: "consult", id: b.id, name: b.name, phone: b.phone, start: b.start, status: b.status, confirmed: !!b.confirmed })))
          .sort((a, b) => Date.parse(a.start) - Date.parse(b.start));
        const upcomingConsults = bks.filter(b => b.status === "booked" && Date.parse(b.start) >= tomorrowStart).map(b => ({ name: b.name, phone: b.phone, start: b.start, confirmed: !!b.confirmed }));
        return send(res, 200, { now: new Date(now).toISOString(), assistant: { on: st.ai.on, ready: ai.configured(), alerts: st.ai.alerts },
          texting: sms.configured(), carrier, needs: nd.filter(n => !n.done).slice(0, 20), activity: act.slice(0, 12), today: items, tomorrowConsults: upcomingConsults });
      }
      if (q.get("view") === "schedule" || q.get("view") === "settings") {
        if (!db.configured()) return send(res, 503, { error: "not_configured", need: "DATABASE" });
        if (q.get("view") === "schedule") return send(res, 200, { bookings: await schedule(), texting: sms.configured() });
        const host = req.headers["x-forwarded-host"] || req.headers.host;
        return send(res, 200, { settings: await db.settings(), texting: sms.configured(), assistant: ai.configured(), feed: "https://" + host + "/api/cal?k=" + sms.feedKey() });
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
module.exports.autoMark = autoMark;
