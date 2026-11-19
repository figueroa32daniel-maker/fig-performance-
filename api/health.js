/*
 * A quick "is everything working?" check: https://www.figperformance.com/api/health
 * Says only yes/no for each part (never any keys, names or numbers), so it is safe to be public.
 * The daily job and the outside monitor both read it. Result is remembered for 5 minutes.
 */
"use strict";
const sms = require("./_sms.js");
const db = require("./_db.js");
const ai = require("./_ai.js");

async function check() {
  const out = { database: "off", texting: "off", assistant: ai.configured() ? "ready" : "off", dailyJob: "unknown", booking: "unknown" };
  if (db.configured()) {
    try {
      await db.cmd("SET", "health:ping", String(Date.now()), "EX", "600"); out.database = "ok";
      const last = +(await db.cmd("GET", "health:cron")) || 0;
      out.dailyJob = !last ? "never ran" : (Date.now() - last < 26 * 3600e3 ? "ok" : "late");
      const s = await db.settings();
      out.booking = Object.keys(s.hours).some(d => s.hours[d]) ? "ok" : "no hours set";
      const fails = +(await db.cmd("GET", "health:sendfail")) || 0;
      if (sms.configured()) {
        const r = await sms.twilio(".json");                      // the account itself: are the keys good and the account active?
        const active = !!(r && r.ok && r.j && r.j.status === "active");
        out.texting = !active ? "account problem" : (fails >= 5 ? "sends failing" : "ok");
        const c = await db.carrierWatch();
        out.carrierApproval = c === "approved" ? "approved" : c === "failed" ? "rejected" : c === "in_review" ? "in review" : "unknown";
      }
    } catch (e) { out.database = "error"; }
  }
  const bad = Object.keys(out).filter(k => ["ok", "ready", "off", "approved", "in review", "unknown"].indexOf(out[k]) < 0 && !(k === "dailyJob" && out[k] === "never ran") && !(k === "booking" && out.database === "off"));
  return { ok: bad.length === 0, problems: bad, checks: out, at: new Date().toISOString() };
}

module.exports = async function handler(req, res) {
  res.setHeader("Content-Type", "application/json"); res.setHeader("Cache-Control", "no-store");
  try {
    let body = null;
    if (db.configured()) { try { body = await db.getJSON("health:cache"); } catch (e) { /* fall through to a live check */ } }
    if (!body) {
      body = await check();
      if (db.configured()) { try { await db.cmd("SET", "health:cache", JSON.stringify(body), "EX", "300"); } catch (e) { /* cache is optional */ } }
    }
    res.statusCode = 200; res.end(JSON.stringify(body));
  } catch (e) {
    res.statusCode = 200; res.end(JSON.stringify({ ok: false, problems: ["health check crashed"], at: new Date().toISOString() }));
  }
};
module.exports.check = check;
