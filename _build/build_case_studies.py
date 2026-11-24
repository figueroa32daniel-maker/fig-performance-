"""Case study pages for the eight clients in Dan's Nov 24 2026 document.

Copy supplied by Dan. Numbers, names, ages, timelines and stories are his,
used verbatim in substance. Written in the Fig Performance voice ("we"),
third person, because no client quotes were supplied.

NO PHOTOGRAPHS on these pages. Each carries a PHOTO SLOT comment instead.
See the MEMORY.md log entry for Nov 24 2026.
"""
import sys
from pathlib import Path
from build_pages import page, SITE, CTA, stats

C = [
 dict(slug="ray", name="Ray", age=64, start=218, end=183, months=10, mode="studio",
   h1="Sixty-four, and carrying his own bags of soil again.",
   lede="Ray had not lifted in years and had started asking for help with things he used to handle himself. Thirty-five pounds later, he does not ask.",
   before="Ray walked most mornings and did yard work on the weekends. He had not lifted in years. The change that bothered him was not on the scale: he had started asking for help carrying things he used to pick up without thinking about it.",
   tried="He took longer walks. He ate smaller dinners. Both are reasonable and neither one made him stronger, which was the thing he actually wanted.",
   changed="He started lifting twice a week and kept his morning walks exactly as they were. Nothing was taken away from him.",
   moment="Carrying two bags of soil from the car to the backyard, and not setting them down halfway."),
 dict(slug="matt", name="Matt", age=39, start=212, end=184, months=7, mode="studio",
   h1="A missed Tuesday stopped turning into a missed week.",
   lede="Matt had lifted in his twenties. Then came work, and kids, and workouts whenever he could find one. Twenty-eight pounds in seven months.",
   before="Matt had lifted in his twenties and knew what he was doing. Between work and getting his kids where they needed to be, training had become something he squeezed in when a gap appeared, which is another way of saying it had become optional.",
   tried="He tried a thirty-day challenge. He tried strict meal prep. Both worked exactly as long as his schedule held still, which was never very long.",
   changed="He picked two studio sessions he could usually make, and kept a shorter workout for the weeks that fell apart. Friday pizza stayed where it was.",
   moment="Noticing that a missed Tuesday no longer turned into a missed week."),
 dict(slug="linda", name="Linda", age=57, start=149, end=143, months=6, mode="studio",
   h1="She stopped walking past the heavier dumbbells.",
   lede="Linda never missed a class. She had also been reaching for the same dumbbells for years. Six months later she presses the ones she used to walk past.",
   before="Linda walked with friends and went to group fitness classes regularly. She rarely missed one. The problem was not attendance. For years she had been picking up the same pair of dumbbells, and nothing about her week told her whether that was changing.",
   tried="She added another class and ate a little less. That gave her a busier week. It did not tell her whether she was getting stronger.",
   changed="She kept everything she enjoyed and added one thing: a few lifts, tracked, at the studio, so there was a number to look at.",
   moment="Pressing a pair of dumbbells she used to walk right past on her way to the rack."),
 dict(slug="eric", name="Eric", age=52, start=181, end=176, months=8, mode="online",
   h1="A plan that survived the work trips.",
   lede="Eric ran, lifted when he could, and lost the thread every time he travelled. Online coaching gave him something that held together between airports.",
   before="Eric ran several days a week and lifted when it fit. He wanted a stronger upper body and he wanted to feel better on weekend hikes.",
   tried="He added sets. He swapped exercises based on videos. He followed a six-day lifting split. Every one of them worked until a work trip broke the rhythm, and then he was starting over.",
   changed="With online coaching he followed a shorter plan and logged the same key lifts week after week, so the plan stopped depending on a perfect month.",
   moment="Watching his rows and presses climb on the log, and knowing exactly where to pick up when he got home from a trip."),
 dict(slug="jenna", name="Jenna", age=34, start=172, end=154, months=6, mode="studio",
   h1="She walked straight to the weights.",
   lede="Jenna had a gym membership and a folder of saved workouts she never used. Eighteen pounds later she trains without rehearsing it first.",
   before="Jenna used her gym membership, but every visit looked the same. Treadmill, a few familiar machines, leave. She had workouts saved on her phone and never opened them.",
   tried="The barrier was not motivation. It was standing in a busy weight room trying to work out a lift she had never done while people waited for the equipment.",
   changed="At the studio she learned how to set a lift up, how to pick a starting weight, and how to tell when she was ready to add to it. That is a skill, and it travels.",
   moment="Her first solo gym day with the new routine, when she walked past the treadmill and straight to the weights."),
 dict(slug="natalie", name="Natalie", age=38, start=137, end=134, months=7, mode="online",
   h1="Three pounds on the scale, and a different shape.",
   lede="Natalie was already fit. What she wanted was definition, and cutting harder had always left her flat. The scale barely moved. Everything else did.",
   before="Natalie did Pilates, ran on the weekends and lifted now and then. She wanted more definition in her shoulders and legs.",
   tried="Every time she tried to get leaner she did the same two things: more cardio, smaller portions. It left her feeling flat in her workouts and it never gave her the shape she was after.",
   changed="With online coaching, lifting became a regular part of her week instead of an occasional one, and she tracked what she could actually do.",
   moment="The scale moved three pounds in seven months. Her shoulders and legs changed, and her training log showed she was lifting heavier than she ever had."),
 dict(slug="rosa", name="Rosa", age=43, start=205, end=169, months=11, mode="studio",
   h1="Thirty-six pounds, built around a shift schedule.",
   lede="Rosa worked long shifts and got home hungry with dinner undecided. She needed something that worked at 8:30 at night, not something that needed a quiet week.",
   before="Rosa worked long shifts and often got home hungry with no decision made about dinner. That is where most days came apart, and it was not a willpower problem.",
   tried="She cut carbs. She tried meal-replacement shakes. She did a boot camp. All of it was manageable right up until a shift ran late, which happened constantly.",
   changed="She found two studio times she could usually make, and picked a few dinners she could grab on the way home. The plan had to survive a bad night, so it was built for one.",
   moment="Replacing her work jeans, because the old ones kept sliding down."),
 dict(slug="chris", name="Chris", age=50, start=224, end=193, months=9, mode="online",
   h1="A routine that held up through another trip.",
   lede="Chris trained well at home and lost it every time he travelled. Thirty-one pounds once the plan stopped assuming he would be in one place.",
   before="Whenever Chris spent a few weeks at home, he got into a good routine. Then he would travel, client dinners would run late, and he never knew what the hotel gym was going to have in it.",
   tried="He skipped breakfast after the big dinners. He crammed extra cardio into the weekend to make up for the week. Both are attempts to pay off a debt rather than avoid one.",
   changed="With online coaching he kept a regular lifting plan at home and carried a shorter dumbbell workout for hotel days. He also picked a few reliable orders at the restaurants he ends up in often.",
   moment="Getting home from a trip and going straight back into his regular workouts, instead of spending a week climbing back in."),
]

FAQS = [
 ("Can I train with Fig Performance if I travel for work?",
  "Yes. Online coaching is built for it: a plan you follow at home plus a shorter version for hotel gyms, with a weekly video call. Several clients train this way."),
 ("Do I need to be fit before I start?",
  "No. Every program starts from an InBody scan and a movement assessment at the free consultation, and the first weights come from what you can do that day."),
 ("Is training one on one?",
  "Yes. Fig Performance is a private studio and sessions are one on one with a coach. Semi-private runs in groups of three at most."),
 ("How do I start?",
  "Book the free consultation. InBody scan, movement assessment and a recommended program, with no obligation afterwards."),
]

ALL = [("jonathan", "Jonathan, 43", "one pull-up to five, and golf again")] + [
    (x["slug"], f'{x["name"]}, {x["age"]}',
     f'{x["start"]} to {x["end"]} lb in {x["months"]} months') for x in C]


def related(slug, n=3):
    i = [x[0] for x in ALL].index(slug)
    picks = [ALL[(i + k) % len(ALL)] for k in range(1, n + 1)]
    items = "".join(
        f'<li><a href="/case-studies/{s}">{name}</a>: {head}</li>' for s, name, head in picks)
    return ('<h2 id="more">Other client stories</h2>\n<ul>' + items + '</ul>\n'
            '<p><a href="/case-studies">All nine case studies</a>, or '
            '<a href="/personal-training-placentia">how one-on-one training works</a>.</p>\n\n')


def build(c):
    lost = c["start"] - c["end"]
    where = ("Coached one on one at the studio in Placentia."
             if c["mode"] == "studio" else
             "Coached online, with a weekly one-to-one video call.")
    body = (
      f'<p class="legal-intro">{c["lede"]}</p>\n\n'
      f'<h2 id="results">The numbers</h2>\n'
      + stats([(f"{lost} lb", "lost"),
               (f"{c['start']} to {c['end']}", "pounds"),
               (f"{c['months']} months", "start to finish")])
      + f'\n<p>{where}</p>\n\n'
      '<!-- PHOTO SLOT: left empty on purpose. A before/after is only added here\n'
      '     once Dan pairs it deliberately and confirms this client agreed to be\n'
      '     named alongside it. The homepage gallery runs photos uncaptioned. -->\n\n'
      f'<h2 id="start">Where {c["name"]} started</h2>\n<p>{c["before"]}</p>\n'
      f'<p>{c["tried"]}</p>\n\n'
      f'<h2 id="changed">What changed</h2>\n<p>{c["changed"]}</p>\n\n'
      f'<h2 id="moment">The moment it showed up</h2>\n'
      '<p>We ask every client the same question eventually, because the answer is '
      'never the one on the scale. It is the first ordinary thing that gets easier '
      'without being planned.</p>\n'
      f'<p>For {c["name"]}: {c["moment"]}</p>\n\n'
      '<h2 id="why">Why it held</h2>\n'
      '<p>Nothing here was dramatic. No thirty-day push, no plan that needed a '
      'quiet month to survive. A program you can run on a bad week beats a better '
      'program you abandon in March, and that is most of the difference between '
      f'the {c["months"]} months that worked and the years before them that did not.</p>\n\n'
      + related(c["slug"])
      + CTA)
    toc = [("results", "The numbers"), ("start", "Where it started"),
           ("changed", "What changed"), ("moment", "The moment"), ("why", "Why it held"), ("more", "Other stories")]
    return page(
      f"case-studies/{c['slug']}",
      f"{c['name']}, {c['age']}: {c['start']} to {c['end']} lb | Fig Performance",
      f"{c['name']}, {c['age']}, went from {c['start']} to {c['end']} lb in {c['months']} months with Fig Performance. {c['lede'][:70].rsplit(' ',1)[0]}...",
      f"{c['name']}, {c['age']}: {c['start']} to {c['end']} lb in {c['months']} Months",
      "Case study", c["h1"],
      f"{c['name']}, {c['age']}. {c['start']} to {c['end']} pounds in {c['months']} months. Here is how.",
      toc, body, FAQS, f"{c['name']}'s case study")

if __name__ == "__main__":
    for c in C:
        out = SITE / f"case-studies/{c['slug']}.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        h = build(c)
        out.write_text(h)
        print(f"wrote {out.name:14} {len(h):6} chars")
