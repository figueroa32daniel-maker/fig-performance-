"""Article: Subway after 40. DRAFT Nov 25 2026. Standing approval. Head-to-head (Dave has 1).

SOURCING: Subway is INCONSISTENT across sources and the article says so. The
footlong rotisserie chicken reads 600, 620, 640 and 700 cal and 46, 48, 50, 52 and
58 g protein. Date-check sorts it: the 600/46 figure is from a page ~4 years old,
the 620/48/1,500 mg figure is 13 days old. Ranges are given throughout.

EXCLUDED: UK menu data (thesubwaymenu.uk), which does not match the US menu, the
same call made on Jersey Mike's Canadian data.

DISCARDED: snapcalorie again contradicts itself, headline 640 cal / 52 g against
its own panel at 250 cal / 20.3 g on the same page.

THE STORY: the No Bready Bowl. Subway will build any sub as a bowl. Rotisserie
chicken that way is about 220 cal / 31 g. Also the sodium spread across protein
bowls is enormous, roughly 950 mg to 2,540 mg, flagged as single-source.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "subway-after-40"

body = f"""<p class="legal-intro">Subway will build any sub as a bowl with no bread, and almost nobody asks. A rotisserie chicken No Bready Bowl comes in around 220 calories with roughly 31 grams of protein. The same filling inside a footlong runs somewhere between 600 and 700 calories. The meat was never the expensive part.</p>

<h2 id="bowl">The bowl, not the bread</h2>
<ul>
  <li><strong>Rotisserie chicken No Bready Bowl:</strong> about 220 calories, roughly 31 g protein, around 810 mg sodium</li>
  <li><strong>Rotisserie chicken, the meat alone:</strong> about 120 calories, roughly 21 g protein, around 380 mg sodium</li>
  <li><strong>Footlong rotisserie chicken sub:</strong> roughly 600 to 700 calories, about 46 to 58 g protein</li>
</ul>
<p>This is the same lever as sub in a tub at Jersey Mike's and bunless at Five Guys. The difference at Subway is that it is a named menu format rather than a special request, so there is nothing to explain at the counter.</p>
{stats([("220 cal", "chicken, no bread"), ("31 g", "protein in it"), ("600-700", "the same in a footlong")])}

<h2 id="sodium">The sodium spread between bowls is enormous</h2>
<p>If you do order a protein bowl, which one matters far more than people expect. Published figures put the grilled chicken version near 950 mg of sodium and the spicy Italian version near 2,540 mg, with most of the rest somewhere in between.</p>
<p>That is not a small variation, it is the difference between a normal lunch and a full day of salt, decided entirely by which meat and sauce you pointed at. Chicken runs low. Cured meats and the creamy dressings run high.</p>
{pullquote("The meat was never the expensive part. At a sandwich shop, that is worth knowing.")}

<h2 id="footlong">Why the footlong numbers are all over the place</h2>
<p>Worth saying plainly: Subway's published figures disagree with each other more than most chains in these guides. The same footlong rotisserie chicken sub appears at 600, 620, 640 and 700 calories, and at anywhere from 46 to 58 grams of protein, depending on which source you read.</p>
<p>Some of that is age. The lowest figure comes from a page roughly four years old. Some of it is that a sub is assembled by a person, and the amount of meat, sauce and cheese in it is genuinely variable in a way a wrapped burger is not.</p>
<p>So treat any sub number as approximate. The bowl figures are tighter because there is no bread to vary.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Rotisserie chicken as a No Bready Bowl.</strong> Around 220 calories and roughly 31 g of protein.</li>
  <li><strong>Grilled chicken if you want a full protein bowl.</strong> It carries the least sodium of the lot.</li>
  <li><strong>Double the meat</strong> rather than ordering a footlong. You get the protein without the bread.</li>
  <li><strong>Avoid the cured meat bowls and creamy dressings</strong> if sodium matters. They are where the 2,000 mg plus figures live.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Any sub can be a bowl, it is a named menu format", "Rotisserie chicken bowl: about 220 cal and 31 g protein", "Sodium between bowls ranges from about 950 to 2,540 mg"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because Subway spent thirty years telling people it was the healthy option, and that reputation now does the opposite of what it should: people order a footlong without reading anything, on the grounds that it is a sandwich shop and therefore fine.</p>
<p>The useful version is narrower. Chicken over cured meat, bowl over bread, and watch the dressing. Do those three things and it is a genuinely good lunch. Skip them and you have eaten seven hundred calories and most of a day's salt standing up.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>Subway's figures are less consistent than most chains on this site, and this page gives ranges rather than pretending otherwise. The footlong rotisserie chicken sub appears at 600, 620, 640 and 700 calories across sources; the oldest of those is a page roughly four years out of date and the most recent gives 620 calories with 48 grams of protein and around 1,500 mg of sodium. UK menu data was excluded because it does not match the US menu. One database was discarded for contradicting itself, giving 640 calories and 52 grams in its headline and 250 calories and 20.3 grams in its own panel on the same page. The protein bowl sodium comparison rests on a single recent source and is described as a spread rather than quoted item by item.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/cava-after-40">CAVA</a>: the curated bowls are a day of salt</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/mcdonalds-after-40">McDonald's</a>: the McDouble beats the Big Mac</li><li><a href="/wendys-after-40">Wendy's</a>: the chili is the only side worth having</li><li><a href="/taco-bell-after-40">Taco Bell</a>: three soft tacos beat the Power Bowl</li><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/five-guys-after-40">Five Guys</a>: bunless is 440 calories and almost no salt</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap saves 200 calories</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: the breaded tenders beat the charbroiled sandwich</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders, 280 calories and 47 g</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips, 200 calories and 30 g</li><li><a href="/wingstop-after-40">Wingstop</a>: the flavour swings sodium tenfold</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/rubios-after-40">Rubio's</a>: the famous fish taco is nine grams</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: lowest sodium meal on this site</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/dunkin-after-40">Dunkin'</a>: the Wake-Up Wrap is a snack</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("Can you order a Subway sub without bread?",
     "Yes. Subway serves them as bowls, and it is a named menu format rather than a special request. A rotisserie chicken bowl is around 220 calories with roughly 31 grams of protein against 600 to 700 calories for the same filling in a footlong."),
    ("How much protein is in Subway rotisserie chicken?",
     "The meat alone is about 120 calories with roughly 21 grams of protein. As a no-bread bowl it comes to around 220 calories and about 31 grams once the vegetables and dressing are in."),
    ("Which Subway protein bowl is lowest in sodium?",
     "The grilled chicken version, at around 950 mg. The spicy Italian bowl is near 2,540 mg, and most of the others fall between. Chicken runs low, cured meats and creamy dressings run high. That single choice is the biggest sodium decision on the menu."),
    ("Why do Subway calorie figures vary so much?",
     "Partly because some published pages are several years out of date, and partly because a sub is assembled by hand. The amount of meat, sauce and cheese genuinely varies in a way a wrapped burger does not. Bowl figures are tighter because there is no bread to vary."),
    ("Is Subway actually healthy?",
     "It can be, and its reputation is not doing customers any favours. Chicken over cured meat, bowl over bread, and watch the dressing. Do those three and it is a good lunch. Skip them and a footlong with a creamy dressing can be 700 calories and most of a day's sodium."),
]

html = page(
    SLUG,
    "Subway After 40: What to Order | Fig Performance",
    "What to order at Subway after 40: a rotisserie chicken bowl is 220 calories and 31g of protein, against 600 to 700 for the same filling in a footlong.",
    "Subway After 40: What to Order",
    "Fitness after 40", "Unpopular opinion: the best thing at Subway has no bread in it.",
    "A rotisserie chicken bowl: about 220 calories and roughly 31 grams of protein.",
    [("bowl", "The bowl, not the bread"), ("sodium", "The sodium spread"),
     ("footlong", "Why the numbers vary"), ("order", "What I would order"),
     ("why", "Why it is on the list"), ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "Subway after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
