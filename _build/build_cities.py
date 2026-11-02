"""City landing pages for Fig Performance (Yorba Linda, Brea)."""
from build_pages import page, SITE, CTA


def city_body(city, angle):
    return f"""<p class="legal-intro">Looking for a personal trainer in {city}? Fig Performance is a private, one-on-one strength gym on E. Yorba Linda Blvd in Placentia, a short drive from {city}. It's built for adults over 40 who already exercise and eat reasonably well, and want the effort to finally show.</p>

<h2 id="who">Who we help</h2>
<p>{angle}</p>
<ul>
  <li><strong>Lose fat and build muscle</strong> at the same time, measured with an <a href="/inbody-scan-placentia">InBody body-composition scan</a>.</li>
  <li><strong>Get stronger without getting hurt</strong>, with a plan built around your lower back, knees, hips or shoulders.</li>
  <li><strong>Fit training around a demanding schedule</strong>: we're staffed Monday to Friday, 5 AM to 8 PM, and Saturday, 5 AM to 12 PM.</li>
</ul>

<h2 id="different">What makes Fig Performance different</h2>
<ul>
  <li><strong>One-on-one with Coach Dan.</strong> Every personal training session is just you and an ACSM certified trainer. No hand-offs.</li>
  <li><strong>No crowds, no waiting.</strong> A private 1,500 sq ft facility instead of a packed big-box floor.</li>
  <li><strong>Measured, not guessed.</strong> Scan. Plan. Train. Recover. Re-scan.</li>
  <li><strong>Recovery built in.</strong> Members get <a href="/red-light-therapy-placentia">red light therapy</a> and vibration therapy.</li>
  <li><strong>Concierge option.</strong> Prefer to train at your {city} home or office? Coach Dan can come to you. Ask for a quote.</li>
</ul>

<h2 id="pricing">Pricing</h2>
<p>Personal training is $90 a session, billed weekly or monthly, with a 3-month minimum. Save 20% when you pay in full for 3 months. Membership with classes and recovery tools is also available. See <a href="/pricing">plans and pricing</a>.</p>

<h2 id="start">How to start</h2>
<p>Book a free consult. It takes about an hour: an InBody scan, a movement assessment, a conversation about your goals, and a game plan. You'll know exactly what training would look like before you commit to anything.</p>
<p>New to strength training after 40? Start with <a href="/how-to-lose-weight-after-40">how to lose weight after 40</a>, read <a href="/why-am-i-not-losing-weight">why you might not be losing weight</a>, or see <a href="/build-muscle-after-60">how clients in their 60s and 70s build muscle</a>.</p>

<h2 id="visit">Getting here from {city}</h2>
<p>Fig Performance is at 1284 E. Yorba Linda Blvd, Placentia, CA 92870. <a href="https://www.google.com/maps/search/?api=1&amp;query=Fig%20Performance%2C%201284%20E.%20Yorba%20Linda%20Blvd%2C%20Placentia%2C%20CA%2092870">Get directions from {city}</a>.</p>
{CTA}"""


def city_faqs(city):
    return [
        (f"Is there a personal trainer near {city} for adults over 40?",
         f"Yes. Fig Performance offers private one-on-one personal training for adults over 40 at 1284 E. Yorba Linda Blvd in Placentia, a short drive from {city}. Every session is with Coach Dan, an ACSM certified personal trainer."),
        (f"How much does personal training cost near {city}?",
         "Personal training at Fig Performance is $90 a session with Coach Dan, billed weekly or monthly, with a 3-month minimum. You save 20% when you pay in full for 3 months. The first consult is free."),
        (f"Can a trainer come to my home in {city}?",
         f"Yes. Concierge personal training brings Coach Dan to your home or office in {city}. Because cost depends on location, each concierge plan is quoted individually."),
        ("What are your hours?",
         "Fig Performance is staffed Monday to Friday, 5 AM to 8 PM, and Saturday, 5 AM to 12 PM. Closed Sunday. Personal training is booked by appointment."),
        ("Do I need to be in shape to start?",
         "No. Plans are built around where you are today, including any aches in your back, knees, hips or shoulders. If you're under a doctor's care for an injury, check with your doctor first."),
    ]


CITIES = {
    "Yorba Linda": ("personal-trainer-yorba-linda",
                     "Many of our clients are Yorba Linda professionals and business owners in their 40s, 50s and 60s. They've worked out for years, maybe even hired a trainer before, and they're frustrated that the scale and the mirror aren't changing. We help them:"),
    "Brea": ("personal-trainer-brea",
             "Many of our clients live or work around Brea and spend long days at a desk or on the road. They want to feel strong and look the part again, without spending hours in a crowded gym. We help them:"),
}

pages = {}
for city, (slug, angle) in CITIES.items():
    pages[f"{slug}.html"] = page(
        slug,
        f"Personal Trainer in {city}, CA | Fig Performance",
        f"Private one-on-one personal training near {city} for adults over 40. Lose fat, build strength, track it with InBody scans. Free consult.",
        f"Personal Trainer Near {city} for Adults Over 40 | Fig Performance",
        "Areas we serve", f"Personal Trainer for Adults Over 40 Near {city}",
        f"Private one-on-one strength training in Placentia, a short drive from {city}.",
        [("who", "Who we help"), ("different", "What makes us different"), ("pricing", "Pricing"),
         ("start", "How to start"), ("visit", f"Getting here from {city}")],
        city_body(city, angle), city_faqs(city), f"Personal Trainer {city}")

if __name__ == "__main__":
    for name, content in pages.items():
        (SITE / name).write_text(content)
        print("wrote", name, len(content))
