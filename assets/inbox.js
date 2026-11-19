/* Fig Performance text inbox (staff page). Talks only to /api/inbox on this site. */
(function () {
  "use strict";
  var $ = function (id) { return document.getElementById(id); };
  var login = $("ib-login"), setup = $("ib-setup"), app = $("ib-app"), logout = $("ib-logout");
  var current = null, timer = null, lastSig = "";

  function api(method, data) {
    var url = "/api/inbox", opts = { method: method, credentials: "same-origin", headers: { Accept: "application/json" } };
    if (method === "GET") url += "?" + new URLSearchParams(data || {}).toString();
    else { opts.headers["Content-Type"] = "application/json"; opts.body = JSON.stringify(data || {}); }
    return fetch(url, opts).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (j) { return { status: r.status, j: j }; });
    });
  }
  var tabs = $("ib-tabs"), tab = "texts", signedIn = false;
  function show(which) {                       // which: login | setup | app (texts) | schedule | settings
    login.hidden = which !== "login"; setup.hidden = which !== "setup"; app.hidden = which !== "app";
    $("ib-schedule").hidden = which !== "schedule"; $("ib-settings").hidden = which !== "settings";
    $("ib-week").hidden = which !== "week"; $("ib-clients").hidden = which !== "clients";
    if (which === "login") signedIn = false;
    logout.hidden = !signedIn; tabs.hidden = !signedIn;
    if (which !== "app") { clearInterval(timer); timer = null; }
  }
  function setTab(name) {
    tab = name;
    tabs.querySelectorAll("button").forEach(function (b) { if (b.getAttribute("data-tab") === name) b.setAttribute("aria-current", "true"); else b.removeAttribute("aria-current"); });
    if (name === "texts") start(); else if (name === "schedule") loadSchedule(); else if (name === "week") loadWeek(); else if (name === "clients") loadClients(); else loadSettings();
  }
  tabs.addEventListener("click", function (e) { var b = e.target.closest("button[data-tab]"); if (b) setTab(b.getAttribute("data-tab")); });
  var STATUS = { "new": "New", booked: "Booked", showed: "Showed", no_show: "No-show", signed_up: "Signed up", not_interested: "Not interested" };
  function pretty(n) { var m = /^\+1(\d{3})(\d{3})(\d{4})$/.exec(n || ""); return m ? "(" + m[1] + ") " + m[2] + "-" + m[3] : (n || ""); }
  function ago(iso) {
    var d = new Date(iso), now = new Date();
    if (isNaN(d)) return "";
    var same = d.toDateString() === now.toDateString();
    return same ? d.toLocaleTimeString([], { hour: "numeric", minute: "2-digit" })
      : d.toLocaleDateString([], { month: "short", day: "numeric" }) + ", " + d.toLocaleTimeString([], { hour: "numeric", minute: "2-digit" });
  }
  function el(tag, cls, text) { var n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; }
  function handle(r) {                         // shared handling for "signed out" and "not set up"
    if (r.status === 401) { show("login"); $("ib-pw").focus(); return false; }
    if (r.status === 503) {
      if (r.j.need !== "INBOX_PASSWORD") signedIn = true;
      $("ib-setup-msg").textContent = r.j.need === "INBOX_PASSWORD"
        ? "The inbox password hasn't been added in Vercel yet (INBOX_PASSWORD, at least 12 characters)."
        : r.j.need === "DATABASE"
          ? "The database hasn't been added in Vercel yet (Storage tab). Bookings, hours and follow-ups need it."
          : "The texting account (Twilio) hasn't been connected in Vercel yet. Once its three keys are added, your conversations show up here. The Schedule and Settings tabs work without it.";
      show("setup"); return false;
    }
    signedIn = true;
    return true;
  }

  /* ----- conversations list ----- */
  function loadList(quiet) {
    return api("GET", { view: "list" }).then(function (r) {
      if (!handle(r)) return;
      show("app");
      var list = r.j.conversations || [];
      var sig = JSON.stringify(list.map(function (c) { return [c.with, c.at, c.needsReply, c.pending]; }));
      if (sig === lastSig && quiet) return;
      lastSig = sig;
      var ul = $("ib-convos"); ul.textContent = "";
      $("ib-list-status").textContent = list.length ? "" : "No texts yet. New bookings appear here as soon as the confirmation text goes out.";
      list.forEach(function (c) {
        var li = el("li"), b = el("button", "ib-convo"); b.type = "button";
        b.setAttribute("data-with", c.with);
        if (current === c.with) b.setAttribute("aria-current", "true");
        var top = el("div", "ib-convo-top"), name = el("span", "ib-convo-name", c.name ? c.name + " · " + pretty(c.with) : pretty(c.with));
        if (c.needsReply) name.appendChild(el("span", "ib-badge", "Replied"));
        if (c.optedOut) name.appendChild(el("span", "ib-badge ib-badge-stop", "Opted out"));
        else if (c.status && STATUS[c.status]) name.appendChild(el("span", "ib-tag", STATUS[c.status]));
        top.appendChild(name); top.appendChild(el("span", "ib-convo-time", ago(c.at)));
        b.appendChild(top);
        b.appendChild(el("p", "ib-convo-last", (c.lastInbound ? "" : "You: ") + c.last));
        li.appendChild(b); ul.appendChild(li);
      });
    });
  }
  $("ib-convos").addEventListener("click", function (e) {
    var b = e.target.closest(".ib-convo"); if (b) openThread(b.getAttribute("data-with"));
  });

  /* ----- one conversation ----- */
  function openThread(num, quiet) {
    current = num; app.setAttribute("data-view", "thread");
    return api("GET", { view: "thread", with: num }).then(function (r) {
      if (!handle(r) || current !== num) return;
      if (r.status !== 200) {
        $("ib-who").textContent = num; $("ib-compose").hidden = true; $("ib-pending").hidden = true;
        var mb = $("ib-msgs"); mb.textContent = ""; mb.removeAttribute("data-count");
        mb.appendChild(el("p", "ib-empty", "This sender can't be opened here (not a regular US mobile number)."));
        return;
      }
      var t = r.j;
      $("ib-who").textContent = t.name ? t.name + " · " + pretty(num) : pretty(num);
      var call = $("ib-call"); call.hidden = false; call.href = "tel:" + num; call.textContent = "Call";
      var box = $("ib-msgs"), atBottom = box.scrollHeight - box.scrollTop - box.clientHeight < 60;
      var count = (t.messages || []).length;
      if (!quiet || String(count) !== box.getAttribute("data-count")) {
        box.textContent = ""; box.setAttribute("data-count", String(count));
        if (!count) box.appendChild(el("p", "ib-empty", "No texts with this number yet. Send the first one below."));
        (t.messages || []).forEach(function (m) {
          var failed = m.status === "failed" || m.status === "undelivered";
          var d = el("div", "ib-msg " + (m.inbound ? "in" : "out") + (failed ? " failed" : ""), m.body);
          d.appendChild(el("small", "", ago(m.at) + (failed ? " · not delivered" : "")));
          box.appendChild(d);
        });
        if (!quiet || atBottom) box.scrollTop = box.scrollHeight;
      }
      var pend = $("ib-pending"); pend.textContent = ""; pend.hidden = !(t.pending || []).length;
      (t.pending || []).forEach(function (p) {
        var row = el("p"), txt = el("span", "", p.body), btn = el("button", "ib-link", "Cancel");
        btn.type = "button"; btn.setAttribute("data-sid", p.sid);
        var left = el("span"); left.appendChild(el("strong", "", "Scheduled reminder  ")); left.appendChild(txt);
        row.appendChild(left); row.appendChild(btn); pend.appendChild(row);
      });
      renderLead(num, t.lead);
      $("ib-compose").hidden = !!(t.lead && t.lead.optedOut);
      document.querySelectorAll(".ib-convo").forEach(function (b) {
        if (b.getAttribute("data-with") === num) b.setAttribute("aria-current", "true"); else b.removeAttribute("aria-current");
      });
    });
  }
  $("ib-pending").addEventListener("click", function (e) {
    var b = e.target.closest("button[data-sid]"); if (!b) return;
    b.disabled = true;
    api("POST", { action: "cancel", sid: b.getAttribute("data-sid") }).then(function () { if (current) openThread(current); });
  });
  $("ib-back").addEventListener("click", function () { current = null; app.removeAttribute("data-view"); loadList(); });

  $("ib-compose").addEventListener("submit", function (e) {
    e.preventDefault();
    var ta = $("ib-text"), text = ta.value.trim(), st = $("ib-send-status"), btn = e.target.querySelector("button");
    if (!text || !current || btn.disabled) return;
    btn.disabled = true; st.className = "ib-status"; st.textContent = "";
    api("POST", { action: "send", to: current, body: text }).then(function (r) {
      btn.disabled = false;
      if (!handle(r)) return;
      if (r.status === 200 && r.j.ok) { ta.value = ""; openThread(current); loadList(true); }
      else { st.className = "ib-status err"; st.textContent = r.j.error === "opted_out" ? "This person replied STOP. You can't text them unless they text START." : "That text didn't send. Check the number and try again."; }
    }).catch(function () { btn.disabled = false; st.className = "ib-status err"; st.textContent = "No connection. Try again."; });
  });
  $("ib-text").addEventListener("keydown", function (e) {
    if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) $("ib-compose").requestSubmit();
  });

  $("ib-new").addEventListener("submit", function (e) {
    e.preventDefault();
    var d = $("ib-new-to").value.replace(/\D/g, ""); if (d.length === 11 && d[0] === "1") d = d.slice(1);
    var st = $("ib-list-status");
    if (d.length !== 10) { st.className = "ib-status err"; st.textContent = "Enter a 10-digit mobile number."; return; }
    st.className = "ib-status"; st.textContent = ""; $("ib-new-to").value = "";
    openThread("+1" + d).then(function () { $("ib-text").focus(); });
  });

  /* ----- lead card (status, consent, booking) above a conversation ----- */
  function statusSelect(current, onChange) {
    var s = el("select", "ib-select"); s.setAttribute("aria-label", "Lead status");
    Object.keys(STATUS).forEach(function (k) { var o = el("option", "", STATUS[k]); o.value = k; if (k === current) o.selected = true; s.appendChild(o); });
    s.addEventListener("change", function () { onChange(s.value, s); });
    return s;
  }
  function renderLead(num, lead) {
    var box = $("ib-lead"); box.textContent = ""; box.hidden = !lead;
    if (!lead) return;
    var row = el("div", "ib-lead-row");
    row.appendChild(statusSelect(lead.status || "new", function (v, s) {
      s.disabled = true;
      api("POST", { action: "lead", phone: num, status: v }).then(function () { s.disabled = false; loadList(true); });
    }));
    if (lead.booking) {
      var d = new Date(lead.booking.start);
      row.appendChild(el("span", "ib-tag", "Consult " + d.toLocaleDateString([], { weekday: "short", month: "short", day: "numeric" }) + ", " +
        d.toLocaleTimeString([], { hour: "numeric", minute: "2-digit" }) + (lead.booking.status === "booked" ? (lead.booking.confirmed ? " · confirmed" : " · not confirmed yet") : " · " + (STATUS[lead.booking.status] || lead.booking.status))));
    }
    row.appendChild(el("span", "ib-tag" + (lead.optedOut ? " ib-badge-stop" : ""), lead.optedOut ? "Replied STOP: no texts" : (lead.marketing ? "OK to send follow-up texts" : "Appointment texts only (no marketing consent)")));
    box.appendChild(row);
    if (lead.goal) box.appendChild(el("p", "ib-help", "Goal: " + lead.goal));
  }

  /* ----- Schedule tab ----- */
  function loadSchedule() {
    $("ib-sched-status").textContent = "Loading…";
    api("GET", { view: "schedule" }).then(function (r) {
      if (!handle(r)) return;
      show("schedule");
      var box = $("ib-sched"), list = r.j.bookings || [], now = Date.now(); box.textContent = "";
      $("ib-sched-status").textContent = list.length ? "" : "No consults yet. Set your hours on the Settings tab and bookings will appear here.";
      var groups = [["Needs marking", list.filter(function (b) { return b.status === "booked" && Date.parse(b.start) < now; })],
        ["Coming up", list.filter(function (b) { return b.status === "booked" && Date.parse(b.start) >= now; })],
        ["Past 7 days", list.filter(function (b) { return b.status !== "booked"; }).reverse()]];
      groups.forEach(function (g) {
        if (!g[1].length) return;
        box.appendChild(el("h2", "", g[0]));
        g[1].forEach(function (b) {
          var d = new Date(b.start), card = el("div", "ib-bk");
          var head = el("div", "ib-bk-head");
          head.appendChild(el("strong", "", d.toLocaleDateString([], { weekday: "short", month: "short", day: "numeric" }) + ", " + d.toLocaleTimeString([], { hour: "numeric", minute: "2-digit" })));
          head.appendChild(el("span", "", b.name + " · " + pretty(b.phone)));
          card.appendChild(head);
          var tags = el("div", "ib-lead-row");
          tags.appendChild(el("span", "ib-tag", b.status === "booked" ? (b.confirmed ? "Confirmed" : "Not confirmed yet") : (STATUS[b.status] || (b.status === "cancelled" ? "Cancelled" : b.status))));
          if (b.optedOut) tags.appendChild(el("span", "ib-tag ib-badge-stop", "Replied STOP"));
          else if (!b.marketing) tags.appendChild(el("span", "ib-tag", "No marketing consent"));
          if (b.source && b.source !== "website") tags.appendChild(el("span", "ib-tag", "From: " + b.source));
          card.appendChild(tags);
          if (b.goal) card.appendChild(el("p", "ib-help", "Goal: " + b.goal));
          var acts = el("div", "ib-bk-acts");
          function act(label, set, cls) {
            var bt = el("button", cls || "ib-btn ib-btn-light", label); bt.type = "button";
            bt.addEventListener("click", function () {
              if (set === "cancel" && bt.getAttribute("data-sure") !== "1") { bt.setAttribute("data-sure", "1"); bt.textContent = "Tap again to cancel it"; return; }
              acts.querySelectorAll("button").forEach(function (x) { x.disabled = true; });
              api("POST", { action: "booking", id: b.id, set: set }).then(loadSchedule);
            });
            acts.appendChild(bt);
          }
          if (b.status === "booked" && Date.parse(b.start) < now + 3600 * 1000) { act("Showed", "showed", "ib-btn"); act("No-show", "no_show"); }
          if (b.status === "booked" && Date.parse(b.start) >= now) act("Cancel consult", "cancel");
          var txt = el("button", "ib-link", "Open texts"); txt.type = "button";
          txt.addEventListener("click", function () { setTab("texts"); openThread(b.phone); });
          acts.appendChild(txt);
          var call = el("a", "ib-link", "Call"); call.href = "tel:" + b.phone; acts.appendChild(call);
          card.appendChild(acts); box.appendChild(card);
        });
      });
    });
  }

  /* ----- Week tab: client sessions + consults ----- */
  var weekOf = null, weekData = null;
  function addDays(key, n) { var d = new Date(key + "T12:00:00Z"); d.setUTCDate(d.getUTCDate() + n); return d.toISOString().slice(0, 10); }
  function dayLabel(key, long) { return new Date(key + "T12:00:00Z").toLocaleDateString([], long ? { timeZone: "UTC", weekday: "long", month: "short", day: "numeric" } : { timeZone: "UTC", month: "short", day: "numeric" }); }
  var pacKey = new Intl.DateTimeFormat("en-CA", { timeZone: "America/Los_Angeles", year: "numeric", month: "2-digit", day: "2-digit" });
  var pacTime = new Intl.DateTimeFormat("en-US", { timeZone: "America/Los_Angeles", hour: "numeric", minute: "2-digit" });
  function loadWeek() {
    var q = { view: "week" }; if (weekOf) q.start = weekOf;
    return api("GET", q).then(function (r) {
      if (!handle(r)) return;
      show("week"); weekData = r.j; weekOf = r.j.weekStart;
      $("ib-wk-label").textContent = dayLabel(weekOf) + " to " + dayLabel(addDays(weekOf, 6));
      var cs = $("ib-ses-client"); cs.textContent = "";
      if (!r.j.clients.length) { var o0 = el("option", "", "Add clients on the Clients tab first"); o0.value = ""; cs.appendChild(o0); }
      r.j.clients.forEach(function (c) { var o = el("option", "", c.name); o.value = c.phone; cs.appendChild(o); });
      var ds = $("ib-ses-day"), keep = ds.value; ds.textContent = "";
      for (var i = 0; i < 7; i++) { var k = addDays(weekOf, i), od = el("option", "", dayLabel(k, true)); od.value = k; if (k === keep) od.selected = true; ds.appendChild(od); }
      var hs = $("ib-ses-hour"); if (!hs.options.length) for (var h = 4; h <= 21; h++) { var oh = el("option", "", hourLabel(h)); oh.value = h; hs.appendChild(oh); }
      var box = $("ib-wk-days"); box.textContent = "";
      var items = r.j.sessions.map(function (s) { return { kind: "session", id: s.id, name: s.name, phone: s.phone, start: s.start, fixed: s.fixed, by: s.by }; })
        .concat(r.j.consults.map(function (c) { return { kind: "consult", name: c.name, phone: c.phone, start: c.start, confirmed: c.confirmed, status: c.status }; }));
      for (var d = 0; d < 7; d++) {
        var key = addDays(weekOf, d), todays = items.filter(function (x) { return pacKey.format(new Date(x.start)) === key; }).sort(function (a, b) { return Date.parse(a.start) - Date.parse(b.start); });
        box.appendChild(el("h2", "", dayLabel(key, true)));
        if (!todays.length) { box.appendChild(el("p", "ib-help", "Nothing booked.")); continue; }
        todays.forEach(function (x) {
          var row = el("div", "ib-wk-row" + (x.kind === "consult" ? " is-consult" : ""));
          row.appendChild(el("strong", "", pacTime.format(new Date(x.start))));
          row.appendChild(el("span", "ib-wk-name", (x.kind === "consult" ? "Consult (90 min): " : "") + x.name));
          if (x.kind === "session" && x.fixed) row.appendChild(el("span", "ib-tag", "Fixed weekly"));
          if (x.kind === "session" && x.by === "assistant") row.appendChild(el("span", "ib-tag", "Booked by assistant"));
          if (x.kind === "consult") row.appendChild(el("span", "ib-tag", x.status === "booked" ? (x.confirmed ? "Confirmed" : "Not confirmed yet") : (STATUS[x.status] || x.status)));
          else {
            var rm = el("button", "ib-link", "Remove"); rm.type = "button";
            rm.addEventListener("click", function () { rm.disabled = true; api("POST", { action: "session_remove", id: x.id }).then(loadWeek); });
            row.appendChild(rm);
            // Inside 24 hours (or already past) for a client whose sessions are counted: Dan can take it off and still count it.
            var cl = (r.j.clients || []).filter(function (c) { return c.phone === x.phone; })[0];
            if (cl && typeof cl.credits === "number" && !x.counted && Date.parse(x.start) - Date.now() < 24 * 3600 * 1000) {
              var lc = el("button", "ib-link", "Late cancel / no-show (counts)"); lc.type = "button";
              lc.addEventListener("click", function () { lc.disabled = true; api("POST", { action: "session_remove", id: x.id, charge: true }).then(loadWeek); });
              row.appendChild(lc);
            }
          }
          box.appendChild(row);
        });
      }
    });
  }
  $("ib-wk-prev").addEventListener("click", function () { weekOf = addDays(weekOf, -7); loadWeek(); });
  $("ib-wk-next").addEventListener("click", function () { weekOf = addDays(weekOf, 7); loadWeek(); });
  $("ib-ses-form").addEventListener("submit", function (e) {
    e.preventDefault();
    var st = $("ib-wk-status"), phone = $("ib-ses-client").value; st.className = "ib-status"; st.textContent = "";
    if (!phone) { st.className = "ib-status err"; st.textContent = "Add the client on the Clients tab first."; return; }
    api("POST", { action: "session", phone: phone, date: $("ib-ses-day").value, hour: +$("ib-ses-hour").value }).then(function (r) {
      if (!handle(r)) return;
      if (r.j.ok) loadWeek();
      else { st.className = "ib-status err"; st.textContent = r.j.error === "taken" ? "That hour already has a session or a consult on it." : "Couldn't add that. Check the day and time."; }
    });
  });
  $("ib-wk-copy").addEventListener("click", function () {
    var st = $("ib-wk-status"); st.className = "ib-status"; st.textContent = "Copying…";
    api("POST", { action: "copy_week", from: addDays(weekOf, -7), to: weekOf }).then(function (r) {
      if (!handle(r)) return;
      loadWeek().then(function () { st.textContent = "Added " + r.j.added + " session" + (r.j.added === 1 ? "" : "s") + (r.j.skipped ? ". Skipped " + r.j.skipped + " (hour taken, already past, or client removed)." : "."); });
    });
  });

  /* ----- Clients tab ----- */
  function loadClients() {
    api("GET", { view: "week" }).then(function (r) { if (!handle(r)) return; show("clients"); monthCount = r.j.month || {}; hasReviewLink = !!r.j.reviewLink; renderClients(r.j.clients, r.j.texting); });
  }
  var monthCount = {}, hasReviewLink = false;
  function renderClients(list, texting) {
    var box = $("ib-cl-list"); box.textContent = "";
    if (!list.length) box.appendChild(el("p", "ib-help", "No clients yet."));
    list.forEach(function (c) {
      var row = el("div", "ib-wk-row");
      row.appendChild(el("strong", "", c.name)); row.appendChild(el("span", "ib-wk-name", pretty(c.phone) + (c.note ? " · " + c.note : "")));
      var t = el("button", "ib-link", "Text"); t.type = "button"; t.addEventListener("click", function () { setTab("texts"); openThread(c.phone); }); row.appendChild(t);
      var call = el("a", "ib-link", "Call"); call.href = "tel:" + c.phone; row.appendChild(call);
      var rm = el("button", "ib-link", "Remove"); rm.type = "button";
      rm.addEventListener("click", function () {
        if (rm.getAttribute("data-sure") !== "1") { rm.setAttribute("data-sure", "1"); rm.textContent = "Tap again to remove"; return; }
        api("POST", { action: "client", phone: c.phone, remove: true }).then(function (r) { if (r.j.ok) renderClients(r.j.clients, texting); });
      });
      row.appendChild(rm); box.appendChild(row);
      // Fixed weekly times: these go on the calendar by themselves, three weeks ahead.
      var fx = el("div", "ib-fixed"), fixed = (c.fixed || []).slice();
      function saveFixed(next) { api("POST", { action: "client", phone: c.phone, name: c.name, note: c.note || "", fixed: next }).then(function (r) { if (r.j.ok) renderClients(r.j.clients, texting); }); }
      fx.appendChild(el("span", "ib-fixed-label", fixed.length ? "Fixed every week:" : "No fixed weekly time."));
      fixed.forEach(function (f, i) {
        var chip = el("button", "ib-tag ib-chip", DAYNAME[f.dow] + " " + hourLabel(f.hour) + "  \u00d7"); chip.type = "button";
        chip.setAttribute("aria-label", "Remove fixed time " + DAYNAME[f.dow] + " " + hourLabel(f.hour));
        chip.addEventListener("click", function () { saveFixed(fixed.filter(function (_, k) { return k !== i; })); });
        fx.appendChild(chip);
      });
      var ds = el("select", "ib-select"); ds.setAttribute("aria-label", "Day for " + c.name);
      DAYS.forEach(function (d) { var o = el("option", "", d[1]); o.value = d[0]; ds.appendChild(o); });
      var hs = el("select", "ib-select"); hs.setAttribute("aria-label", "Time for " + c.name);
      for (var h = 4; h <= 21; h++) { var oh = el("option", "", hourLabel(h)); oh.value = h; hs.appendChild(oh); }
      var add = el("button", "ib-btn ib-btn-light", "Add fixed time"); add.type = "button";
      add.addEventListener("click", function () {
        if (fixed.some(function (f) { return f.dow === ds.value && f.hour === +hs.value; })) return;
        saveFixed(fixed.concat([{ dow: ds.value, hour: +hs.value }]));
      });
      fx.appendChild(ds); fx.appendChild(hs); fx.appendChild(add); box.appendChild(fx);
      // Session count: how many they have left, and a quick way to add a new pack when they pay.
      var cr = el("div", "ib-fixed"), counted = typeof c.credits === "number";
      function saveCount(extra) { var p = { action: "client", phone: c.phone, name: c.name, note: c.note || "", fixed: fixed }; for (var k in extra) p[k] = extra[k]; api("POST", p).then(function (r) { if (r.j.ok) renderClients(r.j.clients, texting); }); }
      cr.appendChild(el("span", "ib-fixed-label", (counted ? "Sessions left: " + c.credits + ". " : "Sessions not counted. ") + "This month: " + (monthCount[c.phone] || 0) + " on the schedule."));
      var num = el("input"); num.type = "number"; num.min = 1; num.max = 100; num.value = 12; num.className = "ib-num"; num.setAttribute("aria-label", "Sessions to add for " + c.name);
      var addP = el("button", "ib-btn ib-btn-light", counted ? "Add sessions" : "Start counting"); addP.type = "button";
      addP.addEventListener("click", function () { var n = Math.round(+num.value); if (n > 0) saveCount(counted ? { add: n } : { credits: n }); });
      cr.appendChild(num); cr.appendChild(addP);
      if (counted) { var stop = el("button", "ib-link", "Stop counting"); stop.type = "button"; stop.addEventListener("click", function () { saveCount({ credits: null }); }); cr.appendChild(stop); }
      if (hasReviewLink && texting) {
        var rv = el("button", "ib-link", c.reviewAsked ? "Review asked" : "Ask for a Google review"); rv.type = "button"; rv.disabled = !!c.reviewAsked;
        rv.addEventListener("click", function () {
          if (rv.getAttribute("data-sure") !== "1") { rv.setAttribute("data-sure", "1"); rv.textContent = "Tap again to send the review text"; return; }
          rv.disabled = true; api("POST", { action: "review", phone: c.phone }).then(function (r) { if (r.j.ok) renderClients(r.j.clients, texting); else rv.textContent = r.j.error === "opted_out" ? "They replied STOP" : "Could not send"; });
        });
        cr.appendChild(rv);
      }
      box.appendChild(cr);
    });
  }
  $("ib-cl-form").addEventListener("submit", function (e) {
    e.preventDefault(); var st = $("ib-cl-status"); st.className = "ib-status"; st.textContent = "";
    api("POST", { action: "client", name: $("ib-cl-name").value, phone: $("ib-cl-phone").value, note: $("ib-cl-note").value }).then(function (r) {
      if (!handle(r)) return;
      if (r.j.ok) { e.target.reset(); renderClients(r.j.clients); $("ib-cl-name").focus(); }
      else { st.className = "ib-status err"; st.textContent = r.j.error === "phone" ? "Check the mobile number (10 digits)." : "Enter the client's name."; }
    });
  });

  /* ----- Settings tab ----- */
  $("ib-try-go").addEventListener("click", function () {
    var out = $("ib-try-out"), bt = $("ib-try-go"); if (!$("ib-try-who").value || !$("ib-try-text").value.trim()) { out.textContent = "Pick a client and type a text first."; return; }
    bt.disabled = true; out.textContent = "Thinking...";
    api("POST", { action: "assistant_try", phone: $("ib-try-who").value, text: $("ib-try-text").value }).then(function (r) {
      bt.disabled = false;
      if (r.j && r.j.ok) out.textContent = "It would reply: \u201c" + r.j.reply + "\u201d" + (r.j.did.length ? "  It would have: " + r.j.did.join(", ") + "." : "  No schedule change.") + (r.j.handoff ? "  Passed to you: " + r.j.handoff + "." : "");
      else out.textContent = r.j && r.j.error === "not_configured" ? "The AI key is not connected yet." : "The assistant could not answer (" + ((r.j && r.j.error) || "error") + ").";
    });
  });
  var DAYNAME = { mon: "Mon", tue: "Tue", wed: "Wed", thu: "Thu", fri: "Fri", sat: "Sat", sun: "Sun" };
  var DAYS = [["mon", "Monday"], ["tue", "Tuesday"], ["wed", "Wednesday"], ["thu", "Thursday"], ["fri", "Friday"], ["sat", "Saturday"], ["sun", "Sunday"]];
  var settings = null;
  function hourLabel(h) { return (h % 12 || 12) + ":00 " + (h < 12 ? "AM" : "PM"); }
  function hourSelect(val, from, to, withClosed) {
    var s = el("select", "ib-select");
    if (withClosed) { var c = el("option", "", "Closed"); c.value = ""; s.appendChild(c); }
    for (var h = from; h <= to; h++) { var o = el("option", "", hourLabel(h)); o.value = String(h).padStart(2, "0") + ":00"; if (o.value === val) o.selected = true; s.appendChild(o); }
    return s;
  }
  function renderBlocked() {
    var ul = $("ib-blocked"); ul.textContent = "";
    settings.blocked.slice().sort().forEach(function (d) {
      var li = el("li"), bt = el("button", "ib-link", "Remove"); bt.type = "button";
      li.appendChild(el("span", "", new Date(d + "T12:00:00").toLocaleDateString([], { weekday: "short", month: "short", day: "numeric", year: "numeric" }) + " "));
      bt.addEventListener("click", function () { settings.blocked = settings.blocked.filter(function (x) { return x !== d; }); renderBlocked(); });
      li.appendChild(bt); ul.appendChild(li);
    });
  }
  function loadSettings() {
    api("GET", { view: "settings" }).then(function (r) {
      if (!handle(r)) return;
      show("settings"); settings = r.j.settings; $("ib-feed").value = r.j.feed ? r.j.feed + "&only=training" : ""; $("ib-feed-consults").value = r.j.feed ? r.j.feed + "&only=consults" : "";
      var hours = $("ib-hours"); hours.textContent = "";
      DAYS.forEach(function (d) {
        var h = settings.hours[d[0]], row = el("div", "ib-hours-row"); row.setAttribute("data-day", d[0]);
        row.appendChild(el("span", "ib-hours-day", d[1]));
        var from = hourSelect(h ? h.from : "", 5, 20, true), to = hourSelect(h ? h.to : "18:00", 6, 21, false);
        from.setAttribute("aria-label", d[1] + " first consult starts"); to.setAttribute("aria-label", d[1] + " last consult ends");
        row.appendChild(from); row.appendChild(el("span", "", "to")); row.appendChild(to); hours.appendChild(row);
      });
      $("ib-notice").value = settings.noticeHours; $("ib-ahead").value = settings.daysAhead;
      renderBlocked();
      var f = $("ib-follow"); f.textContent = "";
      settings.followups.forEach(function (x, i) {
        var wrap = el("div", "ib-follow-row"), lab = el("label", "", "Text " + (i + 1) + ": days after the consult"), n = el("input"); n.type = "number"; n.min = "1"; n.max = "120"; n.value = x.day; n.className = "ib-follow-day";
        lab.appendChild(n); wrap.appendChild(lab);
        var ta = el("textarea"); ta.rows = 3; ta.maxLength = 600; ta.value = x.text; ta.className = "ib-follow-text"; ta.setAttribute("aria-label", "Follow-up text " + (i + 1));
        wrap.appendChild(ta); f.appendChild(wrap);
      });
      $("ib-noshow").value = settings.noShowText;
      api("GET", { view: "week" }).then(function (w) {
        var sel = $("ib-try-who"); sel.textContent = "";
        ((w.j && w.j.clients) || []).forEach(function (c) { var o = el("option", "", c.name); o.value = c.phone; sel.appendChild(o); });
        if (!sel.options.length) { var o = el("option", "", "Add a client on the Clients tab first"); o.value = ""; sel.appendChild(o); }
      });
      $("ib-mc-on").checked = settings.missedCall.on; $("ib-mc-ring").checked = settings.missedCall.ring; $("ib-mc-text").value = settings.missedCall.text;
      $("ib-rem-on").checked = settings.sessionReminders;
      $("ib-rv-link").value = settings.review.link; $("ib-rv-text").value = settings.review.text;
      $("ib-ai-on").checked = !!(settings.ai && settings.ai.on);
      $("ib-ai-weekly").checked = !!(settings.ai && settings.ai.weeklyAsk);
      $("ib-ai-facts").value = (settings.ai && settings.ai.facts) || "";
      $("ib-ai-need").hidden = !!r.j.assistant;
    });
  }
  $("ib-block-add").addEventListener("click", function () {
    var v = $("ib-block-date").value; if (!v || !settings) return;
    if (settings.blocked.indexOf(v) < 0) settings.blocked.push(v); $("ib-block-date").value = ""; renderBlocked();
  });
  $("ib-set-form").addEventListener("submit", function (e) {
    e.preventDefault(); if (!settings) return;
    var st = $("ib-set-status"), bad = null;
    document.querySelectorAll(".ib-hours-row").forEach(function (row) {
      var s = row.querySelectorAll("select"), d = row.getAttribute("data-day");
      if (!s[0].value) settings.hours[d] = null;
      else if (s[0].value >= s[1].value) bad = d;
      else settings.hours[d] = { from: s[0].value, to: s[1].value };
    });
    if (bad) { st.className = "ib-status err"; st.textContent = "Check the hours: the end time has to be after the start time."; return; }
    settings.noticeHours = +$("ib-notice").value; settings.daysAhead = +$("ib-ahead").value;
    settings.followups = [].map.call(document.querySelectorAll(".ib-follow-row"), function (w) { return { day: +w.querySelector(".ib-follow-day").value, text: w.querySelector(".ib-follow-text").value }; });
    settings.noShowText = $("ib-noshow").value;
    settings.missedCall = { on: $("ib-mc-on").checked, ring: $("ib-mc-ring").checked, text: $("ib-mc-text").value };
    settings.sessionReminders = $("ib-rem-on").checked;
    settings.review = { link: $("ib-rv-link").value, text: $("ib-rv-text").value };
    settings.ai = { on: $("ib-ai-on").checked, weeklyAsk: $("ib-ai-weekly").checked, facts: $("ib-ai-facts").value };
    var btn = e.target.querySelector('button[type="submit"]'); btn.disabled = true; st.className = "ib-status"; st.textContent = "Saving…";
    api("POST", { action: "settings", settings: settings }).then(function (r) {
      btn.disabled = false;
      if (!handle(r)) return;
      if (r.j.ok) { st.textContent = "Saved. The website is using these now."; loadSettings(); }
      else { st.className = "ib-status err"; st.textContent = "Couldn't save. Try again."; }
    });
  });

  /* ----- sign in / out ----- */
  login.addEventListener("submit", function (e) {
    e.preventDefault();
    var st = $("ib-login-status"), btn = login.querySelector("button");
    btn.disabled = true; st.className = "ib-status"; st.textContent = "";
    api("POST", { action: "login", password: $("ib-pw").value }).then(function (r) {
      btn.disabled = false; $("ib-pw").value = "";
      if (r.status === 200) { signedIn = true; return setTab("texts"); }
      if (r.status === 503) return handle(r);
      st.className = "ib-status err"; st.textContent = r.status === 429 ? "Too many tries. Wait 10 minutes and try again." : "That password isn't right.";
    });
  });
  logout.addEventListener("click", function () { api("POST", { action: "logout" }).then(function () { current = null; lastSig = ""; show("login"); }); });

  function start() {
    loadList().then(function () {
      if (signedIn && !setup.hidden) { tabs.hidden = false; logout.hidden = false; }
      if (app.hidden || timer) return;
      timer = setInterval(function () {            // check for new texts every 20 seconds while the page is open
        if (document.visibilityState !== "visible") return;
        if (tab !== "texts") return;
        loadList(true); if (current) openThread(current, true);
      }, 20000);
    });
  }
  start();
})();
