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
  POLICY_VERSION: "2026-11-17.2"         // bump when privacy/terms/consent text changes
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

  /* ---- Back-to-top button: after ~1.5 screens, hidden while the booking section is on screen ---- */
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

  /* The booking quiz was replaced by assets/booking.js (day and time picker), Nov 17, 2026. */


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


/* FIG Performance GA4 tracking — G-BTJWNH2G73 */
(function () {
  "use strict";
  if (window.__figGA4Loaded) return;
  window.__figGA4Loaded = true;
  var measurementId = "G-BTJWNH2G73";
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
  window.gtag("js", new Date());
  window.gtag("config", measurementId);
  var tag = document.createElement("script");
  tag.async = true;
  tag.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(measurementId);
  document.head.appendChild(tag);

  document.addEventListener("click", function (event) {
    var link = event.target && event.target.closest && event.target.closest("a[href]");
    if (!link) return;
    var href = link.getAttribute("href") || "";
    if (/^tel:/i.test(href)) window.gtag("event", "phone_click");
    if (/^sms:/i.test(href)) window.gtag("event", "sms_click");
  });
})();
