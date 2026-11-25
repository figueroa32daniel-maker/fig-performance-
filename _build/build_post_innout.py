"""Article: In-N-Out after 40. DRAFT, Nov 25 2026. Not published until Dan approves.

Why this one first: trainwithdaveoc.com has ~40 restaurant articles (Chipotle,
Chick-fil-A, Taco Bell, Starbucks, McDonald's, Subway, Panda Express, Wendy's)
and NOTHING on In-N-Out, which is the chain Dan's Orange County clients actually
eat at. Figures are In-N-Out's published nutrition values; aggregator sites
disagree by 20-60 calories on some items, so the page says to check the current
chart rather than pretending to a precision nobody has.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "in-n-out-after-40"

body = f"""<p class="legal-intro">Most trainers would tell you to stay out of In-N-Out. I have never once told a client to stop going. A plan that bans the place your family already eats at is a plan you quit by March, and in this case the ban would be aimed at the wrong thing anyway. In-N-Out is one of the easier places in Orange County to eat well. Two items on that board are doing almost all of the damage, and the burger is not one of them.</p>

<h2 id="numbers">The numbers that matter</h2>
<p>In-N-Out publishes its nutrition information, which is more than a lot of chains do. Here is the short version for the items people actually order.</p>
<ul>
  <li><strong>Hamburger:</strong> about 360 calories</li>
  <li><strong>Cheeseburger:</strong> about 480 calories</li>
  <li><strong>Double-Double:</strong> about 610 calories, 34 g protein</li>
  <li><strong>Fries, regular:</strong> about 360 calories, 6 g protein</li>
</ul>
<p>Look at the last two lines together, because that is the whole article. A Double-Double gives you 34 grams of protein for 610 calories. A regular order of fries gives you 6 grams for 360. One of those is food. The other is a side that costs you most of a meal and leaves you hungry an hour later.</p>
{pullquote("The burger is not your problem. The fries and the shake are your problem.")}

<h2 id="protein-style">Protein Style, and what it actually saves</h2>
<p>Ordering Protein Style swaps the bun for a lettuce wrap. The crew does not blink; roughly everyone orders it at some point.</p>
<p>It takes about 150 calories and close to 30 grams of carbohydrate off any burger on the menu, and the protein does not move. A Double-Double goes from about 610 calories to about 460, and still carries around 30 grams of protein.</p>
{stats([("460 cal", "Double-Double Protein Style"), ("30 g", "protein in it"), ("~150 cal", "saved by dropping the bun")])}
<p>Whether that is worth it depends on you. If you are over 40, training twice a week and trying to hold muscle while losing fat, 30 grams of protein for 460 calories is a genuinely good meal. If you are not in a deficit and you like the bun, eat the bun. The lettuce wrap is a tool, not a virtue.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Double-Double, Protein Style, no spread, mustard and ketchup instead.</strong> About 460 calories before the swap, and the sauce change takes off another 50 to 60. Over 30 grams of protein. This is the order.</li>
  <li><strong>Cheeseburger Protein Style</strong> if you want something lighter. Roughly 280 to 330 calories and around 16 to 19 grams of protein.</li>
  <li><strong>Skip the fries, or share one order.</strong> Not because fries are evil, but because 360 calories buys you almost no protein and no fullness. If you want them, they are the thing to spend on, not an automatic add.</li>
  <li><strong>Water or a diet drink.</strong> A shake is the single biggest number on the board and it is liquid, which means it does nothing for hunger.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Double-Double Protein Style, mustard and ketchup", "Fries are a choice, not a default", "Drink something with no calories"])}

<h2 id="why">Why I do not tell people to avoid it</h2>
<p>Because they go anyway, and then they feel like they blew it, and then the rest of the day goes with it. That cycle costs far more than a burger.</p>
<p>What actually moves the needle for the adults I coach is being able to eat at the places their family already goes and still land near their protein target. In-N-Out is one of the easiest places in Orange County to do that. Chipotle and Chick-fil-A are the other two.</p>
<p>If you want the broader version of this, I wrote <a href="/high-protein-fast-food-after-40">a guide to high-protein fast food after 40</a>, and <a href="/eat-out-lose-fat">a free restaurant playbook</a> you can keep on your phone. If protein is the thing you keep missing, start with <a href="/how-much-protein-after-40">how much you actually need</a>.</p>

<h2 id="caveat">One note on the numbers</h2>
<p>Nutrition aggregator sites disagree about In-N-Out by 20 to 60 calories on several items, usually because they are guessing at the spread or at a Protein Style build. I have used In-N-Out's own published figures here and rounded. Check the current chart in store or on their site if you are tracking closely, because menus and recipes change and this page will not update itself.</p>
<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/chipotle-after-40">Chipotle</a>: 81 g of protein, or 1,400 calories</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li></ul>
<p>All of them follow the same idea: find the protein, spot the one item doing the damage, and order so you are not the person at the table eating differently from everyone else.</p>

{CTA}"""

faqs = [
    ("What is the healthiest thing to order at In-N-Out?",
     "A Double-Double Protein Style with mustard and ketchup instead of spread. It comes in around 400 to 460 calories with over 30 grams of protein, which is a solid meal for anyone trying to hold muscle while losing fat."),
    ("How many calories does Protein Style save?",
     "About 150 calories and close to 30 grams of carbohydrate on any burger on the menu, because the bun is doing almost all of that work. The protein stays the same."),
    ("How much protein is in a Double-Double?",
     "About 34 grams in the standard version and about 30 grams Protein Style. That is a full meal's worth of protein for most adults."),
    ("Are In-N-Out fries bad for you?",
     "They are not bad for you, they are just a poor trade. A regular order is about 360 calories and gives you 6 grams of protein, so it costs most of a meal and does very little for fullness. Share one, or spend those calories on the burger."),
    ("Can I eat fast food and still lose fat after 40?",
     "Yes, if the meals you build hit your protein target and fit your calories. The clients who do best are not the ones who avoid restaurants, they are the ones who have three or four orders they can make anywhere without thinking about it."),
]

html = page(
    SLUG,
    "In-N-Out After 40: What to Order | Fig Performance",
    "What to order at In-N-Out if you are over 40 and trying to lose fat: Protein Style numbers, the Double-Double, and why the fries cost more than the burger.",
    "In-N-Out After 40: What to Order",
    "Fitness after 40", "I tell my clients to eat at In-N-Out.",
    "The burger is not what is keeping you heavy. Two other items on the board are.",
    [("numbers", "The numbers that matter"), ("protein-style", "What Protein Style saves"),
     ("order", "What I would order"), ("why", "Why I do not say avoid it"), ("caveat", "A note on the numbers")],
    body, faqs, "In-N-Out after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
