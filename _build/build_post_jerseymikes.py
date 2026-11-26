"""Article: Jersey Mike's after 40. DRAFT Nov 25 2026, not published until Dan approves.

Dave has NOTHING on Jersey Mike's. Same sourcing rule as the Raising Cane's piece:
no number goes on the page unless two or more independent sources agree, and where
they split the page gives the range. The "sub in a tub" saving (250-350 cal, ~50 g
carbs, protein unchanged) cleared three sources. Deliberately NOT used: the widely
repeated "#7 Turkey tub is 190 calories" figure, because another source puts the
same item near 490 once Mike's Way is on it. Canadian menu data was excluded, it
does not match the US menu.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "jersey-mikes-after-40"

body = f"""<p class="legal-intro">There is a free hack at Jersey Mike's that almost nobody over 40 is using, and it is three words long. Say "sub in a tub" at the counter and they build your sandwich in a bowl instead of on bread. Same meat, same cheese, same toppings, same protein. Somewhere between 250 and 350 calories gone, and about 50 grams of carbs with them. It costs nothing and it is on every order screen in the country.</p>

<h2 id="tub">Sub in a tub</h2>
<p>This is the whole reason the restaurant is on my list. The bread at a sub shop is not a rounding error, it is a third of the meal, and Jersey Mike's will simply leave it out if you ask.</p>
<p>Independent nutrition breakdowns agree on roughly the same saving:</p>
<ul>
  <li><strong>Calories:</strong> about 250 to 350 fewer</li>
  <li><strong>Carbs:</strong> about 50 grams fewer</li>
  <li><strong>Protein:</strong> unchanged</li>
</ul>
<p>That last line is the one that matters. Most ways of cutting calories at a restaurant cost you protein. This one does not cost you a single gram.</p>
{stats([("3 words", "sub in a tub"), ("~300 cal", "gone, typical"), ("0 g", "protein lost")])}

<h2 id="mikes-way">Mike's Way is not free</h2>
<p>Mike's Way is onions, lettuce, tomatoes, spices, and the red wine vinegar and olive oil blend. The vegetables are fine. The oil is roughly 100 calories of pure fat.</p>
<p>I am not telling you to skip it, because Mike's Way is most of why the sandwich tastes like it does. I am telling you it is not a free topping, and if you are already in a tub, asking them to go light on the oil is the second-easiest saving on the menu.</p>
{pullquote("The bread is a third of the meal. They will leave it out if you ask. Almost nobody asks.")}

<h2 id="sodium">The number to actually watch here</h2>
<p>Not calories. Sodium.</p>
<p>A Regular sub at Jersey Mike's can run anywhere from about 1,160 mg to roughly 3,530 mg of sodium depending on what is in it. The high end of that is more than a full day's worth in one sandwich, and the cured meats and the cheese are where it concentrates. The Buffalo Chicken Cheesesteak is one of the worst offenders, with the buffalo sauce stacked on top of the cheese.</p>
<p>If a doctor has said anything to you about blood pressure, that is the column to read at this restaurant, the same as at El Pollo Loco. The protein here is excellent. The salt is the thing worth managing.</p>

<h2 id="range">Why two people can order "a sub" and eat completely differently</h2>
<p>A Regular at Jersey Mike's covers an enormous range: roughly 540 calories at one end and about 1,000 at the other, with protein running anywhere from the mid-20s to the low 50s. Hot grilled subs generally sit lower than the loaded cold classics.</p>
<p>So "I had a sub for lunch" tells you almost nothing. The order inside that sentence is doing all the work, which is exactly the situation where knowing three or four defaults is worth more than any diet.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Regular, sub in a tub.</strong> Start every order here. It is the single highest-value move on this page.</li>
  <li><strong>A grilled chicken or turkey build</strong> rather than a loaded cold cut stack. Same protein, less fat, and meaningfully less sodium.</li>
  <li><strong>Mike's Way, light on the oil.</strong> Keep the vegetables and the vinegar, ease off the blend.</li>
  <li><strong>Skip the chips and the cookie.</strong> They are not on the nutrition conversation anybody has about this place, and they are most of the gap between a good lunch and a bad one.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Say sub in a tub. Three words, about 300 calories, no protein lost", "Mike's Way oil is about 100 calories", "Sodium is the number here, not calories"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because a sub shop is where people go when they think they are making the sensible choice, and it is the restaurant where the gap between the sensible version and the careless version is widest. At In-N-Out the damage is two items you can see. Here it is a bread roll nobody thinks about and a salt load nobody reads.</p>
<p>Three words at the counter closes most of that gap, and you are not asking anybody for a favor. It is on the menu.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>Jersey Mike's publishes a nutrition disclosure report and an online calculator, and the figures above are the ones multiple independent breakdowns agree on. Two things were deliberately left out of this page. One widely repeated figure puts a turkey tub near 190 calories, while another source puts the same item close to 490 once Mike's Way is on it, so neither number is quoted here. Canadian menu data was also excluded, because it does not match the US menu. Builds vary by store and by how heavy a hand is on the oil, so check the chain's current calculator if you are tracking closely.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: about 340 mg of sodium in a full bowl, the lowest on this site</li><li><a href="/five-guys-after-40">Five Guys</a>: a bunless burger is 440 calories, 32 g protein and almost no salt</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips are about 200 calories for 30 g of protein</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders are 280 calories and 47 g of protein</li><li><a href="/cava-after-40">CAVA</a>: curated bowls are close to a day of salt, so build your own</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: five breaded tenders beat the charbroiled sandwich at the same calories</li><li><a href="/dunkin-after-40">Dunkin</a>: the Wake-Up Wrap is 7 to 8 g of protein, which is a snack</li><li><a href="/wingstop-after-40">Wingstop</a>: six plain wings are 540 calories and 60 g of protein</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("What is a sub in a tub at Jersey Mike's?",
     "It is your sandwich built in a bowl instead of on bread. Same meat, cheese and toppings. Independent nutrition breakdowns put the saving at roughly 250 to 350 calories and about 50 grams of carbs, with the protein unchanged. It is a standard order, not a special request."),
    ("How many calories does sub in a tub save?",
     "Around 250 to 350 calories depending on the sub and the bread it would have come on, plus about 50 grams of carbs. The protein stays the same, which is what makes it the best move on the menu."),
    ("Is Jersey Mike's healthy?",
     "It can be, and the range is wide. A Regular sub runs from about 540 calories to roughly 1,000, with protein from the mid-20s to the low 50s. The bigger issue is sodium, which can reach about 3,530 mg in a single Regular. Order a tub, pick a grilled build, and go light on the oil."),
    ("Does Mike's Way add a lot of calories?",
     "The vegetables are negligible. The red wine vinegar and olive oil blend is roughly 100 calories of mostly fat. Keep it if you like it, but ask them to go light if you are already watching the total."),
    ("What is the best high protein order at Jersey Mike's?",
     "A grilled chicken or turkey build, Regular size, ordered as a sub in a tub. You keep all the protein, drop the bread, and avoid most of the fat and sodium that comes with a loaded cold cut stack."),
]

html = page(
    SLUG,
    "Jersey Mike's After 40: What to Order | Fig Performance",
    "What to order at Jersey Mike's after 40: the three words that cut 300 calories with no protein lost, what Mike's Way costs, and the sodium to watch.",
    "Jersey Mike's After 40: What to Order",
    "Fitness after 40", "How to cut 300 calories at Jersey Mike's by saying three words.",
    "Sub in a tub. Same meat, same protein, no bread, and it costs nothing.",
    [("tub", "Sub in a tub"), ("mikes-way", "What Mike's Way costs"), ("sodium", "The number to watch"),
     ("range", "Why two subs are not the same"), ("order", "What I would order"),
     ("why", "Why it is on the list"), ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "Jersey Mike's after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
