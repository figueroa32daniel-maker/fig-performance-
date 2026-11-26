"""Article: Rubio's Coastal Grill after 40. DRAFT Nov 25 2026. Standing approval.

Dave has NOTHING on Rubio's. Born in San Diego, dense across Southern California.

SOURCING: good, and partly FIRST-PARTY. rubios.com publishes a nutrition table and
a menu PDF. Their own PDF gives The Original Fish Taco at 330 cal, and two
independent sources agree at 330 cal / 9 g protein / 370 mg sodium. Their own
nutrition table gives the Grilled Atlantic Salmon taco at 270 cal / 13 g / 160 mg.

One outlier (eatmuch.blog) claims the Original Fish Taco is 260 cal with 14 g
protein, contradicting the chain's own figure and three other sources. Discarded.

THE STORY: the taco Rubio's is famous for is the worst protein order on the menu.
The Original Fish Taco is 330 cal for 9 g protein. The Grilled Gourmet Chicken
Taco is the SAME 330 calories for 20 g. It is battered and fried; the grilled ones
are not.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "rubios-after-40"

body = f"""<p class="legal-intro">The Original Fish Taco is the thing Rubio's built an entire chain on, and it is about 330 calories for roughly 9 grams of protein. The Grilled Gourmet Chicken Taco is the same 330 calories for about 20 grams. Identical calories. More than double the protein. The difference is that one of them is battered and dropped in a fryer.</p>

<h2 id="original">The famous one is the weakest one</h2>
<ul>
  <li><strong>The Original Fish Taco:</strong> about 330 calories, roughly 9 g protein, around 370 mg sodium</li>
  <li><strong>Grilled Gourmet Taco, chicken:</strong> about 330 calories, roughly 20 g protein, around 640 mg sodium</li>
</ul>
<p>Nine grams is not a rounding error below twenty, it is less than half. At 330 calories a taco, three of the originals is a thousand calories and 27 grams of protein, which is a bad day's arithmetic for an adult over 40.</p>
<p>None of this means it is a bad taco. It means it is a fried taco, and fried food in a tortilla with crema is mostly not protein.</p>
{stats([("330 cal", "both tacos"), ("9 g", "the original fish"), ("20 g", "grilled chicken")])}

<h2 id="grilled">The grilled tacos are the actual menu</h2>
<p>Once you stop ordering the famous one, this becomes one of the better restaurants in these guides. From Rubio's own published nutrition information and independent breakdowns:</p>
<ul>
  <li><strong>Grilled Fish Taco, Atlantic Salmon:</strong> about 270 calories, roughly 13 g protein, around <strong>160 mg sodium</strong></li>
  <li><strong>Grilled Wild Alaska Coho Salmon Taco:</strong> about 230 calories, roughly 12 g protein, around 170 mg sodium</li>
  <li><strong>Grilled Mango Wild Grouper Taco:</strong> about 270 calories, roughly 14 g protein, around 430 mg sodium</li>
  <li><strong>Street Taco, steak:</strong> about 110 calories, roughly 7 g protein, around 140 mg sodium</li>
</ul>
<p>Those sodium numbers are remarkable. A grilled salmon taco at around 160 mg is in Flame Broiler territory, and nothing else on a coastal menu usually gets close.</p>
{pullquote("The taco they are famous for has nine grams of protein. The one next to it has twenty, for the same calories.")}

<h2 id="plates">Where it goes wrong fast</h2>
<p>The combination plates and the big bowls are a different restaurant. The Coastal Trio is around 850 calories with roughly 35 grams of protein and about 1,250 mg of sodium, and the lobster bowl pushes past 1,200 calories.</p>
<p>The pattern is the same as everywhere else on this site: the individual grilled items are excellent and the plates built around them are where the day gets away from you.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Two or three grilled tacos,</strong> salmon or grouper. Roughly 230 to 270 calories each with 12 to 14 g of protein and very little sodium.</li>
  <li><strong>Grilled Gourmet Chicken Taco</strong> if you want the most protein per taco, at about 20 g.</li>
  <li><strong>Street tacos</strong> if you want the smallest unit. Around 110 calories and 7 g each.</li>
  <li><strong>Skip the trios and the plates.</strong> They triple the order without tripling the protein.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["The Original Fish Taco is 9 g of protein for 330 calories", "Grilled chicken is 20 g for the same 330", "Grilled salmon tacos are around 160 mg sodium"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because the signature item at a restaurant is almost never chosen for its nutrition, and people order it because it is the signature item. Rubio's is the clearest example of that in any of these guides: the thing with the chain's name attached is the one item on the board I would steer a client away from, and everything beside it is genuinely good.</p>
<p>Grilled fish, low sodium, real portions. It is a better after-40 restaurant than most of this list, once you walk past the taco on the sign.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>Rubio's publishes its own nutrition table and menu PDF, and this page uses those where possible. The chain's own PDF gives the Original Fish Taco at 330 calories, matching two independent breakdowns that also give 9 grams of protein and 370 mg of sodium. The Grilled Atlantic Salmon figures come from Rubio's own nutrition table. One source reports the Original Fish Taco at 260 calories with 14 grams of protein, contradicting both the chain's own figure and three other sources, so it was discarded rather than averaged in.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: lowest sodium meal on this site</li><li><a href="/five-guys-after-40">Five Guys</a>: bunless is 440 calories and almost no salt</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap saves 200 calories</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: the breaded tenders beat the charbroiled sandwich</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips, 200 calories and 30 g</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders, 280 calories and 47 g</li><li><a href="/wingstop-after-40">Wingstop</a>: the flavour swings sodium tenfold</li><li><a href="/cava-after-40">CAVA</a>: the curated bowls are a day of salt</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/dunkin-after-40">Dunkin'</a>: the Wake-Up Wrap is a snack</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/mcdonalds-after-40">McDonald's</a>: the McDouble is 390 calories and 22 g protein, beating the Big Mac</li><li><a href="/taco-bell-after-40">Taco Bell</a>: three soft chicken tacos give 36 g of protein, beating the Power Bowl</li><li><a href="/wendys-after-40">Wendy's</a>: the chili is the only fast food side with real protein in it</li><li><a href="/subway-after-40">Subway</a>: a rotisserie chicken bowl is 220 calories and 31 g of protein</li><li><a href="/panda-express-after-40">Panda Express</a>: super greens with teriyaki chicken is 470 calories and 50 g of protein</li><li><a href="/daves-hot-chicken-after-40">Dave's Hot Chicken</a>: one tender is 490 calories, not the 150 your app says</li><li><a href="/portillos-after-40">Portillo's</a>: the dressing adds 340 calories to every salad on the menu</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("How much protein is in a Rubio's Original Fish Taco?",
     "About 9 grams, at roughly 330 calories and around 370 mg of sodium. It is battered and fried, which is why the protein is low for the calories. The Grilled Gourmet Chicken Taco is the same 330 calories for about 20 grams."),
    ("What is the healthiest thing to order at Rubio's?",
     "The grilled tacos. A Grilled Atlantic Salmon taco is around 270 calories with roughly 13 grams of protein and only about 160 mg of sodium, and the Grilled Wild Alaska Coho Salmon taco is near 230 calories. Those sodium figures are among the lowest of any item in these guides."),
    ("Is Rubio's fish taco healthy?",
     "The original is fine as food and weak as nutrition: about 330 calories for roughly 9 grams of protein. If you want a fish taco that works for you, order one of the grilled versions instead. You get more protein, fewer calories and a fraction of the sodium."),
    ("Is Rubio's good for weight loss?",
     "It is one of the better options on this list once you order grilled. Two or three grilled fish tacos come to roughly 500 to 800 calories with 25 to 40 grams of protein and very low sodium. The combination plates and trios are where it stops working."),
    ("How many calories is the Coastal Trio at Rubio's?",
     "Around 850 calories with roughly 35 grams of protein and about 1,250 mg of sodium. It triples the order without tripling the protein, which is the same pattern as the combo meals at every other chain in these guides."),
]

html = page(
    SLUG,
    "Rubio's After 40: What to Order | Fig Performance",
    "What to order at Rubio's after 40: the Original Fish Taco is 9g of protein for 330 calories, and a grilled chicken taco is 20g for the same.",
    "Rubio's After 40: What to Order",
    "Fitness after 40", "Stop ordering the Original Fish Taco at Rubio's. It is nine grams of protein.",
    "Same 330 calories as the grilled chicken taco, which gives you twenty.",
    [("original", "The famous one is weakest"), ("grilled", "The grilled tacos"),
     ("plates", "Where it goes wrong"), ("order", "What I would order"),
     ("why", "Why it is on the list"), ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "Rubio's after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
