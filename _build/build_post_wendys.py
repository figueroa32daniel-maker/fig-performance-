"""Article: Wendy's after 40. DRAFT Nov 25 2026. Standing approval. Head-to-head (Dave has 1).

SOURCING: good. Grilled Chicken Sandwich clusters at 350-370 cal with 33-35 g
protein and 810-880 mg sodium across six sources. Small chili at 240-280 cal with
15-17 g protein across three.

DISCARDED: a Grilled Barbecue Chicken Sandwich entry from a page 1,815 days old
(2021). Date-check rule.

THE STORY: the chili. Almost no fast food chain has a SIDE with real protein in it.
Wendy's small chili is 15-17 g for 240-280 cal, which turns the grilled chicken
sandwich into a 51 g meal for about 610 calories.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "wendys-after-40"

body = f"""<p class="legal-intro">A grilled chicken sandwich and a small chili at Wendy's comes to about 610 calories with roughly 51 grams of protein. The reason that works is the chili, and the chili is the single most unusual thing on any menu in these guides: a fast food side dish with real protein in it. Everywhere else, the side is fries.</p>

<h2 id="chili">The chili is the whole point</h2>
<p>A small chili runs somewhere around 240 to 280 calories with roughly 15 to 17 grams of protein and real fiber. Compare that with the side it is competing against at every other restaurant on this site:</p>
<ul>
  <li><strong>Wendy's small chili:</strong> about 240 to 280 calories, roughly 15 to 17 g protein</li>
  <li><strong>A medium order of fries, anywhere:</strong> 350 to 500 calories, roughly 4 to 6 g protein</li>
</ul>
<p>Swapping one for the other is worth something like ten grams of protein and a hundred-odd calories in the same transaction. There is no other chain in these twenty-odd guides where the side order can do that.</p>
{stats([("610 cal", "sandwich plus chili"), ("51 g", "protein in it"), ("~16 g", "from the chili alone")])}

<h2 id="grilled">The grilled chicken sandwich</h2>
<ul>
  <li><strong>Grilled Chicken Sandwich:</strong> about 350 to 370 calories, roughly 33 to 35 g protein, around 810 to 880 mg sodium</li>
  <li><strong>Spicy Chicken Sandwich:</strong> about 490 to 510 calories, roughly 28 to 29 g protein</li>
  <li><strong>Classic Chicken Sandwich:</strong> about 490 calories, roughly 28 g protein</li>
</ul>
<p>Grilled is around 120 to 140 calories lighter than the breaded versions and carries five to seven more grams of protein. It costs about fifty cents more, which is the only fast food upgrade in this entire series where paying more gets you a better number.</p>
{pullquote("A side dish with sixteen grams of protein in it. No other chain on this site has one.")}

<h2 id="baconator">What the other end looks like</h2>
<p>A Baconator is around 960 calories with roughly 57 grams of protein and about 1,960 mg of sodium. Son of Baconator is around 670 with about 38 grams and 1,670 mg.</p>
<p>The protein is genuinely high, which is what makes these tempting to someone tracking macros. The sodium is the reason I would not: nearly 2,000 mg in one sandwich is most of a day, and the grilled chicken and chili route gets you to 51 grams for 350 fewer calories.</p>

<h2 id="sodium">Sodium runs high here</h2>
<p>Even the good order is not low. Grilled chicken plus small chili lands near 1,720 mg, because both items carry salt. That is the honest trade at this restaurant: the protein arithmetic is excellent and the sodium arithmetic is not.</p>
<p>If blood pressure is your main concern, the sandwich alone at roughly 810 to 880 mg is the better call, and Flame Broiler or Five Guys are better buildings entirely.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Grilled chicken sandwich and a small chili.</strong> About 610 calories, roughly 51 g of protein.</li>
  <li><strong>Chili instead of fries,</strong> always. Ten more grams of protein for fewer calories.</li>
  <li><strong>Grilled over spicy or classic.</strong> Lighter and more protein, for about fifty cents.</li>
  <li><strong>Skip the Baconator</strong> unless you have budgeted roughly 2,000 mg of sodium for it.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Small chili: about 16 g of protein, unique among fast food sides", "Grilled chicken sandwich: 350-370 cal and 33-35 g", "Together, roughly 51 g for about 610 calories"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because the side order is the decision nobody makes consciously. At every other restaurant in these guides the side is the thing quietly ruining the meal, and the advice is always some version of skip it. Wendy's is the one place where the side can improve the order instead.</p>
<p>That is worth knowing on a Tuesday when you are tired and the drive-through is the plan.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>Six independent sources put the Grilled Chicken Sandwich between 350 and 370 calories with 33 to 35 grams of protein and 810 to 880 mg of sodium, and the spread is small enough that ranges are given rather than a single figure. Three sources put the small chili between 240 and 280 calories with 15 to 17 grams of protein. One entry for a grilled barbecue chicken sandwich was discarded because the page was last updated roughly five years ago and the item does not appear on current menus.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/mcdonalds-after-40">McDonald's</a>: the McDouble beats the Big Mac</li><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/five-guys-after-40">Five Guys</a>: bunless is 440 calories and almost no salt</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap saves 200 calories</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: the breaded tenders beat the charbroiled sandwich</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders, 280 calories and 47 g</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips, 200 calories and 30 g</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/taco-bell-after-40">Taco Bell</a>: three soft tacos beat the Power Bowl</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/rubios-after-40">Rubio's</a>: the famous fish taco is nine grams</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: lowest sodium meal on this site</li><li><a href="/wingstop-after-40">Wingstop</a>: the flavour swings sodium tenfold</li><li><a href="/cava-after-40">CAVA</a>: the curated bowls are a day of salt</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/dunkin-after-40">Dunkin'</a>: the Wake-Up Wrap is a snack</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/subway-after-40">Subway</a>: a rotisserie chicken bowl is 220 calories and 31 g of protein</li><li><a href="/panda-express-after-40">Panda Express</a>: super greens with teriyaki chicken is 470 calories and 50 g of protein</li><li><a href="/daves-hot-chicken-after-40">Dave's Hot Chicken</a>: one tender is 490 calories, not the 150 your app says</li><li><a href="/portillos-after-40">Portillo's</a>: the dressing adds 340 calories to every salad on the menu</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("How much protein is in Wendy's chili?",
     "A small chili carries roughly 15 to 17 grams of protein at about 240 to 280 calories, plus real fiber. That makes it almost unique among fast food sides, which usually deliver 4 to 6 grams for more calories."),
    ("What is the best high protein order at Wendy's?",
     "A grilled chicken sandwich with a small chili, at about 610 calories with roughly 51 grams of protein. The sandwich alone is 350 to 370 calories with 33 to 35 grams."),
    ("Is Wendy's grilled chicken sandwich better than the spicy one?",
     "Yes, on both counts. Grilled is about 350 to 370 calories with 33 to 35 grams of protein; the spicy and classic versions are near 490 to 510 calories with about 28 to 29 grams. Grilled costs around fifty cents more, which is the rare case where paying more gets you a better number."),
    ("Should I get chili instead of fries at Wendy's?",
     "Yes. A small chili is roughly 16 grams of protein for 240 to 280 calories. A medium fries is 4 to 6 grams for 350 to 500. That swap is worth about ten grams of protein and a hundred calories in the same order."),
    ("Is Wendy's high in sodium?",
     "Yes, and that is the honest trade here. A grilled chicken sandwich with small chili lands near 1,720 mg, and a Baconator is around 1,960 mg on its own. The protein arithmetic at Wendy's is excellent; the sodium arithmetic is not."),
]

html = page(
    SLUG,
    "Wendy's After 40: What to Order | Fig Performance",
    "What to order at Wendy's after 40: the chili is the only fast food side with real protein, and with grilled chicken it is 51g for 610 calories.",
    "Wendy's After 40: What to Order",
    "Fitness after 40", "How to get 51 grams of protein at Wendy's for about 610 calories.",
    "A grilled chicken sandwich and a small chili. The chili is the trick.",
    [("chili", "The chili is the point"), ("grilled", "The grilled sandwich"),
     ("baconator", "The other end"), ("sodium", "Sodium runs high"),
     ("order", "What I would order"), ("why", "Why it is on the list"),
     ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "Wendy's after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
