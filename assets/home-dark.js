/*  Fig Performance — homepage (dark) behaviour.
 *  Hides the sticky mobile CTA whenever the real booking picker or the final
 *  call to action is on screen, so the bar never covers the thing it points at.
 *  No dependencies. Fails silently.
 */
(function () {
  "use strict";
  var bar = document.querySelector(".sticky");
  if (!bar) return;

  document.body.classList.add("has-stickycta");

  var watch = [document.getElementById("consult"), document.getElementById("final-cta")]
    .filter(Boolean);
  if (!watch.length || !("IntersectionObserver" in window)) return;

  var showing = {};
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { showing[e.target.id] = e.isIntersecting; });
    var any = Object.keys(showing).some(function (k) { return showing[k]; });
    bar.setAttribute("data-hidden", any ? "true" : "false");
  }, { threshold: 0.12 });

  watch.forEach(function (el) { io.observe(el); });
})();
