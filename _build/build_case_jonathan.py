"""Case study: Jonathan, 43. Modelled on trainwithdaveoc.com/case-studies/<name>.

EVERY fact on this page comes from MEMORY.md "Clients Dan has OK'd naming",
Jonathan entry, back story approved by Dan Nov 7 2026:
  ex-Army, new son, back pain and shoulder pain; was stiff/achy, pain bending
  over and touching his toes, had quit golf; pull-ups 1 -> 5; chin-ups +35 lb;
  Jefferson curl 135 lb; bench 185 lb; golfs again.
Dan's rule (MEMORY.md): don't mention where he lives.
No timeline is stated anywhere on this page because Dan has not given one.
No quotes, because Dan has not given Jonathan's own words. Written in the
Fig Performance voice ("we"), third person about Jonathan.
PHOTO SLOT is left empty on purpose. See the comment in the body.
"""
import sys
from pathlib import Path
from build_pages import page, SITE, CTA, stats
from build_case_studies import review

SLUG = "case-studies/jonathan"

body = """<p class="legal-intro">Jonathan came to Fig Performance at 43 with a back that had been stiff and achy for years, a shoulder that hurt, and a new son at home. He had stopped playing golf altogether. He plays again now.</p>

<h2 id="results">The numbers</h2>
""" + stats([("1 to 5", "pull-ups"), ("135 lb", "Jefferson curl"), ("185 lb", "bench press")]) + """
<p>He also adds 35 pounds to his body weight on chin-ups. None of those are the number he cares about. The one he cares about is that he golfs again.</p>

<!-- PHOTO SLOT: Jonathan's before/after goes here once Dan says which photo is his
     and confirms Jonathan agreed to it being captioned with his name.
     The 24 photos already in the homepage gallery run with no names or captions
     (Dan's decision, Nov 13 2026). A named case study page is a different ask. -->

<h2 id="start">Where he started</h2>
<p>Bending over hurt. Touching his toes hurt. His back was stiff and achy in the way that stops being an event and starts being a fact about your life, the thing you work around without really noticing you are working around it.</p>
<p>He had a shoulder problem on top of it, and a baby at home, which means lifting and lowering a small person several dozen times a day whether your back feels like cooperating or not.</p>
<p>Jonathan is ex-Army. Effort was never his problem. He knew how to train hard and he had done it for years. That is worth saying plainly, because the usual advice aimed at a man with a sore back is some version of try harder, and he had already tried harder. It had not worked, and it was never going to.</p>
<p>At some point he had quit golf. Not cut back to nine holes. Quit.</p>

<h2 id="changed">What we changed</h2>
<p>We did not start by trying to make the pain stop. We started by finding out what his back could still do, and then loading it on purpose.</p>
<p>That included loaded spinal flexion, which is the exact opposite of the advice most people with a cranky back have been handed. Body weight first, a short range if that is all there is, then weight added slowly over months. <a href="/jefferson-curls">Coach Dan's full case for it is here</a>, including who he holds back from it.</p>
<p>The shoulder got the same treatment. Not rest and avoidance, but strength built in the positions that were failing.</p>

<h2 id="now">Where he is now</h2>
<p>One pull-up became five. He hangs 35 pounds off his waist and does chin-ups with it. He benches 185.</p>
<p>And he Jefferson curls 135 pounds, which means a man who could not comfortably bend over to pick something up now rolls his spine down under more than his own body weight and back up again, deliberately, as training.</p>
<p>The golf came back on its own once the back could handle it. Nobody had to program that part.</p>

<h2 id="why">Why this one worked</h2>
<p>Because the problem was never that Jonathan needed to move less. It was that the ranges his back was failing in had not been trained in years, and no amount of avoiding them was going to change that.</p>
<p>That is most of what we do here. Adults over 40 arrive having spent a decade carefully not doing the things that hurt, which is reasonable and which slowly makes the list of things that hurt longer. The way out is usually the direction nobody wants to go.</p>
""" + review(0) + """<h2 id="more">Other client stories</h2>
<ul><li><a href="/case-studies/rosa">Rosa, 43</a>: 205 to 169 lb in 11 months</li><li><a href="/case-studies/ray">Ray, 64</a>: 218 to 183 lb in 10 months</li><li><a href="/case-studies/greg">Greg, 55</a>: 232 to 205 lb in 8 months</li></ul>
<p><a href="/case-studies">All the case studies</a>, or <a href="/personal-training-placentia">how one-on-one training works</a>.</p>

""" + CTA

faqs = [
    ("Can strength training help an achy back?",
     "Often, yes. Backs that are stiff and sore usually belong to people who have been avoiding the movements that hurt, which keeps those positions weak. Loading them gradually tends to help. An injured back is different: see your doctor or physical therapist first."),
    ("Do I need to be fit before I start at Fig Performance?",
     "No. Every program starts from an InBody scan and a movement assessment at the free consultation, and the first weights are chosen from what you can do that day."),
    ("Is training here one on one?",
     "Yes. Fig Performance is a private studio and sessions are one on one with a coach, with semi-private available in groups of three at most."),
    ("How do I start?",
     "Book the free consultation. It includes an InBody scan, a movement assessment and a recommended program, and there is no obligation after it."),
]

html = page(
    SLUG,
    "Jonathan, 43: One Pull-Up to Five, Golf Again | Fig Performance",
    "Jonathan came to Fig Performance at 43 with a stiff, achy back, a sore shoulder and no golf. Pull-ups 1 to 5, a 135 lb Jefferson curl, and back on the course.",
    "Jonathan, 43: One Pull-Up to Five, and Golf Again",
    "Case study",
    "A sore back, a new baby, and no golf. Then five pull-ups.",
    "Jonathan was 43, stiff and achy, and had quit the sport he loved. Here is what changed.",
    [("results", "The numbers"), ("start", "Where he started"), ("changed", "What we changed"),
     ("now", "Where he is now"), ("why", "Why it worked"), ("reviews", "A client review"), ("more", "Other stories")],
    body, faqs, "Jonathan's case study")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    open(out, "w").write(html)
    print("wrote", out, len(html))
