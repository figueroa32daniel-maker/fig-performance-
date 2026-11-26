"""Article: Del Taco after 40. DRAFT Nov 25 2026, not published until Dan approves.

Dave has NOTHING on Del Taco. SOURCE NOTE: unlike the rest of batch 2, this one is
built on Del Taco's OWN published list, "DEL TACO MENU ITEMS - NUTRITIONAL LIST
(November 2026)", page 1 of 4, which Dan pulled up on deltaco.com and sent as a
screen recording. That is why this page quotes exact figures instead of ranges.

It also settles the disagreement that got Del Taco parked in the first place: third
party databases variously claimed 11, 13 and 14 g protein for the Grilled Chicken
Taco. The official list says 11 g. The highest claims were wrong.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "del-taco-after-40"

body = f"""<p class="legal-intro">Three Grilled Chicken Street Tacos at Del Taco are 330 calories, 27 grams of protein and 900 mg of sodium. The Taco Salad with Fresh Guac and grilled chicken is 420 calories, 26 grams of protein and 1,270 mg of sodium. The tacos win on all three counts. They are cheaper too. Yet the salad is what people order when they are trying to be good, because it is a salad.</p>

<h2 id="street-taco">The best item on the menu is the smallest one</h2>
<p>From Del Taco's own November 2026 nutritional list, a single Grilled Chicken Street Taco is:</p>
<ul>
  <li><strong>110 calories</strong></li>
  <li><strong>9 g protein</strong></li>
  <li><strong>3.5 g fat</strong></li>
  <li><strong>300 mg sodium</strong></li>
</ul>
<p>Order three and you are at 330 calories with 27 grams of protein. That is a legitimate meal, built out of the cheapest thing on the board, and it is the order I give clients who tell me their family stops at Del Taco.</p>
{stats([("330 cal", "three street tacos"), ("27 g", "protein in them"), ("900 mg", "sodium, all three")])}

<h2 id="salad">The salad is not the healthy order</h2>
<p>Side by side, grilled chicken both ways:</p>
<ul>
  <li><strong>Three Grilled Chicken Street Tacos:</strong> 330 cal, 27 g protein, 900 mg sodium</li>
  <li><strong>Taco Salad with Fresh Guac, grilled chicken:</strong> 420 cal, 26 g protein, 1,270 mg sodium</li>
</ul>
<p>Ninety more calories, a gram less protein, and nearly 400 mg more sodium. The salad is not a bad item. It is just not the virtuous one, and the gap between how it reads and how it performs is the reason it is in this article.</p>
{pullquote("The tacos beat the salad on calories, on protein and on sodium. The salad just looks like the answer.")}

<h2 id="sodium">Sodium is the real story here</h2>
<p>This is a chain where the calorie column will not scare you but the sodium column should. From the same official list:</p>
<ul>
  <li><strong>Epic Carne Asada Steak Loaded Queso Burrito:</strong> 890 cal, 47 g protein, <strong>3,130 mg sodium</strong></li>
  <li><strong>Epic Grilled Chicken Loaded Queso Burrito:</strong> 860 cal, 43 g protein, 2,770 mg sodium</li>
  <li><strong>Epic Carne Asada Steak Cali Bacon Burrito:</strong> 1,050 cal, 51 g protein, 2,600 mg sodium</li>
  <li><strong>Spicy Grilled Chicken Burrito:</strong> 560 cal, 30 g protein, 1,700 mg sodium</li>
</ul>
<p>The general guidance for an adult is to stay under about 2,300 mg of sodium in a day. One Epic Loaded Queso burrito clears that on its own, before breakfast or dinner. The protein in those burritos is genuinely high, which is exactly what makes them tempting to someone tracking macros, and exactly why the salt is worth saying out loud.</p>

<h2 id="tacos">If you want a taco that is not a street taco</h2>
<p>The grilled chicken options, from the official list:</p>
<ul>
  <li><strong>Grilled Chicken Street Taco:</strong> 110 cal, 9 g protein, 300 mg sodium</li>
  <li><strong>Grilled Chicken Guac'd Up Taco:</strong> 130 cal, 9 g protein, 340 mg sodium</li>
  <li><strong>Grilled Chicken Taco:</strong> 210 cal, 11 g protein, 510 mg sodium</li>
  <li><strong>Grilled Chicken Big Fat Taco:</strong> 340 cal, 16 g protein, 410 mg sodium</li>
</ul>
<p>Note the Guac'd Up: 20 more calories than the street taco for the same protein, and the guacamole is real food. That is a good trade if the street taco leaves you short.</p>
<p>Worth knowing by comparison: the Carnitas Street Taco is 150 calories with 11 g protein and only 240 mg sodium, which is the lowest sodium of any taco on the list. The Carne Asada Steak Street Taco is 120 calories, 10 g protein, 420 mg sodium.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Three Grilled Chicken Street Tacos.</strong> 330 calories, 27 g protein. This is the order.</li>
  <li><strong>Swap one for a Carnitas Street Taco</strong> if you want variety. 11 g of protein and the lowest sodium on the board.</li>
  <li><strong>Skip the Epic burritos</strong> unless you have budgeted the sodium. They are not a calorie problem, they are a salt problem.</li>
  <li><strong>Order in a cup if you want it bowl style.</strong> Del Taco will build a taco or burrito in a cup, which drops the tortilla.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Three grilled chicken street tacos: 330 cal, 27 g protein", "They beat the taco salad on calories, protein and sodium", "One Epic Loaded Queso burrito is more than a day of salt"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because Del Taco is on half the corners in this part of Orange County, it is open when nothing else is, and the item that solves it costs about a dollar fifty. Most of the advice written about this chain is written by people who have never stood in that drive-through at nine at night. Three street tacos and a water is a good decision, and it is available to you every single day without a plan, a prep container or a single ounce of willpower.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>Every figure on this page comes from Del Taco's own published document, "Del Taco Menu Items, Nutritional List, November 2026," read directly rather than through a third party database. That matters more than usual here. Independent nutrition sites disagree about this chain, and for the Grilled Chicken Taco alone they variously report 11, 13 and 14 grams of protein. Del Taco's own list says 11. The higher numbers in circulation are simply wrong, and anyone building a plan on them is overcounting their protein by up to a quarter.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: about 340 mg of sodium in a full bowl, the lowest on this site</li><li><a href="/five-guys-after-40">Five Guys</a>: a bunless burger is 440 calories, 32 g protein and almost no salt</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips are about 200 calories for 30 g of protein</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("How much protein is in a Del Taco grilled chicken taco?",
     "Del Taco's own November 2026 nutritional list puts the Grilled Chicken Taco at 210 calories with 11 grams of protein and 510 mg of sodium. Several third party databases claim 13 or 14 grams, which is higher than the chain's published figure. The Grilled Chicken Street Taco is 110 calories with 9 grams."),
    ("What is the healthiest thing to order at Del Taco?",
     "Three Grilled Chicken Street Tacos, at 330 calories, 27 grams of protein and 900 mg of sodium between them. They beat the Taco Salad with Fresh Guac on all three counts, and they cost less."),
    ("Is the Del Taco taco salad healthy?",
     "It is reasonable, but it is not the best choice on the menu. With grilled chicken it is 420 calories, 26 grams of protein and 1,270 mg of sodium. Three grilled chicken street tacos give you a gram more protein for 90 fewer calories and nearly 400 mg less sodium."),
    ("How much sodium is in a Del Taco Epic burrito?",
     "A lot. The Epic Carne Asada Steak Loaded Queso Burrito is 3,130 mg, and the Epic Grilled Chicken Loaded Queso Burrito is 2,770 mg. General guidance for adults is under roughly 2,300 mg for a whole day, so one of these clears a day's worth by itself."),
    ("Can I eat Del Taco and still lose fat after 40?",
     "Easily, if you know the order. Three grilled chicken street tacos is 330 calories and 27 grams of protein, which fits almost any plan. The chain is not the problem. The Epic burritos and the assumption that the salad is the safe choice are the problem."),
]

html = page(
    SLUG,
    "Del Taco After 40: What to Order | Fig Performance",
    "What to order at Del Taco after 40, from their own nutrition list: three street tacos give 27g of protein for 330 calories and beat the salad on every count.",
    "Del Taco After 40: What to Order",
    "Fitness after 40", "The biggest lie you have been told about Del Taco is that the salad beats the tacos.",
    "Three grilled chicken street tacos: 330 calories, 27 g protein, 900 mg sodium.",
    [("street-taco", "The best item is the smallest"), ("salad", "The salad is not the answer"),
     ("sodium", "Sodium is the real story"), ("tacos", "The other grilled options"),
     ("order", "What I would order"), ("why", "Why it is on the list"),
     ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "Del Taco after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
