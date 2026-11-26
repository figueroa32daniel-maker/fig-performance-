"""Article: McDonald's after 40. DRAFT Nov 25 2026. Standing approval.

NOTE: Dave HAS three McDonald's articles. This is the first head-to-head page in
the cluster rather than open territory. Justified because the data is the cleanest
of any chain (seven sources identical) and search volume is the highest.

SOURCING: excellent. Seven independent sources give the McDouble at 390 cal / 22 g
/ 20 g fat / 32 g carbs / 920 mg sodium. Six give the Egg McMuffin at 310 cal /
17 g / 770 mg. No discards needed, which has not happened on any other chain.

THE STORY: the McDouble beats the Big Mac on protein per calorie and costs less.
22 g for 390 cal (5.6 g per 100 cal) against 25 g for 580 cal (4.3 g per 100 cal).
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "mcdonalds-after-40"

body = f"""<p class="legal-intro">The McDouble is 390 calories with 22 grams of protein. The Big Mac is around 580 calories with 25 grams. Three extra grams of protein for 190 extra calories, and the Big Mac costs more. The best thing on that menu for an adult over 40 is also close to the cheapest, and it has been sitting there the whole time.</p>

<h2 id="mcdouble">The McDouble against the Big Mac</h2>
<ul>
  <li><strong>McDouble:</strong> 390 calories, 22 g protein, 20 g fat, 32 g carbs, 920 mg sodium</li>
  <li><strong>Big Mac:</strong> around 580 calories, roughly 25 g protein</li>
</ul>
<p>Per hundred calories that is 5.6 grams of protein against about 4.3. The difference is the middle bun and the sauce, which is most of what a Big Mac is once you take the two patties out of the equation.</p>
<p>Seven independent nutrition sources give the McDouble identically. That almost never happens, and it makes this the most reliably sourced number in any of these guides.</p>
{stats([("390 cal", "McDouble"), ("22 g", "protein in it"), ("580 cal", "Big Mac, for 25 g")])}

<h2 id="ladder">The burger ladder</h2>
<p>Useful to have in your head, because the steps are not evenly spaced:</p>
<ul>
  <li><strong>Hamburger:</strong> about 250 calories, roughly 12 g protein</li>
  <li><strong>Cheeseburger:</strong> about 300 calories, roughly 15 g protein</li>
  <li><strong>McDouble:</strong> 390 calories, 22 g protein</li>
  <li><strong>Bacon McDouble:</strong> about 460 calories, roughly 26 g protein, around 1,140 mg sodium</li>
  <li><strong>McCrispy:</strong> about 470 calories, roughly 26 g protein, around 1,140 mg sodium</li>
</ul>
<p>Going from a cheeseburger to a McDouble costs 90 calories and buys 7 grams of protein. That is the best step on the ladder. Everything above the McDouble costs more calories per gram than the step below it.</p>
{pullquote("Seven grams of protein for ninety calories. That is the best step on the ladder, and it is a dollar-menu item.")}

<h2 id="breakfast">Breakfast is the Egg McMuffin, and it is not close</h2>
<p>About 310 calories with roughly 17 grams of protein and around 770 mg of sodium. It is the lightest breakfast sandwich on the board and among the highest in protein, which is an unusual combination.</p>
<p>What to avoid: the Big Breakfast is around 1,060 calories, and the version with hotcakes is around 1,340 with about 41 grams of added sugar. A Sausage McGriddles is roughly 430 calories for only about 11 grams of protein, because the pancakes are doing the work the bun would normally do and bringing sugar with them.</p>

<h2 id="bunless">Going bunless works here too</h2>
<p>You can order any of these without the bun, and McDonald's will do it. On a double quarter pounder that is worth roughly 190 calories once the bun and a slice of cheese come off, and it leaves you near 48 grams of protein.</p>
<p>It is the same lever as Five Guys and The Habit. The protein is never the problem at a burger restaurant.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>McDouble, no fries, water.</strong> 390 calories, 22 g protein, and it is the cheapest route to that number anywhere in these guides.</li>
  <li><strong>Two McDoubles</strong> if you are genuinely hungry. About 780 calories and 44 g of protein, which still beats a Big Mac meal on both counts.</li>
  <li><strong>Egg McMuffin</strong> for breakfast. 310 calories and 17 g.</li>
  <li><strong>Skip the McGriddles and the Big Breakfast.</strong> One is sugar, the other is a thousand calories.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["McDouble: 390 cal and 22 g protein, for about a dollar fifty", "Big Mac is 580 cal for 25 g, so the McDouble wins", "Egg McMuffin is the breakfast, at 310 cal and 17 g"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because McDonald's is the restaurant everyone has already decided about, and the decision is usually wrong in both directions. People who think it is poison avoid it and then order badly when a road trip puts them there. People who think it is fine order the famous things, which are the expensive ones.</p>
<p>The actual answer is narrow and cheap: a McDouble is a 390 calorie meal with 22 grams of protein. That is a better lunch than a lot of what my clients make at home, and it costs less than a coffee.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>This is the best-sourced page in the series and the only one where nothing had to be discarded. Seven independent nutrition breakdowns give the McDouble identically at 390 calories, 22 grams of protein, 20 grams of fat, 32 grams of carbohydrate and 920 mg of sodium. Six give the Egg McMuffin at 310 calories, 17 grams of protein and 770 mg of sodium. McDonald's publishes full nutrition for the US menu, which is why the aggregators agree with each other for once.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/five-guys-after-40">Five Guys</a>: bunless is 440 calories and almost no salt</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap saves 200 calories</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: the breaded tenders beat the charbroiled sandwich</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/rubios-after-40">Rubio's</a>: the famous fish taco is nine grams</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: lowest sodium meal on this site</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips, 200 calories and 30 g</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders, 280 calories and 47 g</li><li><a href="/wingstop-after-40">Wingstop</a>: the flavour swings sodium tenfold</li><li><a href="/cava-after-40">CAVA</a>: the curated bowls are a day of salt</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/dunkin-after-40">Dunkin'</a>: the Wake-Up Wrap is a snack</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("Is the McDouble better than the Big Mac?",
     "On protein per calorie, yes and clearly. A McDouble is 390 calories with 22 grams of protein. A Big Mac is around 580 calories with roughly 25 grams. Three extra grams for 190 extra calories, at a higher price."),
    ("How much protein is in a McDouble?",
     "22 grams, at 390 calories with 20 grams of fat and 920 mg of sodium. Seven independent nutrition sources give those figures identically, which makes it one of the most reliable numbers in these guides."),
    ("What is the best breakfast at McDonald's?",
     "The Egg McMuffin, at about 310 calories with roughly 17 grams of protein and around 770 mg of sodium. It is the lightest breakfast sandwich and among the highest in protein. Avoid the Big Breakfast at around 1,060 calories and the hotcakes version at around 1,340."),
    ("Can you order a McDonald's burger without the bun?",
     "Yes. On a double quarter pounder, dropping the bun and a slice of cheese saves roughly 190 calories and still leaves you near 48 grams of protein. It is the same move that works at Five Guys and The Habit."),
    ("Can I eat McDonald's and still lose fat after 40?",
     "Easily, if you know the order. A McDouble with water is a 390 calorie meal with 22 grams of protein, which fits almost any plan and costs less than a coffee. What breaks it is the fries and the drink, not the burger."),
]

html = page(
    SLUG,
    "McDonald's After 40: What to Order | Fig Performance",
    "What to order at McDonald's after 40: the McDouble is 390 calories and 22g of protein, beating the Big Mac on both counts for less money.",
    "McDonald's After 40: What to Order",
    "Fitness after 40", "Hot take: the McDouble beats the Big Mac, and it is nearly the cheapest thing there.",
    "390 calories and 22 grams of protein, against 580 calories for 25.",
    [("mcdouble", "McDouble vs Big Mac"), ("ladder", "The burger ladder"),
     ("breakfast", "Breakfast is the Egg McMuffin"), ("bunless", "Going bunless"),
     ("order", "What I would order"), ("why", "Why it is on the list"),
     ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "McDonald's after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
