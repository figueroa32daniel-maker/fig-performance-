/* ==========================================================
   Fig Performance: on-page consult booking.
   Pick a day -> pick a time -> name, mobile (required), email -> booked.
   Talks to /api/booking (same site): the gym's own booking engine.
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

  /* Returning visitors: their details are filled in for them (this browser only). */
  var SAVED = "fig-booker";
  var saved = {};
  try { saved = JSON.parse(localStorage.getItem(SAVED) || "{}") || {}; } catch (e) { saved = {}; }
  function remember(d) { try { localStorage.setItem(SAVED, JSON.stringify(d)); } catch (e) {} }

  /* Where the visitor came from (ad, Google, Instagram), kept for this visit. */
  var UTM_KEYS = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"];
  var utm = {};
  try {
    var q = new URLSearchParams(location.search);
    UTM_KEYS.forEach(function (k) { if (q.get(k)) utm[k] = q.get(k).slice(0, 100); });
    if (q.get("gclid")) utm.utm_source = utm.utm_source || "google-ads";
    if (q.get("fbclid")) utm.utm_source = utm.utm_source || "facebook";
    if (Object.keys(utm).length) sessionStorage.setItem("fig-utm", JSON.stringify(utm));
    else utm = JSON.parse(sessionStorage.getItem("fig-utm") || "{}") || {};
  } catch (e) {}
  if (!utm.utm_source && document.referrer && document.referrer.indexOf(location.host) < 0) {
    try { utm.utm_source = new URL(document.referrer).hostname.replace(/^www\./, ""); utm.utm_medium = "referral"; } catch (e) {}
  }
  function source() { return UTM_KEYS.filter(function (k) { return utm[k]; }).map(function (k) { return k.replace("utm_", "") + ": " + utm[k]; }).join(", ") || "direct / unknown"; }

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
      var narrow = root.clientWidth > 0 && root.clientWidth <= 520;   // matches the container rule in styles.css (480px inside the padding)
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
        '<label class="bk-field"><span>Name</span><input name="name" autocomplete="name" maxlength="80" placeholder="First and last" value="' + esc(saved.name || "") + '" required></label>' +
        '<label class="bk-field"><span>Mobile phone</span><input name="phone" type="tel" inputmode="tel" autocomplete="tel" maxlength="20" placeholder="(714) 555-0123" value="' + esc(saved.phone || "") + '" required>' +
          '<small class="bk-note">We\'ll text your booking details if confirmed, or follow up about your request. Reply STOP anytime.</small></label>' +
        (request ? '<label class="bk-field bk-wide"><span>Best day and time for you</span><input name="when" maxlength="120" placeholder="e.g. Tuesday after 5 PM" required></label>' : "") +
        '<div class="bk-wide bk-extras">' +
          '<button type="button" class="bk-more" data-more="goal" aria-expanded="false">+ Add your goal <i>(optional)</i></button>' +
          '<button type="button" class="bk-more" data-more="email" aria-expanded="' + (saved.email ? "true" : "false") + '"' + (saved.email ? " hidden" : "") + '>+ Add email for a calendar invite <i>(optional)</i></button>' +
        "</div>" +
        '<label class="bk-field bk-wide" data-extra="goal" hidden><span>Your goal</span><textarea name="goal" rows="2" maxlength="500" placeholder="e.g. lose 20 lb, rebuild after an injury, get strong for a trip"></textarea></label>' +
        '<label class="bk-field bk-wide" data-extra="email"' + (saved.email ? "" : " hidden") + '><span>Email</span><input name="email" type="email" autocomplete="email" maxlength="254" value="' + esc(saved.email || "") + '"></label>' +
        '<input name="website" class="hp-field" tabindex="-1" autocomplete="off" aria-hidden="true">' +
      "</div>" +
      '<p class="consent">By submitting, you agree that Fig Performance may text and call this number about your appointment or consultation request (your confirmation, reminders and replies to your questions), and to our <a href="/privacy">Privacy Policy</a> and <a href="/terms#sms">Terms, including the text message terms</a>. Message frequency varies. Msg &amp; data rates may apply. Reply STOP to opt out, HELP for help.</p>' +
      '<label class="bk-check"><input type="checkbox" name="marketing" value="yes"><span>Optional: also text me training tips and offers from Fig Performance, up to 4 messages a month. Msg &amp; data rates may apply. Reply STOP to opt out. Not required to book or buy anything.</span></label>' +
      '<p class="form-status" role="alert" tabindex="-1"></p>' +
      '<button class="btn btn-gold btn-lg btn-block" type="submit">' + (request ? "Request my free consult" : "Confirm my free consultation") + "</button>" +
      '<p class="bk-fine">Free &middot; No credit card &middot; ' + (request ? "Request only; no appointment reserved yet" : "Confirmed only when your booking succeeds") + "</p>" +
      "</form>" +
      '<p class="bk-talk">Prefer to talk? Call <a href="' + telHref() + '">' + esc(PHONE) + "</a> and we\'ll book it for you.</p>";
    root.innerHTML = html;
  }

  /* ---------- Events ---------- */
  root.addEventListener("click", function (e) {
    var b = e.target.closest("button");
    if (!b || b.disabled || !root.contains(b)) return;
    if (b.hasAttribute("data-more")) {
      var which = b.getAttribute("data-more");
      var box = root.querySelector('[data-extra="' + which + '"]');
      if (box) { box.hidden = false; b.hidden = true; b.setAttribute("aria-expanded", "true"); var inp = box.querySelector("input, textarea"); if (inp) inp.focus(); }
      return;
    }
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

  /* Each error sits under its own field and is read out with it (aria-describedby). */
  function clearFieldErrors(form) {
    form.querySelectorAll(".bk-err").forEach(function (n) { n.remove(); });
    form.querySelectorAll("[aria-invalid]").forEach(function (i) { i.removeAttribute("aria-invalid"); i.removeAttribute("aria-describedby"); });
  }
  function fieldError(form, name, msg) {
    var f = form.elements[name]; if (!f) return;
    var box = f.closest("[data-extra]"); if (box && box.hidden) { box.hidden = false; }
    var note = document.createElement("small");
    note.className = "bk-err"; note.id = "bk-err-" + name; note.setAttribute("role", "alert"); note.textContent = msg;
    f.insertAdjacentElement("afterend", note);
    f.setAttribute("aria-invalid", "true"); f.setAttribute("aria-describedby", note.id); f.focus();
  }

  root.addEventListener("input", function (e) {
    var f = e.target.closest(".bk-form"); if (!f) return;
    if (e.target.hasAttribute("aria-invalid")) {
      var n = f.querySelector("#" + e.target.getAttribute("aria-describedby")); if (n) n.remove();
      e.target.removeAttribute("aria-invalid"); e.target.removeAttribute("aria-describedby");
    }
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
    else if (digits(phone).length !== 10) { err = "Please enter a 10-digit mobile number so we can contact you about your consultation."; bad = "phone"; }
    else if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) { err = "Please check your email, or leave it blank."; bad = "email"; }
    else if (st.mode === "request" && when.length < 2) { err = "Tell us a day and time that suits you."; bad = "when"; }
    clearFieldErrors(form);
    if (err) { fieldError(form, bad, err); return; }
    if (v("website")) return;                                    // bot
    if (Date.now() - loadedAt < 2500) { status.className = "form-status err"; status.textContent = "Please check your details, then tap the button again."; loadedAt = 0; return; }

    btn.disabled = true; var label = btn.textContent; btn.textContent = st.mode === "request" ? "Sending…" : "Booking…";
    status.className = "form-status"; status.textContent = "";

    var marketing = !!(form.elements.marketing && form.elements.marketing.checked);
    var lead = {
      "Name": name, "Mobile": phone, "Email": email || "(not given)", "Goal": goal || "(not given)", "Came from": source(),
      "Consent": "Appointment texts/calls: yes (agreed at booking). Marketing texts: " + (marketing ? "YES (ticked the optional box)" : "no") + ". Policy version " + POLICY,
      "Submitted from": "figperformance.com booking",
      _template: "table", _captcha: "false", _cc: "trainat@figperformance.com"
    };
    if (email) lead._replyto = email;
    partialSent = true;                                         // a real submit replaces the "unfinished" alert

    var done = function (booked, result) {
      lead["Status"] = booked ? "Booked through FIG PERFORMANCE website" : "Needs a time: text them to confirm";
      lead["Appointment"] = booked ? fmtLong.format(new Date(st.time)) + " at " + fmtTime.format(new Date(st.time)) + " (Pacific)" : (when || "(see note)");
      lead._subject = (booked ? "New consult booked: " : "Consult request: ") + name + " · " + lead["Appointment"];
      sendLead(lead);
      remember({ name: name, phone: phone, email: email });
      if (typeof window.gtag === "function") {
        window.gtag("event", booked ? "consult_booked" : "consult_requested");
      }
      showDone(name, booked, result);
    };

    if (st.mode === "request") return done(false);

    fetch("/api/booking", {
      method: "POST", credentials: "same-origin",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify(Object.assign({ name: name, phone: phone, email: email, goal: goal, start: st.time, website: v("website"),
        consent: true, marketing: marketing, page: location.pathname }, utm))
    })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { status: r.status, j: j }; }); })
      .then(function (r) {
        if (r.status === 200 && r.j.ok) return done(true, r.j);
        btn.disabled = false; btn.textContent = label;
        status.className = "form-status err";
        if (r.status === 409 && r.j.error === "already_booked") {
          status.textContent = "This number already has a consult booked. To change it, call or text " + PHONE + ".";
        } else if (r.status === 429) {
          status.textContent = "Too many tries from this connection. Please call or text " + PHONE + " and we'll book it for you.";
        } else if (r.status === 409) {
          status.textContent = "That time was just taken. Here are the next openings.";
          var taken = st.time; st.time = null; st.slots = {}; st.loaded = {};
          setTimeout(function () {
            loadAll().then(function () {
              (st.slots[st.day] || []).length || (st.day = dayList.filter(function (k) { return (st.slots[k] || []).length; })[0] || null);
              st.mode = st.day ? "pick" : "request"; render();
            }).catch(function () { st.mode = "request"; render(); });
          }, 1400);
          void taken;
        } else if (r.status === 400) {
          status.className = "form-status";
          if (r.j.error === "phone") fieldError(form, "phone", "Please check your mobile number.");
          else if (r.j.error === "email") fieldError(form, "email", "Please check your email, or leave it blank.");
          else if (r.j.error === "name") fieldError(form, "name", "Please enter your name.");
          else { status.className = "form-status err"; status.textContent = "Please check your details and try again."; }
          return;
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

  /* Unfinished bookings: if someone types a name and a valid mobile, then leaves without
     confirming, Dan still gets their details. They did NOT agree to texts, so the email says
     call only. Sent once per set of details. */
  var partialSent = false, partialSig = "", idleTimer = null;
  function reportUnfinished(reason) {
    if (partialSent || st.mode === "done") return;
    var form = root.querySelector(".bk-form"); if (!form) return;
    var name = (form.elements.name || {}).value || "", phone = (form.elements.phone || {}).value || "";
    if (name.trim().length < 2 || digits(phone).length !== 10 || (form.elements.website && form.elements.website.value)) return;
    var sig = name.trim() + "|" + digits(phone); if (sig === partialSig) return; partialSig = sig;
    var fd = new FormData();
    fd.append("Status", "UNFINISHED: typed their details but did not book. CALL ONLY (no text consent).");
    fd.append("Name", name.trim()); fd.append("Mobile", phone.trim());
    fd.append("Email", ((form.elements.email || {}).value || "").trim() || "(not given)");
    fd.append("Goal", ((form.elements.goal || {}).value || "").trim() || "(not given)");
    fd.append("Time they were looking at", st.time ? fmtLong.format(new Date(st.time)) + " at " + fmtTime.format(new Date(st.time)) : "(none picked)");
    fd.append("Came from", source()); fd.append("Why sent", reason);
    fd.append("_subject", "Unfinished booking: " + name.trim() + " (call, don't text)");
    fd.append("_template", "table"); fd.append("_captcha", "false"); fd.append("_cc", "trainat@figperformance.com");
    var sent = false;
    try { if (navigator.sendBeacon) sent = navigator.sendBeacon(LEAD_ENDPOINT, fd); } catch (e) {}
    if (!sent) { try { fetch(LEAD_ENDPOINT, { method: "POST", mode: "no-cors", keepalive: true, body: fd }); } catch (e) {} }
  }
  root.addEventListener("input", function () {
    clearTimeout(idleTimer);
    idleTimer = setTimeout(function () { reportUnfinished("stopped typing for 2 minutes"); }, 120000);
  });
  window.addEventListener("pagehide", function () { reportUnfinished("left the page"); });
  document.addEventListener("visibilitychange", function () { if (document.visibilityState === "hidden") reportUnfinished("switched away from the page"); });

  /* After booking: an "Add to my calendar" file, made in the browser. */
  function icsHref() {
    var s = new Date(st.time), e = new Date(s.getTime() + 60 * 60000);
    var f = function (d) { return d.toISOString().replace(/[-:]/g, "").replace(/\.\d{3}/, ""); };
    var body = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Fig Performance//Booking//EN", "BEGIN:VEVENT",
      "UID:" + f(s) + "-" + Math.random().toString(36).slice(2) + "@figperformance.com", "DTSTAMP:" + f(new Date()),
      "DTSTART:" + f(s), "DTEND:" + f(e), "SUMMARY:Free consultation at Fig Performance",
      "LOCATION:Fig Performance\\, 1284 E. Yorba Linda Blvd\\, Placentia\\, CA 92870",
      "DESCRIPTION:InBody scan\\, assessment and game plan. Wear workout clothes. Questions: " + PHONE,
      "END:VEVENT", "END:VCALENDAR"].join("\r\n");
    try { return URL.createObjectURL(new Blob([body], { type: "text/calendar" })); } catch (e) { return null; }
  }

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
            '<ul class="done-steps"><li>' + (result && result.texting ? "We\'re texting you a confirmation now, plus a reminder before your visit." : "Your time is held. We\'ll be in touch before your visit.") + "</li>" + '<li>Wear workout clothes. We\'ll start with your InBody scan.</li><li>Your consult is free.</li></ul>' +
            (function () {
              var id = result && /^\/manage\?t=[A-Za-z0-9_-]{20,40}$/.test(result.manage_url || "") ? result.manage_url.split("=")[1] : null;
              var h = id ? "/api/cal?b=" + id : icsHref();
              return h ? '<a class="btn btn-secondary" href="' + h + '"' + (id ? "" : ' download="fig-performance-consult.ics"') + ">Add to my calendar</a>" : "";
            })() +
            (result && /^\/manage\?t=[A-Za-z0-9_-]{20,40}$/.test(result.manage_url || "") ? '<p class="bk-fine"><a href="' + esc(result.manage_url) + '">Need to change or cancel?</a></p>' : "") +
            '<p class="bk-fine">Questions? Call or text <a href="' + telHref() + '">' + esc(PHONE) + "</a>.</p>"
          : '<h3 class="q-title" tabindex="-1">Consultation requested, ' + first + ".</h3><p>Your appointment is not booked yet. We\'ll follow up to confirm a time. Your consult is free.</p>" +
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
