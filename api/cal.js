/*
 * Dan's calendar feed. Subscribing to this address in Apple Calendar or Google Calendar shows
 * every consult on his own calendar (they refresh on their own schedule, often hourly).
 * The address contains a private key (shown on the inbox Settings tab); without it: 404.
 */
"use strict";
const sms = require("./_sms.js");
const db = require("./_db.js");

function stamp(d) { return new Date(d).toISOString().replace(/[-:]/g, "").replace(/\.\d{3}/, ""); }
function esc(s) { return String(s || "").replace(/\\/g, "\\\\").replace(/[,;]/g, m => "\\" + m).replace(/\r?\n/g, "\\n"); }

module.exports = async function handler(req, res) {
  try {
    const q = new URL(req.url, "http://x").searchParams, k = q.get("k") || "";
    if (!db.configured()) { res.statusCode = 404; return res.end("not found"); }
    if (q.get("b")) {                                        // a client's own "Add to my calendar" file
      const b = await db.getBooking(q.get("b"));
      if (!b || b.status === "cancelled") { res.statusCode = 404; return res.end("not found"); }
      const ics = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Fig Performance//Consults//EN", "METHOD:PUBLISH", "BEGIN:VEVENT",
        "UID:" + b.id.slice(0, 12) + "-client@figperformance.com", "DTSTAMP:" + stamp(b.created), "DTSTART:" + stamp(b.start),
        "DTEND:" + stamp(Date.parse(b.start) + 3600 * 1000), "SUMMARY:Free consultation at Fig Performance",
        "LOCATION:" + esc("Fig Performance, " + sms.ADDRESS + ", CA 92870"),
        "DESCRIPTION:" + esc("InBody scan, assessment and game plan with Coach Dan. Wear workout clothes.\nQuestions: (714) 396-7178"),
        "BEGIN:VALARM", "TRIGGER:-PT2H", "ACTION:DISPLAY", "DESCRIPTION:Consult at Fig Performance", "END:VALARM", "END:VEVENT", "END:VCALENDAR"].join("\r\n");
      res.statusCode = 200; res.setHeader("Content-Type", "text/calendar; charset=utf-8");
      res.setHeader("Content-Disposition", "attachment; filename=\"fig-performance-consult.ics\""); res.setHeader("Cache-Control", "private, no-store");
      return res.end(ics);
    }
    if (!sms.safeEqual(k, sms.feedKey())) { res.statusCode = 404; return res.end("not found"); }
    const now = Date.now();
    const list = (await db.bookingsBetween(now - 30 * 864e5, now + 60 * 864e5)).filter(b => b.status !== "cancelled");
    const lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Fig Performance//Consults//EN", "X-WR-CALNAME:Fig Performance consults", "X-PUBLISHED-TTL:PT30M"];
    list.forEach(b => {
      lines.push("BEGIN:VEVENT", "UID:" + b.id + "@figperformance.com", "DTSTAMP:" + stamp(b.created), "DTSTART:" + stamp(b.start),
        "DTEND:" + stamp(Date.parse(b.start) + 3600 * 1000), "SUMMARY:" + esc("Consult: " + b.name),
        "LOCATION:" + esc("Fig Performance, " + sms.ADDRESS),
        "DESCRIPTION:" + esc(sms.prettyPhone(b.phone) + (b.goal ? "\nGoal: " + b.goal : "") + "\nStatus: " + b.status), "END:VEVENT");
    });
    lines.push("END:VCALENDAR");
    res.statusCode = 200;
    res.setHeader("Content-Type", "text/calendar; charset=utf-8");
    res.setHeader("Cache-Control", "private, no-store");
    res.setHeader("X-Robots-Tag", "noindex");
    return res.end(lines.join("\r\n"));
  } catch (e) { res.statusCode = 500; return res.end("error"); }
};
