/* "Manage my booking" page: view, add to calendar, reschedule or cancel. Reads ?t=<private code>. */
(function () {
  "use strict";
  var root = document.getElementById("mg"), TZ = "America/Los_Angeles", PHONE = "(714) 396-7178", TEL = "tel:+17143967178";
  var t = new URLSearchParams(location.search).get("t") || "";
  var fLong = new Intl.DateTimeFormat("en-US", { timeZone: TZ, weekday: "long", month: "long", day: "numeric" });
  var fTime = new Intl.DateTimeFormat("en-US", { timeZone: TZ, hour: "numeric", minute: "2-digit" });
  var fDay = new Intl.DateTimeFormat("en-US", { timeZone: TZ, weekday: "short", month: "short", day: "numeric" });
  var fKey = new Intl.DateTimeFormat("en-CA", { timeZone: TZ, year: "numeric", month: "2-digit", day: "2-digit" });
  function el(tag, cls, text) { var n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; }
  function api(data) {
    return fetch("/api/booking", { method: "POST", credentials: "same-origin", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { status: r.status, j: j }; }); });
  }
  function help(msg) {
    root.textContent = "";
    var card = el("section", "mg-card"); card.appendChild(el("h1", "", msg));
    var p = el("p", "", "Call or text "), a = el("a", "", PHONE); a.href = TEL; p.appendChild(a); p.appendChild(document.createTextNode(" and we'll sort it out."));
    card.appendChild(p); var home = el("a", "btn btn-secondary", "Book a new time"); home.href = "/#consult"; card.appendChild(home);
    root.appendChild(card);
  }
  function show(b, note) {
    root.textContent = "";
    var card = el("section", "mg-card"), when = new Date(b.start);
    if (note) { var n = el("p", "mg-note", note); n.setAttribute("role", "status"); card.appendChild(n); }
    if (b.status === "cancelled") {
      card.appendChild(el("h1", "", "This consult is cancelled."));
      var again = el("a", "btn btn-primary", "Pick a new time"); again.href = "/#consult"; card.appendChild(again);
      root.appendChild(card); return;
    }
    card.appendChild(el("p", "mg-kicker", "Free consult" + (b.first && b.first !== "there" ? " for " + b.first : "")));
    card.appendChild(el("h1", "", fLong.format(when) + " at " + fTime.format(when)));
    card.appendChild(el("p", "", "Pacific time. Fig Performance, 1284 E. Yorba Linda Blvd, Placentia. Plan on about an hour and 15 minutes, starting with your InBody scan. Wear workout clothes."));
    if (!b.canChange) { card.appendChild(el("p", "ib-status", "This consult has passed. Want another? Book a new time on our home page.")); root.appendChild(card); return; }
    var row = el("div", "mg-actions");
    var cal = el("a", "btn btn-primary", "Add to my calendar"); cal.href = "/api/cal?b=" + encodeURIComponent(t); row.appendChild(cal);
    var g = el("a", "btn btn-secondary", "Add to Google Calendar");
    var s = when.toISOString().replace(/[-:]/g, "").replace(/\.\d{3}/, ""), e = new Date(when.getTime() + 90 * 6e4).toISOString().replace(/[-:]/g, "").replace(/\.\d{3}/, "");
    g.href = "https://calendar.google.com/calendar/render?action=TEMPLATE&text=" + encodeURIComponent("Free consultation at Fig Performance") + "&dates=" + s + "/" + e +
      "&location=" + encodeURIComponent("Fig Performance, 1284 E. Yorba Linda Blvd, Placentia, CA 92870");
    g.target = "_blank"; g.rel = "noopener"; row.appendChild(g);
    var mv = el("button", "btn btn-secondary", "Pick a different time"); mv.type = "button"; row.appendChild(mv);
    var cx = el("button", "ib-link", "Cancel this consult"); cx.type = "button"; row.appendChild(cx);
    card.appendChild(row);
    var status = el("p", "ib-status"); status.setAttribute("role", "alert"); card.appendChild(status);
    var picker = el("div", "mg-picker"); card.appendChild(picker);
    root.appendChild(card);

    cx.addEventListener("click", function () {
      if (cx.getAttribute("data-sure") !== "1") { cx.setAttribute("data-sure", "1"); cx.textContent = "Tap again to cancel for sure"; return; }
      cx.disabled = true;
      api({ action: "cancel", t: t }).then(function (r) { if (r.j.ok) show(r.j.booking); else { status.className = "ib-status err"; status.textContent = "Couldn't cancel. Call or text " + PHONE + "."; cx.disabled = false; } });
    });
    mv.addEventListener("click", function () {
      mv.disabled = true; picker.textContent = "Loading open times…";
      fetch("/api/booking", { headers: { Accept: "application/json" } }).then(function (r) { return r.json(); }).then(function (j) {
        picker.textContent = ""; mv.disabled = false;
        var by = {}; (j.slots || []).forEach(function (iso) { var k = fKey.format(new Date(iso)); (by[k] = by[k] || []).push(iso); });
        var days = Object.keys(by).sort();
        if (!days.length) { picker.appendChild(el("p", "ib-status", "No other times are open right now. Call or text " + PHONE + ".")); return; }
        days.forEach(function (k) {
          picker.appendChild(el("p", "mg-day", fDay.format(new Date(by[k][0]))));
          var grid = el("div", "bk-times");
          by[k].forEach(function (iso) {
            var bt = el("button", "bk-time", fTime.format(new Date(iso))); bt.type = "button";
            bt.addEventListener("click", function () {
              picker.querySelectorAll("button").forEach(function (x) { x.disabled = true; });
              api({ action: "move", t: t, start: iso }).then(function (r) {
                if (r.j.ok) return show(r.j.booking, "Done. Your consult is moved" + (r.j.texting ? " and we've texted you the new time." : "."));
                status.className = "ib-status err";
                status.textContent = r.j.error === "too_many_moves" ? "This consult has been moved a few times already. Call or text " + PHONE + "." : "That time was just taken. Pick another.";
                picker.querySelectorAll("button").forEach(function (x) { x.disabled = false; }); bt.disabled = true;
              });
            });
            grid.appendChild(bt);
          });
          picker.appendChild(grid);
        });
        picker.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }).catch(function () { picker.textContent = ""; mv.disabled = false; status.className = "ib-status err"; status.textContent = "Couldn't load times. Call or text " + PHONE + "."; });
    });
  }
  if (!/^[A-Za-z0-9_-]{20,40}$/.test(t)) return help("This link is missing its code.");
  api({ action: "manage", t: t }).then(function (r) {
    if (r.status === 200 && r.j.ok) return show(r.j.booking);
    help(r.status === 404 ? "We couldn't find that booking." : "Something went wrong.");
  }).catch(function () { help("Something went wrong."); });
})();
