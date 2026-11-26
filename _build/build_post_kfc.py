"""Article: KFC after 40. DRAFT Nov 25 2026, not published until Dan approves.

Dave has NOTHING on KFC. Cleanest data in the batch: six independent sources give
the Original Recipe breast at 390 cal / 39 g / 1,190 mg sodium, and five give the
Kentucky Grilled breast at 210 cal / 38 g. One outlier FAQ page claimed 250-300 cal
and 30 g for the grilled breast while its own calculator said 210/38, so it was
discarded. IMPORTANT and flagged in the article: at least one source reports that
grilled chicken is not currently on the nationwide menu, so the page tells readers
to check their own location rather than promising availability.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "kfc-after-40"

body = f"""<p class="legal-intro">Extra Crispy and Original Recipe are the same cut of chicken. The breading is the only difference, and it is worth about 140 calories and 14 grams of fat on a breast piece. Most people treat that choice as a matter of taste. It is a matter of taste that costs more than a side.</p>

<h2 id="crispy">Original Recipe against Extra Crispy</h2>
<p>Same bird, same piece, two coatings:</p>
<ul>
  <li><strong>Original Recipe breast:</strong> 390 calories, 39 g protein, 21 g fat, 1,190 mg sodium</li>
  <li><strong>Extra Crispy breast:</strong> about 530 calories, roughly 35 g fat</li>
</ul>
<p>That is 140 calories and 14 grams of fat for a thicker crust, with no protein gained. If you prefer Extra Crispy, have it. Just know you are paying a side dish for it.</p>
{stats([("390 cal", "Original Recipe breast"), ("530 cal", "Extra Crispy, same cut"), ("+0 g", "protein gained")])}

<h2 id="grilled">The grilled breast, if your store has it</h2>
<p>Kentucky Grilled Chicken is the best thing on this menu for an adult over 40, and the numbers are not close:</p>
<ul>
  <li><strong>Kentucky Grilled breast:</strong> about 210 calories, 38 g protein, 7 g fat, 0 g carbs</li>
  <li><strong>Original Recipe breast:</strong> 390 calories, 39 g protein</li>
</ul>
<p>One gram of protein apart. One hundred and eighty calories apart. That is one of the largest gaps for the smallest trade-off anywhere in this series.</p>
{pullquote("One gram of protein apart. A hundred and eighty calories apart. Same chicken.")}
<p><strong>The catch:</strong> availability varies by store. At least one nutrition guide reports grilled chicken is no longer a nationwide item, and some locations have dropped it. The two closest to the studio, on Yorba Linda Boulevard and on Imperial Highway, have been carrying it. Menus change without much warning, so call ahead if you are driving somewhere specifically for it. If your store does not have it, the Original Recipe breast is the fallback and it is still 39 grams of protein.</p>

<h2 id="sodium">Sodium, again</h2>
<p>A single Original Recipe breast carries about 1,190 mg. That is not catastrophic on its own, but it is half a day's worth in one piece of chicken before biscuits, gravy or sides enter the picture.</p>
<p>Same note as El Pollo Loco, Jersey Mike's and Panera: if your doctor has mentioned blood pressure, this is the column to read at a fried chicken restaurant, not the fat.</p>

<h2 id="pieces">The pieces are not interchangeable</h2>
<p>An Original Recipe drumstick is about 130 calories with roughly 12 grams of protein. The breast is 390 with 39. Per calorie they are similar, but the breast gives you three times the protein in one piece, which matters when the goal is hitting a target rather than nibbling.</p>
<p>For most people over 40 the useful move is one breast rather than three small pieces, because the small pieces carry proportionally more skin and breading for the meat you get.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Kentucky Grilled breast if the store has it.</strong> 210 calories, 38 grams of protein. Nothing else on the menu comes close.</li>
  <li><strong>Original Recipe, not Extra Crispy,</strong> if grilled is not available. Saves 140 calories for the same protein.</li>
  <li><strong>Breast over a pile of small pieces.</strong> More meat, less coating.</li>
  <li><strong>Green beans or corn on the cob</strong> over the biscuit and the mac. The biscuit is where a reasonable order quietly stops being one.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Extra Crispy costs 140 calories over Original Recipe for zero extra protein", "Grilled breast is 210 cal and 38 g, if your store still has it", "Sodium is about 1,190 mg in one breast"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because fried chicken is the food people assume is automatically off the table, and that assumption is what makes them order badly when they end up there anyway. A KFC breast is 39 grams of protein. That is a real meal. The thing that turns it into a problem is the coating you chose without thinking and the two sides that came with it.</p>
<p>Knowing one sentence, order Original Recipe not Extra Crispy, is worth more over a year than any amount of deciding you will never go.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>This is the best-sourced page in the series. Six independent nutrition breakdowns give the Original Recipe breast at 390 calories, 39 grams of protein and 1,190 mg of sodium, and five give the Kentucky Grilled breast at 210 calories and 38 grams. One page claimed the grilled breast was 250 to 300 calories with 30 grams of protein while its own calculator said 210 and 38, so that figure was discarded rather than averaged in. The availability of grilled chicken is the genuinely uncertain part here. The note about the Yorba Linda Boulevard and Imperial Highway locations comes from Coach Dan rather than from a published source, and chains change menus without announcing it, so this page tells you to call ahead rather than pretending to know.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: about 340 mg of sodium in a full bowl, the lowest on this site</li><li><a href="/five-guys-after-40">Five Guys</a>: a bunless burger is 440 calories, 32 g protein and almost no salt</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips are about 200 calories for 30 g of protein</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders are 280 calories and 47 g of protein</li><li><a href="/cava-after-40">CAVA</a>: curated bowls are close to a day of salt, so build your own</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: five breaded tenders beat the charbroiled sandwich at the same calories</li><li><a href="/dunkin-after-40">Dunkin</a>: the Wake-Up Wrap is 7 to 8 g of protein, which is a snack</li><li><a href="/wingstop-after-40">Wingstop</a>: six plain wings are 540 calories and 60 g of protein</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap Charburger is 290 calories against 470 to 520 on a bun</li><li><a href="/rubios-after-40">Rubio's</a>: the Original Fish Taco is 9 g of protein for 330 calories</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("How much protein is in a KFC chicken breast?",
     "An Original Recipe breast has about 390 calories and 39 grams of protein, with roughly 1,190 mg of sodium. A Kentucky Grilled breast has about 210 calories and 38 grams, which is nearly the same protein for 180 fewer calories."),
    ("Is Original Recipe or Extra Crispy better for weight loss?",
     "Original Recipe. An Extra Crispy breast adds about 140 calories and 14 grams of fat over the Original Recipe version of the same cut, and gains you no extra protein. It is purely the coating."),
    ("Does KFC still have grilled chicken?",
     "It depends on the store. At least one nutrition guide reports it is no longer a nationwide menu item, though the locations nearest Placentia, on Yorba Linda Boulevard and on Imperial Highway, have been carrying it. Call ahead if you are making a trip for it. Where it is available, the Kentucky Grilled breast at roughly 210 calories and 38 grams of protein is the best order in the building."),
    ("Can you eat KFC and still lose fat?",
     "Yes, if the order fits your calories and hits your protein. A breast piece is 39 grams of protein, which is a real meal. What usually ruins it is choosing Extra Crispy without thinking about it and adding a biscuit and a mac and cheese."),
    ("What is the healthiest thing to order at KFC?",
     "Kentucky Grilled breast if your store carries it, otherwise an Original Recipe breast, with green beans or corn on the cob instead of the biscuit. One breast beats a pile of small pieces, which carry more skin and breading for the meat you get."),
]

html = page(
    SLUG,
    "KFC After 40: What to Order | Fig Performance",
    "What to order at KFC after 40: why Extra Crispy costs 140 calories for no extra protein, the 210-calorie grilled breast, and the sodium in one piece.",
    "KFC After 40: What to Order",
    "Fitness after 40", "Stop ordering Extra Crispy at KFC. It is 140 calories of breading.",
    "Same cut of chicken, same protein. The coating is the whole difference.",
    [("crispy", "Original Recipe vs Extra Crispy"), ("grilled", "The grilled breast"), ("sodium", "The sodium number"),
     ("pieces", "The pieces are not equal"), ("order", "What I would order"), ("why", "Why it is on the list"),
     ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "KFC after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
