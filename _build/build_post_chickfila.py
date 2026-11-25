"""Article: Chick-fil-A after 40. DRAFT Nov 25 2026, not published until Dan approves.
Figures are Chick-fil-A's published nutrition values."""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "chick-fil-a-after-40"

body = f"""<p class="legal-intro">You have been told that ordering grilled instead of fried is the healthy choice at Chick-fil-A. The original Chicken Sandwich is 420 calories and 29 grams of protein. The grilled one is 390 and 28. Thirty calories and one gram apart. The difference everyone assumes is enormous is almost nothing, the real gap is somewhere else on that label, and the best item on the board is not either sandwich. Here is how I tell clients to order.</p>

<h2 id="nuggets">The grilled nuggets are the whole story</h2>
<p>Published numbers, straight across:</p>
<ul>
  <li><strong>8-count grilled nuggets:</strong> 130 calories, 25 g protein, 1 g carbs, 440 mg sodium</li>
  <li><strong>8-count breaded nuggets:</strong> 250 calories, 27 g protein, 1,210 mg sodium</li>
  <li><strong>12-count grilled nuggets:</strong> about 200 calories, 38 g protein</li>
</ul>
<p>Look at the first and last lines. Twelve grilled nuggets give you 38 grams of protein for about 200 calories. For comparison, the Spicy Deluxe sandwich has 34 grams and 540 calories. You get more protein from the nuggets for a third of the calories.</p>
{stats([("130 cal", "8 grilled nuggets"), ("25 g", "protein in them"), ("440 mg", "sodium, a third of the breaded")])}
<p>The sodium gap is the part nobody mentions. The breaded 8-count carries 1,210 mg against 440 for grilled. If you are over 40 and your doctor has said anything at all about blood pressure, that one swap is worth more to you than the calories are.</p>

<h2 id="sandwiches">The sandwiches, honestly</h2>
<p>The original Chicken Sandwich is 420 calories and 29 grams of protein. The Grilled Chicken Sandwich is 390 calories and 28 grams. Thirty calories and one gram apart.</p>
<p>So if you want the fried one, have the fried one. The difference people assume is enormous is almost nothing. Where they genuinely separate is sodium: 1,460 mg for the original against 765 for the grilled.</p>
{pullquote("The fried sandwich is not the problem. The fried sandwich plus waffle fries plus a milkshake is the problem, and that is a different sentence.")}

<h2 id="drink">The milkshake costs more than the sandwich</h2>
<p>A vanilla milkshake is about 580 calories. The Chicken Sandwich is 420. The drink is bigger than the meal, and because it is liquid it does almost nothing for how full you feel an hour later.</p>
<p>This is the single most common way a reasonable Chick-fil-A order turns into 1,500 calories. Sandwich, medium waffle fries, sauce and a shake lands around 1,560.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>12-count grilled nuggets and a medium fruit cup.</strong> About 270 calories and 39 grams of protein. There is not a better protein-per-calorie meal in fast food.</li>
  <li><strong>Grilled Chicken Sandwich</strong> if you want something that eats like a proper meal. 390 calories, 28 grams, and the lowest sodium of any sandwich on the board.</li>
  <li><strong>8-count grilled nuggets</strong> when your appetite is low or dinner is coming. 130 calories, 25 grams.</li>
  <li><strong>Water or a diet lemonade.</strong> Saves you 400 to 600 calories against a shake and you will not notice by evening.</li>
</ol>
{callout("If you remember one thing", "Grilled, not breaded", ["Same protein, about half the calories", "A third of the sodium", "The nuggets beat every sandwich on protein per calorie"])}

<h2 id="why">Why I never tell clients to avoid it</h2>
<p>Because they have kids, and the kids want Chick-fil-A, and a plan that cannot survive a Tuesday evening with a nine-year-old is not a plan. The grilled nuggets mean you can sit at the same table and eat something that genuinely helps you.</p>
<p>The broader version of this is in <a href="/high-protein-fast-food-after-40">my guide to high-protein fast food after 40</a>, and there is <a href="/eat-out-lose-fat">a free restaurant playbook</a> for your phone. If you are not sure what you are aiming at, start with <a href="/how-much-protein-after-40">how much protein you need after 40</a>.</p>
<p>Menus change, so check the current nutrition information if you are tracking closely.</p>
<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chipotle-after-40">Chipotle</a>: 81 g of protein, or 1,400 calories</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li></ul>
<p>All of them follow the same idea: find the protein, spot the one item doing the damage, and order so you are not the person at the table eating differently from everyone else.</p>

{CTA}"""

faqs = [
    ("What is the healthiest thing at Chick-fil-A?",
     "Grilled nuggets. An 8-count is 130 calories with 25 grams of protein and 440 mg of sodium. A 12-count with a medium fruit cup comes to about 270 calories and 39 grams of protein."),
    ("How much protein is in Chick-fil-A grilled nuggets?",
     "About 25 grams in an 8-count and about 38 grams in a 12-count, for roughly 130 and 200 calories. That is more protein than the Spicy Deluxe sandwich at under half the calories."),
    ("Is the grilled chicken sandwich better than the fried one?",
     "Barely, on calories and protein: 390 and 28 grams against 420 and 29. The real difference is sodium, 765 mg against 1,460. If blood pressure matters to you, take the grilled one."),
    ("Can I eat Chick-fil-A and still lose fat?",
     "Yes. The order is what decides it. Grilled nuggets and water will support fat loss. A sandwich with waffle fries and a milkshake is around 1,560 calories, which will not."),
    ("What should I skip at Chick-fil-A?",
     "The milkshake, if you are in a deficit. A vanilla shake is about 580 calories, more than the Chicken Sandwich, and being liquid it does very little for fullness."),
]

html = page(
    SLUG,
    "Chick-fil-A After 40: What to Order | Fig Performance",
    "What to order at Chick-fil-A after 40: grilled nuggets at 25g protein for 130 calories, the real sandwich difference, and the drink that costs more than the meal.",
    "Chick-fil-A After 40: What to Order",
    "Fitness after 40", "The biggest lie you have been told about fried chicken.",
    "Grilled instead of fried saves you 30 calories and costs you a gram of protein.",
    [("nuggets", "The grilled nuggets"), ("sandwiches", "The sandwiches, honestly"), ("drink", "The milkshake problem"),
     ("order", "What I would order"), ("why", "Why I do not say avoid it"), ("more", "The other guides")],
    body, faqs, "Chick-fil-A after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
