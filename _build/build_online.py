"""Service page: online personal trainer / online coaching (from Coach Dan's description, Nov 3 2026)."""
from build_pages import page, SITE, CTA

SLUG = "online-personal-trainer"
BOOK = '<p><a class="btn btn-gold" href="/#consult" data-interest="Online coaching">Book a free video call</a></p>'

body = f"""<p class="legal-intro">Online coaching with Coach Dan Figueroa is one-on-one coaching you can do from anywhere: a weekly video call with Dan, a custom training program in the app, a custom nutrition plan built from foods you already enjoy, and real accountability. It's $249 a month as a 3-month program. It's built for adults over 40 who want a coach's guidance but can't make it to sessions in person.</p>
{BOOK}

<h2 id="included">What you get</h2>
<ul>
  <li><strong>A weekly one-on-one accountability call.</strong> Up to about 30 minutes with Dan over Zoom, Google Meet or FaceTime.</li>
  <li><strong>A custom training program in the app.</strong> Built around your goals, your limitations and any past injuries. Every workout has a warm-up, the workout and a cool-down stretch, to keep you flexible and help prevent pain and injury.</li>
  <li><strong>A custom nutrition plan.</strong> Built from the foods you already enjoy, using Dan's 80/20 approach.</li>
  <li><strong>Supplement guidance</strong> in your nutrition tab, aimed at health, energy, strength, endurance, bone health, immune support and longevity. Check with your doctor before starting any supplement, especially if you take medication.</li>
  <li><strong>Travel workouts</strong> for when you're on the road or away from your usual gym.</li>
  <li><strong>Support between calls.</strong> Message Dan when you need help.</li>
</ul>

<h2 id="calls">What happens on your weekly call</h2>
<p>Every week, Dan reviews your progress with you:</p>
<ol>
  <li><strong>Your strength numbers in the app.</strong> If your lifts are going up, you're building muscle.</li>
  <li><strong>Your weekly weigh-ins</strong>, and the trend behind them.</li>
  <li><strong>Troubleshooting:</strong> the app, your nutrition, your training, form and technique, and mindset.</li>
  <li><strong>Adjustments.</strong> Your training and nutrition change as you progress.</li>
</ol>
<p>The two biggest things you're paying for are guidance and accountability: someone who knows what you did this week and what you should do next.</p>

<h2 id="nutrition">Nutrition: the 80/20 approach</h2>
<p>About 80% of your food comes from clean, nutrient-dense whole foods, and about 20% is food you simply enjoy. For nutrition to be sustainable, it has to be flexible and it has to be enjoyable. That's how Dan eats, and it's how he coaches. Dan is a Precision Nutrition Level 1 certified nutrition coach. He isn't a registered dietitian, so if you have a medical condition or a prescribed diet, keep your doctor or dietitian in the loop. Read more about <a href="/nutrition-coaching-placentia">how Dan coaches nutrition</a>.</p>

<h2 id="who">Who online coaching is for</h2>
<ul>
  <li>You want a coach, but your schedule doesn't fit in-person sessions.</li>
  <li>You travel for work, or you live outside North Orange County.</li>
  <li>You already have a gym or a home setup and want to train on your own, with a real plan.</li>
  <li>You want accountability without paying for a trainer at every session.</li>
</ul>

<h2 id="compare">Online coaching vs. in-person training</h2>
<div class="price-table-wrap"><table class="price-table compare-table">
  <thead><tr><th></th><th>Online coaching</th><th>In-person, once a week</th></tr></thead>
  <tbody>
    <tr><td>Price</td><td>$249/month</td><td>$387/month</td></tr>
    <tr><td>Time with Dan</td><td>Weekly video call, about 30 min</td><td>Weekly 50-minute session in the gym</td></tr>
    <tr><td>Custom training program</td><td>Yes, in the app</td><td>Yes</td></tr>
    <tr><td>Custom nutrition plan</td><td>Yes</td><td>Yes</td></tr>
    <tr><td>Form coaching</td><td>On your weekly calls</td><td>Every rep, in person</td></tr>
    <tr><td>InBody scans</td><td>No, weekly weigh-ins instead</td><td>Yes</td></tr>
    <tr><td>Where you train</td><td>Anywhere</td><td>Fig Performance, Placentia</td></tr>
  </tbody>
</table></div>
<p>In-person training is best if you're new to lifting, have old injuries that need hands-on attention, or want every set watched. Online coaching works best if you can train on your own and want the plan, the nutrition and the accountability. See <a href="/pricing">all plans and pricing</a> or <a href="/personal-training-placentia">personal training in Placentia</a>.</p>

<h2 id="price">Price</h2>
<p><strong>$249 a month for 3 months ($747), or $697 if you pay the 3 months in full.</strong> Online coaching is sold as a 3-month program, not month to month, because that's how long it takes to build habits that last and see real results.</p>

<h2 id="start">How to start</h2>
<ol>
  <li>Book a free video call. Tell Dan your goals, your schedule and any injuries.</li>
  <li>Dan builds your training program and nutrition plan.</li>
  <li>You get set up in the app and start training.</li>
</ol>
{BOOK}
{CTA}"""

faqs = [
    ("How much does an online personal trainer cost?",
     "Online coaching with Coach Dan at Fig Performance is $249 a month as a 3-month program ($747), or $697 if you pay in full. It includes a weekly one-on-one video call, a custom training program in the app, a custom nutrition plan and supplement guidance."),
    ("What's included in online coaching?",
     "A weekly accountability call over Zoom, Google Meet or FaceTime; a custom training program in the app with warm-ups and cool-down stretches; a custom 80/20 nutrition plan built from foods you enjoy; supplement guidance; travel workouts; and messaging support between calls."),
    ("Is online personal training as good as in-person?",
     "It depends on you. If you can train on your own and want a plan, nutrition and accountability, online coaching works well and costs less. If you're new to lifting or have injuries that need hands-on attention, in-person training is the better start."),
    ("Can I pay month to month?",
     "Online coaching is a 3-month program. You can pay $249 a month for the 3 months, or $697 up front."),
    ("Do I need a gym?",
     "No. Dan builds the program around the equipment you have, whether that's a full gym, a home setup or just dumbbells, and gives you workouts for when you travel."),
    ("Who is the coach?",
     "Daniel Figueroa, owner of Fig Performance in Placentia, CA. He's an ACSM certified personal trainer and a Precision Nutrition Level 1 certified nutrition coach, and he specializes in adults over 40."),
]

html = page(SLUG,
    "Online Personal Trainer for Adults Over 40 | Fig Performance",
    "Online coaching with Coach Dan: weekly 1:1 video call, custom training in the app, custom 80/20 nutrition. $249/month, 3-month program.",
    "Online Personal Trainer for Adults Over 40: Coach Dan Figueroa",
    "Online coaching", "Online Personal Trainer for Adults Over 40",
    "A weekly call with Dan, a custom program and nutrition plan, and accountability from anywhere. $249/month.",
    [("included", "What you get"), ("calls", "Your weekly call"), ("nutrition", "80/20 nutrition"), ("who", "Who it's for"),
     ("compare", "Online vs. in-person"), ("price", "Price"), ("start", "How to start")],
    body, faqs, "Online Coaching")

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", len(html))
