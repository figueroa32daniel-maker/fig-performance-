"""Article: Panera after 40. DRAFT Nov 25 2026, not published until Dan approves.

Dave has NOTHING on Panera. Same sourcing rule: two or more independent sources
must agree, ranges where they split. Panera's data is noisier than Raising Cane's
or Jersey Mike's, so several items are given as ranges on purpose. Deliberately
NOT used: a per-item sodium figure for the Green Goddess Cobb, because sources
put it anywhere from 940 to 1,980 mg and that is too wide to publish.
"""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "panera-after-40"

body = f"""<p class="legal-intro">The bread bowl at Panera is somewhere around 570 to 650 calories on its own, before anything is poured into it. A bowl of broccoli cheddar soup is about 420. So the bread is the bigger half of the meal, and it is the part most people think of as the dish it comes in. Put them together and you are near 900 calories with roughly 2,170 mg of sodium, which is most of a day's salt in one lunch.</p>

<h2 id="breadbowl">The bowl is the meal</h2>
<p>This is the single most useful thing on this page. The sourdough bread bowl is not a container, it is a loaf of bread that has had a hole made in it, and it carries more calories than the soup it holds.</p>
<ul>
  <li><strong>Bread bowl, bread only:</strong> roughly 570 to 650 calories</li>
  <li><strong>Broccoli cheddar soup, bowl size:</strong> about 420 calories, around 12 g protein, roughly 1,520 mg sodium</li>
  <li><strong>The two together:</strong> about 890 to 950 calories and in the region of 2,170 mg sodium</li>
</ul>
<p>Order the same soup in a regular bowl and you have cut the meal roughly in half without changing a thing about what you came in for.</p>
{stats([("~420 cal", "the soup"), ("~570-650", "the bread around it"), ("~2,170 mg", "sodium, together")])}

<h2 id="halo">Why this one catches people</h2>
<p>Panera reads as the grown-up choice. Bakery, soup, salads, nothing deep-fried in sight. That impression is doing a lot of work it has not earned, and it is the reason I see this restaurant in food logs far more often than In-N-Out.</p>
{pullquote("Nobody walks out of In-N-Out thinking they ate light. People walk out of Panera thinking exactly that.")}
<p>The thing to understand is that the problem here is rarely the protein. It is sodium and it is bread, and both arrive in forms that do not look like a splurge.</p>

<h2 id="sodium">Sodium is the number at this restaurant</h2>
<p>It runs high across the menu, not just in the bread bowl. The soups are where it concentrates most, and a single bowl of broccoli cheddar is already around 1,520 mg before any bread is involved.</p>
<p>Same advice as El Pollo Loco and Jersey Mike's: if a doctor has mentioned your blood pressure, this is the column to read, and reading it does not mean you have to leave. It means you pick differently.</p>

<h2 id="protein">There is real protein here if you look</h2>
<p>The Green Goddess Cobb with chicken is the one I point people at. Sources put it in the region of 500 to 580 calories with about 40 grams of protein, which is a legitimately good lunch and one of the better protein-per-calorie items on the menu.</p>
<p>The newer Market Bowls go the other way. They run heavy, up to roughly 1,100 calories for the biggest of them, and they are served in a format that looks portion-controlled. Read those before you order one.</p>

<h2 id="order">What I would order</h2>
<ol>
  <li><strong>Soup in a bowl, never the bread bowl.</strong> That one swap is 570 to 650 calories.</li>
  <li><strong>Green Goddess Cobb with chicken</strong> if you want the protein in one order. Around 40 grams.</li>
  <li><strong>A You Pick 2 built as a cup of soup plus a salad</strong> rather than soup plus a sandwich. It is one of the lighter full meals in the building.</li>
  <li><strong>Watch the Market Bowls.</strong> They look like the healthy format and several of them are the heaviest food on the menu.</li>
</ol>
{callout("The 15-second version", "If you remember one thing", ["The bread bowl has more calories than the soup in it", "Sodium is the number here, not fat", "Green Goddess Cobb with chicken is about 40 g of protein"])}

<h2 id="why">Why this one is on the list</h2>
<p>Because the restaurants that cost my clients the most are never the ones they feel guilty about. Guilt makes people order carefully. It is the lunch that feels responsible that goes in the log as "soup and bread" and turns out to have been 900 calories and a day of salt.</p>
<p>Panera is a good restaurant to eat at after 40. It is just one where the menu will not warn you, and where the most popular order in the building is the one to walk past.</p>

<h2 id="caveat">A note on these numbers</h2>
<p>Panera publishes nutrition for its menu, but independent breakdowns of it disagree more than most chains on this site, partly because recipes and sizes have changed. Everything above is given as a range where sources split, and nothing is quoted to a precision the data does not support. One figure was left out entirely: the sodium in the Green Goddess Cobb, which sources put anywhere between 940 and 1,980 mg. That gap is too wide to put a number on, so this page does not. Check Panera's current nutrition calculator if you are tracking closely.</p>

<h2 id="more">The rest of the restaurant guides</h2>
<ul><li><a href="/in-n-out-after-40">In-N-Out</a>: the Double-Double against the fries</li><li><a href="/chick-fil-a-after-40">Chick-fil-A</a>: grilled nuggets, 25 g for 130 calories</li><li><a href="/chipotle-after-40">Chipotle</a>: double chicken and where the calories hide</li><li><a href="/el-pollo-loco-after-40">El Pollo Loco</a>: 34 g in a grilled breast, and the sodium</li><li><a href="/raising-canes-after-40">Raising Cane's</a>: the sauce costs more than the chicken</li><li><a href="/jersey-mikes-after-40">Jersey Mike's</a>: the three words that cut 300 calories</li><li><a href="/starbucks-after-40">Starbucks</a>: protein lattes and egg bites</li><li><a href="/kfc-after-40">KFC</a>: Extra Crispy costs 140 calories for nothing</li><li><a href="/del-taco-after-40">Del Taco</a>: three street tacos beat the salad</li><li><a href="/waba-grill-after-40">WaBa Grill</a>: say white meat, eight more grams free</li><li><a href="/flame-broiler-after-40">Flame Broiler</a>: about 340 mg of sodium in a full bowl, the lowest on this site</li><li><a href="/five-guys-after-40">Five Guys</a>: a bunless burger is 440 calories, 32 g protein and almost no salt</li><li><a href="/jack-in-the-box-after-40">Jack in the Box</a>: grilled strips are about 200 calories for 30 g of protein</li><li><a href="/popeyes-after-40">Popeyes</a>: five blackened tenders are 280 calories and 47 g of protein</li><li><a href="/cava-after-40">CAVA</a>: curated bowls are close to a day of salt, so build your own</li><li><a href="/carls-jr-after-40">Carl's Jr</a>: five breaded tenders beat the charbroiled sandwich at the same calories</li><li><a href="/dunkin-after-40">Dunkin</a>: the Wake-Up Wrap is 7 to 8 g of protein, which is a snack</li><li><a href="/wingstop-after-40">Wingstop</a>: six plain wings are 540 calories and 60 g of protein</li><li><a href="/habit-burger-after-40">The Habit</a>: the lettuce wrap Charburger is 290 calories against 470 to 520 on a bun</li><li><a href="/rubios-after-40">Rubio's</a>: the Original Fish Taco is 9 g of protein for 330 calories</li><li><a href="/mcdonalds-after-40">McDonald's</a>: the McDouble is 390 calories and 22 g protein, beating the Big Mac</li><li><a href="/taco-bell-after-40">Taco Bell</a>: three soft chicken tacos give 36 g of protein, beating the Power Bowl</li><li><a href="/wendys-after-40">Wendy's</a>: the chili is the only fast food side with real protein in it</li><li><a href="/subway-after-40">Subway</a>: a rotisserie chicken bowl is 220 calories and 31 g of protein</li></ul>
<p>Same idea every time: find the protein, spot the one item doing the damage, and order so you are not eating differently from everyone else at the table.</p>
{CTA}"""

faqs = [
    ("How many calories is a Panera bread bowl?",
     "The sourdough bread bowl on its own is roughly 570 to 650 calories, which is more than the bowl of soup that goes inside it. Broccoli cheddar in a bread bowl comes to about 890 to 950 calories with roughly 2,170 mg of sodium."),
    ("Is Panera actually healthy?",
     "It can be, but it carries a health halo it has not earned. The problem is rarely protein, it is sodium and bread. A bowl of broccoli cheddar soup is already around 1,520 mg of sodium before any bread bowl is involved. Order soup in a regular bowl and pick a chicken salad and it is a good lunch."),
    ("What is the highest protein order at Panera?",
     "The Green Goddess Cobb with chicken is the one to know, at roughly 500 to 580 calories with about 40 grams of protein. That is one of the better protein-per-calorie items on the menu."),
    ("Are Panera's Market Bowls a good choice?",
     "Not automatically. They are served in a format that reads as portion-controlled, but they run heavy, with the largest around 1,100 calories. Check the number before assuming the bowl is the lighter option."),
    ("What should I avoid at Panera if I am watching my weight?",
     "The bread bowl, first and last. Swapping it for a regular bowl saves 570 to 650 calories and changes nothing about what you came in to eat. After that, watch the sodium across the soups and read the Market Bowls before ordering one."),
]

html = page(
    SLUG,
    "Panera After 40: What to Order | Fig Performance",
    "What to order at Panera after 40: why the bread bowl holds more calories than the soup, the sodium nobody reads, and the salad with 40g of protein.",
    "Panera After 40: What to Order",
    "Fitness after 40", "Unpopular opinion: the bread bowl at Panera has more calories in it than the soup.",
    "About 570 to 650 for the bread. About 420 for what goes inside it.",
    [("breadbowl", "The bowl is the meal"), ("halo", "Why this one catches people"), ("sodium", "The number to watch"),
     ("protein", "Where the protein is"), ("order", "What I would order"), ("why", "Why it is on the list"),
     ("caveat", "A note on the numbers"), ("more", "The other guides")],
    body, faqs, "Panera after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
