"""Article: Dave's Hot Chicken after 40. DRAFT Nov 25 2026. Standing approval.

Dave (trainwithdaveoc) has NOTHING on this chain.

SOURCE: FIRST-PARTY. Dave's Hot Chicken publishes a full nutrition table at
store.daveshotchicken.com/nutrition-information/, linked from the footer of
daveshotchicken.com/nutrition. Every figure here comes from that table.

THIS SETTLES THE BLOCK. Third-party databases reported a single tender at 150,
180, 290, 490 and 550 calories. The chain's own table says a Single Tender is
490 cal (Not Hot / Lite Mild) or 550 cal (Mild through Reaper). The low figures
in circulation are wrong by a factor of three.

NOTE: spice level changes the numbers, which is why the aggregators disagree.
Hotter = more oil = more calories and sodium.

CAUTION flagged by the source read: the Hot Mozz rows appear to be missing a
column and the Top-Loaded Buffalo Mac (Small) has an internally inconsistent
fat-calorie figure. Neither is quoted on this page.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "daves-hot-chicken-after-40"

body = f"""<p class="legal-intro">One tender at Dave's Hot Chicken is 490 calories. Not 150, which is what several nutrition apps will tell you. Four hundred and ninety, from the chain's own published nutrition table, with 25 grams of protein and 1,210 mg of sodium. If you have been logging these as a snack, you have been undercounting by about three hundred calories per tender.</p>

<h2 id="tenders">What a tender actually costs</h2>
<p>Straight from Dave's Hot Chicken's own nutrition information:</p>
<ul>
  <li><strong>Single Tender, Not Hot or Lite Mild:</strong> 490 calories, 25 g protein, 29 g fat, 1,210 mg sodium</li>
  <li><strong>Single Tender, Mild through Reaper:</strong> 550 calories, 25 g protein, 35 g fat, 1,480 mg sodium</li>
  <li><strong>Single Slider, Not Hot or Lite Mild:</strong> 620 calories, 31 g protein, 1,150 mg sodium</li>
  <li><strong>Single Slider, Mild through Reaper:</strong> 680 calories, 31 g protein, 1,420 mg sodium</li>
</ul>
<p>Twenty-five grams of protein is fine. Four hundred and ninety calories to get it is not, and that is the honest summary of this restaurant: the protein is real and it is expensive.</p>
{stats([("490 cal", "one tender"), ("25 g", "protein in it"), ("1,210 mg", "sodium in it")])}

<h2 id="spice">The heat level changes the numbers</h2>
<p>This is the part nobody mentions and it explains why every nutrition app disagrees about this place. Going from Not Hot to Mild or above adds about 60 calories and roughly 270 mg of sodium <em>per tender</em>, because the heat comes from oil and seasoning applied to the chicken.</p>
<p>Order four Reaper tenders instead of four Not Hot and you have added around 240 calories and over a thousand milligrams of sodium without ordering anything extra.</p>
{pullquote("The heat is made of oil. Every step up the spice board costs you about sixty calories a tender.")}

<h2 id="sauce">Dave's Sauce is not a condiment</h2>
<ul>
  <li><strong>Dave's Sauce, 1.5 oz dipper cup:</strong> 290 calories, 30 g fat, 0 g protein</li>
  <li><strong>Dave's Sauce, 4 oz cup:</strong> 760 calories, 80 g fat</li>
  <li><strong>Ranch, 1.5 oz dipper:</strong> 200 calories</li>
</ul>
<p>A small cup of Dave's Sauce carries more calories than two-thirds of a tender and gives you nothing in return. The large cup is 760 calories, which is more than most entire meals in these guides.</p>
<p>Separately, the Spicy Buffalo sauce is only 25 calories but carries around 1,180 mg of sodium in a 1.5 oz cup, which is a different kind of problem.</p>

<h2 id="sides">The sides, including the one that looks healthy</h2>
<ul>
  <li><strong>Kale Slaw:</strong> 270 calories, 2 g protein, <strong>26 g fat</strong>, 170 mg sodium</li>
  <li><strong>Mac and Cheese:</strong> 290 calories, 14 g protein, 1,090 mg sodium</li>
  <li><strong>French Fries:</strong> 440 calories, 6 g protein, 1,200 mg sodium</li>
</ul>
<p>Read the slaw again. It is kale, so it reads as the virtuous choice, and it carries 26 grams of fat for 2 grams of protein. The mac and cheese has seven times the protein for twenty more calories. That is not an argument for the mac, it is an argument for reading the card.</p>

<h2 id="loaded">The top-loaded items are in a category of their own</h2>
<p>These are the largest single numbers anywhere in these twenty-eight restaurant guides:</p>
<ul>
  <li><strong>Top-Loaded Fries, Large:</strong> 1,630 calories, 51 g protein, <strong>4,570 mg sodium</strong></li>
  <li><strong>Top-Loaded Buffalo Mac, Large:</strong> 2,960 calories, 66 g protein, 220 g fat, <strong>7,020 mg sodium</strong></li>
</ul>
<p>Seven thousand milligrams is three days of sodium in one item. I am not going to tell you never to eat it. I am going to tell you that it exists, that it is shareable, and that nothing else on this website comes within half of it.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Two tenders, Not Hot or Lite Mild, no sauce cup.</strong> Around 980 calories and 50 g of protein. That is the honest best case here.</li>
  <li><strong>Stay at the lower spice levels</strong> if calories matter. Each step up is roughly 60 calories a tender.</li>
  <li><strong>Mac and cheese over kale slaw</strong> if you want a side with protein in it.</li>
  <li><strong>Skip Dave's Sauce</strong> or split one small cup. 290 calories for zero protein.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["One tender is 490 calories, not 150", "Hotter spice adds about 60 cal and 270 mg sodium per tender", "A small Dave's Sauce cup is 290 calories"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because this was the hardest restaurant in the whole series to write honestly, and the reason is instructive. The pages ranking for "Dave's Hot Chicken nutrition" report a single tender at anywhere from 150 to 550 calories. People are planning meals off numbers that are wrong by a factor of three.</p>
<p>Dave's Hot Chicken publishes the real figures. Almost nobody reads them. This is good food that costs what it costs, and you deserve to know the actual number before you decide.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>Every figure above comes from Dave's Hot Chicken's own published nutrition information, not from a third-party database. That matters more here than anywhere else in these guides: independent sites report a single tender at 150, 180, 290, 490 and 550 calories, a nearly fourfold spread, and the low figures are simply wrong. Part of the confusion is that spice level genuinely changes the numbers, so a single "tender" has two correct answers depending on how hot you ordered it. Two rows on the chain's table were not used here: the Hot Mozz items appear to be missing a column, and the small Top-Loaded Buffalo Mac lists a calories-from-fat figure that does not reconcile with its own total fat.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders, 280 calories and 47 g</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/wingstop-after-40">Wingstop</a>: the flavour swings sodium tenfold</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/five-guys-after-40">Five Guys</a>: bunless is 440 calories and almost no salt</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap saves 200 calories</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: the breaded tenders beat the charbroiled sandwich</li><li><a href="/mcdonalds-after-40">McDonald's</a>: the McDouble beats the Big Mac</li><li><a href="/wendys-after-40">Wendy's</a>: the chili is the only side worth having</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips, 200 calories and 30 g</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/taco-bell-after-40">Taco Bell</a>: three soft tacos beat the Power Bowl</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/rubios-after-40">Rubio's</a>: the famous fish taco is nine grams</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: lowest sodium meal on this site</li><li><a href="/cava-after-40">CAVA</a>: the curated bowls are a day of salt</li><li><a href="/panda-express-after-40">Panda Express</a>: the base is the whole decision</li><li><a href="/subway-after-40">Subway</a>: the best thing there has no bread in it</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/panera-after-40">Panera</a>: the bread bowl holds more than the soup</li><li><a href="/dunkin-after-40">Dunkin'</a>: the Wake-Up Wrap is a snack</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/portillos-after-40">Portillo's</a>: the dressing adds 340 calories to every salad on the menu</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("How many calories is one tender at Dave's Hot Chicken?",
     "490 calories at Not Hot or Lite Mild, and 550 at Mild through Reaper, from the chain's own published nutrition information. Each carries 25 grams of protein. Several nutrition apps report figures as low as 150 calories, which is wrong by a factor of three."),
    ("Does the spice level change the calories at Dave's Hot Chicken?",
     "Yes, and this is why nutrition apps disagree about this restaurant. Going from Not Hot to Mild or hotter adds roughly 60 calories and about 270 mg of sodium per tender, because the heat is applied as seasoned oil."),
    ("How many calories is Dave's Sauce?",
     "A 1.5 ounce dipper cup is 290 calories with 30 grams of fat and no protein. The 4 ounce cup is 760 calories. That small cup carries more calories than two-thirds of a tender."),
    ("Is the kale slaw at Dave's Hot Chicken healthy?",
     "Not especially. It is 270 calories with 26 grams of fat and only 2 grams of protein. The mac and cheese is 290 calories with 14 grams of protein. The slaw reads as the virtuous choice and is not."),
    ("What is the highest calorie item at Dave's Hot Chicken?",
     "The large Top-Loaded Buffalo Mac, at 2,960 calories with 220 grams of fat and about 7,020 mg of sodium. That is roughly three days of sodium in one item, and it is the largest single figure in any of these restaurant guides."),
]

html = page(
    SLUG,
    "Dave's Hot Chicken After 40: What to Order | Fig Performance",
    "What to order at Dave's Hot Chicken after 40: one tender is 490 calories, not the 150 your app says, and the spice level changes the numbers.",
    "Dave's Hot Chicken After 40: What to Order",
    "Fitness after 40", "Unpopular opinion: one tender at Dave's Hot Chicken is a meal, not a snack.",
    "490 calories and 25 grams of protein, from their own nutrition table.",
    [("tenders", "What a tender costs"), ("spice", "Heat changes the numbers"),
     ("sauce", "Dave's Sauce is not a condiment"), ("sides", "The sides"),
     ("loaded", "The top-loaded items"), ("order", "What I would order"),
     ("why", "Why it is on the list"), ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "Dave's Hot Chicken after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
