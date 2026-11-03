"""Article + free PDF: simple meal plan for weight loss and grocery list (from Coach Dan's voice answers, Nov 3 2026)."""
import sys
from build_pages import page, SITE, CTA

DATE = "2026-11-03"
SLUG = "meal-plan-for-weight-loss"
PDF = "/assets/fig-performance-meal-plan.pdf"
CAL = "https://calendly.com/trainwithcoachdan/free-consult-inbody-scan"
SG = "https://www.hhs.gov/surgeongeneral/reports-and-publications/alcohol-cancer/index.html"
DOWNLOAD = f'<p><a class="btn btn-gold" href="{PDF}" download>Download the free meal plan (PDF)</a></p>'

body = f"""<p class="legal-intro">A simple meal plan for weight loss doesn't need fancy recipes. Every meal and snack has the same four things: protein, carbs, fats and fiber. That combination keeps you full longer, so you don't snack, overeat or run out of energy. Below is the exact template Coach Dan Figueroa uses with clients at Fig Performance, with breakfast, lunch, dinner and snack options and a grocery list. Download the free PDF. No email needed.</p>
{DOWNLOAD}

<h2 id="rule">The one rule behind every meal</h2>
<p>Build every meal around <strong>protein, carbs, fats and fiber</strong>. Protein and fiber keep you full. Carbs give your brain and your workouts energy. Fats help you absorb nutrients and make food taste good. Together, they give your body what it needs to build and keep muscle while you lose fat.</p>
<p>These are templates, not rigid meals. Swap in foods you like, as long as each meal still has all four.</p>

<h2 id="plate">How to build your plate</h2>
<ul>
  <li><strong>A palm of protein:</strong> about the size and thickness of your palm. Choose lean sources most of the time.</li>
  <li><strong>A fist of vegetables.</strong></li>
  <li><strong>Carbs fill the rest:</strong> preferably high-fiber ones, like sweet potato, brown rice, quinoa or whole wheat pasta.</li>
</ul>
<p>Don't cut carbs to zero. Your brain runs on glucose, and the recommended minimum for adults is about 130 grams of carbs a day. You'll need more to fuel workouts, golf, hikes and anything else active you do.</p>
<p>For protein, aim for 0.7 to 1 gram per pound of body weight a day, or at least your goal weight in grams. If your goal is 160 pounds, that's at least 160 grams.</p>

<h2 id="breakfast">Breakfast options</h2>
<h3>1. The quick one (when you're rushing to work or a meeting)</h3>
<p>A protein shake with at least 30 grams of protein, plus a slice of sourdough toast. Top the toast with sugar-free jelly, avocado or peanut butter. Want more? Blend a tablespoon of peanut butter into the shake.</p>
<h3>2. The yogurt bowl</h3>
<p>Nonfat Greek yogurt with high-fiber berries like blueberries or raspberries, a little granola and a drizzle of honey.</p>
<h3>3. The bigger breakfast (when you have more time)</h3>
<p>About a half cup of egg whites plus one whole egg, or turkey bacon, turkey sausage or chicken sausage. Add a slice of sourdough toast or a low-carb bagel with sugar-free jelly, avocado or peanut butter.</p>

<h2 id="lunch">Lunch options</h2>
<h3>1. Protein and a high-fiber carb</h3>
<p>A lean protein like chicken, turkey, lean steak, or fish like salmon (great for omega-3 fats), with a high-fiber carb: sweet potato, brown or white rice, whole wheat pasta, quinoa or bulgur. Add vegetables.</p>
<h3>2. The salad bowl</h3>
<p>Chicken, plenty of vegetables, a carb like quinoa or sweet potato, and a light dressing. Bolthouse Farms dressings are a good lower-calorie option.</p>
<h3>3. The high-protein sandwich</h3>
<p>Two slices of sourdough bread, turkey or ham adding up to about 30 grams of protein, vegetables, and mustard or another low-calorie spread for flavor.</p>

<h2 id="dinner">Dinner</h2>
<p>Same template as lunch: a palm of lean protein, a fist of vegetables, and a high-fiber carb. Rotate your proteins and carbs through the week so you don't get bored.</p>

<h2 id="snacks">Snacks</h2>
<p>Anything quick and high in protein, ideally paired with fiber:</p>
<ul>
  <li>A protein bar with blueberries, raspberries or blackberries</li>
  <li>A protein shake with a small handful of almonds and a piece of fruit</li>
  <li>A Greek yogurt cup</li>
  <li>Beef jerky or protein chips with whole wheat crackers</li>
</ul>

<h2 id="sample">A sample day</h2>
<ul>
  <li><strong>Breakfast:</strong> protein shake (30+ g protein) and sourdough toast with peanut butter</li>
  <li><strong>Lunch:</strong> chicken, sweet potato and vegetables</li>
  <li><strong>Snack:</strong> Greek yogurt cup and berries</li>
  <li><strong>Dinner:</strong> salmon, brown rice and vegetables</li>
  <li><strong>Snack:</strong> protein bar and an apple</li>
</ul>

<h2 id="grocery">Grocery list</h2>
<ul>
  <li><strong>Protein:</strong> chicken breast, ground or sliced turkey, lean steak, salmon or other fish, eggs and egg whites, turkey bacon, chicken or turkey sausage, nonfat Greek yogurt, protein powder, protein bars, beef jerky</li>
  <li><strong>Carbs:</strong> sourdough bread, low-carb bagels, sweet potatoes, brown or white rice, whole wheat pasta, quinoa, bulgur, granola, whole wheat crackers</li>
  <li><strong>Fruit:</strong> blueberries, raspberries, blackberries, apples, bananas</li>
  <li><strong>Vegetables:</strong> salad greens and whatever vegetables you'll actually eat</li>
  <li><strong>Fats:</strong> avocado, peanut butter, almonds, olive oil</li>
  <li><strong>Extras:</strong> sugar-free jelly, honey, mustard, light dressing</li>
</ul>

<h2 id="eating-out">Eating out and drinking</h2>
<p>It comes down to how important your goal is, and whether it has a deadline. If you want to lose 30 pounds in 12 weeks, you can still splurge. Just know every splurge pushes the finish line back a little. If that's okay with you, that's fine.</p>
<p>If you have no deadline and you're building habits for life, enjoy special occasions. But if you've been chasing the same goal for a long time and never get there, it's time to set some personal boundaries.</p>
<p>That goes for drinking too. Ask yourself honestly: do drinks during the week, plus weekend brunch, girls' night, guys' night, watching the game, the Super Bowl or family events, fit your goals? Is there room to cut back? A glass of wine can be a treat if it fits your plan, but it isn't a health food. The U.S. Surgeon General has warned that alcohol raises cancer risk, even at moderate amounts (<a href="{SG}" target="_blank" rel="noopener noreferrer">HHS</a>).</p>

<h2 id="eighty-twenty">Keep it 80/20</h2>
<p>About 80% of your food should come from whole, nutrient-dense foods, and about 20% can be food you simply enjoy. Nutrition only works long term if it's flexible and enjoyable. Read more in <a href="/how-to-lose-weight-after-40">how to lose weight after 40</a> and <a href="/why-am-i-not-losing-weight">why am I not losing weight</a>.</p>

<h2 id="download">Get the free PDF</h2>
<p>Everything on this page, on one printable plan you can stick on the fridge. No email or sign-up needed.</p>
{DOWNLOAD}

<h2 id="coach">Want a plan built around you?</h2>
<p>Book a free consultation, in person at Fig Performance in Placentia or as a <a href="/online-personal-trainer">virtual call for online coaching</a>. Coach Dan, a Precision Nutrition Level 1 certified nutrition coach, builds your plan from the foods you already like. See <a href="/nutrition-coaching-placentia">how nutrition coaching works</a>.</p>
<p><a class="btn btn-gold" href="{CAL}" target="_blank" rel="noopener">Book a free consult</a></p>
{CTA}"""

faqs = [
    ("What's a simple meal plan for weight loss?",
     "Build every meal around protein, carbs, fats and fiber: a palm of lean protein, a fist of vegetables, and high-fiber carbs for the rest of the plate. For example, a protein shake and sourdough toast for breakfast, chicken with sweet potato for lunch, salmon with brown rice for dinner, and Greek yogurt or a protein bar with fruit as snacks."),
    ("How much protein should I eat to lose weight?",
     "Coach Dan recommends 0.7 to 1 gram per pound of body weight a day, or at least your goal weight in grams. Spread it across your meals and start at breakfast."),
    ("Should I cut carbs to lose weight?",
     "No. Choose high-fiber carbs and fill the rest of your plate with them after protein and vegetables. Adults need about 130 grams of carbs a day for brain function, and more to fuel exercise."),
    ("What should I buy at the grocery store for weight loss?",
     "Lean proteins (chicken, turkey, lean steak, fish, eggs, Greek yogurt, protein powder), high-fiber carbs (sweet potatoes, rice, quinoa, whole wheat pasta, sourdough), berries and fruit, vegetables, and healthy fats like avocado, peanut butter and almonds."),
    ("Can I still eat out and drink while losing weight?",
     "Yes, but every splurge pushes your goal back a little. If you have a deadline, set boundaries around drinks and eating out. A glass of wine can be a treat if it fits your plan, but it isn't a health food."),
    ("Is the meal plan PDF really free?",
     "Yes. Download it from this page. No email or sign-up needed."),
]

html = page(
    SLUG,
    "Meal Plan for Weight Loss + Grocery List (Free PDF) | Fig Performance",
    "A simple meal plan for weight loss from Coach Dan: protein, carbs, fats and fiber at every meal, breakfast to snacks, a grocery list and a free PDF.",
    "Simple Meal Plan for Weight Loss + Grocery List (Free PDF)",
    "Nutrition", "Simple Meal Plan for Weight Loss (Free PDF)",
    "Protein, carbs, fats and fiber at every meal: options, a sample day and a grocery list. No email needed.",
    [("rule", "The one rule"), ("plate", "Build your plate"), ("breakfast", "Breakfast"), ("lunch", "Lunch"), ("dinner", "Dinner"),
     ("snacks", "Snacks"), ("sample", "Sample day"), ("grocery", "Grocery list"), ("eating-out", "Eating out and drinking"), ("download", "Free PDF")],
    body, faqs, "Meal Plan for Weight Loss", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
