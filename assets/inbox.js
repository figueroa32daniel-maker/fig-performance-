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
  function show(which) {
    login.hidden = which !== "login"; setup.hidden = which !== "setup"; app.hidden = which !== "app";
    logout.hidden = which !== "app";
    if (which !== "app") { clearInterval(timer); timer = null; }
  }
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
      $("ib-setup-msg").textContent = r.j.need === "INBOX_PASSWORD"
        ? "The inbox password hasn't been added in Vercel yet (INBOX_PASSWORD, at least 12 characters)."
        : "The texting account (Twilio) hasn't been connected in Vercel yet. Once its three keys are added, your conversations show up here.";
      show("setup"); return false;
    }
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
      $("ib-compose").hidden = false;
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
      else { st.className = "ib-status err"; st.textContent = "That text didn't send. Check the number and try again."; }
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

  $("ib-connect").addEventListener("click", function () {
    var st = $("ib-connect-status"); st.className = "ib-status"; st.textContent = "Connecting…";
    api("POST", { action: "connect" }).then(function (r) {
      if (!handle(r)) return;
      if (r.j.ok) st.textContent = r.j.already ? "Already connected." : "Connected. Reminders now follow your calendar.";
      else { st.className = "ib-status err"; st.textContent = r.j.error || "Couldn't connect."; }
    });
  });

  /* ----- sign in / out ----- */
  login.addEventListener("submit", function (e) {
    e.preventDefault();
    var st = $("ib-login-status"), btn = login.querySelector("button");
    btn.disabled = true; st.className = "ib-status"; st.textContent = "";
    api("POST", { action: "login", password: $("ib-pw").value }).then(function (r) {
      btn.disabled = false; $("ib-pw").value = "";
      if (r.status === 200) return start();
      if (r.status === 503) return handle(r);
      st.className = "ib-status err"; st.textContent = r.status === 429 ? "Too many tries. Wait 10 minutes and try again." : "That password isn't right.";
    });
  });
  logout.addEventListener("click", function () { api("POST", { action: "logout" }).then(function () { current = null; lastSig = ""; show("login"); }); });

  function start() {
    loadList().then(function () {
      if (app.hidden || timer) return;
      timer = setInterval(function () {            // check for new texts every 20 seconds while the page is open
        if (document.visibilityState !== "visible") return;
        loadList(true); if (current) openThread(current, true);
      }, 20000);
    });
  }
  start();
})();
