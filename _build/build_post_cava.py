"""Article: CAVA after 40. DRAFT Nov 25 2026. Standing approval, restaurant cluster.

Dave has NOTHING on CAVA.

SOURCING: strong. Six independent sources give Grilled Chicken at 250 cal / 28 g /
13 g fat / 3 g carbs / 670 mg sodium. One outlier claims 33 g protein; discarded,
six against one.

THE STORY: CAVA has a Panera-style health halo. Its CURATED (pre-designed) bowls
run 1,670-2,210 mg sodium against a 2,300 mg daily value, i.e. nearly a full day in
one bowl. Building your own off a greens base is 395 cal / 37 g / 1,045 mg. Also:
grilled STEAK carries about 390 mg less sodium than the chicken, which is genuinely
counterintuitive, and falafel is 350 cal for only 6 g protein.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "cava-after-40"

body = f"""<p class="legal-intro">CAVA's curated bowls, the pre-designed ones on the board with names, run somewhere between about 1,670 and 2,210 mg of sodium each. The daily value is 2,300. So the healthy-looking Mediterranean bowl you ordered because it was not a burger is most of a day's salt in one sitting. Build the same bowl yourself and you can get the same protein for roughly half of that.</p>

<h2 id="curated">The curated bowls are the trap</h2>
<p>This is a restaurant where the pre-built option is worse than the one you assemble, and that is unusual. Curated bowls land roughly between 580 and 860 calories, and every single one of them sits in that 1,670 to 2,210 mg sodium band.</p>
<p>A bowl you build yourself, greens base with grilled chicken, hummus, tzatziki and a light dressing, comes to about 395 calories with roughly 37 grams of protein and around 1,045 mg of sodium. Same restaurant, same ingredients, half the salt.</p>
{stats([("1,670-2,210 mg", "sodium, curated bowls"), ("~1,045 mg", "the bowl you build"), ("2,300 mg", "a full day")])}

<h2 id="chicken">The grilled chicken is the anchor</h2>
<p>Six independent nutrition sources agree on this one, which is rare:</p>
<ul>
  <li><strong>Grilled Chicken:</strong> 250 calories, 28 g protein, 13 g fat, 3 g carbs, 670 mg sodium</li>
  <li><strong>Grilled Steak:</strong> about 170 calories, roughly 23 g protein</li>
  <li><strong>Power Greens base:</strong> about 30 calories, 2 g protein, 35 mg sodium</li>
</ul>
<p>A greens base costs you almost nothing in calories or salt, which is exactly what you want it to do. It leaves the whole budget for protein.</p>

<h2 id="steak">The counterintuitive one: steak is lower sodium than chicken</h2>
<p>CAVA's grilled steak carries roughly 390 mg less sodium than its grilled chicken. Nobody expects that. A SuperGreens bowl with grilled steak and tzatziki lands near 235 calories with about 28 grams of protein and only around 375 mg of sodium.</p>
<p>If blood pressure is the thing you are managing rather than calories, steak is the better order here, and that sentence is true at almost no other restaurant in these guides.</p>
{pullquote("The pre-made bowl is the problem. At most places it is the opposite.")}

<h2 id="falafel">Falafel is not a protein</h2>
<p>A serving of falafel is about 350 calories with roughly 6 grams of protein and around 810 mg of sodium. It is chickpeas, but it is fried chickpeas, and six grams is not a meal's worth of anything.</p>
<p>If you are eating vegetarian here, the falafel is the item that feels like the protein and is not. Build around the dips and the greens instead, and know that you are eating a carbohydrate dish.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Build your own, never curated.</strong> Greens base, grilled protein, two dips, light dressing. Roughly 395 calories and 37 g of protein.</li>
  <li><strong>Double grilled chicken</strong> if you want the protein high. That lands near 500 calories for about 56 g, though it also pushes sodium toward 1,340 mg.</li>
  <li><strong>Grilled steak instead of chicken</strong> if sodium is your priority. About 390 mg less.</li>
  <li><strong>Greens base, not grains,</strong> unless you have earned the carbs. The base is where the calories hide.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Never order a curated bowl, build your own", "Grilled chicken: 250 cal and 28 g protein", "Falafel is 350 cal for 6 g of protein"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because CAVA is where people go when they have decided to be good, the same way they go to Panera. And like Panera, the place is fine and the default order is not. The difference is that here the fix is completely free: walk past the board with the named bowls and build the thing yourself.</p>
<p>Thirty-seven grams of protein for under 400 calories is a very good lunch. You just have to not order the one with the name on it.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>Six independent nutrition breakdowns give CAVA's grilled chicken identically at 250 calories, 28 grams of protein and 670 mg of sodium, which is unusually strong agreement. One source claims 33 grams of protein for the same item; six against one, so this page uses 28. Built-bowl figures depend entirely on what goes in the bowl, so the numbers above describe the specific builds named rather than any bowl you make. Portions vary with whoever is serving. Check CAVA's own nutrition calculator if you are tracking closely.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: lowest sodium meal on this site</li><li><a href="/five-guys-after-40">Five Guys</a>: bunless is 440 calories and almost no salt</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips, 200 calories and 30 g</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders, 280 calories and 47 g</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: five breaded tenders beat the charbroiled sandwich at the same calories</li><li><a href="/dunkin-after-40">Dunkin</a>: the Wake-Up Wrap is 7 to 8 g of protein, which is a snack</li><li><a href="/wingstop-after-40">Wingstop</a>: six plain wings are 540 calories and 60 g of protein</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap Charburger is 290 calories against 470 to 520 on a bun</li><li><a href="/rubios-after-40">Rubio's</a>: the Original Fish Taco is 9 g of protein for 330 calories</li><li><a href="/mcdonalds-after-40">McDonald's</a>: the McDouble is 390 calories and 22 g protein, beating the Big Mac</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("Is CAVA healthy?",
     "It can be, but the default is not. CAVA's curated bowls run between roughly 1,670 and 2,210 mg of sodium each, against a 2,300 mg daily value. A bowl you build yourself off a greens base with grilled chicken and two dips is about 395 calories with roughly 37 grams of protein and around 1,045 mg of sodium."),
    ("How much protein is in CAVA grilled chicken?",
     "28 grams for 250 calories, with 13 g of fat and 670 mg of sodium. Six independent nutrition sources agree on that figure, which makes it one of the more reliable numbers in these guides."),
    ("Should I order a curated bowl or build my own at CAVA?",
     "Build your own. The curated bowls are the pre-designed ones on the menu board, and every one of them sits in the 1,670 to 2,210 mg sodium range. Building the same ingredients yourself gets similar protein for roughly half the salt."),
    ("Is falafel a good protein at CAVA?",
     "No. A serving is about 350 calories with roughly 6 grams of protein and around 810 mg of sodium. It is fried chickpeas. It feels like the protein in a vegetarian order and it is not."),
    ("What is the lowest sodium order at CAVA?",
     "A SuperGreens base with grilled steak and tzatziki, which lands near 235 calories with about 28 grams of protein and only around 375 mg of sodium. CAVA's steak carries roughly 390 mg less sodium than its chicken, which surprises most people."),
]

html = page(
    SLUG,
    "CAVA After 40: What to Order | Fig Performance",
    "What to order at CAVA after 40: the curated bowls are close to a day of sodium, and building your own gets 37g of protein for under 400 calories.",
    "CAVA After 40: What to Order",
    "Fitness after 40", "Stop ordering the curated bowls at CAVA. Each one is close to a day of salt.",
    "Build it yourself and get the same protein for about half the sodium.",
    [("curated", "The curated bowls are the trap"), ("chicken", "The grilled chicken"),
     ("steak", "Steak is lower sodium than chicken"), ("falafel", "Falafel is not a protein"),
     ("order", "What I would order"), ("why", "Why it is on the list"),
     ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "CAVA after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
