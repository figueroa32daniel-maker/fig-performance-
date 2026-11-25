"""Reference page: plain definitions of the body composition and training terms used across the site.

Written so an AI answer engine can lift one self-contained definition without
needing the rest of the page. Every definition matches what the service pages
already say; nothing here claims a measurement or a result the site does not
already describe.
"""
from build_pages import page, SITE, CTA

SLUG = "body-composition-glossary"
MAYO = "https://www.mayoclinic.org/healthy-lifestyle/fitness/expert-answers/whole-body-vibration/faq-20057958"

TERMS = [
    ("body-composition", "Body composition",
     "Body composition is what your weight is actually made of: fat, muscle, bone and water. Two people at the same weight and height can have very different body compositions, which is why the bathroom scale on its own tells you so little. It is the number that matters most for how you look, how strong you are and how you move after 40."),

    ("body-fat-percentage", "Body fat percentage",
     "Body fat percentage is the share of your total weight that is fat. A man at 200 pounds and 25% body fat is carrying 50 pounds of fat and 150 pounds of everything else. Tracking the percentage alongside your weight is how you tell whether you are losing fat or losing muscle."),

    ("fat-mass", "Fat mass",
     "Fat mass is the weight of the fat on your body, in pounds, rather than as a percentage. It is the clearer number to watch while you are training, because percentages move when either fat or muscle changes. If your fat mass drops by 8 pounds while your weight only drops by 4, you built muscle at the same time."),

    ("skeletal-muscle-mass", "Skeletal muscle mass",
     "Skeletal muscle mass is the muscle you can train: the muscle attached to your bones that moves your body. It is the number strength training is meant to raise, and the one that quietly falls with age if nothing is done about it. An <a href=\"/inbody-scan-placentia\">InBody scan</a> reports it separately from your total lean mass, so you can see whether your training is working."),

    ("lean-mass-segment", "Lean mass by segment",
     "Segmental lean analysis breaks your lean mass down by body part: each arm, each leg and your trunk. It shows up imbalances that a single whole-body number hides, like one leg carrying noticeably less muscle than the other after an old injury. Coach Dan uses it to decide what to prioritize in your program."),

    ("visceral-fat", "Visceral fat",
     "Visceral fat is the deeper fat stored around your organs, rather than the fat you can pinch under your skin. An InBody scan reports it as a visceral fat level rather than in pounds. It responds well to the same things that drive the rest of fat loss, which is strength training, enough protein and daily walking."),

    ("body-water", "Body water",
     "Total body water is how much of your weight is fluid, inside and outside your cells. It is mostly useful as context: it explains why your weight can jump 2 or 3 pounds overnight after a salty meal or a hard session, with no change in fat at all. Knowing that saves a lot of worry about a single morning on the scale."),

    ("bmr", "Basal metabolic rate (BMR)",
     "Your basal metabolic rate is roughly the energy your body uses at complete rest, just keeping you alive. It is the floor your daily calorie needs are built on, before any movement or training is added. Because muscle is metabolically active, building muscle tends to raise it, which is one reason strength training matters more than cardio for long-term fat loss."),

    ("inbody-scan", "InBody scan",
     "An InBody scan is a body-composition test that takes about a minute. You stand on the device barefoot and hold the hand electrodes while it sends a small, painless electrical signal through your body and measures how that signal travels through muscle, fat and water. It reports your body fat percentage and fat mass, skeletal muscle mass, lean mass by segment, visceral fat level, body water and BMR. Full detail is on the <a href=\"/inbody-scan-placentia\">InBody scan page</a>."),

    ("body-recomposition", "Body recomposition",
     "Body recomposition is losing fat and building muscle at the same time, so your weight barely moves while your body changes shape. It is common in the first months of coached strength training, especially for people over 40 who have not lifted before. It is also the main reason the scale is a poor judge of progress and a scan is a good one. Coach Dan explains it in <a href=\"/how-to-lose-weight-after-40\">how to lose weight after 40</a>."),

    ("sarcopenia", "Sarcopenia",
     "Sarcopenia is the gradual loss of muscle mass and strength that comes with age. It starts earlier than most people expect and it is the reason a 55-year-old can weigh what they did at 35 and still feel weaker and softer. Resistance training and enough protein are the two things with the strongest evidence behind them for slowing it down."),

    ("progressive-overload", "Progressive overload",
     "Progressive overload means gradually asking your body to do slightly more than it is used to, by adding weight, reps, sets or better control. Without it, a program stops producing change however hard the sessions feel. It is the difference between training and just exercising."),

    ("one-on-one-training", "One-on-one personal training",
     "One-on-one personal training at Fig Performance means every session is private, with Coach Dan coaching only you. Sessions run 50 minutes, your program is built around your scan and anything that hurts, and nutrition coaching is included. It is $60 to $90 a session, billed weekly or monthly, with a 3-month minimum; where you land in that range depends on how often you train and whether you pay in full, and you get your exact rate at your free consult. See <a href=\"/pricing\">plans and pricing</a>."),

    ("semi-private-training", "Semi-private training",
     "Semi-private training is coached small-group strength training, by appointment, in groups of no more than three. You still train on your own program, with Coach Dan correcting form and loading the sessions, and <a href=\"/red-light-therapy-placentia\">red light therapy</a> and <a href=\"/vibration-therapy-placentia\">vibration therapy</a> are included. It starts at $180 a month."),

    ("red-light-therapy", "Red light therapy",
     "Red light therapy means sitting or standing in front of a panel that emits red and near-infrared light. At Fig Performance it is part of the recovery routine and is included with semi-private training. It is offered for general wellness and does not diagnose, treat, cure or prevent any disease. See our <a href=\"/disclaimer#recovery-tech\">health disclaimer</a>."),

    ("whole-body-vibration", "Whole body vibration",
     "Whole body vibration means standing or holding a position on a platform that vibrates quickly, which makes your muscles contract and relax many times a second. According to the <a href=\"%s\" target=\"_blank\" rel=\"noopener noreferrer\">Mayo Clinic</a>, some research suggests it may help muscle strength, balance in older adults and bone loss, though the research is limited. We use it for recovery, never as a replacement for training. More on the <a href=\"/vibration-therapy-placentia\">vibration therapy page</a>." % MAYO),
]

GROUPS = [
    ("scan", "What your InBody scan measures",
     "Every Fig Performance client starts with an <a href=\"/inbody-scan-placentia\">InBody scan</a>, and these are the numbers on the printout.",
     ["body-composition", "body-fat-percentage", "fat-mass", "skeletal-muscle-mass",
      "lean-mass-segment", "visceral-fat", "body-water", "bmr", "inbody-scan"]),
    ("training", "Training and progress",
     "The terms that come up when Coach Dan explains why the scale is not telling you the whole story.",
     ["body-recomposition", "sarcopenia", "progressive-overload"]),
    ("ways", "Ways to train with us",
     "Two offers, and what each one includes.",
     ["one-on-one-training", "semi-private-training"]),
    ("recovery", "Recovery",
     "Both are included with semi-private training, and both are offered for general wellness rather than as medical treatment.",
     ["red-light-therapy", "whole-body-vibration"]),
]

BY_ID = {t[0]: t for t in TERMS}

sections = []
for anchor, heading, blurb, ids in GROUPS:
    parts = [f'<h2 id="{anchor}">{heading}</h2>', f"<p>{blurb}</p>"]
    for tid in ids:
        _, name, definition = BY_ID[tid]
        parts.append(f'<h3 id="{tid}">{name}</h3>\n<p>{definition}</p>')
    sections.append("\n\n".join(parts))

body = (
    '<p class="legal-intro">These are the body composition and training terms we use with clients at '
    '<a href="/">Fig Performance in Placentia</a>, each one defined in plain language. If you have just had an '
    '<a href="/inbody-scan-placentia">InBody scan</a> and want to know what a number on the printout means, start '
    'with the first section. Everything here is general education for healthy adults, not medical advice.</p>\n\n'
    + "\n\n".join(sections)
    + '\n\n<h2 id="start">Where to start</h2>\n'
    '<p>If you are over 40 and cannot tell whether you are losing fat or losing muscle, the scan answers it in about '
    'a minute and the free consult costs nothing. You get your numbers, a movement assessment and a straight '
    'recommendation, and you decide from there. Our guide to '
    '<a href="/fitness-after-40">fitness after 40</a> covers the training side in more depth.</p>\n'
    + CTA
)

faqs = [
    ("What does skeletal muscle mass mean on an InBody scan?",
     "Skeletal muscle mass is the muscle attached to your bones, the muscle you train in the gym. It is reported separately from total lean mass, which also includes water and organ tissue. Raising it is the point of strength training, and it is the number that falls with age if you do nothing about it."),
    ("What is a visceral fat level?",
     "Visceral fat is the deeper fat stored around your organs rather than under your skin, and an InBody scan reports it as a level rather than in pounds. It comes down with the same approach that drives the rest of fat loss: strength training, enough protein and daily walking."),
    ("What is the difference between body fat percentage and fat mass?",
     "Fat mass is the weight of your fat in pounds. Body fat percentage is that weight as a share of your total weight. The percentage can move when either number changes, so looking at both tells you whether you lost fat, gained muscle or did both at once."),
    ("Can you lose fat and build muscle at the same time after 40?",
     "Yes, and it is common in the first months of coached strength training, especially if you have not lifted before. It is called body recomposition, and it is the reason your weight can sit still while your body clearly changes. A scan shows it; the scale does not."),
    ("Do I need an InBody scan to start training?",
     "No, but it is the fastest way to know where you stand, and it is free with your first consult at Fig Performance. Skip the scan if you have a pacemaker or another implanted electronic device, or if you are pregnant. You can still do the rest of the consult."),
]

TOC = [("scan", "What your scan measures"), ("training", "Training and progress"),
       ("ways", "Ways to train"), ("recovery", "Recovery"), ("start", "Where to start"),
       ("faq-title", "FAQ")]

html_out = page(SLUG,
    "Body Composition Terms Explained | Fig Performance",
    "Plain definitions of the body composition and InBody terms we use at Fig Performance in Placentia: visceral fat, skeletal muscle mass, BMR and more.",
    "Body Composition and Training Terms, Explained",
    "Reference", "Body Composition and Training Terms, Explained",
    "What every number on your InBody printout means, and the words we use for training, in plain language.",
    TOC, body, faqs, "Glossary", updated="2026-11-24")

# DefinedTermSet is the schema built for a glossary, and page() does not emit it.
import json, re
terms_ld = {
    "@context": "https://schema.org",
    "@type": "DefinedTermSet",
    "name": "Body Composition and Training Terms",
    "url": f"https://www.figperformance.com/{SLUG}",
    "hasDefinedTerm": [
        {"@type": "DefinedTerm", "name": name,
         "description": re.sub(r"<[^>]+>", "", definition),
         "url": f"https://www.figperformance.com/{SLUG}#{tid}"}
        for tid, name, definition in TERMS
    ],
}
marker = "</head>"
html_out = html_out.replace(
    marker,
    '  <script type="application/ld+json">%s</script>\n%s'
    % (json.dumps(terms_ld, ensure_ascii=False), marker), 1)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html_out)
    print("wrote", SLUG, len(html_out), "bytes,", len(TERMS), "terms")
