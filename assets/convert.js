/*  Fig Performance — conversion layer (Nov 24, 2026)
 *
 *  1. "Next open times": shows the 3 soonest free-consult openings right under
 *     the hero, from the gym's own booking engine (/api/booking). The strip
 *     stays hidden unless real times come back, so it can never show a lie.
 *  2. Sticky mobile CTA bar, hidden whenever the real booking picker is on screen.
 *
 *  No dependencies. Fails silently and leaves the page exactly as it was.
 */
(function () {
  "use strict";

  var TZ = "America/Los_Angeles";

  /* ---------------- 1. Next open times ---------------- */

  var strip = document.getElementById("nextopen");

  function dayLabel(d) {
    var fmt = function (x) {
      return x.toLocaleDateString("en-US", { timeZone: TZ, year: "numeric", month: "numeric", day: "numeric" });
    };
    var now = new Date();
    var tomorrow = new Date(now.getTime() + 864e5);
    if (fmt(d) === fmt(now)) return "Today";
    if (fmt(d) === fmt(tomorrow)) return "Tomorrow";
    return d.toLocaleDateString("en-US", { timeZone: TZ, weekday: "short", month: "short", day: "numeric" });
  }

  function timeLabel(d) {
    return d.toLocaleTimeString("en-US", { timeZone: TZ, hour: "numeric", minute: "2-digit" });
  }

  function renderSlots(slots, duration) {
    var list = strip.querySelector(".nextopen-slots");
    var label = strip.querySelector(".nextopen-label");
    if (!list) return;

    var now = Date.now();
    var next = slots
      .map(function (iso) { return new Date(iso); })
      .filter(function (d) { return !isNaN(d) && d.getTime() > now; })
      .sort(function (a, b) { return a - b; })
      .slice(0, 3);

    if (!next.length) return;                     // nothing open: leave the strip hidden

    if (label && duration) {
      label.textContent = "Next open times · Free " + duration + "-min consult";
    }

    var html = "";
    next.forEach(function (d) {
      html += '<li><a class="nextopen-slot" href="#consult">' +
              "<b>" + dayLabel(d) + "</b>" + timeLabel(d) +
              "</a></li>";
    });
    html += '<li><a class="nextopen-all" href="#consult">See all times &rarr;</a></li>';
    list.innerHTML = html;
    strip.hidden = false;
  }

  if (strip) {
    try {
      fetch("/api/booking", { headers: { Accept: "application/json" }, credentials: "same-origin" })
        .then(function (r) { if (!r.ok) throw new Error(String(r.status)); return r.json(); })
        .then(function (j) { renderSlots(j.slots || [], j.duration); })
        .catch(function () { /* strip stays hidden */ });
    } catch (e) { /* strip stays hidden */ }
  }

  /* ---------------- 2. Sticky mobile CTA ---------------- */

  var bar = document.querySelector(".stickycta");
  if (!bar) return;

  document.body.classList.add("has-stickycta");

  // Hide the bar whenever the real booking picker (or the final CTA) is on screen,
  // so it never sits on top of the thing it is pointing at.
  var watch = [document.getElementById("consult"), document.getElementById("final-cta")]
    .filter(Boolean);

  if (watch.length && "IntersectionObserver" in window) {
    var showing = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { showing[e.target.id] = e.isIntersecting; });
      var any = Object.keys(showing).some(function (k) { return showing[k]; });
      bar.setAttribute("data-hidden", any ? "true" : "false");
    }, { threshold: 0.12 });
    watch.forEach(function (el) { io.observe(el); });
  }
})();
