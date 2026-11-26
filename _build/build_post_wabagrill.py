"""Article: WaBa Grill after 40. DRAFT Nov 25 2026.

Dave has NOTHING on WaBa Grill, and it is dense in North OC where he has no location.

SOURCING, read this before editing. WaBa's data in circulation is BAD. The same
Chicken Bowl appears at 630, 640 and 760 calories, at 38, 46 and 60 g protein, and
at 120, 900 and 2,455 mg sodium. The 760-calorie and 2,455 mg figures trace to pages
five-plus years old; the 120 mg sodium figure is obviously an error.

What DOES hold: two independently maintained, recently updated sources give the same
white-meat comparison, 630 cal / 46 g for the White Meat Chicken Bowl against
640 cal / 38 g for the regular Chicken Bowl. That comparison is the spine of this
article and it is all the article asserts firmly. Sodium is explicitly reported as
contested rather than given a number. If Dan screen-records WaBa's own nutrition
page the way he did Del Taco's, this page can be tightened the same day.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "waba-grill-after-40"

body = f"""<p class="legal-intro">There are two words at the WaBa Grill counter that are worth about eight grams of protein, and they cost nothing. Ask for <strong>white meat</strong>. The White Meat Chicken Bowl comes to roughly 630 calories with about 46 grams of protein. The regular Chicken Bowl is about 640 calories with 38 grams. Same bowl, same price range, ten fewer calories, eight more grams of protein.</p>

<h2 id="white-meat">White meat against regular chicken</h2>
<p>This is the only thing you need to remember about this restaurant:</p>
<ul>
  <li><strong>White Meat Chicken Bowl:</strong> about 630 calories, roughly 46 g protein, about 5 g fat</li>
  <li><strong>Regular Chicken Bowl:</strong> about 640 calories, roughly 38 g protein, about 11 g fat</li>
</ul>
<p>Eight grams of protein is not a rounding error at our age. It is the difference between a lunch that holds you to dinner and one that has you looking in the pantry at four o'clock. And unlike almost every other upgrade in fast food, this one does not cost you calories.</p>
{stats([("+8 g", "protein, white meat"), ("-10 cal", "and slightly fewer calories"), ("2 words", "at the counter")])}

<h2 id="veggie">The veggie bowl is the better version of the same idea</h2>
<p>Swapping some of the rice for steamed vegetables is the other free move here. A White Meat Chicken Veggie Bowl lands near 580 calories with roughly 47 grams of protein, which is a better number than the standard bowl in both directions.</p>
<p>The bowls at WaBa are carb-heavy by design. That is not automatically a problem, but if you are eating one at lunch and sitting at a desk afterwards, the veggie version is the one I would pick.</p>
{pullquote("Two words at the counter. Eight grams of protein. Nobody tells you this.")}

<h2 id="sodium">The number I cannot give you, and why</h2>
<p>Sodium. I am not going to put a figure on it, because the figures in circulation for this chain do not agree and I am not going to pick one and pretend.</p>
<p>For the same Chicken Bowl, published breakdowns range from about 900 mg to roughly 2,455 mg. That is not a small disagreement, it is the difference between a normal lunch and most of a day's salt. Some of the higher numbers trace back to pages that are five years old and may describe an older recipe. One widely syndicated figure of 120 mg is almost certainly a data entry error.</p>
<p>So here is the honest version: WaBa's teriyaki sauce is the likely source of most of the sodium, it is served by the ladle, and you can ask for it on the side. If you are managing blood pressure, do that, and ask the store for their current nutrition sheet rather than trusting any website including this one.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>White Meat Chicken Veggie Bowl.</strong> Around 580 calories and roughly 47 grams of protein. Best item on the board.</li>
  <li><strong>Say white meat every time.</strong> Eight grams of protein for nothing is the single best-value sentence in this series.</li>
  <li><strong>Sauce on the side.</strong> It is where the sugar and most of the sodium live, and on the side you decide how much.</li>
  <li><strong>Half the rice, more vegetables</strong> if you are eating this at lunch on a desk day.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Say white meat. Eight more grams of protein, slightly fewer calories", "Veggie bowl beats the standard bowl", "Ask for sauce on the side, that is where the sodium is"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because WaBa is on half the corners in this part of Orange County and almost nothing honest has been written about it. The national chains have armies of dietitians producing content. The regional ones that people here actually eat at every week get ignored, which is exactly why the one useful fact about this menu is not common knowledge.</p>
<p>It is a good restaurant for an adult over 40. Grilled protein, steamed vegetables, no fryer. It just has a default setting that quietly gives you less protein than the version standing next to it.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>This page is deliberately more cautious than the others in this series. Published nutrition data for WaBa Grill disagrees badly: the same Chicken Bowl appears at 630, 640 and 760 calories, at 38, 46 and 60 grams of protein, and at anywhere from 120 to 2,455 mg of sodium across different databases. The white meat comparison above comes from two independently maintained sources that were updated recently and that agree with each other exactly, which is why it is the only thing stated firmly here. Everything else is given as approximate, and sodium is not given at all. Ask your store for their current sheet. If WaBa publishes an updated nutrition document, this page will be rewritten against it.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("What is the healthiest thing to order at WaBa Grill?",
     "A White Meat Chicken Veggie Bowl, at roughly 580 calories with about 47 grams of protein. Ask for the sauce on the side. The single most useful habit is saying white meat every time you order."),
    ("Is white meat chicken at WaBa Grill worth it?",
     "Yes, and it is the best value in this whole series of guides. The White Meat Chicken Bowl is about 630 calories with roughly 46 grams of protein against about 640 calories and 38 grams for the regular Chicken Bowl. Eight more grams of protein and slightly fewer calories, for two words at the counter."),
    ("How much sodium is in a WaBa Grill bowl?",
     "Honestly, the published figures do not agree. The same Chicken Bowl appears at anywhere from about 900 mg to roughly 2,455 mg depending on which database you read, and one syndicated figure of 120 mg is almost certainly an error. The teriyaki sauce is the likely source, so ask for it on the side and ask your store for their current nutrition sheet."),
    ("Is WaBa Grill good for weight loss?",
     "It can be. It is grilled protein and steamed vegetables with no fryer involved, which puts it ahead of most fast food. The bowls are carb-heavy by design, so the veggie bowl is usually the better pick, and white meat gives you more protein for the same calories."),
    ("How much protein is in a WaBa Grill chicken bowl?",
     "Roughly 38 grams for the regular Chicken Bowl and about 46 grams for the White Meat Chicken Bowl, at nearly identical calories. Figures vary between published sources, so treat these as approximate rather than exact."),
]

html = page(
    SLUG,
    "WaBa Grill After 40: What to Order | Fig Performance",
    "What to order at WaBa Grill after 40: why white meat gives you 8 more grams of protein for the same calories, and the sodium number nobody can agree on.",
    "WaBa Grill After 40: What to Order",
    "Fitness after 40", "Stop ordering the regular chicken at WaBa Grill. White meat costs you nothing.",
    "Eight more grams of protein for the same calories. You just have to say the words.",
    [("white-meat", "White meat vs regular"), ("veggie", "The veggie bowl"), ("sodium", "The number I cannot give you"),
     ("order", "What I would order"), ("why", "Why it is on the list"),
     ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "WaBa Grill after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
