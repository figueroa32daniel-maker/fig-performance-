"""Article: Portillo's after 40. DRAFT Nov 25 2026. Standing approval.

Dave has NOTHING on Portillo's. Buena Park location serves North OC.

SOURCE: FIRST-PARTY. Portillo's publishes a Nutrition and Allergen PDF dated
9.29.26, linked from portillos.com/nutrition. Every figure here is from it.

THE STORY: the dressing. Across every salad on the menu it adds a consistent
~340 calories and almost no protein. Caesar with grilled chicken is 328 cal /
37 g without it and 668 cal / 39 g with it. That is the cleanest single finding
in the series: same number, every salad, no exceptions.

NOT QUOTED: burger and chicken-sandwich protein and carbs, and fries sodium,
because those columns were garbled in the source read. Also NOT quoted: the
Jumbo fries figure of 2,415 cal, which does not reconcile with the regular and
large sizes and looks like a typo on the chain's own document.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "portillos-after-40"

body = f"""<p class="legal-intro">A Classic Caesar Salad with grilled chicken at Portillo's is 328 calories with 37 grams of protein. The same salad with the dressing on it is 668 calories with 39 grams. The dressing costs you 340 calories and buys you two grams of protein. That is true of every salad on their menu, and the number barely moves.</p>

<h2 id="dressing">The dressing is 340 calories, every time</h2>
<p>From Portillo's own nutrition document, dressed against undressed:</p>
<ul>
  <li><strong>Caesar with grilled chicken:</strong> 328 cal / 37 g without, 668 cal / 39 g with</li>
  <li><strong>Chopped Salad:</strong> 506 cal / 42 g without, 846 cal / 42 g with</li>
  <li><strong>Classic Caesar:</strong> 200 cal / 12 g without, 540 cal / 14 g with</li>
  <li><strong>Spicy Chicken Chopped:</strong> 739 cal / 45 g without, 1,079 cal / 45 g with</li>
</ul>
<p>Three hundred and forty calories, four times, almost exactly. Ask for it on the side and use a third of it and you have saved yourself more than two hundred calories without noticing.</p>
{stats([("328 cal", "caesar + chicken, dry"), ("668 cal", "the same with dressing"), ("+2 g", "protein the dressing adds")])}

<h2 id="caesar">The Caesar with grilled chicken is the order</h2>
<p>Thirty-seven grams of protein for 328 calories and 826 mg of sodium is a genuinely excellent number, and it is sitting on the menu of a place famous for Italian beef and chili dogs.</p>
<p>The Greek Salad with chicken is the next best at 325 calories with 27 grams. The Chopped Salad carries the most protein at 42 grams, but it costs 506 calories undressed because of what else is in it.</p>
{pullquote("Thirty-seven grams of protein for 328 calories, at the hot dog place.")}

<h2 id="dogs">The hot dogs are smaller than they feel</h2>
<ul>
  <li><strong>Hot Dog with Everything, regular:</strong> 352 calories, 13 g protein, 1,572 mg sodium</li>
  <li><strong>Hot Dog with Everything, jumbo:</strong> 462 calories, 19 g protein, 2,062 mg sodium</li>
  <li><strong>Chili Cheese Dog, regular:</strong> 511 calories, 22 g protein, 1,649 mg sodium</li>
</ul>
<p>Three hundred and fifty calories for a hot dog is not the disaster people assume. The sodium is. A regular dog with everything carries over 1,500 mg, and the jumbo clears 2,000, which is most of a day in one item that takes four minutes to eat.</p>

<h2 id="beef">Italian beef, and the broiled chicken nobody orders</h2>
<ul>
  <li><strong>Italian Beef, regular:</strong> 693 calories, 33 g protein, 1,237 mg sodium</li>
  <li><strong>Italian Beef, Big Beef:</strong> 1,040 calories, 50 g protein, 1,856 mg sodium</li>
  <li><strong>Broiled Chicken Sandwich:</strong> 406 calories, 769 mg sodium</li>
  <li><strong>Breaded Chicken Sandwich:</strong> 601 calories, 2,058 mg sodium</li>
</ul>
<p>Look at those last two together. Broiled against breaded is 195 calories and, more importantly, around 1,290 mg of sodium. The broiled chicken sandwich is the lowest sodium main on the entire menu and almost nobody orders it, because you do not go to Portillo's for broiled chicken.</p>

<h2 id="worst">Where it tops out</h2>
<p>A Triple Cheeseburger is 1,419 calories with about 3,545 mg of sodium, and a double Rodeo Burger is 1,164 calories with 3,000 mg. Those are day-and-a-half sodium figures in a single sandwich.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Classic Caesar with grilled chicken, dressing on the side.</strong> 328 calories and 37 g of protein before you add any of it back.</li>
  <li><strong>Broiled chicken sandwich</strong> if you want a sandwich. 406 calories and the lowest sodium main here.</li>
  <li><strong>A regular dog with everything</strong> over a jumbo or a chili cheese. 352 calories, and the sodium is the reason not the fat.</li>
  <li><strong>Dressing on the side, always.</strong> It is 340 calories at this restaurant no matter which salad you picked.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Dressing adds 340 calories to every salad on the menu", "Caesar with grilled chicken, dry: 328 cal and 37 g protein", "Broiled chicken sandwich is the lowest sodium main"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because the Buena Park location is fifteen minutes from the studio and people treat the whole place as a write-off day. It does not have to be. There is a 328 calorie, 37 gram salad on that menu, and the single decision that matters most is one you make while they are still building it.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>Every figure above comes from Portillo's own Nutrition and Allergen document, dated September 2026. Three things were deliberately left out. The protein and carbohydrate columns for burgers and chicken sandwiches were not legible in the source, so only calories, fat and sodium are quoted for those. The sodium column for fries was likewise unreadable. And the document lists a Jumbo fries figure of 2,415 calories, which does not reconcile with the regular at 340 and the large at 483 and looks like an error on the page, so it is not quoted here.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/five-guys-after-40">Five Guys</a>: bunless is 440 calories and almost no salt</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap saves 200 calories</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: the breaded tenders beat the charbroiled sandwich</li><li><a href="/mcdonalds-after-40">McDonald's</a>: the McDouble beats the Big Mac</li><li><a href="/wendys-after-40">Wendy's</a>: the chili is the only side worth having</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders, 280 calories and 47 g</li><li><a href="/daves-hot-chicken-after-40">Dave's Hot Chicken</a>: one tender is 490 calories</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/wingstop-after-40">Wingstop</a>: the flavour swings sodium tenfold</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips, 200 calories and 30 g</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/taco-bell-after-40">Taco Bell</a>: three soft tacos beat the Power Bowl</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/rubios-after-40">Rubio's</a>: the famous fish taco is nine grams</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: lowest sodium meal on this site</li><li><a href="/cava-after-40">CAVA</a>: the curated bowls are a day of salt</li><li><a href="/panda-express-after-40">Panda Express</a>: the base is the whole decision</li><li><a href="/subway-after-40">Subway</a>: the best thing there has no bread in it</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/dunkin-after-40">Dunkin'</a>: the Wake-Up Wrap is a snack</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("What is the healthiest thing to order at Portillo's?",
     "The Classic Caesar Salad with grilled chicken, undressed, at 328 calories with 37 grams of protein and 826 mg of sodium. Ask for the dressing on the side, because it adds 340 calories."),
    ("How many calories is Portillo's salad dressing?",
     "About 340 calories, and it is remarkably consistent across the menu. It adds 340 to the Caesar with chicken, 340 to the Chopped Salad, 340 to the plain Caesar and 340 to the Spicy Chicken Chopped. It also adds almost no protein."),
    ("How many calories is a Portillo's hot dog?",
     "A regular Hot Dog with Everything is 352 calories with 13 grams of protein. The jumbo is 462 with 19 grams. The number to watch is sodium, not calories: the regular carries about 1,572 mg and the jumbo about 2,062 mg."),
    ("How many calories is an Italian beef at Portillo's?",
     "A regular Italian Beef sandwich is 693 calories with 33 grams of protein and about 1,237 mg of sodium. The Big Beef is 1,040 calories with 50 grams of protein."),
    ("What is the lowest sodium item at Portillo's?",
     "Among the mains, the Broiled Chicken Sandwich at about 769 mg, which is roughly 1,290 mg less than the breaded version of the same sandwich. The undressed Classic Caesar is lower still at 270 mg, but without chicken it is not a meal."),
]

html = page(
    SLUG,
    "Portillo's After 40: What to Order | Fig Performance",
    "What to order at Portillo's after 40: the salad dressing adds 340 calories to every salad, and a Caesar with grilled chicken is 328 calories dry.",
    "Portillo's After 40: What to Order",
    "Fitness after 40", "Stop letting them dress the salad at Portillo's. It is 340 calories and two grams of protein.",
    "Caesar with grilled chicken: 328 calories dry, 668 with the dressing on.",
    [("dressing", "The dressing is 340 calories"), ("caesar", "The Caesar is the order"),
     ("dogs", "The hot dogs"), ("beef", "Italian beef and broiled chicken"),
     ("worst", "Where it tops out"), ("order", "What I would order"),
     ("why", "Why it is on the list"), ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "Portillo's after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
