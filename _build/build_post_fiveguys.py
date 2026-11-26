"""Article: Five Guys after 40. DRAFT Nov 25 2026. Standing approval, restaurant cluster.

Dave has NOTHING on Five Guys.

SOURCING. Five Guys toppings are free and unlimited, which is why calorie figures
split: the Little Hamburger reads 480 at some sources and 540 at others, and one
states outright that 480 is "without heavy toppings". Protein (23 g) and sodium
(380 mg) agree across four sources, so those are stated firmly and calories are
given as a range with the reason.

Firmly sourced (2+ agreeing): Bunless Little Hamburger 220 cal / 16 g / 50 mg.
Bunless Hamburger 440 cal / 32 g / 100 mg. Bun adds about 240 cal and ~35-39 g carbs.
Five Guys serves any sandwich as a bowl or lettuce wrap.

NOT stated as fact: the regular fries figure. Only one source gave a hard number
(953 cal), so the page describes the fries as large without quoting a figure.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "five-guys-after-40"

body = f"""<p class="legal-intro">A bunless hamburger at Five Guys is about 440 calories with roughly 32 grams of protein and around 100 mg of sodium. That last number is lower than almost anything else in these guides, and most people have no idea, because they have never thought of Five Guys as anything other than the place with the enormous fries.</p>

<h2 id="bun">The bun is 240 calories and they will leave it off</h2>
<p>Five Guys will build any sandwich as a bowl or wrapped in lettuce, and they are unusually good at it. The bun is worth about 240 calories and somewhere around 35 to 39 grams of carbohydrate.</p>
<ul>
  <li><strong>Bunless Hamburger:</strong> about 440 calories, roughly 32 g protein, around 100 mg sodium</li>
  <li><strong>Bunless Little Hamburger:</strong> about 220 calories, roughly 16 g protein, around 50 mg sodium</li>
</ul>
<p>Sixteen grams of protein for 220 calories and 50 mg of salt is a better profile than most things people pack in a lunch box, and it comes off a flat-top in a burger restaurant.</p>
{stats([("240 cal", "the bun"), ("440 cal", "bunless hamburger"), ("100 mg", "sodium in it")])}

<h2 id="little">Little means one patty, not a small burger</h2>
<p>This is the thing people get wrong at the counter. A "Little" Hamburger is not a smaller burger, it is a <em>single patty</em> burger. The regular Hamburger comes with two.</p>
<ul>
  <li><strong>Little Hamburger:</strong> roughly 480 to 540 calories, about 23 g protein, around 380 mg sodium</li>
  <li><strong>Hamburger (two patties):</strong> roughly 700 to 840 calories, about 39 g protein, around 430 mg sodium</li>
</ul>
<p>One patty is about 300 calories and 16 grams of protein. If you are ordering out of habit rather than hunger, Little is almost always the right call.</p>

<h2 id="sodium">The surprise: this is a low sodium restaurant</h2>
<p>Five Guys burgers run around 380 to 430 mg of sodium. Bunless they drop to 50 to 100. Compare that with a Jersey Mike's regular sub reaching toward 3,530 mg, a Del Taco Epic burrito at 3,130, or a Panera bread bowl near 2,170.</p>
<p>If a doctor has talked to you about blood pressure, Five Guys is a far better place to end up than its reputation suggests. The fat and the calories are real. The salt is not the issue here.</p>
{pullquote("A bunless Five Guys burger has less sodium than most things in your own refrigerator.")}

<h2 id="fries">The fries are the entire problem</h2>
<p>I am not going to put a number on them, because the published figures vary and a Five Guys fry order is famously not a standard portion. What I will tell you is that a regular order is one of the largest single servings of fries in American fast food, frequently reported at somewhere near a thousand calories, and that it is routinely more than the burger it came with.</p>
<p>Order the smallest size they have, or skip them, or split one. The burger is not what makes this restaurant expensive in calories.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Bunless hamburger or a burger bowl.</strong> About 440 calories, roughly 32 g protein, very low sodium.</li>
  <li><strong>Pile on the free vegetables.</strong> Lettuce, tomato, grilled onions, grilled mushrooms, peppers. All free, all basically no calories.</li>
  <li><strong>Little, not regular,</strong> if you want the bun. One patty instead of two.</li>
  <li><strong>Sort out the fries before you order,</strong> not after they arrive. That decision is the meal.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Bunless or bowl: the bun is about 240 calories", "Little means one patty, not a small burger", "The fries are bigger than the burger"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because Five Guys has a reputation as the indulgent choice, and half of that reputation is earned by the fries alone. The burger underneath is grilled beef with free vegetables and almost no salt. Take the bun off and it is one of the cleaner things you can order in a strip mall.</p>
<p>The clients who struggle are not the ones who go to Five Guys. They are the ones who go and order on autopilot, which here means two patties, a bun and a bag of fries bigger than the sandwich.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>Five Guys toppings are free and unlimited, which is exactly why published calorie figures for the same burger disagree. The Little Hamburger appears at 480 calories at some sources and 540 at others, and one states plainly that the lower figure is without heavy toppings. Protein at about 23 grams and sodium at about 380 mg agree across four independent sources, so those are given firmly and the calories are given as a range. The bunless figures above each come from two sources that agree. The fries are deliberately not quoted, because the published numbers vary and the portion genuinely is not standard.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: lowest sodium meal on this site</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips are about 200 calories for 30 g of protein</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders are 280 calories and 47 g of protein</li><li><a href="/cava-after-40">CAVA</a>: curated bowls are close to a day of salt, so build your own</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: five breaded tenders beat the charbroiled sandwich at the same calories</li><li><a href="/dunkin-after-40">Dunkin</a>: the Wake-Up Wrap is 7 to 8 g of protein, which is a snack</li><li><a href="/wingstop-after-40">Wingstop</a>: six plain wings are 540 calories and 60 g of protein</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap Charburger is 290 calories against 470 to 520 on a bun</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("Can you order a burger without the bun at Five Guys?",
     "Yes. They will serve any sandwich as a bowl or wrapped in lettuce, and they do it well. The bun is worth about 240 calories and roughly 35 to 39 grams of carbohydrate, so it is a meaningful saving for one sentence at the counter."),
    ("How much protein is in a Five Guys burger?",
     "A Little Hamburger, which is one patty, has about 23 grams. The regular Hamburger has two patties and about 39 grams. A bunless hamburger is roughly 440 calories with about 32 grams of protein."),
    ("What is the difference between a Little Hamburger and a Hamburger at Five Guys?",
     "The number of patties, not the size of the burger. Little means one patty, regular means two. That is roughly a 300 calorie difference for about 16 grams of protein."),
    ("Is Five Guys high in sodium?",
     "No, and this surprises people. The burgers run around 380 to 430 mg, and bunless they drop to roughly 50 to 100 mg. That is far below a Jersey Mike's sub, a Del Taco Epic burrito or a Panera bread bowl. The calories are real at Five Guys, but the salt is not the problem."),
    ("Can I eat Five Guys on a diet?",
     "Yes, if you handle the fries. A bunless burger with free vegetable toppings is around 440 calories and roughly 32 grams of protein. A regular order of fries is one of the largest in American fast food and is usually bigger than the burger, so decide about it before you order rather than after it arrives."),
]

html = page(
    SLUG,
    "Five Guys After 40: What to Order | Fig Performance",
    "What to order at Five Guys after 40: a bunless burger is 440 calories with 32g of protein and only 100mg of sodium. The fries are the real problem.",
    "Five Guys After 40: What to Order",
    "Fitness after 40", "How to get 32 grams of protein at Five Guys for 440 calories and almost no salt.",
    "Take the bun off. They do it well, and the bun is 240 calories.",
    [("bun", "The bun is 240 calories"), ("little", "Little means one patty"), ("sodium", "A low sodium restaurant"),
     ("fries", "The fries are the problem"), ("order", "What I would order"),
     ("why", "Why it is on the list"), ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "Five Guys after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
