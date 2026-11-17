/* ==========================================================
   Fig Performance: on-page consult booking.
   Pick a day -> pick a time -> name, mobile (required), email -> booked.
   Talks to /api/booking (same site), which books into Calendly.
   If online booking is down, the same form sends Dan a request instead,
   so a visitor's number is never lost.
   ========================================================== */
(function () {
  "use strict";
  var root = document.getElementById("booking");
  if (!root) return;

  var TZ = "America/Los_Angeles";
  var DAYS = 14;
  var PHONE = (window.CONFIG && CONFIG.PHONE) || "(714) 396-7178";
  var LEAD_ENDPOINT = (window.CONFIG && CONFIG.FORM_ENDPOINT) || "https://formsubmit.co/ajax/figueroa32daniel@gmail.com";
  var POLICY = (window.CONFIG && CONFIG.POLICY_VERSION) || "";
  var loadedAt = Date.now();

  var st = { mode: "loading", slots: {}, day: null, time: null, page: 0, loaded: {} };

  var fmtDay = new Intl.DateTimeFormat("en-US", { timeZone: TZ, weekday: "short" });
  var fmtNum = new Intl.DateTimeFormat("en-US", { timeZone: TZ, day: "numeric" });
  var fmtMon = new Intl.DateTimeFormat("en-US", { timeZone: TZ, month: "short" });
  var fmtTime = new Intl.DateTimeFormat("en-US", { timeZone: TZ, hour: "numeric", minute: "2-digit" });
  var fmtLong = new Intl.DateTimeFormat("en-US", { timeZone: TZ, weekday: "long", month: "long", day: "numeric" });
  var fmtKey = new Intl.DateTimeFormat("en-CA", { timeZone: TZ, year: "numeric", month: "2-digit", day: "2-digit" });

  function key(d) { return fmtKey.format(d); }              // YYYY-MM-DD in Pacific time
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function telHref() { return "tel:+1" + PHONE.replace(/\D/g, "").slice(-10); }
  function smsHref() { return "sms:+1" + PHONE.replace(/\D/g, "").slice(-10); }

  var dayList = [];
  (function () {
    var noon = new Date();
    for (var i = 0; i < DAYS; i++) dayList.push(key(new Date(noon.getTime() + i * 864e5)));
  })();

  /* ---------- Data ---------- */
  function loadWeek(fromKey) {
    if (st.loaded[fromKey]) return st.loaded[fromKey];
    var p = fetch("/api/booking?from=" + fromKey, { headers: { Accept: "application/json" }, credentials: "same-origin" })
      .then(function (r) { if (!r.ok) throw new Error(String(r.status)); return r.json(); })
      .then(function (j) {
        (j.slots || []).forEach(function (iso) {
          var k = key(new Date(iso));
          (st.slots[k] = st.slots[k] || []).push(iso);
        });
        Object.keys(st.slots).forEach(function (k) { st.slots[k].sort(); st.slots[k] = st.slots[k].filter(function (v, i, a) { return a.indexOf(v) === i; }); });
      });
    st.loaded[fromKey] = p;
    return p;
  }
  function loadAll() {
    return Promise.all([loadWeek(dayList[0]), loadWeek(dayList[7])]);
  }

  /* ---------- Render ---------- */
  function render() {
    if (st.mode === "loading") {
      root.innerHTML = '<p class="bk-loading" role="status">Loading open times&hellip;</p>';
      return;
    }
    if (st.mode === "done") return;
    var html = "";
    if (st.mode === "pick") {
      html += '<p class="bk-label"><span>1</span> Pick a day</p>';
      html += '<div class="bk-days" role="group" aria-label="Days">';
      var narrow = window.matchMedia && window.matchMedia("(max-width: 420px)").matches;
      var first = narrow ? 0 : st.page * 7, last = narrow ? DAYS : first + 7;
      html += '<button type="button" class="bk-page" data-page="-1" aria-label="Earlier days"' + (st.page === 0 ? " disabled" : "") + '><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg></button>';
      html += '<div class="bk-day-row">';
      for (var i = first; i < last; i++) {
        var k = dayList[i];
        var d = new Date(k + "T12:00:00Z");
        var open = (st.slots[k] || []).length > 0;
        var sun = fmtDay.format(d) === "Sun";
        html += '<button type="button" class="bk-day" data-day="' + k + '"' +
          (open ? "" : " disabled") + ' aria-pressed="' + (st.day === k) + '">' +
          '<span class="bk-dow">' + fmtDay.format(d) + '</span>' +
          '<span class="bk-num">' + fmtNum.format(d) + '</span>' +
          '<span class="bk-mon">' + (open ? fmtMon.format(d) : (sun ? "Closed" : "Full")) + "</span></button>";
      }
      html += "</div>";
      html += '<button type="button" class="bk-page" data-page="1" aria-label="Later days"' + (st.page === 1 ? " disabled" : "") + '><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg></button>';
      html += "</div>";

      html += '<p class="bk-label"><span>2</span> Pick a time' + (st.day ? ' <em>' + esc(fmtLong.format(new Date(st.day + "T12:00:00Z"))) + " (Pacific)</em>" : "") + "</p>";
      if (!st.day) {
        html += '<p class="bk-hint">Choose a day above to see open times.</p>';
      } else {
        html += '<div class="bk-times" role="group" aria-label="Times">';
        (st.slots[st.day] || []).forEach(function (iso) {
          html += '<button type="button" class="bk-time" data-time="' + esc(iso) + '" aria-pressed="' + (st.time === iso) + '">' + esc(fmtTime.format(new Date(iso))) + "</button>";
        });
        html += "</div>";
      }
    }

    var request = st.mode === "request";
    if (request) {
      html += '<p class="bk-down" role="status">Online booking is taking a break. Leave your details and the time that suits you, and we\'ll text you to confirm, usually within a few hours. Or call/text <a href="' + telHref() + '">' + esc(PHONE) + "</a>.</p>";
    }
    var ready = request || st.time;
    html += '<form class="bk-form" novalidate' + (ready ? "" : " hidden") + ">";
    if (!request) html += '<p class="bk-label"><span>3</span> Your details</p><p class="bk-summary">' + (st.time ? esc(fmtLong.format(new Date(st.time))) + " at " + esc(fmtTime.format(new Date(st.time))) + " (Pacific) &middot; Fig Performance, Placentia" : "") + "</p>";
    html +=
      '<div class="bk-fields">' +
        '<label class="bk-field"><span>Full name</span><input name="name" autocomplete="name" maxlength="80" required></label>' +
        '<label class="bk-field"><span>Mobile phone</span><input name="phone" type="tel" inputmode="tel" autocomplete="tel" maxlength="20" placeholder="(714) 555-0123" required></label>' +
        '<label class="bk-field bk-wide"><span>Email</span><input name="email" type="email" autocomplete="email" maxlength="254" required></label>' +
        (request ? '<label class="bk-field bk-wide"><span>Best day and time for you</span><input name="when" maxlength="120" placeholder="e.g. Tuesday after 5 PM" required></label>' : "") +
        '<label class="bk-field bk-wide"><span>Your goal <i>(optional)</i></span><textarea name="goal" rows="2" maxlength="500" placeholder="e.g. lose 20 lb, get stronger, back pain"></textarea></label>' +
        '<input name="website" class="hp-field" tabindex="-1" autocomplete="off" aria-hidden="true">' +
      "</div>" +
      '<p class="consent">We\'ll text you a confirmation and reminders for your appointment. By booking, you agree to our <a href="/privacy">Privacy Policy</a> and <a href="/terms">Terms</a>, and that Fig Performance may call or text this number about your consultation and services. Msg frequency varies. Msg &amp; data rates may apply. Reply STOP to opt out, HELP for help. Consent is not a condition of purchase.</p>' +
      '<p class="form-status" role="alert" tabindex="-1"></p>' +
      '<button class="btn btn-gold btn-lg btn-block" type="submit">' + (request ? "Request my free consult" : "Confirm my free consultation") + "</button>" +
      '<p class="bk-fine">Free &middot; No credit card &middot; About an hour, including your InBody scan</p>' +
      "</form>";
    root.innerHTML = html;
  }

  /* ---------- Events ---------- */
  root.addEventListener("click", function (e) {
    var b = e.target.closest("button");
    if (!b || b.disabled || !root.contains(b)) return;
    if (b.hasAttribute("data-page")) {
      st.page = Math.max(0, Math.min(1, st.page + Number(b.getAttribute("data-page"))));
      render();
      var f = root.querySelector('.bk-page:not([disabled])'); if (f) f.focus();
    } else if (b.hasAttribute("data-day")) {
      st.day = b.getAttribute("data-day"); st.time = null;
      render();
      var t = root.querySelector(".bk-time"); if (t) t.focus({ preventScroll: true });
    } else if (b.hasAttribute("data-time")) {
      st.time = b.getAttribute("data-time");
      render();
      var form = root.querySelector(".bk-form");
      if (form) {
        var r = form.getBoundingClientRect();
        if (r.top > window.innerHeight * 0.7) form.scrollIntoView({ behavior: "smooth", block: "start" });
        form.querySelector('input[name="name"]').focus({ preventScroll: true });
      }
    }
  });

  root.addEventListener("input", function (e) {
    var f = e.target.closest(".bk-form"); if (!f) return;
    e.target.removeAttribute("aria-invalid");
    var s = f.querySelector(".form-status.err"); if (s) { s.className = "form-status"; s.textContent = ""; }
  });

  function digits(v) { var d = String(v || "").replace(/\D/g, ""); if (d.length === 11 && d[0] === "1") d = d.slice(1); return d; }

  root.addEventListener("submit", function (e) {
    e.preventDefault();
    var form = e.target;
    var btn = form.querySelector('button[type="submit"]');
    var status = form.querySelector(".form-status");
    if (btn.disabled) return;
    var v = function (n) { var el = form.elements[n]; return el ? String(el.value || "").trim() : ""; };
    var name = v("name"), phone = v("phone"), email = v("email"), goal = v("goal"), when = v("when");
    var err = null, bad = null;
    if (name.length < 2) { err = "Please enter your name."; bad = "name"; }
    else if (digits(phone).length !== 10) { err = "Please enter a 10-digit mobile number so we can text your confirmation."; bad = "phone"; }
    else if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) { err = "Please enter a valid email."; bad = "email"; }
    else if (st.mode === "request" && when.length < 2) { err = "Tell us a day and time that suits you."; bad = "when"; }
    form.querySelectorAll("input").forEach(function (i) { i.removeAttribute("aria-invalid"); });
    if (err) {
      status.className = "form-status err"; status.textContent = err;
      var f = form.elements[bad]; if (f) { f.setAttribute("aria-invalid", "true"); f.focus(); }
      return;
    }
    if (v("website")) return;                                    // bot
    if (Date.now() - loadedAt < 2500) { status.className = "form-status err"; status.textContent = "Please check your details, then tap the button again."; loadedAt = 0; return; }

    btn.disabled = true; var label = btn.textContent; btn.textContent = st.mode === "request" ? "Sending…" : "Booking…";
    status.className = "form-status"; status.textContent = "";

    var lead = {
      "Name": name, "Mobile": phone, "Email": email, "Goal": goal || "(not given)",
      "Consent": "Yes: agreed to Privacy Policy & Terms and to calls/texts about consultation & services (STOP to opt out; not a condition of purchase). Policy version " + POLICY,
      "Submitted from": "figperformance.com booking",
      _template: "table", _captcha: "false", _replyto: email
    };

    var done = function (booked, result) {
      lead["Status"] = booked ? "BOOKED in Calendly" : "Needs a time: text them to confirm";
      lead["Appointment"] = booked ? fmtLong.format(new Date(st.time)) + " at " + fmtTime.format(new Date(st.time)) + " (Pacific)" : (when || "(see note)");
      lead._subject = (booked ? "New consult booked: " : "Consult request: ") + name + " · " + lead["Appointment"];
      sendLead(lead);
      showDone(name, booked, result);
    };

    if (st.mode === "request") return done(false);

    fetch("/api/booking", {
      method: "POST", credentials: "same-origin",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify({ name: name, phone: phone, email: email, goal: goal, start: st.time, website: v("website") })
    })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { status: r.status, j: j }; }); })
      .then(function (r) {
        if (r.status === 200 && r.j.ok) return done(true, r.j);
        btn.disabled = false; btn.textContent = label;
        status.className = "form-status err";
        if (r.status === 409) {
          status.textContent = "Someone just took that time. Please pick another.";
          var times = st.slots[st.day] || []; st.slots[st.day] = times.filter(function (t) { return t !== st.time; });
          st.time = null; setTimeout(function () { render(); }, 1600);
        } else if (r.status === 400) {
          status.textContent = r.j.error === "phone" ? "Please check your mobile number." : r.j.error === "email" ? "Please check your email." : "Please check your details and try again.";
        } else {
          // Booking system trouble: don't lose them. Send Dan the request with the time they picked.
          when = fmtLong.format(new Date(st.time)) + " at " + fmtTime.format(new Date(st.time)) + " (online booking failed, please confirm)";
          done(false);
        }
        status.focus();
      })
      .catch(function () {
        when = fmtLong.format(new Date(st.time)) + " at " + fmtTime.format(new Date(st.time)) + " (online booking failed, please confirm)";
        done(false);
      });
  });

  function sendLead(data) {
    try {
      fetch(LEAD_ENDPOINT, {
        method: "POST", mode: "cors", credentials: "omit", keepalive: true,
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(data)
      }).catch(function () {});
    } catch (e) {}
  }

  function showDone(name, booked, result) {
    st.mode = "done";
    var first = esc(name.split(" ")[0]);
    var when = booked ? esc(fmtLong.format(new Date(st.time))) + " at " + esc(fmtTime.format(new Date(st.time))) : "";
    root.setAttribute("data-state", "done");
    root.innerHTML =
      '<div class="quiz-done">' +
        '<div class="done-check" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12l5 5 9-10"/></svg></div>' +
        (booked
          ? '<h3 class="q-title" tabindex="-1">You\'re booked, ' + first + ".</h3><p><strong>" + when + "</strong> (Pacific)<br>Fig Performance &middot; 1284 E. Yorba Linda Blvd, Placentia</p>" +
            '<ul class="done-steps"><li>We\'re texting you a confirmation now, plus a reminder before your visit.</li><li>Wear workout clothes. We\'ll start with your InBody scan.</li><li>Your consult is free.</li></ul>' +
            (result && result.reschedule_url ? '<p class="bk-fine"><a href="' + esc(result.reschedule_url) + '" target="_blank" rel="noopener">Need a different time?</a></p>' : "")
          : '<h3 class="q-title" tabindex="-1">Got it, ' + first + ".</h3><p>We'll text you shortly to lock in your time. Your consult is free.</p>" +
            '<p class="bk-fine">Can\'t wait? Call or text <a href="' + telHref() + '">' + esc(PHONE) + "</a>.</p>") +
      "</div>";
    var h = root.querySelector(".q-title"); if (h) h.focus();
  }

  /* ---------- Start ---------- */
  render();
  var started = false;
  function start() {
    if (started) return; started = true;
    loadAll()
      .then(function () {
        st.mode = "pick";
        var firstOpen = dayList.filter(function (k) { return (st.slots[k] || []).length; })[0];
        if (!firstOpen) st.mode = "request";
        else { st.day = firstOpen; st.page = dayList.indexOf(firstOpen) >= 7 ? 1 : 0; }
        root.setAttribute("data-state", st.mode);
        render();
      })
      .catch(function () { st.mode = "request"; root.setAttribute("data-state", "request"); render(); });
  }
  // Load times when the booking section gets close to the screen (keeps the page fast).
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(function (es, o) { if (es[0].isIntersecting) { o.disconnect(); start(); } }, { rootMargin: "800px 0px" }).observe(root);
  } else start();
  document.querySelectorAll('a[href="#consult"], a[href="/#consult"]').forEach(function (a) { a.addEventListener("click", start); });
})();
