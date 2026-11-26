"""Article: Chipotle after 40. DRAFT Nov 25 2026, not published until Dan approves.
Figures are Chipotle's published nutrition values, including the official high-protein
menu it launched in December 2025."""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "chipotle-after-40"

body = f"""<p class="legal-intro">Almost every client I have coached has tried to eat <em>less</em> at Chipotle. Order the salad, hold the rice, go easy on the chicken because it sounds like a lot of meat. It goes wrong every time, because none of that is where the calories live. Chipotle is the easiest place in Orange County to hit a protein target and the easiest place to eat 1,000 calories believing you ate a salad, and the fix is to add meat, not subtract it. Here is how I tell clients to order.</p>

<h2 id="chicken">Start with the chicken, and consider doubling it</h2>
<p>Chipotle's adobo chicken is the best protein-per-calorie item on the menu. A 4 oz portion is about 180 calories and 32 grams of protein. Steak is about 150 calories and 23 grams, so it looks leaner on the calorie line and gives you nine grams less.</p>
<p>Doubling the chicken costs you another 180 calories and buys another 32 grams of protein. For most adults over 40 trying to hold muscle, that is the single best trade available in any fast-casual restaurant in the country.</p>
{stats([("180 cal", "4 oz adobo chicken"), ("32 g", "protein in it"), ("64 g", "if you double it")])}

<h2 id="menu">The official high-protein menu</h2>
<p>In December 2025 Chipotle added a high-protein menu, which saved me a lot of explaining. The published numbers:</p>
<ul>
  <li><strong>Double High Protein Bowl:</strong> 81 g protein, 760 calories. Double adobo chicken, light white rice, black beans, fajita veggies, tomato salsa, Monterey Jack, extra romaine.</li>
  <li><strong>High Protein, High Fiber Bowl:</strong> 46 g protein, 540 calories, 14 g fiber.</li>
  <li><strong>High Protein, Low Calorie Bowl:</strong> 36 g protein, 470 calories.</li>
  <li><strong>High Protein Cup:</strong> 32 g protein, 180 calories. Four ounces of chicken on its own.</li>
</ul>
<p>That last one is quietly the most useful item on the board. It is a protein portion you can add to anything, or eat in the car at 4 pm when dinner is three hours away and you are about to make a decision you regret.</p>
{pullquote("Eighty-one grams of protein in one bowl. There is no supplement aisle version of that which tastes better or costs less.")}

<h2 id="creep">Where the calories actually come from</h2>
<p>The popular build is chicken, white rice, black beans, tomato salsa, cheese and sour cream. That is about 765 calories and 52 grams of protein. Perfectly fine if that fits your day.</p>
<p>The problem is that the same bowl with a tortilla, guacamole, queso and chips alongside clears 1,400 without feeling like a bigger meal, because none of the additions change the look of what is in front of you. The calories hide in the toppings, not the protein.</p>
{callout("The four decisions", "Everything else is noise", ["Double chicken, almost always", "One starch, not three: rice or tortilla or chips", "Guacamole or cheese or sour cream, pick one", "Salsa and fajita veggies are free volume, use them"])}

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Bowl, double chicken, light white rice, black beans, fajita veggies, tomato salsa, lettuce.</strong> Around 600 to 650 calories with roughly 70 grams of protein. This is the order.</li>
  <li><strong>Want it lighter?</strong> Swap the rice for supergreens. You lose about 200 calories and keep all the protein.</li>
  <li><strong>Want guacamole?</strong> Have it, and drop the rice. It is one or the other, not both.</li>
  <li><strong>Skip the chips.</strong> Not because they are bad, but because they are the one item that adds several hundred calories and no protein, and nobody has ever stopped at half a bag.</li>
</ol>
<p>Sodium is worth a word. Chipotle bowls run high, often over 1,000 mg once the salsas and cheese are in. If you are watching blood pressure, that matters more than the calories do, and going lighter on the salsas and the cheese is the lever.</p>

<h2 id="why">Why this is the restaurant I recommend most</h2>
<p>Because you can see the food being built, every ingredient has a published number, and the protein is not hiding under breading. That combination does not exist at most places.</p>
<p>For the wider version of this, I wrote <a href="/high-protein-fast-food-after-40">a guide to high-protein fast food after 40</a>, and there is <a href="/eat-out-lose-fat">a free restaurant playbook</a> you can keep on your phone. If you are not sure what your protein target even is, start with <a href="/how-much-protein-after-40">how much you actually need after 40</a>.</p>
<p>Menus and recipes change. Check Chipotle's current nutrition calculator if you are tracking closely, because this page will not update itself.</p>
<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: about 340 mg of sodium in a full bowl, the lowest on this site</li><li><a href="/five-guys-after-40">Five Guys</a>: a bunless burger is 440 calories, 32 g protein and almost no salt</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips are about 200 calories for 30 g of protein</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders are 280 calories and 47 g of protein</li><li><a href="/cava-after-40">CAVA</a>: curated bowls are close to a day of salt, so build your own</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: five breaded tenders beat the charbroiled sandwich at the same calories</li><li><a href="/dunkin-after-40">Dunkin</a>: the Wake-Up Wrap is 7 to 8 g of protein, which is a snack</li><li><a href="/wingstop-after-40">Wingstop</a>: six plain wings are 540 calories and 60 g of protein</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap Charburger is 290 calories against 470 to 520 on a bun</li><li><a href="/rubios-after-40">Rubio's</a>: the Original Fish Taco is 9 g of protein for 330 calories</li><li><a href="/mcdonalds-after-40">McDonald's</a>: the McDouble is 390 calories and 22 g protein, beating the Big Mac</li><li><a href="/taco-bell-after-40">Taco Bell</a>: three soft chicken tacos give 36 g of protein, beating the Power Bowl</li><li><a href="/wendys-after-40">Wendy's</a>: the chili is the only fast food side with real protein in it</li><li><a href="/subway-after-40">Subway</a>: a rotisserie chicken bowl is 220 calories and 31 g of protein</li><li><a href="/panda-express-after-40">Panda Express</a>: super greens with teriyaki chicken is 470 calories and 50 g of protein</li><li><a href="/daves-hot-chicken-after-40">Dave's Hot Chicken</a>: one tender is 490 calories, not the 150 your app says</li><li><a href="/portillos-after-40">Portillo's</a>: the dressing adds 340 calories to every salad on the menu</li></ul>
<p>All of them follow the same idea: find the protein, spot the one item doing the damage, and order so you are not the person at the table eating differently from everyone else.</p>

{CTA}"""

faqs = [
    ("What is the highest protein order at Chipotle?",
     "Chipotle's own Double High Protein Bowl, at 81 grams of protein for 760 calories. It is double adobo chicken with light white rice, black beans, fajita veggies, tomato salsa, Monterey Jack and extra romaine."),
    ("Is Chipotle good for weight loss?",
     "It can be one of the best options available, because the protein is high and every ingredient has a published number. A bowl with double chicken, light rice, beans, salsa and lettuce lands around 600 to 650 calories with close to 70 grams of protein."),
    ("Chicken or steak at Chipotle?",
     "Chicken, if protein is what you are after. Adobo chicken is about 180 calories and 32 grams of protein per portion. Steak is about 150 calories and 23 grams, so you give up nine grams to save 30 calories."),
    ("How many calories is a normal Chipotle bowl?",
     "The most popular build, with chicken, white rice, black beans, tomato salsa, cheese and sour cream, is about 765 calories and 52 grams of protein. Adding a tortilla, guacamole, queso and chips can take the same meal past 1,400."),
    ("What should I skip at Chipotle?",
     "Chips, if you are in a deficit. They add several hundred calories and almost no protein, and most people do not stop at half. Past that, pick one of guacamole, cheese or sour cream rather than all three."),
]

html = page(
    SLUG,
    "Chipotle After 40: What to Order | Fig Performance",
    "How to order at Chipotle if you are over 40: the high-protein menu numbers, double chicken, and where the calories actually hide. From Coach Dan in Placentia.",
    "Chipotle After 40: What to Order",
    "Fitness after 40", "Hot take: the problem with your Chipotle bowl is that there is not enough chicken in it.",
    "The protein is not what turns this into 1,400 calories. The things next to it are.",
    [("chicken", "Start with the chicken"), ("menu", "The high-protein menu"), ("creep", "Where the calories come from"),
     ("order", "What I would order"), ("why", "Why I recommend it most"), ("more", "The other guides")],
    body, faqs, "Chipotle after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
