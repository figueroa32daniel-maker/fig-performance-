"""Placentia personal training page + free consult offer page."""
from build_pages import page, SITE, CTA

CAL = "https://calendly.com/trainwithcoachdan/free-consult-inbody-scan"
BOOK = f'<p><a class="btn btn-gold" href="{CAL}" target="_blank" rel="noopener">Book your free consult online</a></p>'

pt_body = f"""<p class="legal-intro">Fig Performance is a private, one-on-one personal training gym in Placentia, CA, built for adults over 40. Every session is with Coach Dan Figueroa, an ACSM certified personal trainer, at 1284 E. Yorba Linda Blvd. No crowds, no waiting for equipment, and progress you can measure with an InBody scan.</p>

<h2 id="who">Who we train</h2>
<p>Most clients are 40 to 70, work demanding jobs, and already "eat pretty healthy." They want to lose fat, build muscle and feel strong again, and they're tired of guessing. Many have hurt a back, knee or shoulder before, so every plan starts around what your body can do today.</p>

<h2 id="how">How personal training works</h2>
<ol>
  <li><strong>Free consult and InBody scan.</strong> About an hour: body fat, muscle and visceral fat, a strength assessment and your goals.</li>
  <li><strong>Your plan.</strong> Training two or more times a week, plus a simple <a href="/nutrition-coaching-placentia">nutrition plan</a> built from foods you already like.</li>
  <li><strong>Train one-on-one.</strong> 50-minute sessions with Coach Dan. We track every lift so you get stronger each week.</li>
  <li><strong>Recover.</strong> Red light therapy and vibration therapy are part of the routine.</li>
  <li><strong>Re-scan.</strong> InBody shows what changed, then we adjust.</li>
</ol>

<h2 id="results">Real results from Placentia clients</h2>
<ul>
  <li><strong>Teresa, 60:</strong> couldn't do a single bodyweight exercise. About three months later she did her first pull-up. <a href="/build-muscle-after-60">Read her story</a>.</li>
  <li><strong>Sam, 70:</strong> deadlifts about 135 pounds for reps and presses the 45-pound dumbbells.</li>
  <li>One client lost 10 pounds in her first four weeks.</li>
</ul>
<p>Fig Performance is rated 5.0 on Google, and Coach Dan's coaching business is rated 5.0 across 38 Yelp reviews.</p>

<h2 id="pricing">Pricing</h2>
<p>Personal training is $90 a session with Coach Dan, billed weekly or monthly, with a 3-month minimum. Save 20% when you pay 3 months in full. Your first consult and InBody scan are free. See <a href="/pricing">all plans and pricing</a>, or read <a href="/personal-training-cost-placentia">how much personal training costs in Placentia</a>.</p>

<h2 id="hours">Hours and location</h2>
<p>1284 E. Yorba Linda Blvd, Placentia, CA 92870. Staffed Monday to Friday, 5 AM to 8 PM, and Saturday, 5 AM to 12 PM. Easy to reach from <a href="/personal-trainer-yorba-linda">Yorba Linda</a>, <a href="/personal-trainer-brea">Brea</a>, Fullerton, Anaheim Hills and Villa Park.</p>

<h2 id="start">Start with a free consult</h2>
<p>Your consult and InBody scan are free, with no commitment. <a href="/free-consult-placentia">See what's included</a>.</p>
{BOOK}
{CTA}"""

pt_faqs = [
    ("How much does a personal trainer cost in Placentia?",
     "At Fig Performance, personal training is $90 a session with Coach Dan, billed weekly or monthly, with a 3-month minimum. You save 20% when you pay 3 months in full. The first consult and InBody scan are free."),
    ("Is there a personal trainer in Placentia for people over 40?",
     "Yes. Fig Performance in Placentia specializes in one-on-one strength training for adults over 40, with InBody scans to track fat and muscle and plans built around old injuries."),
    ("How often should I train with a personal trainer?",
     "Many Fig Performance clients over 40 train twice a week in 50-minute sessions and add daily walking. Some train three or four times a week."),
    ("What areas do you serve?",
     "Fig Performance is at 1284 E. Yorba Linda Blvd in Placentia and serves Placentia, Yorba Linda, Brea, Fullerton, Anaheim Hills and Villa Park. Concierge training at your home or office is also available."),
    ("Do I need to be in shape to start?",
     "No. Plans start where your body is today. If you're under a doctor's care for an injury, check with your doctor first."),
]

fc_body = f"""<p class="legal-intro">Book a free consult with InBody scan at Fig Performance in Placentia, free and with no commitment. In about an hour you'll know your real body composition, how strong you are, and exactly what a plan would look like for you.</p>
{BOOK}

<h2 id="included">What's included</h2>
<ul>
  <li><strong>InBody body-composition scan:</strong> body fat, muscle mass and visceral fat, not just your weight. You keep the printout.</li>
  <li><strong>Movement and strength assessment:</strong> how you move, where you're strong, and what to work around.</li>
  <li><strong>Goals conversation:</strong> what you want, what you've tried, and what's gotten in the way.</li>
  <li><strong>Your game plan:</strong> how often to train, what to focus on, and how nutrition fits, before you commit to anything.</li>
</ul>

<h2 id="who">Who it's for</h2>
<p>Adults over 40 in Placentia, Yorba Linda, Brea, Fullerton, Anaheim Hills and Villa Park who want to lose fat, build muscle and get stronger, with a coach who measures progress instead of guessing.</p>

<h2 id="expect">What to expect</h2>
<ol>
  <li>Pick a time online. Weekdays 5 AM to 8:30 PM, Saturdays 5 AM to noon.</li>
  <li>Wear clothes you can move in. For the most accurate InBody reading, skip a big meal and heavy exercise for a few hours beforehand.</li>
  <li>Meet Coach Dan at 1284 E. Yorba Linda Blvd, Placentia.</li>
  <li>Leave with your numbers and a plan. No pressure to sign up.</li>
</ol>

<h2 id="coach">Your coach</h2>
<p>Coach Dan Figueroa is an ACSM certified personal trainer with more than 10 years of coaching. Fig Performance is rated 5.0 on Google. Read how <a href="/build-muscle-after-60">Teresa did her first pull-up at 60</a> or <a href="/how-to-lose-weight-after-40">how Dan approaches weight loss after 40</a>.</p>
{BOOK}
{CTA}"""

fc_faqs = [
    ("Is the consult really free?",
     "Yes. The consult and InBody scan are free, with no obligation to sign up."),
    ("How long does the consult take?",
     "About an hour, including the InBody scan, a movement and strength assessment, and your game plan."),
    ("What is an InBody scan?",
     "A quick, painless body-composition scan that measures body fat, muscle mass and visceral fat. You stand on the device for about a minute."),
    ("Who shouldn't do an InBody scan?",
     "People with a pacemaker or other implanted electronic device, and people who are pregnant, should skip the scan. You can still do the rest of the consult."),
    ("Can I book online?",
     "Yes. Pick a time on Coach Dan's calendar, or call or text (714) 396-7178."),
]

pages = {
    "personal-training-placentia": page(
        "personal-training-placentia",
        "Personal Training in Placentia, CA for Adults 40+ | Fig Performance",
        "Private one-on-one personal training in Placentia, CA for adults over 40. $90 a session, InBody scans, real client results. Free consult with InBody scan.",
        "Personal Training in Placentia, CA | Fig Performance",
        "Placentia, CA", "Personal Training in Placentia, CA",
        "One-on-one strength coaching for adults over 40, measured with InBody scans.",
        [("who", "Who we train"), ("how", "How it works"), ("results", "Client results"), ("pricing", "Pricing"), ("hours", "Hours and location"), ("start", "Free consult")],
        pt_body, pt_faqs, "Personal Training in Placentia"),
    "free-consult-placentia": page(
        "free-consult-placentia",
        "Free Consult + InBody Scan in Placentia | Fig Performance",
        "Free consult with InBody body-composition scan in Placentia, CA. About an hour, free, no commitment. Book online with Coach Dan.",
        "Free Consult + InBody Scan in Placentia",
        "Free offer", "Free Consult + InBody Scan in Placentia",
        "Free, no commitment. Your numbers, your strength and your plan in about an hour.",
        [("included", "What's included"), ("who", "Who it's for"), ("expect", "What to expect"), ("coach", "Your coach")],
        fc_body, fc_faqs, "Free Consult + InBody Scan"),
}

if __name__ == "__main__":
    for slug, h in pages.items():
        (SITE / f"{slug}.html").write_text(h)
        print("wrote", slug, len(h))
