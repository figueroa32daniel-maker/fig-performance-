/*
 * Daily follow-ups (Vercel Cron runs this once a day, mid-morning Pacific; see vercel.json).
 * Sends the next follow-up text to each person who is due, but ONLY if all of these are true:
 *   - they ticked the optional marketing box when they booked
 *   - they have not texted STOP
 *   - Dan hasn't marked them signed up or not interested, and they haven't replied
 *   - it's between 9 AM and 8 PM Pacific
 * It is safe for anyone to call this address: it only does work that is already due, and at most once.
 */
"use strict";
const sms = require("./_sms.js");
const db = require("./_db.js");

function done(res, code, body) { res.statusCode = code; res.setHeader("Content-Type", "application/json"); res.setHeader("Cache-Control", "no-store"); res.end(JSON.stringify(body)); }
function eligible(lead) {
  return lead && lead.consent && lead.consent.marketingTexts === true && !lead.optedOut &&
    (lead.status === "showed" || lead.status === "no_show") && lead.followBase;
}

module.exports = async function handler(req, res) {
  try {
    if (!db.configured()) return done(res, 200, { ok: true, skipped: "not set up" });
    if (sms.tooMany("cron", 6, 3600 * 1000)) return done(res, 429, { error: "slow_down" });
    try { await db.ensureFixed(3); } catch (e) { console.error("fixed sessions fill failed", e && e.message); }   // keeps fixed weekly clients on the calendar
    if (!sms.configured()) return done(res, 200, { ok: true, skipped: "texting not set up" });
    if (sms.quietHours()) return done(res, 200, { ok: true, skipped: "quiet hours" });
    const s = await db.settings(), now = Date.now();
    let sent = 0;
    for (const phone of await db.dueFollowups(now)) {
      // Claim it first (remove from the due list) so a second run can never send the same text twice.
      if (!(await db.cmd("ZREM", "fu:due", phone))) continue;
      const lead = await db.getLead(phone);
      if (!eligible(lead)) continue;
      const step = lead.followStep || 0, plan = s.followups[step];
      if (!plan) continue;
      const ok = await sms.sendText(phone, plan.text.replace(/\{first\}/g, sms.first(lead.name)));
      if (!ok) continue;                                     // failed: dropped rather than retried forever
      sent++;
      lead.followStep = step + 1; lead.lastFollowAt = new Date().toISOString();
      await db.saveLead(lead);
      const next = s.followups[step + 1];
      if (next) await db.scheduleFollowup(phone, Date.parse(lead.followBase) + next.day * 864e5);
    }
    // Nudge Dan about yesterday's consults he hasn't marked (follow-ups only start once he does).
    const unmarked = (await db.bookingsBetween(now - 36 * 3600 * 1000, now - 2 * 3600 * 1000)).filter(b => b.status === "booked");
    if (unmarked.length && (await db.cmd("SET", "nudge:" + db.dateKey(new Date()), "1", "NX", "EX", "90000")) === "OK") {
      await sms.tellDan("Fig inbox: " + unmarked.length + " recent consult" + (unmarked.length > 1 ? "s" : "") + " not marked yet (showed or no-show). figperformance.com/inbox");
    }
    // Show-up helper: who is coming in the next 30 hours and hasn't confirmed? Dan gets one text to call them.
    const soon = (await db.bookingsBetween(now, now + 30 * 3600 * 1000)).filter(b => b.status === "booked" && !b.confirmed);
    if (soon.length && (await db.cmd("SET", "unconfirmed:" + db.dateKey(new Date()), "1", "NX", "EX", "90000")) === "OK") {
      await sms.tellDan("Not confirmed yet: " + soon.slice(0, 5).map(b => sms.first(b.name) + " " + sms.when(b.start).day.split(",")[0] + " " + sms.when(b.start).time + " " + sms.prettyPhone(b.phone)).join("; ") + ". A quick call helps them show up.");
    }
    return done(res, 200, { ok: true, sent });
  } catch (e) {
    console.error("cron error", e && e.message);
    return done(res, 500, { error: "server" });
  }
};
