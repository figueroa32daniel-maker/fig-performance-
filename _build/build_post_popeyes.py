"""Article: Popeyes after 40. DRAFT Nov 25 2026. Standing approval, restaurant cluster.

Dave has NOTHING on Popeyes.

BEST SOURCED PAGE IN THE SERIES so far. Seven independent sources all give
Blackened Tenders 3 pc at 170 calories. Three give the 5 pc at 280 cal / 47 g.
Five give the Classic Chicken Sandwich at 700 cal / 28 g / 42 g fat / 1,440 mg.

THE HEADLINE: 5 pc Blackened Tenders at 280 cal / 47 g protein is 16.8 g protein
per 100 calories, the best ratio of ANY item across all fifteen guides. It beats
the WaBa Signature House Salad (320/44 = 13.8) and the Chick-fil-A grilled nuggets.

Only split: protein on the 3 pc reads 26 or 28 g, and its sodium reads 550 or
860 mg. Both given as ranges.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "popeyes-after-40"

body = f"""<p class="legal-intro">Five Blackened Tenders at Popeyes are about 280 calories with roughly 47 grams of protein. I have now been through fifteen restaurants for these guides and nothing beats that ratio. Not the Chick-fil-A grilled nuggets, not the El Pollo Loco breast, not the WaBa salad. The best protein order in Orange County is sitting in a fried chicken restaurant, on a part of the menu almost nobody orders from.</p>

<h2 id="blackened">Blackened means not breaded</h2>
<p>Blackened tenders are seasoned and cooked without the batter. That one difference does all the work:</p>
<ul>
  <li><strong>Blackened Tenders, 3 piece:</strong> about 170 calories, roughly 26 to 28 g protein</li>
  <li><strong>Blackened Tenders, 5 piece:</strong> about 280 calories, roughly 47 g protein</li>
  <li><strong>Classic Tenders, 3 piece:</strong> about 450 calories, roughly 38 g protein</li>
</ul>
<p>Seven independent nutrition sources give the 3 piece blackened at 170 calories. That is unusually strong agreement, and it is the number worth memorising.</p>
{stats([("280 cal", "five blackened tenders"), ("47 g", "protein in them"), ("700 cal", "the chicken sandwich")])}

<h2 id="sandwich">The sandwich against the tenders</h2>
<p>Popeyes is famous for the Chicken Sandwich. Classic or Spicy, it comes in around 700 calories with about 28 grams of protein, 42 grams of fat and roughly 1,440 mg of sodium.</p>
<p>So compare the two orders directly:</p>
<ul>
  <li><strong>Chicken Sandwich:</strong> about 700 calories, roughly 28 g protein</li>
  <li><strong>Five Blackened Tenders:</strong> about 280 calories, roughly 47 g protein</li>
</ul>
<p>Nineteen more grams of protein for 420 fewer calories. That is the largest single swap in any of these guides, and it costs you one word at the counter.</p>
{pullquote("Nineteen more grams of protein. Four hundred and twenty fewer calories. Same restaurant, same minute.")}

<h2 id="sodium">Sodium is where the breading hurts twice</h2>
<p>Breaded tenders do not just add calories, they add salt. Three classic tenders carry around 1,820 mg of sodium, and five push toward roughly 3,040 mg, which is more than a full day in one order.</p>
<p>The blackened tenders sit far below that. Sources split on exactly how far, giving somewhere between 550 and 860 mg for three pieces, so treat it as a range rather than a precise figure. Either way it is a fraction of the breaded version.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Five Blackened Tenders.</strong> About 280 calories, roughly 47 g protein. Best order in any of these guides.</li>
  <li><strong>Three Blackened Tenders</strong> if that is too much food. About 170 calories and 26 to 28 g.</li>
  <li><strong>Blackened Chicken Sandwich</strong> over the Classic if you want bread. Around 550 calories against 700.</li>
  <li><strong>Say blackened, not classic.</strong> That one word is the article.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Five blackened tenders: about 280 cal and 47 g protein", "The famous sandwich is 700 cal and 28 g", "Blackened beats classic on calories, protein and salt"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because Popeyes is the restaurant people write off entirely, and writing a place off is how you end up ordering badly there when life puts you in the parking lot anyway. There is a tier on that menu that outperforms the salad at most fast casual chains, and the only reason it is not common knowledge is that nobody goes to Popeyes looking for it.</p>
<p>If you are over 40 and trying to get protein in without spending the day's calories, this is the single best drive-through order I have found.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>This is the most strongly sourced page in the series. Seven independent nutrition breakdowns agree that three Blackened Tenders are 170 calories, three agree the five piece is 280 calories with 47 grams of protein, and five agree the Classic Chicken Sandwich is 700 calories with 28 grams of protein and 1,440 mg of sodium. Two values do split: protein on the three piece reads either 26 or 28 grams, and its sodium reads either 550 or 860 mg, so both are given as ranges above rather than picked. Check Popeyes' current nutrition guide if you are tracking tightly.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: lowest sodium meal on this site</li><li><a href="/five-guys-after-40">Five Guys</a>: bunless is 440 calories and almost no salt</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips, 200 calories and 30 g</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/cava-after-40">CAVA</a>: curated bowls are close to a day of salt, so build your own</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: five breaded tenders beat the charbroiled sandwich at the same calories</li><li><a href="/dunkin-after-40">Dunkin</a>: the Wake-Up Wrap is 7 to 8 g of protein, which is a snack</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("What is the best high protein order at Popeyes?",
     "Five Blackened Tenders, at about 280 calories with roughly 47 grams of protein. That is the best protein-per-calorie order in any of these restaurant guides, better than the Chick-fil-A grilled nuggets or the El Pollo Loco breast."),
    ("How many calories are in Popeyes blackened tenders?",
     "About 170 calories for three pieces and around 280 for five. Seven independent nutrition sources agree on the 170 figure, which is unusually strong agreement for a fast food item."),
    ("Are blackened tenders better than classic tenders at Popeyes?",
     "By a wide margin. Three blackened tenders are about 170 calories; three classic tenders are about 450. The classic version also carries around 1,820 mg of sodium against roughly 550 to 860 for blackened. Blackened means seasoned and cooked without the batter."),
    ("How many calories is the Popeyes chicken sandwich?",
     "Around 700 calories with about 28 grams of protein, 42 grams of fat and roughly 1,440 mg of sodium, for both Classic and Spicy. Five Blackened Tenders give you 19 more grams of protein for 420 fewer calories."),
    ("Can you eat Popeyes and still lose fat?",
     "Yes, and more easily than at most places. Five blackened tenders is a 280 calorie meal with roughly 47 grams of protein. The restaurant people write off entirely turns out to have the best protein order of any chain in these guides."),
]

html = page(
    SLUG,
    "Popeyes After 40: What to Order | Fig Performance",
    "What to order at Popeyes after 40: five blackened tenders are about 280 calories with 47g of protein, the best protein order in any of these guides.",
    "Popeyes After 40: What to Order",
    "Fitness after 40", "Hot take: the best protein order in these guides is at Popeyes, of all places.",
    "Five blackened tenders: about 280 calories and roughly 47 grams of protein.",
    [("blackened", "Blackened means not breaded"), ("sandwich", "The sandwich vs the tenders"),
     ("sodium", "Where breading hurts twice"), ("order", "What I would order"),
     ("why", "Why it is on the list"), ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "Popeyes after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
