/* ==========================================================
   Fig Performance: /sign page (waiver + PT client checklist)
   - Prefills program details from the link Dan sends:
       /sign?name=&sessions=&billing=&today=&recurring=&start=
     Valid params are shown read-only; missing ones stay editable.
   - Validates everything with clear messages, then lets the form POST
     natively to FormSubmit (redirects to /signed via _next).
   - Adds hidden fields with the full text as signed, timestamps and the
     document version so the emailed record is self-contained.
   No inline code: CSP is script-src 'self'.
   ========================================================== */
(function () {
  "use strict";
  var DOC_VERSION = "waiver-v1 2026-10-24; checklist-v1 2026-10-24";
  var TZ = "America/Los_Angeles";
  var MIN_FILL_MS = 5000;             // nobody reads and signs two documents faster than this
  var doc = document;
  var form = doc.getElementById("sign-form");
  if (!form) return;
  var loadedAt = Date.now();
  var $ = function (id) { return doc.getElementById(id); };

  form.noValidate = true;             // we show our own, clearer messages

  /* ---------- helpers ---------- */
  function clean(v, max) {
    return String(v == null ? "" : v).replace(/[\u0000-\u001F\u007F<>]/g, "").replace(/\s+/g, " ").trim().slice(0, max || 200);
  }
  function norm(v) { return clean(v, 200).toLowerCase().replace(/[^\p{L}\p{M}' \-]/gu, "").replace(/\s+/g, " ").trim(); }
  function digits(v) { return String(v || "").replace(/\D/g, ""); }
  function phoneOk(v) { var d = digits(v); if (d.length === 11 && d.charAt(0) === "1") d = d.slice(1); return d.length === 10; }
  function money(v) {
    var s = String(v == null ? "" : v).replace(/[$,\s]/g, "");
    if (!/^\d{1,6}(\.\d{1,2})?$/.test(s)) return null;
    return Number(s).toFixed(2);
  }
  function isoDateOk(s) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(s)) return false;
    var p = s.split("-").map(Number), d = new Date(Date.UTC(p[0], p[1] - 1, p[2]));
    return d.getUTCFullYear() === p[0] && d.getUTCMonth() === p[1] - 1 && d.getUTCDate() === p[2];
  }
  function addMonths(s, n) {          // "2026-11-02" + 3 months, clamped to month end
    var p = s.split("-").map(Number), y = p[0], m = p[1] - 1 + n, d = p[2];
    y += Math.floor(m / 12); m = ((m % 12) + 12) % 12;
    var last = new Date(Date.UTC(y, m + 1, 0)).getUTCDate();
    return new Date(Date.UTC(y, m, Math.min(d, last)));
  }
  function longDate(dt, tz) { return dt.toLocaleDateString("en-US", { timeZone: tz || TZ, year: "numeric", month: "long", day: "numeric" }); }
  function pacificStamp(dt) {
    return dt.toLocaleString("en-US", { timeZone: TZ, year: "numeric", month: "long", day: "numeric", hour: "numeric", minute: "2-digit", second: "2-digit", timeZoneName: "short" });
  }
  function setErr(id, on) {
    var i = $(id), m = $(id + "-err");
    if (i) {
      i.setAttribute("aria-invalid", String(on));
      var help = i.getAttribute("data-help") || "";
      if (on) i.setAttribute("aria-describedby", (help ? help + " " : "") + id + "-err");
      else if (help) i.setAttribute("aria-describedby", help); else i.removeAttribute("aria-describedby");
    }
    if (m) m.hidden = !on;
  }
  // remember any existing describedby (help text) so errors add to it rather than replace it
  form.querySelectorAll("input[aria-describedby]").forEach(function (i) { i.setAttribute("data-help", i.getAttribute("aria-describedby")); });

  /* ---------- date: auto-filled (Pacific) and read-only ---------- */
  var today = longDate(new Date());
  form.querySelectorAll(".date-stamp").forEach(function (i) { i.value = today; i.readOnly = true; i.setAttribute("aria-readonly", "true"); });

  /* ---------- prefill from the link ---------- */
  var q = new URLSearchParams(window.location.search);
  var prefilled = [];
  function lock(input) { input.readOnly = true; input.setAttribute("aria-readonly", "true"); input.classList.add("is-locked"); }

  var name = clean(q.get("name"), 120);
  if (name) {                          // name stays editable: the client confirms their own legal name
    var parts = name.split(" ");
    if (!$("f-first").value) $("f-first").value = parts.shift();
    if (parts.length && !$("f-last").value) $("f-last").value = parts.join(" ");
  }
  var sess = clean(q.get("sessions"), 2);
  if (/^[1-7]$/.test(sess)) { $("f-sessions").value = sess; lock($("f-sessions")); prefilled.push("sessions"); }
  var bill = clean(q.get("billing"), 10).toLowerCase();
  if (bill === "weekly" || bill === "monthly") {
    var on = $(bill === "weekly" ? "f-bill-weekly" : "f-bill-monthly"), off = $(bill === "weekly" ? "f-bill-monthly" : "f-bill-weekly");
    on.checked = true; off.disabled = true;        // checked one still submits
    on.closest(".radio-row").classList.add("is-locked");
    prefilled.push("billing");
  }
  var td = money(q.get("today"));
  if (td !== null) { $("f-today").value = td; lock($("f-today")); prefilled.push("today"); }
  var rc = money(q.get("recurring"));
  if (rc !== null) { $("f-recurring").value = rc; lock($("f-recurring")); prefilled.push("recurring"); }
  /* Standard plans: fill the amounts from sessions + billing when the link doesn't set them.
     Monthly = $387 per weekly session ($90 x 4.3 weeks); weekly = $90 per session. First payment = one period. */
  if (td === null && rc === null && /^[1-3]$/.test(sess) && (bill === "weekly" || bill === "monthly")) {
    var plan = (bill === "weekly" ? 90 : 387) * Number(sess);
    var planTxt = plan.toFixed(2);
    $("f-today").value = planTxt; lock($("f-today")); prefilled.push("today");
    $("f-recurring").value = planTxt; lock($("f-recurring")); prefilled.push("recurring");
  }
  var sd = clean(q.get("start"), 10);
  if (isoDateOk(sd)) { $("f-start").value = sd; lock($("f-start")); prefilled.push("start"); }
  if (prefilled.length) $("program-note").hidden = false;

  /* ---------- derived fields ---------- */
  function billingValue() { var c = form.querySelector('input[name="Billing"]:checked'); return c ? c.value : ""; }
  function syncUnit() {
    var b = billingValue();
    $("recurring-unit").textContent = b === "Weekly" ? "week" : b === "Monthly" ? "month" : "week or month";
  }
  function syncEnds() {
    var s = $("f-start").value;
    $("f-ends").value = isoDateOk(s) ? longDate(addMonths(s, 3), "UTC") : "";
  }
  form.querySelectorAll('input[name="Billing"]').forEach(function (r) { r.addEventListener("change", function () { syncUnit(); setErr("f-billing", false); }); });
  $("f-start").addEventListener("change", syncEnds);
  $("f-start").addEventListener("input", syncEnds);
  syncUnit(); syncEnds();

  /* ---------- under-18 guardian block ---------- */
  var gSec = $("sec-guardian"), gFields = ["f-g-sig", "f-g-rel", "f-g-phone", "f-g-date"];
  function syncMinor() {
    var minor = $("f-minor").checked;
    gSec.hidden = !minor;
    gFields.forEach(function (id) { var i = $(id); i.disabled = !minor; if (id !== "f-g-date") i.required = minor; });
    $("submit-step").textContent = minor ? "5" : "4";
    if (!minor) ["f-g-sig", "f-g-rel", "f-g-phone"].forEach(function (id) { setErr(id, false); });
  }
  $("f-minor").addEventListener("change", syncMinor);
  syncMinor();

  /* ---------- initials: uppercase letters only ---------- */
  form.querySelectorAll(".init-input").forEach(function (i) {
    i.addEventListener("input", function () { var v = i.value.toUpperCase().replace(/[^\p{L}]/gu, "").slice(0, 4); if (v !== i.value) i.value = v; });
  });

  /* clear an error as soon as the person edits that field */
  form.querySelectorAll("input").forEach(function (i) {
    i.addEventListener("input", function () { if (i.id && $(i.id + "-err")) setErr(i.id, false); });
    i.addEventListener("change", function () { if (i.id && $(i.id + "-err")) setErr(i.id, false); });
  });

  /* ---------- validation ---------- */
  var NAME_RE = /^[\p{L}\p{M}' .\-]+$/u;
  function validate() {
    var bad = [];
    function check(id, ok) { setErr(id, !ok); if (!ok) bad.push(id); }
    var first = clean($("f-first").value, 60), last = clean($("f-last").value, 60);
    check("f-first", !!first && NAME_RE.test(first));
    check("f-last", !!last && NAME_RE.test(last));
    check("f-phone", phoneOk($("f-phone").value));
    check("f-email", /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(clean($("f-email").value, 254)));
    check("f-ec-name", clean($("f-ec-name").value, 80).length >= 2);
    check("f-ec-phone", phoneOk($("f-ec-phone").value));

    var sig = norm($("f-sig-waiver").value), nf = norm(first), nl = norm(last);
    var sigWords = " " + sig + " ";
    check("f-sig-waiver", !!sig && !!nf && !!nl && sig.split(" ").length >= 2 &&
      sigWords.indexOf(" " + nf.split(" ")[0] + " ") > -1 && sig.indexOf(nl) > -1);
    check("f-date-waiver", !!clean($("f-date-waiver").value, 40));

    for (var n = 1; n <= 6; n++) check("f-init-" + n, /^\p{L}{2,4}$/u.test($("f-init-" + n).value.trim()));

    check("f-sessions", /^[1-7]$/.test($("f-sessions").value.trim()));
    check("f-billing", !!billingValue());
    check("f-today", money($("f-today").value) !== null);
    check("f-recurring", money($("f-recurring").value) !== null);
    check("f-start", isoDateOk($("f-start").value));

    var sig2 = norm($("f-sig-checklist").value);
    check("f-sig-checklist", !!sig2 && sig2 === sig && bad.indexOf("f-sig-waiver") === -1);
    check("f-date-checklist", !!clean($("f-date-checklist").value, 40));

    if ($("f-minor").checked) {
      var g = norm($("f-g-sig").value);
      check("f-g-sig", g.split(" ").length >= 2 && NAME_RE.test(clean($("f-g-sig").value, 120)) && g !== sig);
      check("f-g-rel", clean($("f-g-rel").value, 40).length >= 2);
      check("f-g-phone", phoneOk($("f-g-phone").value));
    }
    check("f-consent", $("f-consent").checked);
    return bad;
  }

  /* ---------- record built at submit ---------- */
  function textOf(el) { return el.textContent.replace(/\s+/g, " ").trim(); }
  function addHidden(name, value) {
    var i = doc.createElement("input");
    i.type = "hidden"; i.name = name; i.value = value; i.setAttribute("data-generated", "1");
    form.appendChild(i);
  }
  function buildRecord(now) {
    form.querySelectorAll('[data-generated="1"]').forEach(function (n) { n.remove(); });
    var first = clean($("f-first").value, 60), last = clean($("f-last").value, 60), full = first + " " + last;
    var stamp = pacificStamp(now), iso = now.toISOString();
    var minor = $("f-minor").checked;
    var w = [], c = [];

    w.push("FIG PERFORMANCE - Liability Waiver and Release of Liability (" + DOC_VERSION.split(";")[0] + ")");
    w.push("First: " + first + " | Last: " + last);
    w.push("Cell Phone: " + clean($("f-phone").value, 20));
    w.push("Email: " + clean($("f-email").value, 254));
    w.push("Emergency Contact (name and phone): " + clean($("f-ec-name").value, 80) + ", " + clean($("f-ec-phone").value, 20));
    $("waiver-doc").querySelectorAll(".doc-head, .doc-p").forEach(function (p) { w.push(textOf(p)); });
    w.push("Sign Here: /s/ " + clean($("f-sig-waiver").value, 120) + " (MEMBER SIGNATURE, typed electronic signature)     Date: " + $("f-date-waiver").value);
    if (minor) w.push("If the member is under 18, parent or guardian signature: /s/ " + clean($("f-g-sig").value, 120) + " (" + clean($("f-g-rel").value, 40) + ")   Date: " + $("f-g-date").value);
    else w.push("Member confirmed they are 18 or older (under-18 box not checked).");

    c.push("FIG PERFORMANCE - Personal Training Client Checklist (" + DOC_VERSION.split("; ")[1] + ")");
    c.push("Client Name: " + full + "      Date: " + $("f-date-checklist").value);
    $("checklist-doc").querySelectorAll(".check-item").forEach(function (li) {
      var n = li.getAttribute("data-item");
      c.push(textOf(li.querySelector(".doc-p")) + "  Initials: " + $("f-init-" + n).value.trim());
    });
    var b = billingValue(), unit = b === "Weekly" ? "week" : "month";
    c.push("Program Outline");
    c.push("Program consists of " + $("f-sessions").value.trim() + " (50-minute) session(s) per week.");
    c.push("Billing: " + b + "      Amount due today: $" + money($("f-today").value) + "      Then $" + money($("f-recurring").value) + " per " + unit);
    c.push("Start date: " + longDate(new Date($("f-start").value + "T12:00:00Z"), "UTC") + " (" + $("f-start").value + ")      Commitment ends: " + $("f-ends").value);
    c.push("Acknowledged and agreed by:");
    c.push("Client Signature: /s/ " + clean($("f-sig-checklist").value, 120) + " (typed electronic signature)      Date: " + $("f-date-checklist").value);
    if (minor) c.push("Parent or guardian signature: /s/ " + clean($("f-g-sig").value, 120) + " (" + clean($("f-g-rel").value, 40) + ")      Date: " + $("f-g-date").value);
    c.push("Trainer Signature: (to be countersigned by Fig Performance)");
    c.push("Fig Performance (Train With Dan Inc.) · Placentia, CA · (714) 396-7178 · trainat@figperformance.com");

    $("f-subject").value = "SIGNED: Fig Performance waiver and checklist - " + full;
    addHidden("_replyto", clean($("f-email").value, 254));
    addHidden("Signed at (Pacific)", stamp);
    addHidden("Signed at (ISO 8601, UTC)", iso);
    addHidden("Signer device time zone", (Intl.DateTimeFormat().resolvedOptions().timeZone || "unknown"));
    addHidden("Document versions", DOC_VERSION);
    addHidden("Program details prefilled by link", prefilled.length ? "Yes (" + prefilled.join(", ") + ")" : "No (entered on the page)");
    addHidden("Signed from", window.location.origin + window.location.pathname);
    addHidden("Waiver full text as signed", w.join("\n\n"));
    addHidden("Checklist full text as signed", c.join("\n\n"));
    $("sign-stamp").textContent = "Signed electronically by " + full + " on " + stamp + ".";
  }

  /* ---------- submit ---------- */
  var status = $("sign-status"), btn = $("sign-submit"), btnLabel = btn.textContent;
  form.addEventListener("submit", function (e) {
    status.className = "form-status"; status.textContent = "";
    var bad = validate();
    if (bad.length) {
      e.preventDefault();
      status.className = "form-status err";
      status.textContent = bad.length === 1 ? "One item needs your attention before you can sign. It's highlighted above." :
        bad.length + " items need your attention before you can sign. They're highlighted above, starting with the first one.";
      var first = $(bad[0]) || form.querySelector('input[name="Billing"]');
      if (bad[0] === "f-billing") first = $("f-bill-weekly").disabled ? $("f-bill-monthly") : $("f-bill-weekly");
      first.focus();
      return;
    }
    if (form.elements._honey.value) { e.preventDefault(); return; }       // bot: drop silently
    if (Date.now() - loadedAt < MIN_FILL_MS) {
      e.preventDefault();
      status.className = "form-status err";
      status.textContent = "Please take a moment to review both documents, then tap Sign and submit again.";
      loadedAt = Date.now() - MIN_FILL_MS;
      status.focus(); return;
    }
    if (btn.disabled) { e.preventDefault(); return; }                      // no double submits
    buildRecord(new Date());
    btn.disabled = true; btn.textContent = "Submitting...";
    // native POST continues to FormSubmit, which redirects to /signed
  });
  // coming back with the Back button (bfcache): re-enable the button
  window.addEventListener("pageshow", function () { btn.disabled = false; btn.textContent = btnLabel; });
})();
