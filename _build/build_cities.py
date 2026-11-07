"""City landing pages for Fig Performance: Yorba Linda, Brea, Fullerton, Anaheim Hills.

Each page has its own angle, route and FAQ so the four pages read as four pages,
not one template. Facts come only from the live site and MEMORY.md. No client is
placed in a city unless Dan has said so (none have, so none are).
"""
from build_pages import page, SITE, CTA

SHARED_TRAIN = """<h2 id="training">What training looks like</h2>
<ol>
  <li><strong>Free consult and InBody scan.</strong> About an hour: body fat, muscle and visceral fat, a movement and strength assessment, and your goals.</li>
  <li><strong>Your plan.</strong> Two or more 50-minute sessions a week, one-on-one with Coach Dan, plus a simple <a href="/nutrition-coaching-placentia">nutrition plan</a> built from foods you already eat.</li>
  <li><strong>Recover.</strong> Members use <a href="/red-light-therapy-placentia">red light therapy</a> and <a href="/vibration-therapy-placentia">vibration therapy</a> as part of the routine.</li>
  <li><strong>Re-scan.</strong> The <a href="/inbody-scan-placentia">InBody</a> shows what changed. Then we adjust. Scan. Plan. Train. Recover. Re-scan.</li>
</ol>
<p>Coach Dan Figueroa is an ACSM certified personal trainer and a Precision Nutrition Level 1 certified nutrition coach. Every session is with him. No hand-offs to a junior trainer.</p>"""

SHARED_PRICE = """<h2 id="pricing">Pricing</h2>
<p>Personal training is $90 a session, billed weekly or monthly, with a 3-month minimum. Save 20% when you pay in full for 3 months. Membership with classes and recovery tools is quoted at the consult. See <a href="/pricing">plans and pricing</a> or the <a href="/personal-training-cost-placentia">personal training cost guide</a>.</p>"""


def start_block(city):
    return f"""<h2 id="start">How to start</h2>
<p>Book a free consult. You'll leave with your InBody numbers, an honest read on your strength, and a plan, before you commit to anything. If you'd rather read first, start with the <a href="/fitness-after-40">fitness after 40 guides</a>.</p>
<p>Prefer not to drive? <a href="/in-home-personal-training">In-home personal training</a> brings Coach Dan to your {city} home or office. Concierge plans are quoted individually.</p>"""


def visit_block(city, route):
    return f"""<h2 id="visit">Getting here from {city}</h2>
<p>{route}</p>
<p>Fig Performance is at 1284 E. Yorba Linda Blvd, Placentia, CA 92870, staffed Monday to Friday, 5 AM to 8 PM, and Saturday, 5 AM to 12 PM. Closed Sunday. <a href="https://www.google.com/maps/search/?api=1&amp;query=Fig%20Performance%2C%201284%20E.%20Yorba%20Linda%20Blvd%2C%20Placentia%2C%20CA%2092870">Get directions from {city}</a>.</p>
{CTA}"""


# ------------------------------------------------------------------ cities
CITIES = {
    "Yorba Linda": {
        "slug": "personal-trainer-yorba-linda",
        "h1": "Personal Trainer Near Yorba Linda for Adults Over 40",
        "lede": "Private one-on-one strength training on Yorba Linda Blvd, just across the Placentia line.",
        "intro": """<p class="legal-intro">Looking for a personal trainer in Yorba Linda? Fig Performance is a private, one-on-one strength gym on E. Yorba Linda Blvd in Placentia, the same road that runs through Yorba Linda, a short drive west. It's built for adults over 40 who already exercise and eat reasonably well, and want the effort to finally show in the mirror and on the scan.</p>""",
        "who": """<h2 id="who">Who we help in Yorba Linda</h2>
<p>Yorba Linda calls itself the Land of Gracious Living, and the people Fig Performance is built for have earned it: business owners, executives and professionals in their 40s, 50s and 60s with full calendars and a long history of working out. The pattern we hear most from clients is "I'm doing everything right and nothing is changing." Usually something is changing, just not the number on the scale. We help them:</p>
<ul>
  <li><strong>Find out what's actually happening.</strong> An InBody scan separates fat from muscle, so you stop guessing whether the last six months worked.</li>
  <li><strong>Lift heavier than "light weights."</strong> Muscle after 40 responds to progressive strength work, not endless cardio. <a href="/strength-training-for-women-over-50">Here's how that looks for women over 50</a>, and <a href="/workout-plan-for-men-over-40">for men over 40</a>.</li>
  <li><strong>Protect what you love doing.</strong> Golf, tennis, hiking the Chino Hills trails, keeping up with grandkids. Training is built around the back, hips and shoulders those hobbies lean on.</li>
</ul>""",
        "why": """<h2 id="why">Why Yorba Linda clients drive to Placentia</h2>
<p>There are plenty of gyms closer to home. People choose Fig Performance for three reasons: every session is private and one-on-one, so there's no waiting on a rack or being watched; progress is measured with an InBody scan instead of a mirror and a hope; and the whole thing fits a working schedule, with the doors open at 5 AM on weekdays and Saturdays.</p>""",
        "route": "Yorba Linda Blvd runs straight from Yorba Linda into Placentia, and we're on it. Head west on Yorba Linda Blvd and the gym is on the Placentia side of the line. Imperial Highway works too if you're coming from the eastern end of town.",
        "faqs": [
            ("Is there a personal trainer near Yorba Linda for adults over 40?",
             "Yes. Fig Performance offers private one-on-one personal training for adults over 40 at 1284 E. Yorba Linda Blvd in Placentia, a short drive west of Yorba Linda on the same road. Every session is with Coach Dan, an ACSM certified personal trainer."),
            ("How much does a personal trainer cost near Yorba Linda?",
             "Personal training at Fig Performance is $90 a session, billed weekly or monthly, with a 3-month minimum. You save 20% when you pay in full for 3 months. The first consult and InBody scan are free."),
            ("Can a personal trainer come to my home in Yorba Linda?",
             "Yes. In-home personal training brings Coach Dan to your home or office in Yorba Linda. Each concierge plan is quoted individually because cost depends on location and schedule."),
            ("I've worked out for years. Will this be different?",
             "Most of our clients have. The difference is one-on-one coaching with a real strength progression, and an InBody scan every few months so you can see fat and muscle change separately instead of guessing from the scale."),
            ("What if I have an old back, knee or shoulder problem?",
             "Plans are built around what your body can do today. Coach Dan has trained clients in their 60s and 70s with shoulder arthritis and past injuries. If you're under a doctor's care, check with your doctor first."),
        ],
    },
    "Brea": {
        "slug": "personal-trainer-brea",
        "h1": "Personal Trainer Near Brea for Adults Over 40",
        "lede": "Private one-on-one strength training in Placentia, a quick drive south of Brea.",
        "intro": """<p class="legal-intro">Looking for a personal trainer in Brea? Fig Performance is a private, one-on-one strength gym at 1284 E. Yorba Linda Blvd in Placentia, a quick drive south from Brea down Kraemer Blvd or the 57. It's built for adults over 40 with demanding jobs who want to lose fat, build strength and stop wondering whether their workouts are working.</p>""",
        "who": """<h2 id="who">Who we help in Brea</h2>
<p>Brea is where a lot of North Orange County goes to work. If you spend your days in an office or a business park, in meetings or on the 57, your energy is usually spent by the time the gym would normally happen. We help people in that spot:</p>
<ul>
  <li><strong>Train before work, not after.</strong> Doors open at 5 AM, Monday through Saturday. A 50-minute session fits before the commute.</li>
  <li><strong>Undo a desk.</strong> Tight hips, a stiff upper back and a cranky lower back are the usual starting point. The plan starts there.</li>
  <li><strong>See a number move.</strong> Many clients haven't lost weight in years despite "eating pretty healthy." The <a href="/inbody-scan-placentia">InBody scan</a> shows whether it's fat, muscle or water, and <a href="/why-am-i-not-losing-weight">this guide</a> explains the most common reasons the scale is stuck.</li>
</ul>""",
        "why": """<h2 id="why">Why Brea clients drive to Placentia</h2>
<p>Brea has big gyms. What it doesn't have much of is a private floor where the only two people in the room are you and your coach. At Fig Performance there's no waiting for a squat rack at 5:30 PM, no being watched, and no coach splitting attention between four clients. Progress is measured on an InBody scan, so you know in 90 days whether the plan is working.</p>""",
        "route": "From Brea, take Kraemer Blvd south into Placentia and turn onto Yorba Linda Blvd, or take the 57 south and exit at Yorba Linda Blvd. From the Brea Mall area, Imperial Highway to Kraemer is the simplest route.",
        "faqs": [
            ("Is there a personal trainer near Brea for adults over 40?",
             "Yes. Fig Performance offers private one-on-one personal training for adults over 40 at 1284 E. Yorba Linda Blvd in Placentia, a quick drive south of Brea by Kraemer Blvd or the 57. Every session is with Coach Dan, an ACSM certified personal trainer."),
            ("How much does a personal trainer cost near Brea?",
             "Personal training at Fig Performance is $90 a session, billed weekly or monthly, with a 3-month minimum. You save 20% when you pay in full for 3 months. The first consult and InBody scan are free."),
            ("Can I train before work?",
             "Yes. Fig Performance is staffed from 5 AM on weekdays and Saturdays. Early sessions are popular with clients who commute to Brea offices, so book your consult early to lock in a time."),
            ("Can a personal trainer come to my office in Brea?",
             "Yes. In-home and in-office personal training is available in Brea. Each concierge plan is quoted individually because cost depends on location and schedule."),
            ("I sit all day. Can I still start strength training?",
             "Yes. Most clients start with tight hips and a stiff back from desk work. The first weeks build mobility and basic strength patterns before loading them. If you're under a doctor's care for an injury, check with your doctor first."),
        ],
    },
    "Fullerton": {
        "slug": "personal-trainer-fullerton",
        "h1": "Personal Trainer Near Fullerton for Adults Over 40",
        "lede": "Private one-on-one strength training on Yorba Linda Blvd, a few minutes east of Fullerton.",
        "intro": """<p class="legal-intro">Looking for a personal trainer in Fullerton? Fig Performance is a private, one-on-one strength gym at 1284 E. Yorba Linda Blvd in Placentia, a few minutes east of Fullerton on the same road that runs past Cal State Fullerton. It's built for adults over 40 who want to lose fat, build muscle and get stronger, with a coach who measures the results.</p>""",
        "who": """<h2 id="who">Who we help in Fullerton</h2>
<p>Fullerton is a university town with a major hospital and a busy downtown, so if you work on campus, on a hospital schedule or in an office, you know what it's like to run out of day before you get to the gym. The same goes for anyone who has belonged to the same Fullerton gym for years and quietly stopped seeing changes. Many of our clients are over 50. Some are over 70. We help them:</p>
<ul>
  <li><strong>Build muscle at any age.</strong> <a href="/build-muscle-after-60">Teresa, 60, and Sam, 70</a>, started from almost nothing. Sam now deadlifts 135 pounds. Teresa did her first pull-up in about three months.</li>
  <li><strong>Train around long shifts.</strong> We're open 5 AM to 8 PM on weekdays and 5 AM to noon on Saturdays, so sessions fit around hospital, campus and clinic schedules.</li>
  <li><strong>Lose fat without losing muscle.</strong> The <a href="/inbody-scan-placentia">InBody scan</a> tracks both, which matters most for anyone over 40, and especially for anyone on a GLP-1 medication. <a href="/glp-1-muscle-loss">Here's how we handle that</a>.</li>
</ul>""",
        "why": """<h2 id="why">Why Fullerton clients drive to Placentia</h2>
<p>Fullerton has no shortage of gyms, and most of them are busy at the hours a working adult can train. Fig Performance is the opposite: a private floor, one coach, one client. There's no waiting for equipment, no crowd, and no guesswork about whether you're getting stronger, because every lift is tracked and every few months the InBody shows what changed.</p>""",
        "route": "Yorba Linda Blvd runs east out of Fullerton, past Cal State Fullerton, straight into Placentia. Stay on it and we're on the right-hand side after you cross into Placentia. From downtown Fullerton, Chapman Ave east to Placentia Ave, then north to Yorba Linda Blvd, is the other direct route.",
        "faqs": [
            ("Is there a personal trainer near Fullerton for adults over 40?",
             "Yes. Fig Performance offers private one-on-one personal training for adults over 40 at 1284 E. Yorba Linda Blvd in Placentia, a few minutes east of Fullerton on Yorba Linda Blvd. Every session is with Coach Dan, an ACSM certified personal trainer."),
            ("How much does a personal trainer cost near Fullerton?",
             "Personal training at Fig Performance is $90 a session, billed weekly or monthly, with a 3-month minimum. You save 20% when you pay in full for 3 months. The first consult and InBody scan are free."),
            ("Do you train seniors?",
             "Yes. Clients in their 60s and 70s train at Fig Performance, including people with shoulder arthritis and past injuries. Plans start with what your body can do today. Read the strength training for seniors guide for how that works."),
            ("Can a personal trainer come to my home in Fullerton?",
             "Yes. In-home personal training is available in Fullerton. Each concierge plan is quoted individually because cost depends on location and schedule."),
            ("What's included in the free consult?",
             "About an hour with Coach Dan: an InBody body-composition scan, a movement and strength assessment, a conversation about your goals, and a plan. There's no commitment."),
        ],
    },
    "Anaheim Hills": {
        "slug": "personal-trainer-anaheim-hills",
        "h1": "Personal Trainer Near Anaheim Hills for Adults Over 40",
        "lede": "Private one-on-one strength training in Placentia, a straight shot north of the 91.",
        "intro": """<p class="legal-intro">Looking for a personal trainer in Anaheim Hills? Fig Performance is a private, one-on-one strength gym at 1284 E. Yorba Linda Blvd in Placentia, a straight shot north from the 91 by Imperial Highway or Lakeview Ave. It's built for adults over 40 who already take care of themselves and want a coach who makes the work count.</p>""",
        "who": """<h2 id="who">Who we help in Anaheim Hills</h2>
<p>If you live in Anaheim Hills, odds are you have two things going on: long days, often with a commute on the 91, and an active life you want to protect. Hiking the canyon trails, golf, cycling, chasing kids or grandkids. The goal is rarely just to look better. It's to keep doing those things at 55, 65 and 75. We help them:</p>
<ul>
  <li><strong>Build strength that carries over.</strong> Squats, hinges, presses, carries and pull-ups, loaded progressively. <a href="/strength-training-for-seniors">Here's what that looks like for clients in their 70s</a>.</li>
  <li><strong>Protect knees, hips and backs.</strong> Hills are hard on joints. Training is built around the ones that complain.</li>
  <li><strong>Make a limited schedule count.</strong> Two 50-minute one-on-one sessions a week, planned and tracked, do more than five unplanned hours at a crowded gym.</li>
</ul>""",
        "why": """<h2 id="why">Why Anaheim Hills clients drive to Placentia</h2>
<p>It's a private gym, which is rare on this side of the county. The only people on the floor are you and Coach Dan. No waiting, no crowd, no coach splitting attention. Progress is measured with an InBody scan, so fat and muscle are tracked separately and you know whether the plan is working before you've spent a year on it.</p>""",
        "route": "From Anaheim Hills, take the 91 to Imperial Highway or Lakeview Ave and head north into Placentia, then turn onto Yorba Linda Blvd. From the Santa Ana Canyon Rd side, Lakeview north is the most direct route.",
        "faqs": [
            ("Is there a personal trainer near Anaheim Hills for adults over 40?",
             "Yes. Fig Performance offers private one-on-one personal training for adults over 40 at 1284 E. Yorba Linda Blvd in Placentia, north of Anaheim Hills by Imperial Highway or Lakeview Ave. Every session is with Coach Dan, an ACSM certified personal trainer."),
            ("How much does a personal trainer cost near Anaheim Hills?",
             "Personal training at Fig Performance is $90 a session, billed weekly or monthly, with a 3-month minimum. You save 20% when you pay in full for 3 months. The first consult and InBody scan are free."),
            ("Can a personal trainer come to my home in Anaheim Hills?",
             "Yes. In-home personal training is available in Anaheim Hills. Each concierge plan is quoted individually because cost depends on location and schedule."),
            ("Will strength training help my hiking, golf or cycling?",
             "That's the point of it. Stronger legs, hips and back mean more power and fewer aches in whatever you do outside the gym. Training is built around the joints your activities lean on."),
            ("How many times a week do I need to come?",
             "Most clients over 40 train twice a week in 50-minute one-on-one sessions and add daily walking. Some train three or four times a week. We'll settle on the right number at your free consult."),
        ],
    },
}

pages = {}
for city, c in CITIES.items():
    body = "\n\n".join([c["intro"], c["who"], c["why"], SHARED_TRAIN, SHARED_PRICE, start_block(city), visit_block(city, c["route"])])
    toc = [("who", f"Who we help in {city}"), ("why", "Why clients drive to Placentia"), ("training", "What training looks like"),
           ("pricing", "Pricing"), ("start", "How to start"), ("visit", f"Getting here from {city}")]
    pages[f"{c['slug']}.html"] = page(
        c["slug"],
        f"Personal Trainer in {city}, CA | Fig Performance",
        f"Private one-on-one personal training near {city} for adults over 40. Lose fat, build strength, track it with InBody scans. Free consult.",
        f"Personal Trainer Near {city} for Adults Over 40 | Fig Performance",
        "Areas we serve", c["h1"], c["lede"], toc, body, c["faqs"], f"Personal Trainer {city}")

if __name__ == "__main__":
    for name, content in pages.items():
        (SITE / name).write_text(content)
        print("wrote", name, len(content))
