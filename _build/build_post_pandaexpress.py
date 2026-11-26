"""Article: Panda Express after 40. DRAFT Nov 25 2026. Standing approval. Head-to-head (Dave has 1).

SOURCING: strong. Six sources give Grilled Teriyaki Chicken at 275-280 cal, four
of them identically at 275 cal / 33 g / 470 mg. Protein reads 33, 36 or 38 g
depending on portion size listed (6.0 vs 6.1 oz), so a range is given.
Three sources give standard Teriyaki Chicken at 340 cal / 41 g.

THE STORY: the base decides everything. Super Greens + Teriyaki Chicken is about
470 cal / 50 g protein. Chow Mein + Orange Chicken + Beijing Beef is about 1,580
cal and 2,450 mg sodium. Same restaurant, same visit.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "panda-express-after-40"

body = f"""<p class="legal-intro">Super Greens with Teriyaki Chicken at Panda Express is about 470 calories with roughly 50 grams of protein. Chow Mein with Orange Chicken and Beijing Beef is around 1,580 calories and about 2,450 mg of sodium. Same restaurant, same queue, same thirty seconds at the counter. The base you point at is doing almost all of the work.</p>

<h2 id="base">The base is the decision</h2>
<p>Everything at Panda Express is a base plus one, two or three entrées. The entrées get the attention and the base decides the meal:</p>
<ul>
  <li><strong>Super Greens:</strong> roughly 90 to 180 calories</li>
  <li><strong>Chow Mein or fried rice:</strong> several hundred, and the single biggest line in most orders</li>
</ul>
<p>Choose greens and you have bought yourself room for two entrées. Choose chow mein and one entrée is already most of a meal.</p>
{stats([("470 cal", "greens + teriyaki chicken"), ("50 g", "protein in it"), ("1,580 cal", "the chow mein version")])}

<h2 id="grilled">Grilled Teriyaki Chicken is the best entrée on the board</h2>
<ul>
  <li><strong>Grilled Teriyaki Chicken:</strong> about 275 to 280 calories, roughly 33 to 38 g protein, around 470 to 630 mg sodium</li>
  <li><strong>Teriyaki Chicken (standard):</strong> about 340 calories, roughly 41 g protein</li>
  <li><strong>Orange Chicken:</strong> about 490 to 510 calories, roughly 25 to 26 g protein, around 820 mg sodium</li>
</ul>
<p>Orange Chicken is the top seller in the chain. Grilled Teriyaki Chicken gives you more protein than it for roughly half the calories, because one is battered and fried in a sweet sauce and the other is not.</p>
{pullquote("The best-selling item gives you half the protein per calorie of the one next to it.")}

<h2 id="others">The other useful entrées</h2>
<ul>
  <li><strong>String Bean Chicken Breast:</strong> about 190 to 210 calories, roughly 12 to 15 g protein, and among the lowest sodium entrées</li>
  <li><strong>Broccoli Beef:</strong> about 150 calories</li>
  <li><strong>Mushroom Chicken:</strong> about 180 calories, roughly 13 g protein</li>
</ul>
<p>These are the light ones rather than the high protein ones. They are useful as a second entrée beside grilled teriyaki chicken, not as the main event.</p>

<h2 id="sodium">Sodium stacks fast here</h2>
<p>Individually most entrées are reasonable, with grilled teriyaki chicken around 470 to 630 mg. The problem is that a plate is two or three of them on a base, and the sauced items carry considerably more. A plate built from fried items and chow mein can reach roughly 2,450 mg, which is a full day in one lunch.</p>
<p>The same rule as everywhere else on this site: it is not the protein, it is the sauce and the carbohydrate it is sitting on.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Super Greens base, Grilled Teriyaki Chicken.</strong> Around 470 calories and roughly 50 g of protein if you double the entrée.</li>
  <li><strong>Grilled Teriyaki Chicken over Orange Chicken,</strong> every time. More protein, half the calories.</li>
  <li><strong>Add String Bean Chicken or Broccoli Beef</strong> as the second entrée rather than another fried one.</li>
  <li><strong>Skip the chow mein and fried rice</strong> unless you have budgeted for them. They are the meal, not the side.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Super Greens base, not chow mein or fried rice", "Grilled Teriyaki Chicken: about 275 cal and 33 g protein", "Orange Chicken is double the calories for less protein"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because this is one of the few fast food menus where you assemble the meal yourself, which means the arithmetic is in your hands and nobody ever tells you that. People order Orange Chicken on chow mein out of pure habit, and the identical visit with greens and grilled teriyaki chicken is a third of the calories with twice the protein.</p>
<p>Fifty grams of protein for 470 calories is a good day's lunch anywhere. That it is available in a food court is the useful part.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>Six independent sources give Grilled Teriyaki Chicken between 275 and 280 calories, with four agreeing exactly on 275 calories, 33 grams of protein and 470 mg of sodium. The protein figure reads 33, 36 or 38 grams depending on whether the source lists a 6.0 or 6.1 ounce portion, which is why a range is given rather than a single number. Three sources agree the standard Teriyaki Chicken is around 340 calories with 41 grams. Plate totals depend entirely on what you put on them, so the combinations quoted above describe those specific builds.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/cava-after-40">CAVA</a>: the curated bowls are a day of salt</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: lowest sodium meal on this site</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders, 280 calories and 47 g</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/mcdonalds-after-40">McDonald's</a>: the McDouble beats the Big Mac</li><li><a href="/wendys-after-40">Wendy's</a>: the chili is the only side worth having</li><li><a href="/taco-bell-after-40">Taco Bell</a>: three soft tacos beat the Power Bowl</li><li><a href="/subway-after-40">Subway</a>: the best thing there has no bread in it</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/rubios-after-40">Rubio's</a>: the famous fish taco is nine grams</li><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/five-guys-after-40">Five Guys</a>: bunless is 440 calories and almost no salt</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap saves 200 calories</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: the breaded tenders beat the charbroiled sandwich</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips, 200 calories and 30 g</li><li><a href="/wingstop-after-40">Wingstop</a>: the flavour swings sodium tenfold</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/dunkin-after-40">Dunkin'</a>: the Wake-Up Wrap is a snack</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/daves-hot-chicken-after-40">Dave's Hot Chicken</a>: one tender is 490 calories, not the 150 your app says</li><li><a href="/portillos-after-40">Portillo's</a>: the dressing adds 340 calories to every salad on the menu</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("What is the highest protein item at Panda Express?",
     "Grilled Teriyaki Chicken, at about 275 to 280 calories with roughly 33 to 38 grams of protein. The standard Teriyaki Chicken carries slightly more protein at around 41 grams, but for 340 calories."),
    ("Is Orange Chicken bad at Panda Express?",
     "It is the worst protein-per-calorie entrée among the popular ones. Orange Chicken is about 490 to 510 calories for roughly 25 to 26 grams of protein. Grilled Teriyaki Chicken gives you more protein for roughly half the calories, because one is battered and fried in a sweet sauce and the other is grilled."),
    ("What is the healthiest thing to order at Panda Express?",
     "A Super Greens base with Grilled Teriyaki Chicken. That combination comes to around 470 calories with roughly 50 grams of protein if you double the entrée. The base is the decision that matters most on this menu."),
    ("How much sodium is in a Panda Express plate?",
     "It depends entirely on the build. Individual entrées are reasonable, with grilled teriyaki chicken around 470 to 630 mg. A plate of fried items on chow mein can reach roughly 2,450 mg, which is a full day's worth in one lunch."),
    ("Should I get chow mein or super greens?",
     "Super Greens, at roughly 90 to 180 calories against several hundred for chow mein or fried rice. Choosing greens buys you room for a second entrée, which is where the protein comes from."),
]

html = page(
    SLUG,
    "Panda Express After 40: What to Order | Fig Performance",
    "What to order at Panda Express after 40: super greens with teriyaki chicken is about 470 calories and 50g of protein. The base is the whole decision.",
    "Panda Express After 40: What to Order",
    "Fitness after 40", "How to get 50 grams of protein at Panda Express for about 470 calories.",
    "Super greens, not chow mein. The base you point at decides the meal.",
    [("base", "The base is the decision"), ("grilled", "Grilled teriyaki chicken"),
     ("others", "The other useful entrees"), ("sodium", "Sodium stacks fast"),
     ("order", "What I would order"), ("why", "Why it is on the list"),
     ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "Panda Express after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
