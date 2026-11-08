"""Guide: How much does personal training cost in Placentia?"""
from build_pages import page, SITE, CTA

SLUG = "personal-training-cost-placentia"
CAL = "https://calendly.com/trainwithcoachdan/free-consult-inbody-scan"

body = f"""<p class="legal-intro">Personal training at Fig Performance in Placentia costs $90 a session, or $360 a month for one session a week, with a free first consult and InBody scan. Most gyms in town don't post their personal training prices, so here's what training actually costs, what changes the price, and how to compare your options.</p>

<h2 id="fig">Fig Performance prices (2026)</h2>
<div class="price-table-wrap"><table class="price-table">
  <thead><tr><th>Sessions a week</th><th>Monthly</th><th>3 months paid upfront</th></tr></thead>
  <tbody>
    <tr><td>1</td><td>$360</td><td>$864</td></tr>
    <tr><td>2</td><td>$720</td><td>$1,728</td></tr>
    <tr><td>3</td><td>$1,080</td><td>$2,592</td></tr>
    <tr><td>4</td><td>$1,440</td><td>$3,456</td></tr>
  </tbody>
</table></div>
<ul>
  <li>Every session is one-on-one with Coach Dan Figueroa, ACSM certified.</li>
  <li>3-month minimum on every training plan.</li>
  <li><strong>Save 20%</strong> when you pay 3 months in full.</li>
  <li>The first consult and InBody body-composition scan are free.</li>
</ul>
<p>Semi-private training, with coached small-group sessions, open gym, red light and vibration therapy, is $199 to $345 a month depending on how many sessions a week you choose. A membership with open gym is $79.99 a month plus a $50 yearly maintenance fee, month to month. No initiation fee on any plan. Concierge training at your home or office is quoted by location. Full details are on the <a href="/pricing">pricing page</a>.</p>

<h2 id="types">The main types of training in Placentia</h2>
<ul>
  <li><strong>Big-box gym membership.</strong> The cheapest way to get access to equipment. For example, Crunch Fitness Placentia lists plans from about $10 to $35 a month (<a href="https://www.crunch.com/locations/placentia" target="_blank" rel="noopener noreferrer">crunch.com</a>, checked Oct 31, 2026). You get equipment, not coaching. Personal training there is a separate cost.</li>
  <li><strong>Group classes and semi-private training.</strong> A coach runs several people at once. Lower cost per session, less individual attention.</li>
  <li><strong>Private one-on-one training.</strong> One coach, one client, a plan built around your body and goals. The highest cost per session, and usually the fastest results, especially if you have old injuries or specific goals.</li>
</ul>

<h2 id="price">What changes the price</h2>
<ul>
  <li><strong>One-on-one vs. shared sessions.</strong> Splitting a coach's hour with others lowers the price and the attention you get.</li>
  <li><strong>Session length.</strong> Compare the cost per minute: a 30-minute session at $60 costs more per minute than 50 minutes at $90.</li>
  <li><strong>How often you train.</strong> Most adults over 40 see results training two times a week.</li>
  <li><strong>What's included.</strong> Nutrition coaching, body-composition scans, recovery tools and a written program add value even when the session price looks the same.</li>
  <li><strong>Commitment.</strong> Packages and paid-in-full plans usually lower the per-session cost.</li>
</ul>

<h2 id="compare">How to compare trainers in Placentia</h2>
<ol>
  <li>Ask for the price per session and per month. If a gym won't tell you until you visit, ask why.</li>
  <li>Ask who will actually train you, and whether it's always the same coach.</li>
  <li>Ask how they measure progress. The scale alone misses fat loss and muscle gain.</li>
  <li>Check credentials (ACSM, NASM, NSCA) and read recent Google and Yelp reviews.</li>
  <li>Ask about injuries. A good trainer works around a bad back or shoulder instead of ignoring it.</li>
  <li>Try a free consult before you commit to a package.</li>
</ol>

<h2 id="worth">Is personal training worth it after 40?</h2>
<p>For most busy adults over 40, the cost buys three things a membership can't: a plan built around your body, someone making sure you get stronger every week, and accountability to keep showing up. Teresa, 60, went from no bodyweight exercises to her first pull-up in about three months. <a href="/build-muscle-after-60">Read her story</a>, or see <a href="/how-to-lose-weight-after-40">how Coach Dan approaches weight loss after 40</a>.</p>

<h2 id="start">Start with a free consult</h2>
<p>See your InBody numbers and get a plan before you spend anything. <a href="/free-consult-placentia">See what's included</a>.</p>
<p><a class="btn btn-gold" href="{CAL}" target="_blank" rel="noopener">Book your free consult online</a></p>
{CTA}"""

faqs = [
    ("How much does personal training cost in Placentia?",
     "At Fig Performance, one-on-one personal training is $90 a session: $360 a month for once a week or $720 a month for twice a week. Save 20% by paying 3 months in full. The first consult and InBody scan are free."),
    ("How much is a gym membership in Placentia?",
     "Big-box gyms in Placentia list memberships from roughly $10 to $35 a month for equipment access. Personal training is usually extra. At Fig Performance, an open-gym membership is $79.99 a month, and semi-private small-group training with recovery tools is $199 to $345 a month."),
    ("Why is one-on-one training more expensive than a gym membership?",
     "A membership pays for equipment. One-on-one training pays for a coach's full attention: a plan built for you, form correction on every set, and progress tracking."),
    ("How many personal training sessions a week do I need?",
     "Many Fig Performance clients over 40 train twice a week in 50-minute sessions and add daily walking."),
    ("Is there a free trial?",
     "Fig Performance offers a free consult with an InBody body-composition scan, about an hour, with no commitment."),
]

html = page(SLUG,
    "Personal Training Cost in Placentia, CA (2026 Prices) | Fig Performance",
    "How much personal training costs in Placentia, CA: real 2026 prices ($90 a session, $360/month), what changes the price, and how to compare trainers.",
    "How Much Does Personal Training Cost in Placentia? (2026)",
    "Prices", "How Much Does Personal Training Cost in Placentia?",
    "Real 2026 prices, what changes them, and how to compare your options.",
    [("fig", "Fig Performance prices"), ("types", "Types of training"), ("price", "What changes the price"), ("compare", "How to compare"), ("worth", "Is it worth it?"), ("start", "Free consult")],
    body, faqs, "Personal Training Cost", kind="article", published="2026-10-31")

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", len(html))
