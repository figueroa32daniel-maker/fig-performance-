"""DRAFT city page for Placentia itself, written overnight Nov 25 2026. NOT published.

Why it exists: there are seven "Personal Trainer in <City>, CA" pages for
neighbouring towns and none for Placentia, where the studio actually is. The
homepage carries that keyword and sits at position 21 for "personal trainer
placentia ca" (Search Console, last 3 months).

[DAN] Decide before publishing: this page and the homepage both target the same
query. A dedicated page usually wins it and frees the homepage for brand terms,
but it is a real change to the page that currently ranks. Your call.
"""
from build_pages import page, SITE, CTA
from build_cities import SHARED_TRAIN, SHARED_PRICE

SLUG = "personal-trainer-placentia"

body = f"""<p class="legal-intro">Fig Performance is a <a href="/what-is-private-personal-training">private, one-on-one</a> strength studio at 1284 E. Yorba Linda Blvd in Placentia. Not a gym floor you walk onto alone. A room where one coach trains one person at a time, built for adults over 40 who are already doing the work and want it to start showing.</p>

<h2 id="who">Who trains here</h2>
<p>Placentia is a town of people who have been busy for thirty years: business owners, teachers, nurses, people in the trades, parents whose kids have left and who suddenly have an hour back. The ones who come to us usually arrive with some version of the same sentence. <em>I used to be in shape. I still move. Nothing is changing.</em></p>
<ul>
  <li><strong>You want to know what is actually happening.</strong> An InBody scan separates fat from muscle, so the last six months stop being a guess.</li>
  <li><strong>You want to be strong, not just lighter.</strong> Teresa started here at 60 and did her first pull-up about three months later. Sam is 70 and deadlifts 135 pounds for reps.</li>
  <li><strong>You want to keep what you like doing.</strong> Golf, hiking, grandkids, carrying your own bags. Jonathan had quit golf with a back that hurt to bend. He plays again.</li>
</ul>
<p><a href="/case-studies">Fifteen client case studies are here</a>, with their numbers and what changed.</p>

<h2 id="local">A Placentia gym, not a chain</h2>
<p>We are on E. Yorba Linda Blvd, a few minutes from anywhere in town: Tri-City Park, the Alta Vista and Kraemer neighbourhoods, Valencia and El Dorado. There is parking at the door. Most clients are here and gone inside an hour.</p>
<p>What that means in practice is that there is no waiting for a rack, nobody watching you learn something new, and no hand-off to a junior trainer. Every session is with Coach Dan.</p>

{SHARED_TRAIN}

{SHARED_PRICE}

<h2 id="start">How to start</h2>
<p>Book a free consult. It takes about an hour: an InBody scan, a movement and strength assessment, and a plan, before you pay for anything. You will leave knowing your numbers either way.</p>
<p>If you would rather read first, the <a href="/fitness-after-40">fitness after 40 guides</a> are a good place to start, or the <a href="/personal-training-cost-placentia">cost guide</a> if price is the question.</p>

<h2 id="visit">Finding us</h2>
<p>Fig Performance, 1284 E. Yorba Linda Blvd, Placentia, CA 92870. Staffed Monday to Friday, 5 AM to 8:30 PM, and Saturday, 5 AM to 12 PM. Closed Sunday. <a href="https://www.google.com/maps/search/?api=1&amp;query=Fig%20Performance%2C%201284%20E.%20Yorba%20Linda%20Blvd%2C%20Placentia%2C%20CA%2092870">Get directions</a>.</p>
<p>Coming from out of town? We also have pages for <a href="/personal-trainer-yorba-linda">Yorba Linda</a>, <a href="/personal-trainer-brea">Brea</a>, <a href="/personal-trainer-fullerton">Fullerton</a> and <a href="/personal-trainer-anaheim-hills">Anaheim Hills</a>.</p>
{CTA}"""

faqs = [
    ("Who is the best personal trainer in Placentia, CA?",
     "We would say Coach Dan, but go and compare. Fig Performance is a private one-on-one studio at 1284 E. Yorba Linda Blvd, Placentia. Coach Dan Figueroa is an ACSM certified personal trainer and a Precision Nutrition Level 1 certified nutrition coach, and every session is with him. The first consult and InBody scan are free, so you can judge for yourself before paying anything."),
    ("How much does a personal trainer cost in Placentia?",
     "At Fig Performance, personal training is $60 to $90 a session, billed weekly or monthly, with a 3-month minimum. Where you land in the range depends on how often you train, and you get the exact number at your free consult. Semi-private small-group training starts at $180 a month."),
    ("Do I need to be fit before I start?",
     "No. Most people here started after a long gap, an injury, or both. The first weights are chosen from what you can do on the day of your assessment, not from a template."),
    ("What are your hours?",
     "Monday to Friday, 5 AM to 8:30 PM, and Saturday, 5 AM to 12 PM. Closed Sunday. Sessions are by appointment."),
    ("Do you train people over 60?",
     "Often. Teresa did her first pull-up at 60 and Sam deadlifts 135 pounds at 70. Training is built around what your joints and history allow, and it progresses from there."),
]

html = page(
    SLUG,
    "Personal Trainer in Placentia, CA | Fig Performance",
    "Private one-on-one personal training in Placentia, CA for adults over 40. Free consult and InBody scan at 1284 E. Yorba Linda Blvd. $60 to $90 a session.",
    "Personal Trainer in Placentia, CA",
    "Placentia, CA", "A personal trainer in Placentia, for adults over 40.",
    "One coach, one person, one room. Free consult and InBody scan.",
    [("who", "Who trains here"), ("local", "A Placentia gym"), ("training", "What training looks like"),
     ("pricing", "Pricing"), ("start", "How to start"), ("visit", "Finding us")],
    body, faqs, "Personal trainer in Placentia")

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
