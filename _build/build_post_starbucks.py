"""Article: Starbucks after 40. DRAFT Nov 25 2026, not published until Dan approves.
Figures from Starbucks' published nutrition information, including the protein
lattes and protein cold foam added to the permanent menu."""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "starbucks-after-40"

body = f"""<p class="legal-intro">The standard advice about Starbucks is to drink your coffee black and eat somewhere else. That advice is out of date. Starbucks put protein-boosted milk and a protein cold foam on the permanent menu, which turned the coffee itself into a protein source instead of a thing you drink alongside one. Breakfast is where almost every client I work with leaks protein, and this is now one of the easiest places to stop it, because you are standing in that line anyway.</p>

<h2 id="protein-drinks">The drinks changed</h2>
<p>Starbucks added protein-boosted milk and a protein cold foam to the permanent menu, which turned the coffee itself into a protein source rather than a thing you drink alongside one. Published numbers for a grande:</p>
<ul>
  <li><strong>Iced Vanilla Protein Latte:</strong> about 270 calories, 29 g protein</li>
  <li><strong>Vanilla Protein Latte, hot:</strong> about 310 calories, 27 g protein</li>
  <li><strong>Iced Protein Matcha:</strong> about 300 calories, 36 g protein</li>
  <li><strong>Protein cold foam</strong> added to any cold drink: roughly 15 g protein for about 70 to 90 calories</li>
</ul>
<p>For comparison, a regular Chocolate Cream Cold Brew is about 240 calories with 3 grams of protein. The protein version is about 330 calories with 19 grams. Ninety more calories buys you sixteen grams of protein, which is a trade worth taking at 7 am.</p>
{stats([("29 g", "protein, iced vanilla protein latte"), ("270 cal", "what it costs you"), ("15 g", "from cold foam alone")])}
<p>One caveat worth saying out loud: the sugar on several of these is high, around 27 to 34 grams in a grande. If you are managing blood sugar, ask for sugar-free vanilla, which keeps the protein and takes most of that out.</p>

<h2 id="food">The egg bites are the other half</h2>
<ul>
  <li><strong>Egg White and Roasted Red Pepper:</strong> about 170 calories, 12 to 13 g protein</li>
  <li><strong>Bacon and Gruyère:</strong> about 300 calories, 19 g protein</li>
  <li><strong>Kale and Mushroom:</strong> about 150 calories, 13 g protein</li>
</ul>
<p>Pair any of those with a protein latte and you have a breakfast in the 25 to 45 gram protein range for under 500 calories, bought in the time it takes to stand in line. That is a genuinely good meal, not a compromise.</p>
{pullquote("A bagel and a latte is about 500 calories and twelve grams of protein. Egg bites and a protein latte is about the same calories and forty. Same queue, same five minutes.")}

<h2 id="avoid">What quietly costs you the most</h2>
<p>The drinks people think of as treats are not usually the problem, because they know what they are. The problem is the drink somebody believes is a coffee: a venti blended thing with whipped cream, running 400 to 500 calories with almost no protein, drunk on an empty stomach at 9 am.</p>
<p>It is liquid, so it does very little for hunger, and because it is a drink rather than a meal it does not get counted. That is the one to look at.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Iced vanilla protein latte, sugar-free vanilla, plus egg white bites.</strong> Roughly 400 calories and over 40 grams of protein. This is the order.</li>
  <li><strong>Any cold drink with protein cold foam</strong> if you want a smaller step. Fifteen grams of protein for about 80 calories on top of a coffee you already buy.</li>
  <li><strong>Bacon and Gruyère egg bites</strong> if you want it to actually feel like breakfast. 300 calories, 19 grams.</li>
  <li><strong>Plain cold brew or an Americano</strong> if you have eaten already. Nearly no calories, and no reason to complicate it.</li>
</ol>
{callout("If you remember one thing", "Fix breakfast first", ["Protein cold foam: 15 g for about 80 calories", "Egg bites beat anything in the pastry case", "Sugar-free vanilla keeps the protein, drops the sugar"])}

<h2 id="why">Why I bother writing about a coffee shop</h2>
<p>Because the adults I coach are not failing at dinner. Dinner is usually fine. They are failing between 6 am and 10 am, when they have twenty minutes and no plan, and whatever they grab sets up the rest of the day.</p>
<p>If you fix one meal, fix that one. <a href="/how-much-protein-after-40">How much protein you need after 40</a> covers the target, <a href="/high-protein-fast-food-after-40">the fast food guide</a> covers the rest of the week, and there is <a href="/eat-out-lose-fat">a restaurant playbook</a> you can keep on your phone.</p>
<p>Starbucks changes its menu constantly. Check the current nutrition information if you are tracking closely.</p>
<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chipotle-after-40">Chipotle</a>: 81 g of protein, or 1,400 calories</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: about 340 mg of sodium in a full bowl, the lowest on this site</li><li><a href="/five-guys-after-40">Five Guys</a>: a bunless burger is 440 calories, 32 g protein and almost no salt</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips are about 200 calories for 30 g of protein</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders are 280 calories and 47 g of protein</li><li><a href="/cava-after-40">CAVA</a>: curated bowls are close to a day of salt, so build your own</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: five breaded tenders beat the charbroiled sandwich at the same calories</li><li><a href="/dunkin-after-40">Dunkin</a>: the Wake-Up Wrap is 7 to 8 g of protein, which is a snack</li><li><a href="/wingstop-after-40">Wingstop</a>: six plain wings are 540 calories and 60 g of protein</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap Charburger is 290 calories against 470 to 520 on a bun</li><li><a href="/rubios-after-40">Rubio's</a>: the Original Fish Taco is 9 g of protein for 330 calories</li><li><a href="/mcdonalds-after-40">McDonald's</a>: the McDouble is 390 calories and 22 g protein, beating the Big Mac</li><li><a href="/taco-bell-after-40">Taco Bell</a>: three soft chicken tacos give 36 g of protein, beating the Power Bowl</li><li><a href="/wendys-after-40">Wendy's</a>: the chili is the only fast food side with real protein in it</li><li><a href="/subway-after-40">Subway</a>: a rotisserie chicken bowl is 220 calories and 31 g of protein</li><li><a href="/panda-express-after-40">Panda Express</a>: super greens with teriyaki chicken is 470 calories and 50 g of protein</li></ul>
<p>All of them follow the same idea: find the protein, spot the one item doing the damage, and order so you are not the person at the table eating differently from everyone else.</p>

{CTA}"""

faqs = [
    ("What is the highest protein drink at Starbucks?",
     "The iced protein matcha, at around 36 grams of protein for about 300 calories. The iced vanilla protein latte is close behind at about 29 grams for 270 calories."),
    ("How much protein is in Starbucks protein cold foam?",
     "Around 15 grams for roughly 70 to 90 calories, added to any cold drink. It is the easiest way to add real protein to a coffee you were buying anyway."),
    ("What is the best high-protein breakfast at Starbucks?",
     "A protein latte with egg bites. Egg white and roasted red pepper bites are about 170 calories and 12 to 13 grams, bacon and gruyere about 300 and 19. Together with a protein latte that is 25 to 45 grams of protein for under 500 calories."),
    ("Are Starbucks protein drinks high in sugar?",
     "Several are, around 27 to 34 grams in a grande. Asking for sugar-free vanilla keeps the protein and removes most of the sugar, which matters if you are managing blood sugar."),
    ("What should I avoid at Starbucks if I am losing fat?",
     "The venti blended drinks with whipped cream. They run 400 to 500 calories with almost no protein, and because they are liquid they do very little for hunger."),
]

html = page(
    SLUG,
    "Starbucks After 40: What to Order | Fig Performance",
    "How to order at Starbucks after 40: protein lattes at 29g, cold foam that adds 15g, the egg bites worth buying, and the drink that quietly costs you most.",
    "Starbucks After 40: What to Order",
    "Fitness after 40", "How to get 29 grams of protein at Starbucks, in the line you already stand in.",
    "Protein lattes, cold foam, and the egg bites worth buying.",
    [("protein-drinks", "The drinks changed"), ("food", "The egg bites"), ("avoid", "What costs you most"),
     ("order", "What I would order"), ("why", "Why a coffee shop"), ("more", "The other guides")],
    body, faqs, "Starbucks after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
