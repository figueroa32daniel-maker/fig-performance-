"""Article: El Pollo Loco after 40. DRAFT Nov 25 2026, not published until Dan approves.
Figures from El Pollo Loco's published nutrition guide and their Protein Packed menu.
Dave has nothing on this chain and it is everywhere in Orange County."""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "el-pollo-loco-after-40"

body = f"""<p class="legal-intro">A fire-grilled chicken breast here is 200 calories and 34 grams of protein, a better protein-to-calorie ratio than almost anything you will cook at home, for about six dollars, five minutes from most of Placentia. The calories are not the issue at this restaurant, which is why I tell clients to stop looking at that column. There is a different number on the menu that matters more, and it matters most to the people who have had a doctor mention blood pressure.</p>

<h2 id="chicken">The chicken itself is the best thing on any menu around here</h2>
<p>Published numbers for the fire-grilled pieces:</p>
<ul>
  <li><strong>Breast:</strong> 200 calories, 34 g protein, 8 g fat</li>
  <li><strong>Thigh:</strong> 200 calories, 21 g protein, 12 g fat</li>
  <li><strong>Leg:</strong> 110 calories, 11 g protein</li>
  <li><strong>Wing:</strong> 70 calories, 10 g protein</li>
</ul>
<p>The breast is the one. Thirty-four grams for 200 calories is a ratio you normally only get from a chicken breast you grilled yourself, egg whites or a protein shake. Two of them is 68 grams of protein for 400 calories, which covers most adults' entire protein target for a day in one sitting.</p>
{stats([("200 cal", "fire-grilled breast"), ("34 g", "protein in it"), ("68 g", "if you order two")])}

<h2 id="sodium">Now the number I actually watch</h2>
<p>Sodium. El Pollo Loco bowls are enormous on it, and almost nobody mentions this.</p>
<ul>
  <li><strong>Original Pollo Bowl:</strong> 580 calories, 41 g protein, <strong>2,030 mg sodium</strong></li>
  <li><strong>Double Chicken Bowl:</strong> 930 calories, 74 g protein, <strong>2,670 mg sodium</strong></li>
</ul>
<p>The general guidance for adults is to stay under about 2,300 mg of sodium a day. One Double Chicken Bowl clears that on its own, before breakfast and dinner are counted.</p>
<p>If you are over 40 and your doctor has mentioned your blood pressure, that matters more than any calorie figure on this page. It does not mean never eat there. It means order the chicken and the salad rather than the bowl, because the sodium is in the rice, the beans and the sauces, not in the grilled chicken.</p>
{pullquote("The chicken is excellent. The bowl it comes in is where the problem lives.")}

<h2 id="salad">The quietly best item on the menu</h2>
<p>The Mexican Caesar Salad is listed at 52 grams of protein for 350 calories. That is the best protein-per-calorie meal of any restaurant I have written about, and most people have never ordered it.</p>
<p>El Pollo Loco has also put out a Protein Packed menu, more than twenty items built around the grilled chicken, with the Double Chicken Bowl at 74 grams leading on protein and a lot of options in the 40 to 60 gram range.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Mexican Caesar Salad.</strong> 52 g of protein for 350 calories. If you take nothing else from this page, take this line.</li>
  <li><strong>Two fire-grilled chicken breasts and a side salad.</strong> Around 450 calories, close to 70 grams of protein, and far less sodium than any bowl.</li>
  <li><strong>Original Pollo Bowl</strong> if you want the full meal and the sodium is not a concern for you. 580 calories, 41 grams.</li>
  <li><strong>Ask for the sauces on the side.</strong> This is where a lot of the sodium and most of the hidden calories sit.</li>
</ol>
{callout("For an Orange County week", "Three orders worth memorising", ["Mexican Caesar Salad: 52 g protein, 350 cal", "Two grilled breasts and a salad: ~70 g protein", "Skip the bowl if blood pressure is on your radar"])}

<h2 id="why">Why this one is on the list at all</h2>
<p>Because it is fire-grilled chicken, not breaded, and because there is one on practically every major street in north Orange County. Convenience is most of what decides whether a plan survives a bad week, and this is about as convenient as high-protein food gets around here.</p>
<p>The wider version of this is in <a href="/high-protein-fast-food-after-40">my guide to high-protein fast food after 40</a>, with <a href="/eat-out-lose-fat">a free restaurant playbook</a> for your phone. If you have not worked out your target yet, start with <a href="/how-much-protein-after-40">how much protein you need after 40</a>.</p>
<p>Menus and recipes change. Check El Pollo Loco's current nutrition guide if you are tracking closely, especially for sodium.</p>
<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chipotle-after-40">Chipotle</a>: 81 g of protein, or 1,400 calories</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li></ul>
<p>All of them follow the same idea: find the protein, spot the one item doing the damage, and order so you are not the person at the table eating differently from everyone else.</p>

{CTA}"""

faqs = [
    ("Is El Pollo Loco healthy?",
     "The fire-grilled chicken is one of the best high-protein options in fast food: a breast is about 200 calories and 34 grams of protein. The thing to watch is sodium, because the bowls run from roughly 2,030 to 2,670 mg, which is at or above a whole day's guidance."),
    ("What is the highest protein item at El Pollo Loco?",
     "The Double Chicken Bowl at about 74 grams of protein for 930 calories. For protein per calorie, the Mexican Caesar Salad is better: around 52 grams for 350 calories."),
    ("How much protein is in an El Pollo Loco chicken breast?",
     "About 34 grams for 200 calories, with 8 grams of fat. Two breasts gets most adults to roughly 68 grams, which is a full day's target for many people."),
    ("What is the lowest sodium option at El Pollo Loco?",
     "The grilled chicken pieces themselves, with a salad, and sauces on the side. The sodium sits in the rice, beans and sauces that come with the bowls, not in the grilled chicken."),
    ("Is El Pollo Loco good for weight loss?",
     "It can be, because the protein is high and the chicken is grilled rather than fried. A Mexican Caesar Salad or two grilled breasts with a side salad will support fat loss. A Double Chicken Bowl at 930 calories is a bigger meal than most people need in one sitting."),
]

html = page(
    SLUG,
    "El Pollo Loco After 40: What to Order | Fig Performance",
    "What to order at El Pollo Loco after 40: 34g of protein in a grilled breast, the 52g salad nobody orders, and the sodium number in the bowls worth knowing.",
    "El Pollo Loco After 40: What to Order",
    "Fitness after 40", "Stop reading the calorie column at El Pollo Loco. It is the wrong number to worry about.",
    "34 grams of protein for 200 calories, and the number nobody mentions.",
    [("chicken", "The chicken itself"), ("sodium", "The number I watch"), ("salad", "The best item on the menu"),
     ("order", "What I would order"), ("why", "Why it is on the list"), ("more", "The other guides")],
    body, faqs, "El Pollo Loco after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
