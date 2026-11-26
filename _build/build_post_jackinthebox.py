"""Article: Jack in the Box after 40. DRAFT Nov 25 2026. Standing approval, restaurant cluster.

Dave has NOTHING on Jack in the Box. SoCal dense, open 24 hours.

SOURCING, this one is thinner than most. The Grilled Chicken Sandwich reads 430,
500, 510 and 600 calories across sources, and 20, 29, 30 and 33 g protein. 500 cal
appears in three sources and 33 g in two, so those are stated as approximate.
SODIUM IS NOT STATED as a single figure: the same sandwich appears at 900, 1,000,
1,090 and 1,440 mg. The article says so and tells readers to check.

What DOES hold across sources: grilled beats crispy by roughly 150-200 calories,
and the grilled strips and grilled salad are the lean tier. That is the article.
If Dan ever screen-records Jack in the Box's own nutrition page, rewrite this
against it the way Del Taco was rewritten.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "jack-in-the-box-after-40"

body = f"""<p class="legal-intro">Jack in the Box is running two different restaurants out of the same window. One of them is fried, enormous and open at two in the morning on purpose. The other is grilled chicken, and it is genuinely fine. The gap between those two menus is the widest of any chain in these guides, and which one you are eating from comes down to about four words at the speaker.</p>

<h2 id="two-menus">The two menus</h2>
<p>On the grilled side, the numbers land roughly here:</p>
<ul>
  <li><strong>Grilled Chicken Sandwich:</strong> around 500 calories, roughly 33 g protein</li>
  <li><strong>Grilled chicken strips, 4 piece:</strong> about 200 calories, roughly 30 g protein</li>
  <li><strong>Grilled Chicken Salad:</strong> about 320 calories, roughly 32 g protein</li>
</ul>
<p>Thirty grams of protein for 200 calories in the strips is a serious number. It is in the same bracket as the Chick-fil-A grilled nuggets, at a restaurant nobody thinks of this way.</p>
{stats([("200 cal", "grilled strips, 4 pc"), ("30 g", "protein in them"), ("~200 cal", "saved vs crispy")])}

<h2 id="grilled">Grilled over crispy is worth about 200 calories</h2>
<p>Across the menu, choosing the grilled version of a chicken item saves somewhere in the region of 150 to 200 calories against the crispy version of the same thing. The Homestyle Ranch Chicken Club sits near 700 calories; the Grilled Chicken Sandwich is near 500.</p>
<p>That is one word at the order screen for the same amount of chicken. It is the Chick-fil-A and KFC lesson again, and it keeps being true because breading is just flour and oil wrapped around the thing you actually wanted.</p>
{pullquote("Two menus, one window. The grilled one is fine. Nobody told you it was there.")}

<h2 id="sodium">The number I am not going to give you</h2>
<p>Sodium. Published figures for the same Grilled Chicken Sandwich range from about 900 mg to roughly 1,440 mg depending on which source you read, and I am not going to pick one and present it as fact.</p>
<p>What is safe to say: this is a fast food restaurant, the sauces and the bread carry salt, and the grilled items sit meaningfully below the fried burgers and combos. If you are managing blood pressure, the strips and the salad are the safer end of the menu, and asking for sauce on the side is free.</p>

<h2 id="late">The two in the morning problem</h2>
<p>This restaurant is open when nothing else is, and that is when the worst decisions get made. If you are standing there late, the useful thing to know is that four grilled chicken strips exist, they are around 200 calories, and they will do the job of stopping you being hungry without costing you the day.</p>
<p>That is not a lecture about not going. It is the single order worth memorising for the night you end up there anyway.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Grilled chicken strips.</strong> About 200 calories, roughly 30 g protein. Best item on the board.</li>
  <li><strong>Grilled Chicken Salad</strong> if you want a full meal. Around 320 calories with about 32 g protein.</li>
  <li><strong>Say grilled, not crispy.</strong> Worth roughly 150 to 200 calories for the same chicken.</li>
  <li><strong>Sauce on the side,</strong> since the sodium figures here are all over the place and that is the lever you control.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Grilled strips: about 200 cal and 30 g protein", "Grilled over crispy saves roughly 200 calories", "Sodium figures here disagree, keep sauce on the side"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because this is the restaurant people end up at rather than choose, usually late, usually hungry, usually without a plan. Every other guide on this site is about ordering well somewhere you decided to go. This one is about having a default for the place you did not decide to go.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>This page is the least precisely sourced in the series and it says so rather than hiding it. Published figures for the Jack in the Box Grilled Chicken Sandwich range from 430 to 600 calories and from 20 to 33 grams of protein across different databases, and sodium for that one item appears at 900, 1,000, 1,090 and 1,440 mg. Where sources cluster, around 500 calories and roughly 33 grams of protein, this page says approximately. Where they do not cluster, as with sodium, this page gives no figure at all. Treat everything here as a guide to which tier of the menu to order from rather than as exact macros, and check the chain's own current nutrition information if you are tracking tightly.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: lowest sodium meal on this site</li><li><a href="/five-guys-after-40">Five Guys</a>: bunless is 440 calories and almost no salt</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders are 280 calories and 47 g of protein</li><li><a href="/cava-after-40">CAVA</a>: curated bowls are close to a day of salt, so build your own</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: five breaded tenders beat the charbroiled sandwich at the same calories</li><li><a href="/dunkin-after-40">Dunkin</a>: the Wake-Up Wrap is 7 to 8 g of protein, which is a snack</li><li><a href="/wingstop-after-40">Wingstop</a>: six plain wings are 540 calories and 60 g of protein</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap Charburger is 290 calories against 470 to 520 on a bun</li><li><a href="/rubios-after-40">Rubio's</a>: the Original Fish Taco is 9 g of protein for 330 calories</li><li><a href="/mcdonalds-after-40">McDonald's</a>: the McDouble is 390 calories and 22 g protein, beating the Big Mac</li><li><a href="/taco-bell-after-40">Taco Bell</a>: three soft chicken tacos give 36 g of protein, beating the Power Bowl</li><li><a href="/wendys-after-40">Wendy's</a>: the chili is the only fast food side with real protein in it</li><li><a href="/subway-after-40">Subway</a>: a rotisserie chicken bowl is 220 calories and 31 g of protein</li><li><a href="/panda-express-after-40">Panda Express</a>: super greens with teriyaki chicken is 470 calories and 50 g of protein</li><li><a href="/daves-hot-chicken-after-40">Dave's Hot Chicken</a>: one tender is 490 calories, not the 150 your app says</li><li><a href="/portillos-after-40">Portillo's</a>: the dressing adds 340 calories to every salad on the menu</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("What is the healthiest thing at Jack in the Box?",
     "Grilled chicken strips, at about 200 calories for roughly 30 grams of protein, are the best item on the menu. The Grilled Chicken Salad is the best full meal at around 320 calories with about 32 grams."),
    ("How much protein is in the Jack in the Box grilled chicken sandwich?",
     "Sources cluster around 33 grams at roughly 500 calories, though published figures for this item vary more than most, from 430 to 600 calories and from 20 to 33 grams of protein. Treat it as approximate."),
    ("Is grilled better than crispy at Jack in the Box?",
     "Yes, and by a meaningful margin. Choosing grilled over crispy saves somewhere around 150 to 200 calories for the same amount of chicken. The breading is flour and oil around the thing you actually wanted."),
    ("How much sodium is in Jack in the Box food?",
     "Honestly, the published figures do not agree well enough to quote. The same grilled chicken sandwich appears anywhere from about 900 to roughly 1,440 mg depending on the source. What is safe to say is that the grilled items sit well below the fried burgers and combos, and asking for sauce on the side is free."),
    ("What should I order at Jack in the Box late at night?",
     "Four grilled chicken strips, around 200 calories and roughly 30 grams of protein. It is the one order worth memorising for the nights you end up there without a plan."),
]

html = page(
    SLUG,
    "Jack in the Box After 40: What to Order | Fig Performance",
    "What to order at Jack in the Box after 40: grilled chicken strips are about 200 calories for 30g of protein, and grilled beats crispy by roughly 200.",
    "Jack in the Box After 40: What to Order",
    "Fitness after 40", "Unpopular opinion: Jack in the Box has two menus, and one of them is fine.",
    "Grilled chicken strips: about 200 calories and roughly 30 grams of protein.",
    [("two-menus", "The two menus"), ("grilled", "Grilled beats crispy"), ("sodium", "The number I will not give"),
     ("late", "The 2am problem"), ("order", "What I would order"),
     ("why", "Why it is on the list"), ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "Jack in the Box after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
