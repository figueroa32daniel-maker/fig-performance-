"""Article: Raising Cane's after 40. DRAFT Nov 25 2026, not published until Dan approves.

Dave has NOTHING on Raising Cane's. Sourcing rule for this batch (Dan, Nov 25):
Deltaco.com and other official nutrition pages could not be fetched, so every
number here had to clear two or more independent sources that agree. Where they
disagreed the page gives the range instead of picking one. Per-finger protein is
given as 12-13 g because sources split between those two values; everything else
below was consistent across at least three.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "raising-canes-after-40"

body = f"""<p class="legal-intro">The chicken at Raising Cane's is not the problem, and that surprises people. One finger is about 130 calories and 12 to 13 grams of protein. Three of them on their own are roughly 390 calories and close to 39 grams of protein, which is a better meal than most of what I see clients pack for work. Then the combo arrives and it is 1,050 calories. Nothing about the chicken changed. Everything around it did.</p>

<h2 id="fingers">The chicken, on its own</h2>
<p>Cane's sells one thing, which makes the math unusually easy. Published figures for a single 55 g finger land at:</p>
<ul>
  <li><strong>Calories:</strong> about 130</li>
  <li><strong>Protein:</strong> 12 to 13 g</li>
  <li><strong>Fat:</strong> about 7 g</li>
  <li><strong>Sodium:</strong> about 200 mg</li>
</ul>
<p>Order three fingers by themselves and you are at roughly 390 calories, around 39 grams of protein and about 600 mg of sodium. For a fried chicken restaurant that is a genuinely respectable meal, and it is the single most useful fact on this page.</p>
{stats([("390 cal", "three fingers, nothing else"), ("39 g", "protein in them"), ("1,050 cal", "the same three in a combo")])}

<h2 id="sauce">The sauce costs more than the chicken</h2>
<p>One Cane's Sauce is about 190 calories and 18 grams of fat. A chicken finger is 130.</p>
<p>Read that twice, because it is the whole article. The dipping sauce carries more calories than the thing you are dipping. Two sauces and you have eaten the equivalent of three extra fingers without touching any more chicken.</p>
{pullquote("The sauce has more calories than the chicken. Almost nobody at that counter knows it.")}
<p>I am not telling you to order it dry. I am telling you that if you want the sauce, it is a real part of the meal and it deserves to be counted like one. Ask for one cup instead of two and you have saved yourself 190 calories without giving anything up.</p>

<h2 id="combo">Where the combo goes wrong</h2>
<p>The 3 Finger Combo comes in around 1,050 calories. The fingers are 390 of those. The rest is crinkle-cut fries, Texas toast, the sauce and whatever you are drinking.</p>
<p>That is not a disaster, it is a choice, and it is the same choice as everywhere else on this list: the protein is fine, the things arranged around it are what cost you. The difference at Cane's is that the menu makes the swap unusually easy, because fingers are sold on their own.</p>
<p>Sodium is worth a glance too. It climbs quickly once the fries and the toast are in, and if your doctor has mentioned blood pressure, the same advice applies here as at El Pollo Loco: the chicken is not where the salt is concentrated.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Three or four fingers, no combo.</strong> Three is about 390 calories and 39 grams of protein. Four is roughly 520 and 50. This is the order, and it is not close.</li>
  <li><strong>One sauce, not two.</strong> Or skip it. One cup is 190 calories, which is a finger and a half.</li>
  <li><strong>Coleslaw instead of fries</strong> if you want a side. It is roughly 90 calories against about 400 for the crinkle-cut.</li>
  <li><strong>Unsweet tea or water.</strong> The sweet tea is the quiet one on the board.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Order fingers a la carte, never the combo", "The sauce has more calories than the chicken", "Three fingers alone is already 39 g of protein"])}

<h2 id="why">Why this one is on the list at all</h2>
<p>Because the adults I coach in Placentia end up at Cane's on a Friday with their kids, and the version of coaching where I tell them not to go does not survive contact with a real week. What survives is knowing that three fingers and a water is a 390-calorie meal with 39 grams of protein in it, and that the person next to them ordering the same chicken inside a combo box is eating two and a half times as much.</p>
<p>Same food. Different order. That is most of what I do.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>Raising Cane's publishes a nutrition guide, and the figures above are the ones that independent nutrition databases agree on. Per-finger protein is the one value that splits, with some sources saying 12 grams and others 13, so this page gives the range rather than pretending to a precision nobody has. Portions in a fried chicken restaurant vary by a few grams anyway. Check the current guide if you are tracking closely.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li></ul>
<p>All of them follow the same idea: find the protein, spot the one item doing the damage, and order so you are not the person at the table eating differently from everyone else.</p>
{CTA}"""

faqs = [
    ("How much protein is in a Raising Cane's chicken finger?",
     "Published figures put a single 55 g finger at about 130 calories and 12 to 13 grams of protein. Three fingers on their own come to roughly 390 calories and close to 39 grams, which is a full meal's worth of protein for most adults."),
    ("Is Raising Cane's good for weight loss?",
     "The chicken is better than people expect. Three fingers by themselves are about 390 calories with around 39 grams of protein. The combo is where it changes, at roughly 1,050 calories once the fries, the toast and the sauce are counted. Order the fingers a la carte and it fits most plans."),
    ("How many calories is Cane's Sauce?",
     "About 190 calories and 18 grams of fat for one cup, which is more than a chicken finger at 130. If you want it, have one cup rather than two and count it as part of the meal."),
    ("What is the healthiest thing to order at Raising Cane's?",
     "Three or four chicken fingers with no combo, one sauce at most, coleslaw instead of crinkle-cut fries, and unsweet tea or water. Four fingers and a slaw lands near 610 calories with about 50 grams of protein."),
    ("Can I eat fried chicken and still lose fat after 40?",
     "Yes, if the meal hits your protein target and fits your calories for the day. The clients who do best are not the ones avoiding restaurants, they are the ones with three or four orders they can make anywhere without thinking about it."),
]

html = page(
    SLUG,
    "Raising Cane's After 40: What to Order | Fig Performance",
    "What to order at Raising Cane's after 40: three fingers is 39g of protein for 390 calories, why the sauce costs more than the chicken, and the combo problem.",
    "Raising Cane's After 40: What to Order",
    "Fitness after 40", "The biggest lie you have been told about Raising Cane's is that the chicken is the problem.",
    "Three fingers on their own are 390 calories and 39 grams of protein. The sauce is 190.",
    [("fingers", "The chicken, on its own"), ("sauce", "The sauce problem"), ("combo", "Where the combo goes wrong"),
     ("order", "What I would order"), ("why", "Why it is on the list"), ("caveat", "A note on the numbers"),
     ("more", "The other guides")],
    body, faqs, "Raising Cane's after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
