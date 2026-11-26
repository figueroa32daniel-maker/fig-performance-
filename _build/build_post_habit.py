"""Article: The Habit Burger Grill after 40. DRAFT Nov 25 2026. Standing approval.

Dave has NOTHING on The Habit. SoCal chain, founded Santa Barbara.

SOURCING: Charburger reads 470, 500 and 520 calories across sources, and the spread
is explained rather than contradictory: 470 is the seeded bun, 520 the wheat bun.
Two sources give the seeded version identically at 470 cal / 23 g / 1,140 mg.
Lettuce Wrap Charburger at 290 cal / 18 g / 840 mg, with one stale 2021 source
giving 352 cal, discarded on the date-check rule.

THE STORY: sodium. Most Habit burgers clear 1,000 mg each, BBQ Bacon is 1,760 mg
and Teriyaki 1,690 mg. The lettuce wrap is the lever: 290 cal and 840 mg.

FLAGGED IN THE ARTICLE as single-source: the wheat bun appears to carry MORE
calories than the seeded bun (520 vs 470), which is counterintuitive. Only one
source covers both, so the page says so.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "habit-burger-after-40"

body = f"""<p class="legal-intro">A Lettuce Wrap Charburger at The Habit is about 290 calories with roughly 18 grams of protein and around 840 mg of sodium. The same burger on a bun is somewhere between 470 and 520 calories with 1,140 to 1,240 mg of sodium. The char-grilled patty is the good part of this restaurant. The bun is carrying more than its share of the damage.</p>

<h2 id="wrap">The lettuce wrap is the order</h2>
<ul>
  <li><strong>Lettuce Wrap Charburger:</strong> about 290 calories, roughly 18 g protein, around 840 mg sodium</li>
  <li><strong>Charburger, seeded bun:</strong> about 470 calories, roughly 23 g protein, around 1,140 mg sodium</li>
  <li><strong>Charburger, wheat bun:</strong> about 520 calories, roughly 26 g protein, around 1,220 mg sodium</li>
</ul>
<p>That is roughly 180 to 230 calories and 300 to 380 mg of sodium for a piece of bread, and The Habit will swap it for lettuce without any fuss. Same char-grilled patty, same toppings.</p>
{stats([("290 cal", "lettuce wrap"), ("470-520", "the same burger on a bun"), ("840 mg", "sodium, wrapped")])}

<h2 id="sodium">Sodium is the honest problem here</h2>
<p>Most burgers at The Habit clear 1,000 mg of sodium on their own, and the sauced ones go considerably further:</p>
<ul>
  <li><strong>BBQ Bacon Charburger:</strong> about 680 calories, roughly 30 g protein, around <strong>1,760 mg</strong> sodium</li>
  <li><strong>Teriyaki Charburger:</strong> about 560 calories, roughly 27 g protein, around 1,690 mg sodium</li>
</ul>
<p>Those two are among the highest sodium single items in any of these guides, and in both cases the sauce is what did it. The plain Charburger is roughly 600 mg lower than the BBQ Bacon version for the same basic burger.</p>
{pullquote("Char-grilled beef over an open flame is the good part. The sauce and the bun are doing the damage.")}

<h2 id="bun">Something odd about the buns</h2>
<p>This one is worth flagging carefully. On the figures I could find, the wheat bun appears to carry <em>more</em> calories than the seeded bun, roughly 520 against 470, with about twelve more grams of carbohydrate.</p>
<p>If that holds, it reverses what almost everyone assumes when they pick wheat. I am flagging it rather than stating it flatly, because only one source covers both versions and I would want a second before anybody changes an order over it. Either way, the lettuce wrap beats both by a wide margin, so it is not the decision that matters.</p>

<h2 id="double">The Double is better arithmetic than it looks</h2>
<p>A Double Charburger comes in around 730 calories with roughly 37 grams of protein and about 1,300 mg of sodium. Against a single at roughly 500 and 21 to 23 grams, the second patty is costing you about 230 calories for around 14 extra grams of protein, without much extra salt.</p>
<p>If you are actually hungry, that is a better trade than adding a side. The sides are where this restaurant quietly gets expensive.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Lettuce Wrap Charburger.</strong> About 290 calories, roughly 18 g protein, around 840 mg sodium.</li>
  <li><strong>Double it</strong> if you want real protein. The second patty is efficient; the bun and sides are not.</li>
  <li><strong>Avoid BBQ and Teriyaki</strong> if sodium is a concern. Both clear 1,690 mg.</li>
  <li><strong>Skip the fries and the shake.</strong> The burger is rarely the problem at this chain.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["Lettuce wrap: about 290 cal and 840 mg sodium", "On a bun the same burger is 470 to 520 cal", "BBQ Bacon is about 1,760 mg of sodium"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because The Habit grills over an open flame, which makes it genuinely better food than most of this list, and because that fact leads people to stop reading the rest of the menu. Char-grilled beef is not the issue. A bun, a sauce and a side are, and they are all optional.</p>
<p>It is also a Southern California chain that the national nutrition writers mostly ignore, which is exactly the gap these guides exist to fill.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>The Charburger appears at 470, 500 and 520 calories across sources, and that spread is explained rather than contradictory: 470 is the seeded bun version and 520 is the wheat bun version. Two sources give the seeded Charburger identically at 470 calories, 23 grams of protein and 1,140 mg of sodium. The Lettuce Wrap Charburger is given here at 290 calories; one source reports 352, but that page was last updated in 2021 and is treated as out of date. The wheat versus seeded bun comparison rests on a single source and is flagged as such in the text above rather than presented as settled.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/five-guys-after-40">Five Guys</a>: bunless is 440 calories and almost no salt</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: the breaded tenders beat the charbroiled sandwich</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: lowest sodium meal on this site</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips, 200 calories and 30 g</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders, 280 calories and 47 g</li><li><a href="/wingstop-after-40">Wingstop</a>: the flavour swings sodium tenfold</li><li><a href="/cava-after-40">CAVA</a>: the curated bowls are a day of salt</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/dunkin-after-40">Dunkin'</a>: the Wake-Up Wrap is a snack</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/rubios-after-40">Rubio's</a>: the Original Fish Taco is 9 g of protein for 330 calories</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("How many calories is a Habit Charburger?",
     "About 470 calories on the seeded bun, with roughly 23 grams of protein and around 1,140 mg of sodium. The wheat bun version comes in near 520. As a lettuce wrap it drops to about 290 calories and 840 mg of sodium."),
    ("Can you get a lettuce wrap at The Habit?",
     "Yes, and it is the best order on the menu. A Lettuce Wrap Charburger is about 290 calories with roughly 18 grams of protein and around 840 mg of sodium, which saves you 180 to 230 calories and 300 to 380 mg of sodium over the same burger on a bun."),
    ("Is The Habit high in sodium?",
     "Yes. Most of its burgers clear 1,000 mg on their own, and the sauced ones go much higher. The BBQ Bacon Charburger is around 1,760 mg and the Teriyaki around 1,690 mg, which are among the highest single items in any of these guides. The sauce is what does it."),
    ("Is the Double Charburger worth it?",
     "If you are genuinely hungry, yes. A Double is around 730 calories with roughly 37 grams of protein and about 1,300 mg of sodium. The second patty costs about 230 calories for roughly 14 extra grams of protein without much extra salt, which is better arithmetic than adding a side."),
    ("Is The Habit healthier than other burger chains?",
     "The patty is char-grilled over an open flame, which is a genuine advantage. The sodium is not. Order it as a lettuce wrap, avoid the BBQ and Teriyaki versions, and it compares well with anything else on this list."),
]

html = page(
    SLUG,
    "The Habit After 40: What to Order | Fig Performance",
    "What to order at The Habit Burger Grill after 40: the lettuce wrap Charburger is 290 calories against 470 to 520 on a bun, and sodium is the real issue.",
    "The Habit After 40: What to Order",
    "Fitness after 40", "Hot take: the best thing at The Habit is a Charburger with no bun at all.",
    "About 290 calories wrapped in lettuce. The same burger on a bun is 470 to 520.",
    [("wrap", "The lettuce wrap is the order"), ("sodium", "Sodium is the problem"),
     ("bun", "Something odd about the buns"), ("double", "The Double is good arithmetic"),
     ("order", "What I would order"), ("why", "Why it is on the list"),
     ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "The Habit after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
