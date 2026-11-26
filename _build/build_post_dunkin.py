"""Article: Dunkin' after 40. DRAFT Nov 25 2026. Standing approval, restaurant cluster.

Dave has NOTHING on Dunkin'.

SOURCING: four sources give the Wake-Up Wrap at 180 cal; protein splits 7 vs 8 g
and sodium splits 430 vs 470 mg, both given as ranges. Four give the Egg White &
Veggie wrap at 190 cal. Omelet Bites at 180 cal / 13 g protein.

THE HONEST ANGLE: Dunkin' is a LOW protein restaurant. Its best food item is 13 g.
That is not a meal for an adult over 40, and the article says so plainly rather
than pretending the Wake-Up Wrap is breakfast. Direct contrast with Starbucks,
which now runs protein lattes near 29 g.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "dunkin-after-40"

body = f"""<p class="legal-intro">A Dunkin' Wake-Up Wrap is about 180 calories with roughly 7 to 8 grams of protein. That is a perfectly reasonable thing to eat. It is not breakfast. For an adult over 40 trying to hold onto muscle, seven grams at seven in the morning is the amount of protein that guarantees you are hungry again at ten.</p>

<h2 id="protein">The protein problem</h2>
<p>This is the lowest protein restaurant in any of these guides, and that is the single most useful thing to know before you walk in:</p>
<ul>
  <li><strong>Wake-Up Wrap:</strong> about 180 calories, roughly 7 to 8 g protein</li>
  <li><strong>Egg White and Veggie Wake-Up Wrap:</strong> about 190 calories, roughly 8 to 9 g protein</li>
  <li><strong>Egg White and Veggie Omelet Bites:</strong> about 180 calories, roughly 13 g protein</li>
  <li><strong>Egg and Cheese sandwich:</strong> about 440 calories, roughly 15 g protein</li>
</ul>
<p>The best protein-per-calorie item in the building is 13 grams. At Popeyes you can get 47 grams for 280 calories. That is not a criticism of Dunkin', it is a description of what the menu is built to do.</p>
{stats([("13 g", "best protein item here"), ("47 g", "five tenders at Popeyes"), ("180 cal", "both of them")])}

<h2 id="bites">Omelet bites are the order</h2>
<p>If you are eating here, the Egg White and Veggie Omelet Bites are the pick. Around 180 calories, roughly 13 grams of protein, and only about 7 grams of carbohydrate. That is nearly double the protein of a Wake-Up Wrap at the same calories.</p>
<p>Two orders of those gets you to about 26 grams, which is a real breakfast. One order is a snack with a coffee, and there is nothing wrong with that as long as you know which one you bought.</p>
{pullquote("Seven grams at seven in the morning is why you are hungry at ten.")}

<h2 id="starbucks">Why Starbucks pulled ahead here</h2>
<p>Worth saying plainly, because it changes where I send people. Starbucks put protein-boosted milk and a protein cold foam on its permanent menu, which means the coffee itself can carry close to 29 grams. Dunkin' has no equivalent, so the protein has to come from the food.</p>
<p>If your morning stop is about getting protein in on the way to work, Starbucks is currently the better building. If it is about coffee and you are eating properly later, Dunkin' is fine and cheaper.</p>

<h2 id="sodium">Sodium and the donut question</h2>
<p>Sodium in the wraps runs somewhere around 430 to 470 mg, which is unremarkable. The thing worth watching here is not salt, it is that this is a bakery, and the items that arrive with the coffee are mostly sugar and flour.</p>
<p>That is not news to anyone. The useful version is this: decide about the donut before you are in the queue looking at it, the same way you decide about the fries at Five Guys before you order.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Egg White and Veggie Omelet Bites.</strong> About 180 calories, roughly 13 g protein. Best item here.</li>
  <li><strong>Two orders of them</strong> if this is actually your breakfast. About 26 g of protein.</li>
  <li><strong>Black coffee or an unsweetened iced coffee.</strong> The flavoured drinks carry most of the sugar in this restaurant.</li>
  <li><strong>Treat one Wake-Up Wrap as a snack,</strong> not a meal, and plan the rest of your morning around that.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Best protein item here is about 13 g", "A Wake-Up Wrap is a snack at 7 to 8 g", "If you want protein with coffee, Starbucks has more"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because plenty of my clients stop here every single morning, and the trap is not the donut. Everyone already knows about the donut. The trap is a 180 calorie wrap that feels like a decision made in good faith and leaves you eleven grams short of a breakfast, every day, for a year.</p>
<p>Protein first thing matters more after 40 than it did at 25, and this is the restaurant where it is easiest to accidentally skip.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>Four independent sources give the Wake-Up Wrap at 180 calories. Its protein splits between 7 and 8 grams and its sodium between 430 and 470 mg depending on the source, so both are given as ranges above. The Egg White and Veggie wrap at 190 calories is likewise agreed by four sources. Builds differ slightly between the meat and non-meat versions of each wrap, so treat these as close rather than exact, and check Dunkin's current nutrition information if you are tracking tightly.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: lowest sodium meal on this site</li><li><a href="/five-guys-after-40">Five Guys</a>: bunless is 440 calories and almost no salt</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips, 200 calories and 30 g</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders, 280 calories and 47 g</li><li><a href="/cava-after-40">CAVA</a>: the curated bowls are a day of salt</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: the breaded tenders beat the charbroiled sandwich</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/wingstop-after-40">Wingstop</a>: six plain wings are 540 calories and 60 g of protein</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("How much protein is in a Dunkin' Wake-Up Wrap?",
     "About 7 to 8 grams, at roughly 180 calories. That is a snack rather than a breakfast for most adults over 40, and it is the main thing to understand about eating here."),
    ("What is the highest protein item at Dunkin'?",
     "The Egg White and Veggie Omelet Bites, at about 180 calories with roughly 13 grams of protein and only around 7 grams of carbohydrate. That is nearly double the protein of a Wake-Up Wrap at the same calories."),
    ("Is Dunkin' or Starbucks better for protein?",
     "Starbucks, currently and clearly. Starbucks put protein-boosted milk and a protein cold foam on its permanent menu, so the drink itself can carry close to 29 grams. Dunkin' has no equivalent, so all the protein has to come from the food, where the best item is 13 grams."),
    ("Can I have a proper breakfast at Dunkin'?",
     "Yes, but you have to order for it. Two servings of Egg White and Veggie Omelet Bites comes to around 360 calories with roughly 26 grams of protein, which is a real breakfast. One wrap on its own is not."),
    ("Is Dunkin' bad for weight loss?",
     "Not especially. The calories are modest and the sodium is unremarkable. The risk is different here: it is easy to eat a 180 calorie item that feels like a sensible breakfast and leaves you short on protein, hungry mid-morning, and eating again before lunch."),
]

html = page(
    SLUG,
    "Dunkin' After 40: What to Order | Fig Performance",
    "What to order at Dunkin' after 40: the Wake-Up Wrap is only 7 to 8g of protein, and the omelet bites nearly double it at the same calories.",
    "Dunkin' After 40: What to Order",
    "Fitness after 40", "Unpopular opinion: Dunkin's Wake-Up Wrap is a snack, not a breakfast.",
    "About 180 calories and roughly 7 to 8 grams of protein. That is the whole issue.",
    [("protein", "The protein problem"), ("bites", "Omelet bites are the order"),
     ("starbucks", "Why Starbucks pulled ahead"), ("sodium", "Sodium and the donut"),
     ("order", "What I would order"), ("why", "Why it is on the list"),
     ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "Dunkin after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
