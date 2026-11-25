"""Index page listing every client case study. Linked from the homepage results section."""
import sys
from pathlib import Path
from build_pages import page, SITE, CTA

SLUG = "case-studies"

ROWS = [
 ("jonathan", "Jonathan, 43", "One pull-up to five, and golf again",
  "A stiff, achy back, a sore shoulder and a new baby. He had quit golf. He plays again."),
 ("rosa", "Rosa, 43", "205 to 169 lb in 11 months",
  "Long shifts, home hungry, dinner undecided. A plan built to survive a bad night."),
 ("ray", "Ray, 64", "218 to 183 lb in 10 months",
  "He had started asking for help carrying things. Thirty-five pounds later he does not."),
 ("chris", "Chris, 50", "224 to 193 lb in 9 months",
  "Good at home, lost on the road. A routine that held up through the next trip."),
 ("matt", "Matt, 39", "212 to 184 lb in 7 months",
  "Work, kids, and workouts whenever. A missed Tuesday stopped becoming a missed week."),
 ("jenna", "Jenna, 34", "172 to 154 lb in 6 months",
  "Treadmill, same machines, leave. Now she walks straight to the weights."),
 ("linda", "Linda, 57", "149 to 143 lb in 6 months",
  "She never missed a class. She had also used the same dumbbells for years."),
 ("eric", "Eric, 52", "181 to 176 lb in 8 months",
  "Every work trip reset the plan. Online coaching gave him one that did not."),
 ("natalie", "Natalie, 38", "137 to 134 lb in 7 months",
  "Three pounds on the scale, and the shape she had been cutting for."),
  ("greg", "Greg, 55", "232 to 205 lb in 8 months",
  "A regional sales leader whose weekday workouts vanished with every trip."),
 ("karen", "Karen, 53", "176 to 152 lb in 9 months",
  "Enterprise sales, always on the go. Strength training stopped waiting for next quarter."),
 ("marcus", "Marcus, 47", "218 to 196 lb in 7 months",
  "Cybersecurity IT manager. A late incident no longer wrecks the week."),
 ("alyssa", "Alyssa, 36", "167 to 149 lb in 6 months",
  "A CEO on flights and late dinners, with a plan for home and one for hotels."),
 ("diane", "Diane, 58", "148 to 139 lb in 7 months",
  "A chiropractor who now trains before her first patient."),
 ("lauren", "Lauren, 42", "151 to 144 lb in 5 months",
  "A CFO whose lifting used to disappear every month-end close."),
]

cards = "\n".join(
  f'<p><a href="/case-studies/{s}"><strong>{n}</strong>: {head}</a><br>{blurb}</p>'
  for s, n, head, blurb in ROWS)

body = (
 '<p class="legal-intro">Fifteen clients, their numbers, and what actually changed. '
 'Some trained one on one at the studio in Placentia. Some were coached online. '
 'Every one of them had tried something before this that did not hold.</p>\n\n'
 '<h2 id="stories">The stories</h2>\n' + cards + "\n\n"
 '<h2 id="common">What they have in common</h2>\n'
 '<p>Not much, on paper. A 34-year-old who avoided the weight room and a 64-year-old '
 'who had not lifted in years do not need the same program.</p>\n'
 '<p>What repeats is the shape of the thing that failed before. A plan that worked '
 'while the schedule held still. A challenge with an end date. More cardio and smaller '
 'portions, again. The fix is almost never more effort. It is a plan that survives a '
 'bad week, and someone keeping track so you can see it working before you can feel it.</p>\n'
 + CTA)

faqs = [
 ("What is included in one-on-one training?",
  "A program built from your InBody scan and movement assessment, nutrition coaching, sessions with a coach, and a weekly re-scan so progress is measured rather than guessed."),
 ("How long does it take to see a change?",
  "It depends on the starting point and the goal. In these stories the first everyday sign showed up well before the final number did, which is the part most people are surprised by."),
 ("Do you coach people outside Placentia?",
  "Yes. Online coaching includes a weekly one-to-one video call, a custom training plan and an 80/20 nutrition plan, and several of these clients trained that way."),
 ("How do I start?",
  "Book the free consultation: InBody scan, movement assessment and a recommended program, with no obligation afterwards."),
]

html = page(
  SLUG,
  "Client Case Studies | Fig Performance, Placentia CA",
  "Fifteen Fig Performance clients, their numbers and what changed. Fat loss, strength and training around pain, at the Placentia studio and online with Coach Dan.",
  "Client Case Studies | Fig Performance",
  "Results",
  "Fifteen clients. Their numbers, and what actually changed.",
  "Fat loss, strength, and training around pain. Studio and online.",
  [("stories", "The stories"), ("common", "What they share")],
  body, faqs, "Case studies")

if __name__ == "__main__":
    out = SITE / "case-studies/index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", out.name, len(html))
