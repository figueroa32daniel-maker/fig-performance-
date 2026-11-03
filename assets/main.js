/* ==========================================================
   Fig Performance — site config
   Phone/email also appear in index.html (links + JSON-LD) so they
   work without JS. Changing them here updates the visible text and
   links; setting one to "" hides its UI everywhere.
   ========================================================== */
var CONFIG = {
  PHONE: "(714) 396-7178",            // display format; links use +1 digits
  EMAIL: "trainat@figperformance.com",
  FORM_ENDPOINT: "https://formsubmit.co/ajax/figueroa32daniel@gmail.com",
  POLICY_VERSION: "2026-10-24.2"         // bump when privacy/terms/consent text changes
};

(function () {
  "use strict";
  var doc = document;

  /* ---- Contact details from CONFIG ---- */
  function applyContact(kind, value) {
    var v = (value || "").trim();
    var digits = v.replace(/\D/g, "");
    if (digits.length === 10) digits = "1" + digits;
    doc.querySelectorAll('[data-contact="' + kind + '"]').forEach(function (el) { el.hidden = !v; });
    if (!v) return;
    doc.querySelectorAll('[data-contact-text="' + kind + '"]').forEach(function (el) { el.textContent = v; });
    doc.querySelectorAll(kind === "phone" ? 'a[href^="tel:"], a[href^="sms:"]' : 'a[href^="mailto:"]').forEach(function (a) {
      var scheme = a.getAttribute("href").split(":")[0];
      a.setAttribute("href", scheme + ":" + (kind === "phone" ? "+" + digits : v));
    });
  }
  applyContact("phone", CONFIG.PHONE);
  applyContact("email", CONFIG.EMAIL);

  /* ---- Year ---- */
  var y = doc.getElementById("year"); if (y) y.textContent = new Date().getFullYear();

  /* ---- Mobile nav ---- */
  var header = doc.querySelector(".site-header");
  var toggle = doc.querySelector(".nav-toggle");
  function setNav(open) {
    header.classList.toggle("nav-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  }
  if (toggle) {
    toggle.addEventListener("click", function () { setNav(!header.classList.contains("nav-open")); });
    doc.querySelectorAll("#site-nav a").forEach(function (a) { a.addEventListener("click", function () { setNav(false); }); });
    doc.addEventListener("keydown", function (e) { if (e.key === "Escape" && header.classList.contains("nav-open")) { setNav(false); toggle.focus(); } });
  }

  /* ---- Mobile sticky CTA (shows after hero, hides at the form) ---- */
  var mcta = doc.querySelector(".mobile-cta");
  var hero = doc.querySelector(".hero");
  var consult = doc.getElementById("consult");
  if (mcta && "IntersectionObserver" in window) {
    doc.body.classList.add("has-mobile-cta");
    var heroVisible = true, consultVisible = false;
    var update = function () {
      var on = !heroVisible && !consultVisible;
      mcta.classList.toggle("show", on);
      mcta.setAttribute("aria-hidden", String(!on));
      mcta.querySelectorAll("a").forEach(function (l) { l.tabIndex = on ? 0 : -1; });
    };
    new IntersectionObserver(function (es) { heroVisible = es[0].isIntersecting; update(); }).observe(hero);
    new IntersectionObserver(function (es) { consultVisible = es[0].isIntersecting; update(); }, { threshold: 0.05 }).observe(consult);
  }

  /* ---- Back-to-top button: after ~1.5 screens, hidden while the booking quiz is on screen ---- */
  (function () {
    var btn = doc.querySelector(".to-top");
    if (!btn) return;
    var consultEl = doc.getElementById("consult"), inConsult = false, ticking = false;
    var update = function () {
      ticking = false;
      var on = window.scrollY > window.innerHeight * 1.5 && !inConsult;
      btn.classList.toggle("show", on);
      btn.tabIndex = on ? 0 : -1;
      btn.setAttribute("aria-hidden", String(!on));
    };
    if (consultEl && "IntersectionObserver" in window) {
      new IntersectionObserver(function (es) { inConsult = es[0].isIntersecting; update(); }, { threshold: 0 }).observe(consultEl);
    }
    window.addEventListener("scroll", function () { if (!ticking) { ticking = true; window.requestAnimationFrame(update); } }, { passive: true });
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" });
      var skip = doc.querySelector(".brand");
      if (skip) skip.focus({ preventScroll: true });
    });
    update();
  })();

  /* ---- Subtle reveal on scroll ---- */
  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var targets = doc.querySelectorAll(".feature, .price-card, .step, .visit-card, .section-head, .tech-list li");
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    targets.forEach(function (t) { t.classList.add("reveal"); io.observe(t); });
  }

  /* ---- Photo galleries (client results, inside the gym): carousel arrows + tap-to-enlarge lightbox ---- */
  (function () {
    doc.querySelectorAll(".results-wrap").forEach(function (wrap) {
      var track = wrap.querySelector(".results-track");
      if (!track) return;
      var btns = wrap.querySelectorAll(".results-btn");
      function updateBtns() {
        var max = track.scrollWidth - track.clientWidth - 2;
        btns.forEach(function (b) {
          b.disabled = b.getAttribute("data-dir") === "-1" ? track.scrollLeft <= 2 : track.scrollLeft >= max;
        });
      }
      btns.forEach(function (b) {
        b.addEventListener("click", function () {
          var dir = parseInt(b.getAttribute("data-dir"), 10) || 1;
          track.scrollBy({ left: dir * track.clientWidth * 0.9, behavior: "smooth" });
        });
      });
      track.addEventListener("scroll", updateBtns, { passive: true });
      window.addEventListener("resize", updateBtns);
      updateBtns();
    });

    var dlg = doc.getElementById("lightbox");
    if (!dlg || typeof dlg.showModal !== "function") return; // links still open the full image
    var img = dlg.querySelector(".lb-img"), count = dlg.querySelector(".lb-count");
    var links = [], idx = 0, opener = null;
    function show(i) {
      idx = (i + links.length) % links.length;
      var a = links[idx], src = a.querySelector("img");
      img.src = a.getAttribute("href");
      img.alt = src ? src.alt : "";
      count.textContent = (idx + 1) + " / " + links.length;
    }
    doc.querySelectorAll("a[data-lightbox]").forEach(function (a) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        var group = a.getAttribute("data-lightbox");
        links = Array.prototype.slice.call(doc.querySelectorAll('a[data-lightbox="' + group + '"]'));
        dlg.setAttribute("aria-label", group === "gym" ? "Enlarged gym photo" : "Enlarged client progress photo");
        opener = a; show(links.indexOf(a)); dlg.showModal();
        dlg.querySelector(".lb-close").focus();
      });
    });
    dlg.querySelector(".lb-close").addEventListener("click", function () { dlg.close(); });
    dlg.querySelector(".lb-prev").addEventListener("click", function () { show(idx - 1); });
    dlg.querySelector(".lb-next").addEventListener("click", function () { show(idx + 1); });
    dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
    dlg.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") { e.preventDefault(); show(idx - 1); }
      else if (e.key === "ArrowRight") { e.preventDefault(); show(idx + 1); }
    });
    var sx = null;
    dlg.addEventListener("touchstart", function (e) { sx = e.touches[0].clientX; }, { passive: true });
    dlg.addEventListener("touchend", function (e) {
      if (sx === null) return;
      var dx = e.changedTouches[0].clientX - sx; sx = null;
      if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1));
    }, { passive: true });
    dlg.addEventListener("close", function () { img.removeAttribute("src"); if (opener) opener.focus(); });
  })();

  /* ==========================================================
     Booking quiz: one question per screen, tap-to-advance
     ========================================================== */
  var STORE = "fig-quiz-v3";
  var quiz = doc.getElementById("quiz");
  var body = doc.getElementById("quiz-body");

  /* Other pages: links to /#consult with data-interest save the choice so the quiz on the
     home page opens with it preselected (validated there by sanitizeState). */
  if (!quiz) {
    doc.querySelectorAll('a[href="/#consult"][data-interest]').forEach(function (link) {
      link.addEventListener("click", function () {
        try {
          var s = JSON.parse(sessionStorage.getItem(STORE) || "null");
          if (!s || typeof s !== "object" || s.done) s = { step: 0, a: {} };
          if (!s.a || typeof s.a !== "object") s.a = {};
          s.a.interest = link.getAttribute("data-interest"); s.preset = true;
          if (!(s.step > 1)) s.step = s.a.goal ? 2 : 0;
          sessionStorage.setItem(STORE, JSON.stringify(s));
        } catch (e) {}
      });
    });
  }
  if (!quiz || !body) return;

  var ICON = {
    strength: '<path d="M6 7v10M18 7v10M3 9v6M21 9v6M6 12h12"/>',
    weight: '<path d="M4 20h16M7 20l2-12h6l2 12"/><circle cx="12" cy="5" r="2"/>',
    pain: '<path d="M12 21s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.5-7 10-7 10z"/>',
    perf: '<path d="M13 2L4 14h7l-1 8 9-12h-7l1-8z"/>',
    unsure: '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6V14M12 17.5h.01"/>',
    one: '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-8 8-8s8 3.6 8 8"/>',
    key: '<path d="M12 2l8 3v6c0 5-3.4 9.4-8 11-4.6-1.6-8-6-8-11V5l8-3z"/>',
    sunrise: '<path d="M12 3v3M5 9l1.5 1.5M19 9l-1.5 1.5M3 17h18M7 17a5 5 0 0 1 10 0M8 21h8"/>',
    sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    moon: '<path d="M20 14.5A8 8 0 1 1 9.5 4 6.5 6.5 0 0 0 20 14.5z"/>',
    cal: '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    check: '<path d="M5 12l5 5 9-10"/>',
    note: '<path d="M4 4h16v12H8l-4 4V4z"/><path d="M8 9h8M8 12h5"/>',
    video: '<rect x="2" y="6" width="14" height="12" rx="2"/><path d="M16 10l6-3v10l-6-3"/>',
    home: '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-5h4v5"/>',
    conf: '<path d="M12 2l2.9 6.2 6.6.8-4.9 4.6 1.3 6.6L12 17l-5.9 3.2 1.3-6.6L2.5 9l6.6-.8L12 2z"/>'
  };
  function icon(k) { return '<svg viewBox="0 0 24 24" aria-hidden="true">' + ICON[k] + "</svg>"; }

  var STEPS = [
    { key: "goal", title: "What matters most to you right now?", sub: "Pick the one that fits best.", options: [
      ["Get stronger", "strength"], ["Lose weight", "weight"], ["Move without pain", "pain"],
      ["Feel healthier and more confident", "conf"], ["Not sure yet", "unsure"] ] },
    { key: "interest", title: "How would you like to train?", sub: "You can change your mind at the consult.", options: [
      ["1:1 personal training", "one", "$90/session \u00b7 save 20% paying 3 months in full"],
      ["Membership", "key", "Classes up to 2\u20133x a week + access + recovery"],
      ["Concierge personal training", "home", "Dan comes to your home gym \u00b7 North Orange County and surrounding areas"],
      ["Online coaching", "video", "$249/mo, 3-month program \u00b7 weekly video call + app + nutrition"], ["Not sure, help me choose", "unsure"] ] },
    { key: "time", title: "What fits around your workday?", sub: "Staffed Mon\u2013Fri, 5 AM to 8 PM, and Sat, 5 AM to noon.", options: [
      ["Before work", "sunrise", "Early morning"], ["Midday", "sun", "Lunch hour"], ["After work", "moon", "Until 8 PM"], ["Saturday", "cal"] ] },
    { key: "pain", multi: true, title: "Anything bothering you?", sub: "Optional. Tap any that apply and Dan will plan around it.", options: [
      "Lower back", "Knee", "Hip", "Shoulder", "Neck", "None" ] },
    { key: "contact", title: "Where should Dan reach you?" }
  ];
  var TOTAL = STEPS.length;

  var st = { step: 0, a: {}, first: "", phone: "", email: "", done: false };
  /* ---- Hardening helpers ---- */
  var MAX = { first: 40, phone: 20, email: 254 };
  var MIN_FILL_MS = 3000;                 // humans can't finish 4 taps + a form faster than this
  var loadedAt = Date.now();
  // Strip control chars and angle brackets, collapse whitespace, cap length.
  function clean(v, max) {
    return String(v == null ? "" : v).replace(/[\u0000-\u001F\u007F<>]/g, "").replace(/\s+/g, " ").trim().slice(0, max || 200);
  }
  function allowed(stepKey, v) {
    var s = STEPS.filter(function (x) { return x.key === stepKey; })[0];
    if (!s || !s.options) return false;
    return s.options.some(function (o) { return (Array.isArray(o) ? o[0] : o) === v; });
  }
  // Only accept saved answers that match real options (sessionStorage can be edited by anyone).
  function sanitizeState(x) {
    var out = { step: 0, a: {}, first: "", phone: "", email: "", done: false, preset: false, t0: 0 };
    if (!x || typeof x !== "object") return out;
    var n = parseInt(x.step, 10); out.step = (n >= 0 && n < TOTAL) ? n : 0;
    var a = x.a || {};
    ["goal", "interest", "time"].forEach(function (k) { if (typeof a[k] === "string" && allowed(k, a[k])) out.a[k] = a[k]; });
    if (Array.isArray(a.pain)) out.a.pain = a.pain.filter(function (v) { return allowed("pain", v); }).slice(0, 6);
    out.first = clean(x.first, MAX.first); out.phone = clean(x.phone, MAX.phone); out.email = clean(x.email, MAX.email);
    out.preset = !!x.preset; out.t0 = Number(x.t0) > 0 ? Number(x.t0) : 0;
    return out;
  }
  try { var saved = JSON.parse(sessionStorage.getItem(STORE) || "null"); if (saved && !saved.done) { st = sanitizeState(saved); save(); } } catch (e) {}
  function markStart() { if (!st.t0) { st.t0 = Date.now(); save(); } }
  function save() { try { sessionStorage.setItem(STORE, JSON.stringify(st)); } catch (e) {} }

  var top = quiz.querySelector(".quiz-top"), bar = quiz.querySelector(".quiz-bar"), barFill = bar.querySelector("span");
  var count = quiz.querySelector(".quiz-count"), back = quiz.querySelector(".quiz-back");
  top.hidden = false; bar.hidden = false;

  function esc(t) { return String(t).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }

  function render(focus) {
    var s = STEPS[st.step];
    count.textContent = "Step " + (st.step + 1) + " of " + TOTAL;
    barFill.style.width = ((st.step + 1) / TOTAL * 100) + "%";
    bar.setAttribute("aria-hidden", "true");
    back.hidden = st.step === 0;
    var h = "";
    if (s.multi) {
      var sel = Array.isArray(st.a[s.key]) ? st.a[s.key] : [];
      h += '<div class="q" role="group" aria-labelledby="q-title"><h3 id="q-title" class="q-title" tabindex="-1">' + esc(s.title) + "</h3>";
      if (s.sub) h += '<p class="q-sub">' + esc(s.sub) + "</p>";
      h += '<div class="chips">';
      s.options.forEach(function (o) {
        h += '<button type="button" class="chip" data-value="' + esc(o) + '" aria-pressed="' + (sel.indexOf(o) > -1) + '">' +
             '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5 9-10"/></svg>' + esc(o) + "</button>";
      });
      h += '</div><div class="q-actions"><button type="button" class="btn btn-primary btn-lg btn-block q-next"></button></div></div>';
      body.innerHTML = h;
      var nextBtn = body.querySelector(".q-next");
      var sync = function () { var cur = st.a[s.key] || []; nextBtn.textContent = cur.length ? "Continue" : "Skip for now"; };
      sync();
      body.querySelectorAll(".chip").forEach(function (c) {
        c.addEventListener("click", function () {
          markStart();
          var v = c.getAttribute("data-value"), cur = Array.isArray(st.a[s.key]) ? st.a[s.key].slice() : [];
          var i = cur.indexOf(v);
          if (i > -1) cur.splice(i, 1);
          else if (v === "None") cur = ["None"];
          else { cur = cur.filter(function (x) { return x !== "None"; }); cur.push(v); }
          st.a[s.key] = cur; save();
          body.querySelectorAll(".chip").forEach(function (x) { x.setAttribute("aria-pressed", String(cur.indexOf(x.getAttribute("data-value")) > -1)); });
          sync();
        });
      });
      nextBtn.addEventListener("click", function () { st.step = Math.min(st.step + 1, TOTAL - 1); save(); render(true); });
    } else if (s.options) {
      h += '<div class="q" role="group" aria-labelledby="q-title"><h3 id="q-title" class="q-title" tabindex="-1">' + esc(s.title) + "</h3>";
      if (s.sub) h += '<p class="q-sub">' + esc(s.sub) + "</p>";
      h += '<div class="opts' + (s.options.length <= 2 ? " opts-2" : "") + '">';
      s.options.forEach(function (o) {
        var on = st.a[s.key] === o[0];
        h += '<button type="button" class="opt" data-value="' + esc(o[0]) + '" aria-pressed="' + on + '">' +
             '<span class="opt-ic">' + icon(o[1]) + "</span>" +
             '<span class="opt-txt"><span class="opt-label">' + esc(o[0]) + "</span>" + (o[2] ? '<span class="opt-sub">' + esc(o[2]) + "</span>" : "") + "</span>" +
             '<svg class="opt-arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg></button>';
      });
      h += "</div></div>";
      body.innerHTML = h;
      body.querySelectorAll(".opt").forEach(function (b) {
        b.addEventListener("click", function () {
          markStart();
          st.a[s.key] = b.getAttribute("data-value");
          body.querySelectorAll(".opt").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
          var next = st.step + 1;
          if (STEPS[next] && STEPS[next].key === "interest" && st.preset) next++; // already answered via a pricing card
          st.step = Math.min(next, TOTAL - 1); save();
          setTimeout(function () { render(true); }, 160); // brief visual confirmation, then advance
        });
      });
    } else {
      h += '<form class="q q-contact" id="lead-form" novalidate>' +
        '<h3 id="q-title" class="q-title" tabindex="-1">' + esc(s.title) + "</h3>" +
        '<p class="q-promise">Dan will reach out by text or call within 1 business day to book your free consult.</p>' +
        '<div class="hp" aria-hidden="true"><label for="q-hp">Leave empty</label><input id="q-hp" name="_honey" type="text" tabindex="-1" autocomplete="off"></div>' +
        '<div class="field"><label for="q-first">First name</label>' +
          '<input id="q-first" name="first" type="text" maxlength="40" autocomplete="given-name" autocapitalize="words" enterkeyhint="next" required value="' + esc(st.first) + '">' +
          '<p class="error" id="q-first-err" hidden>Please add your first name (letters only).</p></div>' +
        '<div class="field"><label for="q-phone">Mobile number</label>' +
          '<input id="q-phone" name="phone" type="tel" maxlength="20" inputmode="tel" autocomplete="tel" enterkeyhint="next" required placeholder="(714) 000-0000" value="' + esc(st.phone) + '">' +
          '<p class="error" id="q-phone-err" hidden>Please enter a valid mobile number.</p></div>' +
        '<div class="field"><label for="q-email">Email <span class="opt-tag">(optional)</span></label>' +
          '<input id="q-email" name="email" type="email" maxlength="254" inputmode="email" autocomplete="email" autocapitalize="off" spellcheck="false" enterkeyhint="send" value="' + esc(st.email) + '">' +
          '<p class="error" id="q-email-err" hidden>That email doesn\'t look right.</p></div>' +
        '<button class="btn btn-primary btn-lg btn-block" type="submit">Book my free consult</button>' +
        '<p class="consent">By tapping &ldquo;Book my free consult,&rdquo; you agree to our <a href="/privacy" target="_blank" rel="noopener noreferrer">Privacy Policy</a> and <a href="/terms" target="_blank" rel="noopener noreferrer">Terms</a>, and that Fig Performance may call or text this number about your consultation and services. Msg frequency varies; msg &amp; data rates may apply. Reply STOP to opt out, HELP for help. Consent is not a condition of purchase.</p>' +
        '<div class="form-status" role="alert" tabindex="-1"></div>' +
        "</form>";
      body.innerHTML = h;
      wireContact();
    }
    if (focus) {
      var t = body.querySelector(".q-title");
      if (t) t.focus({ preventScroll: true });
      var r = quiz.getBoundingClientRect();
      if (r.top < 60 || r.top > window.innerHeight * 0.5) quiz.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  back.addEventListener("click", function () {
    if (st.step > 0) { st.step--; save(); render(true); }
  });

  function setErr(id, on) {
    var i = doc.getElementById(id), m = doc.getElementById(id + "-err");
    if (i) { i.setAttribute("aria-invalid", String(on)); if (on) i.setAttribute("aria-describedby", id + "-err"); else i.removeAttribute("aria-describedby"); }
    if (m) m.hidden = !on;
  }

  function wireContact() {
    var form = doc.getElementById("lead-form"), F = form.elements;
    var status = form.querySelector(".form-status"), btn = form.querySelector('button[type="submit"]');
    ["first", "phone", "email"].forEach(function (n) {
      F[n].addEventListener("input", function () { st[n] = String(F[n].value).slice(0, MAX[n]); save(); setErr("q-" + n, false); });
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      status.className = "form-status"; status.textContent = "";
      var first = clean(F.first.value, MAX.first);
      var phone = clean(F.phone.value, MAX.phone).replace(/[^0-9+().\- ]/g, "");
      var email = clean(F.email.value, MAX.email).replace(/\s/g, "");
      var digits = phone.replace(/\D/g, ""), bad = null;
      if (!first || !/^[\p{L}\p{M}' .\-]+$/u.test(first)) { setErr("q-first", true); bad = bad || F.first; }
      if (digits.length < 10 || digits.length > 15) { setErr("q-phone", true); bad = bad || F.phone; }
      if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { setErr("q-email", true); bad = bad || F.email; }
      if (bad) { bad.focus(); return; }
      if (F._honey.value) return;            // bot filled the hidden honeypot: drop silently
      if (Date.now() - (st.t0 || loadedAt) < MIN_FILL_MS) {   // submitted impossibly fast: likely a bot
        status.className = "form-status err";
        status.textContent = "Please take a moment to check your details, then tap the button again.";
        st.t0 = Date.now() - MIN_FILL_MS; save();            // a real person's second tap goes through
        status.focus(); return;
      }

      var a = sanitizeState(st).a;
      var data = {
        "First name": first,
        "Mobile": phone,
        "Email": email || "(not provided)",
        "Main goal": a.goal || "(skipped)",
        "Interested in": a.interest || "(skipped)",
        "Best time to train": a.time || "(skipped)",
        "Pain or problem areas": (a.pain && a.pain.length) ? a.pain.join(", ") : "(skipped)",
        "Consent": "Yes: agreed to Privacy Policy & Terms and to calls/texts about consultation & services (STOP to opt out; not a condition of purchase). Policy version " + CONFIG.POLICY_VERSION,
        "Submitted from": "figperformance.com booking quiz",
        _subject: "New Fig Performance consult request: " + first + " (" + (a.interest || "interest not given") + ")",
        _template: "table",
        _captcha: "false"
      };
      if (email) data._replyto = email;

      if (btn.disabled) return;              // no double submits
      btn.disabled = true; var label = btn.textContent; btn.textContent = "Sending...";
      var ctrl = ("AbortController" in window) ? new AbortController() : null;
      var timer = setTimeout(function () { if (ctrl) ctrl.abort(); }, 15000);
      (navigator.onLine === false ? Promise.reject(new Error("offline")) : fetch(CONFIG.FORM_ENDPOINT, {
        method: "POST",
        mode: "cors",
        credentials: "omit",
        referrerPolicy: "strict-origin-when-cross-origin",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data),
        signal: ctrl ? ctrl.signal : undefined
      }))
        .then(function (res) { return res.json().catch(function () { return {}; }).then(function (j) { return { ok: res.ok, j: j }; }); })
        .then(function (r) {
          clearTimeout(timer);
          if (!r.ok || (r.j && (r.j.success === false || r.j.success === "false"))) throw new Error("send failed");
          st.done = true;
          try { sessionStorage.removeItem(STORE); } catch (e) {}
          showThanks(first, a.interest);
        })
        .catch(function (err) {
          clearTimeout(timer);
          btn.disabled = false; btn.textContent = label;
          if (err && err.message === "offline") {
            status.className = "form-status err";
            status.textContent = "You appear to be offline. Your answers are saved; reconnect and tap the button again.";
            status.focus(); return;
          }
          status.className = "form-status err";
          status.innerHTML = "Sorry, that didn't go through. Please try again in a moment" +
            (CONFIG.PHONE ? ', or call/text <a href="tel:+1' + CONFIG.PHONE.replace(/\D/g, "").slice(-10) + '">' + esc(CONFIG.PHONE) + "</a>." :
             ', or message us on <a href="https://www.instagram.com/figperformance/" target="_blank" rel="noopener noreferrer">Instagram</a>.');
          status.focus();
        });
    });
  }

  function showThanks(first, interest) {
    var next = {
      "1:1 personal training": "Dan will reach out to set up your free 1:1 consult this week: about an hour for an assessment, your goals, and a game plan.",
      "Membership": "Dan will reach out to schedule your tour during pre-opening week. Membership doesn't include weekly one-on-one personal training.",
      "Concierge personal training": "Dan will reach out to set up a free phone call, then an assessment at your home.",
      "Online coaching": "Dan will reach out to set up a free video call to talk through your goals and how online coaching works.",
      "Not sure, help me choose": "Dan will reach out, talk through your goals, and help you pick the right fit."
    }[interest] || "Dan will reach out to book your free consult.";
    top.hidden = true; bar.hidden = true;
    quiz.setAttribute("data-state", "done");
    body.innerHTML =
      '<div class="quiz-done">' +
        '<div class="done-check" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12l5 5 9-10"/></svg></div>' +
        '<h3 class="q-title" tabindex="-1">You\'re in, ' + esc(first) + ".</h3>" +
        "<p>" + esc(next) + "</p>" +
        '<ul class="done-steps"><li>Keep your phone handy; Dan will reach out by text or call.</li><li>Your consult is free.</li></ul>' +
        '<p class="done-event"><strong>Grand opening:</strong> Saturday, November 14, 10 AM&ndash;1 PM at 1284 E. Yorba Linda Blvd, Placentia. <a href="/grand-opening.ics" download>Add to calendar</a></p>' +
        '<a class="btn btn-secondary" href="https://www.instagram.com/figperformance/" target="_blank" rel="noopener noreferrer">See us on Instagram</a>' +
      "</div>";
    body.querySelector(".q-title").focus();
  }

  /* CTAs: preselect interest from pricing cards, then bring the quiz into focus */
  doc.querySelectorAll('a[href="#consult"]').forEach(function (link) {
    link.addEventListener("click", function () {
      if (st.done) return;
      var pre = link.getAttribute("data-interest");
      if (pre) {
        st.a.interest = pre; st.preset = true;
        if (st.step <= 1) st.step = st.a.goal ? 2 : 0;  // skip the question they already answered by tapping a card
        save(); render(false);
      }
      setTimeout(function () { var t = body.querySelector(".q-title"); if (t) t.focus({ preventScroll: true }); }, 450);
    });
  });

  render(false);


})();

/* ============ v31: hero studio video (poster paints first; video fetched only after load + idle) ============ */
(function () {
  var v = document.querySelector(".tour-video");
  if (!v) return;
  var frame = v.closest(".tour-frame");
  var btn = frame && frame.querySelector(".tour-toggle");
  var mq = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
  var conn = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
  var manual = (mq && mq.matches) || !!(conn && conn.saveData);
  var sourced = false, ready = false, visible = true, userPaused = false;
  v.muted = true;
  function attachSources() {
    if (sourced) return;
    var small = Math.min(window.innerWidth, screen.width || 9999) < 700;
    v.querySelectorAll("source[data-src]").forEach(function (s) { s.src = (small && s.getAttribute("data-src-sm")) || s.getAttribute("data-src"); });
    v.preload = "auto"; v.load(); sourced = true;
  }
  function sync() {
    if (!btn) return;
    var playing = !v.paused;
    btn.classList.toggle("is-playing", playing);
    btn.setAttribute("aria-label", playing ? "Pause the studio video" : "Play the studio video");
  }
  function tryPlay() {
    attachSources();
    var p = v.play();
    if (p && p.catch) p.catch(function () { if (frame) frame.classList.add("is-manual"); sync(); });
  }
  v.addEventListener("playing", function () { if (frame) frame.classList.add("is-live"); });
  v.addEventListener("play", sync); v.addEventListener("pause", sync);
  if (btn) {
    btn.hidden = false;
    btn.addEventListener("click", function () {
      if (v.paused) { userPaused = false; tryPlay(); } else { userPaused = true; v.pause(); }
    });
  }
  if (manual && frame) frame.classList.add("is-manual");
  function start() {
    ready = true;
    if (manual) return;
    attachSources();
    if (visible && !userPaused) tryPlay();
  }
  function whenIdle() {
    if ("requestIdleCallback" in window) window.requestIdleCallback(start, { timeout: 2500 });
    else setTimeout(start, 1200);
  }
  if (document.readyState === "complete") whenIdle();
  else window.addEventListener("load", whenIdle, { once: true });
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        visible = e.isIntersecting;
        if (visible && ready && !manual && !userPaused) tryPlay();
        else if (!visible && !v.paused) v.pause();
      });
    }, { threshold: 0.35 }).observe(v);
  }
  if (mq && mq.addEventListener) mq.addEventListener("change", function (e) { if (e.matches) { manual = true; v.pause(); if (frame) frame.classList.add("is-manual"); } });
})();
