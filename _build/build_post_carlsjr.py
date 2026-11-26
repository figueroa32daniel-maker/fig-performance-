"""Article: Carl's Jr after 40. DRAFT Nov 25 2026. Standing approval, restaurant cluster.

Dave has NOTHING on Carl's Jr, and CKE was founded in Anaheim.

SOURCING: carlsjr.com's OWN menu page gives the Charbroiled BBQ Chicken Sandwich at
440 cals, and three independent sources corroborate 440. Older pages showing 370,
380, 400 and 430 are stale, same date-check pattern as the WaBa 2,455 mg figure.

THE COUNTERINTUITIVE FINDING: at the same 440 calories, five Hand-Breaded Chicken
Tenders give about 41 g protein while the Charbroiled BBQ Chicken Sandwich gives
about 35 g. Two sources agree on each. The BREADED item wins on protein per calorie
here, which is the opposite of KFC, Chick-fil-A and Jack in the Box. Reason: the
sandwich carries a bun and BBQ sauce, about 48-57 g carbs and 13-14 g sugar.

NOT stated firmly: Charbroiled Chicken Club figures, which range 530-690 cal and
38-43 g protein across sources. Given as a range.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "carls-jr-after-40"

body = f"""<p class="legal-intro">Every other guide on this site tells you to pick the grilled version. At Carl's Jr that advice breaks. Five Hand-Breaded Chicken Tenders are about 440 calories with roughly 41 grams of protein. The Charbroiled BBQ Chicken Sandwich, per Carl's Jr's own menu, is also 440 calories, with about 35 grams. Same calories. The fried one wins by six grams.</p>

<h2 id="tenders">The breaded tenders beat the charbroiled sandwich</h2>
<ul>
  <li><strong>Hand-Breaded Chicken Tenders, 5 piece:</strong> about 440 calories, roughly 41 g protein</li>
  <li><strong>Charbroiled BBQ Chicken Sandwich:</strong> 440 calories, roughly 35 g protein</li>
  <li><strong>Hand-Breaded Chicken Tenders, 3 piece:</strong> about 260 calories, roughly 25 g protein</li>
</ul>
<p>This is not an argument for breading. It is an argument about what else is in the order. The sandwich carries a sourdough bun and BBQ sauce, which between them account for somewhere around 48 to 57 grams of carbohydrate and 13 to 14 grams of sugar. That is where its calories go.</p>
{stats([("440 cal", "both orders"), ("41 g", "five tenders"), ("35 g", "the BBQ sandwich")])}

<h2 id="sandwich">The sandwich is still a good order</h2>
<p>I want to be clear, because the headline could be read the wrong way. The Charbroiled BBQ Chicken Sandwich is one of the better things on this menu. It is charbroiled chicken breast, lettuce and tomato, it is 440 calories, and 35 grams of protein in a sandwich you can eat with one hand is a real meal.</p>
<p>The point is narrower than "fried is fine." It is that at this particular restaurant, the grilled-versus-fried rule does not do the work you expect, because the difference is being driven by the bun and the sauce rather than the cooking method.</p>
{pullquote("At every other chain, grilled wins. Here the bun and the BBQ sauce decide it instead.")}

<h2 id="sodium">Sodium is the real caution</h2>
<p>Around 1,310 to 1,350 mg in the BBQ chicken sandwich, which is over half a day in one item before anything else arrives. The Charbroiled Chicken Club runs higher still, with sources putting it somewhere between roughly 1,280 and 1,660 mg.</p>
<p>Same note as most of these guides: if blood pressure is your concern, the tenders without a sauced bun are the lower-salt route, and anything that arrives dressed is where the salt is hiding.</p>

<h2 id="club">The Club is not the upgrade it looks like</h2>
<p>Published figures for the Charbroiled Chicken Club vary more than most, landing somewhere between about 530 and 690 calories with roughly 38 to 43 grams of protein. Even at the friendly end of that range, you are paying well over a hundred extra calories for a handful of extra grams, and the sodium goes up with it.</p>
<p>If you want more protein, order more tenders. It is cheaper and the arithmetic is better.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Five Hand-Breaded Chicken Tenders.</strong> About 440 calories, roughly 41 g protein. Best protein per calorie on the menu.</li>
  <li><strong>Charbroiled BBQ Chicken Sandwich</strong> if you want a proper sandwich. 440 calories and about 35 g.</li>
  <li><strong>Three tenders</strong> for a smaller meal. Around 260 calories and 25 g.</li>
  <li><strong>Water, not a drink.</strong> A large soda or shake can carry as many calories as the sandwich and zero grams of protein.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Five tenders beat the BBQ sandwich at the same calories", "440 cal and about 41 g against 440 and 35", "Sodium is the caution, roughly 1,310 mg in the sandwich"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because CKE started in Anaheim and these are on half the corners around here, and because this is the one restaurant where the rule the rest of these guides taught you gives the wrong answer. That is worth knowing on its own. A rule you apply without checking is how people end up ordering worse while believing they ordered better.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>The 440 calorie figure for the Charbroiled BBQ Chicken Sandwich comes from Carl's Jr's own menu page and is corroborated by three independent sources. Older pages showing 370, 380, 400 or 430 calories for the same sandwich appear to be out of date rather than wrong at the time, which is the same pattern that produces most of the disagreement across these guides. The 41 grams of protein in five tenders is given by two sources that agree. Charbroiled Chicken Club figures vary too widely to state precisely, from about 530 to 690 calories, so they are given as a range above.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: lowest sodium meal on this site</li><li><a href="/five-guys-after-40">Five Guys</a>: bunless is 440 calories and almost no salt</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips, 200 calories and 30 g</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders, 280 calories and 47 g</li><li><a href="/cava-after-40">CAVA</a>: the curated bowls are a day of salt</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/dunkin-after-40">Dunkin</a>: the Wake-Up Wrap is 7 to 8 g of protein, which is a snack</li><li><a href="/wingstop-after-40">Wingstop</a>: six plain wings are 540 calories and 60 g of protein</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap Charburger is 290 calories against 470 to 520 on a bun</li><li><a href="/rubios-after-40">Rubio's</a>: the Original Fish Taco is 9 g of protein for 330 calories</li><li><a href="/mcdonalds-after-40">McDonald's</a>: the McDouble is 390 calories and 22 g protein, beating the Big Mac</li><li><a href="/taco-bell-after-40">Taco Bell</a>: three soft chicken tacos give 36 g of protein, beating the Power Bowl</li><li><a href="/wendys-after-40">Wendy's</a>: the chili is the only fast food side with real protein in it</li><li><a href="/subway-after-40">Subway</a>: a rotisserie chicken bowl is 220 calories and 31 g of protein</li><li><a href="/panda-express-after-40">Panda Express</a>: super greens with teriyaki chicken is 470 calories and 50 g of protein</li><li><a href="/daves-hot-chicken-after-40">Dave's Hot Chicken</a>: one tender is 490 calories, not the 150 your app says</li><li><a href="/portillos-after-40">Portillo's</a>: the dressing adds 340 calories to every salad on the menu</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("What is the highest protein order at Carl's Jr?",
     "Five Hand-Breaded Chicken Tenders, at about 440 calories with roughly 41 grams of protein. That beats the Charbroiled BBQ Chicken Sandwich, which is the same 440 calories for about 35 grams."),
    ("How many calories is the Charbroiled BBQ Chicken Sandwich?",
     "440 calories, according to Carl's Jr's own menu, with roughly 35 grams of protein and somewhere around 1,310 to 1,350 mg of sodium. Several older pages still show 370 or 400 calories for this item, which appear to be out of date."),
    ("Is charbroiled always better than breaded at Carl's Jr?",
     "Not on protein per calorie, which surprises people. At the same 440 calories, five breaded tenders give about 41 grams of protein against about 35 for the charbroiled sandwich. The difference comes from the bun and the BBQ sauce, not the cooking method."),
    ("Is the Charbroiled Chicken Club a better choice?",
     "Usually not. Published figures range from roughly 530 to 690 calories with about 38 to 43 grams of protein, and the sodium is higher than the BBQ sandwich. If you want more protein, ordering more tenders gives better arithmetic for less money."),
    ("Can you eat Carl's Jr and still lose fat after 40?",
     "Yes. A 440 calorie order with 35 to 41 grams of protein fits most plans. The things that break it are the drink, which can carry as many calories as the sandwich with no protein, and the sodium, which is over half a day in a single sauced item."),
]

html = page(
    SLUG,
    "Carl's Jr After 40: What to Order | Fig Performance",
    "What to order at Carl's Jr after 40: at the same 440 calories, five breaded tenders give 41g of protein and the charbroiled sandwich gives 35.",
    "Carl's Jr After 40: What to Order",
    "Fitness after 40", "The biggest lie you have been told about Carl's Jr is that charbroiled always beats breaded.",
    "Same 440 calories. Five tenders give 41 grams of protein. The sandwich gives 35.",
    [("tenders", "Tenders beat the sandwich"), ("sandwich", "The sandwich is still good"),
     ("sodium", "Sodium is the caution"), ("club", "The Club is not an upgrade"),
     ("order", "What I would order"), ("why", "Why it is on the list"),
     ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "Carl's Jr after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
