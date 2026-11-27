"""Article: calorie deficit after 40 (from Coach Dan's voice memos; approved by Dan Nov 16 2026)."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-16"
SLUG = "calorie-deficit"
HAUB = "https://consumerist.com/2010/11/08/professor-drops-27-pounds-in-10-weeks-on-twinkie-diet/"
BWP = "https://www.niddk.nih.gov/bwp"

body = f"""<p class="legal-intro">Every January the same thing happens. People slash their calories, double their cardio, lose eight pounds in three weeks, feel awful, and by March they've gained it back. Then they decide their metabolism is broken. It isn't. Weight loss is simple: burn more than you consume. The hard part is setting a deficit you can actually live with, and that's what this article is about.</p>
<p>Here's exactly how I set a calorie deficit for a new client, why it's not about what you eat or when you eat it, what goes wrong every January, and my three rules for the new year.</p>

<h2 id="simple">A calorie deficit is thermodynamics</h2>
<p>A calorie deficit means eating less than your body burns. It's the only way fat loss happens. Every diet that works, low-carb, keto, intermittent fasting, works because it puts you in a deficit. There's nothing special about fasting other than that it's a structured way of eating less.</p>
<p>The clearest proof is an experiment a nutrition professor at Kansas State University ran on himself in 2010. Mark Haub ate mostly Twinkies, snack cakes, Doritos and Oreos for ten weeks, but held himself to about 1,800 calories a day, down from about 2,500. He lost 27 pounds. His LDL, the "bad" cholesterol, dropped 20%, his HDL, the "good" cholesterol, rose 20%, and his triglycerides fell 39% (<a href="{HAUB}" target="_blank" rel="noopener noreferrer">reported by CNN</a>).</p>
{stats([("27 lb", "lost in 10 weeks"), ("1,800", "calories a day"), ("&minus;20%", "LDL cholesterol")])}
<p>Neither Haub nor I recommend the Twinkie diet. The point is what it proves: how much you eat decides whether you lose weight. What you eat decides how you feel doing it, whether you keep your muscle, and whether you can keep it up. The GLP-1 medications made the same point to millions of people. A lot of folks were sure their weight was hormones or inflammation. Then a drug turned their appetite down, they ate less, and the weight came off.</p>
{pullquote("It's not about what you eat or when you eat it. It's whether you're eating less than you burn. Everything else is how you make that livable.", "Coach Dan Figueroa")}

<h2 id="set">How I set a deficit for a new client</h2>
<ol>
  <li><strong>InBody scan.</strong> The scan gives us your basal metabolic rate, the calories your body burns at rest, based on your actual muscle and fat, not a formula's guess.</li>
  <li><strong>Your real week.</strong> How much you move, what kind of job you have, how often you train. A contractor and a CFO with the same BMR burn very different totals.</li>
  <li><strong>The deficit.</strong> Usually 300 to 500 calories a day below what you burn. The InBody report suggests a range, and we pick the number that fits your life.</li>
  <li><strong>A test week.</strong> The first week is a test. If the weight goes down, we've got it. If it doesn't, I give it two weeks before changing anything, because water can hold the scale still while fat is coming off, and then it drops all at once. That's why we scan weekly: the InBody shows what changed underneath the scale.</li>
</ol>
{callout("The setup", "Scan, then math", ["InBody for your BMR", "Add your activity and job", "Subtract 300 to 500 calories", "Test for one to two weeks, scan weekly, adjust"])}

<h2 id="low">How aggressive should a deficit be?</h2>
<p>A 1,000-calorie deficit can be done. I've done it with clients. <a href="/how-to-lose-10-pounds-in-a-month">Adriana lost 10 pounds in her first month</a> on roughly a 1,000-calorie daily deficit, about 500 from eating less and 500 from moving more. But I would not start someone there, especially someone who's very heavy. An aggressive deficit has to be calculated: you need a history of what you've been eating, how you felt at those calories, and an honest look at the trade-off. Cut harder and you get more headaches and your training suffers. Is it worth it for a few weeks? Sometimes. As a lifestyle? No.</p>
<p>For most clients over 40, 300 to 500 calories a day below what you burn is the number: about half a pound to a pound a week, slow enough to keep your muscle, your energy and your sanity. Be strategic, logical and reasonable, and think about whether you can still be doing it in six months.</p>

<h2 id="skinnyfat">Why "intermittent fasting worked" and you still look soft</h2>
<p>Here's a story I hear constantly. Someone starts intermittent fasting. They don't eat until 4 or 5 p.m., then they eat one meal, maybe 800 calories, they're full, they go to sleep, and they do it again the next day. They lose weight and they credit the fasting.</p>
<p>It's not the fasting. It's that they're eating 800 calories a day. That's 5,600 calories a week. Of course they lost weight.</p>
<p>Then a couple of months in, they come to me and say, "I lost the weight, but I'm not toned. I don't look defined. I look skinny fat." That's because they lost weight for the sake of losing weight, with almost no protein and no lifting, so a big share of what came off was muscle. The goal isn't a smaller number on the scale. It's better body composition: less fat, same or more muscle. That takes enough protein, strength training, and carbohydrates placed strategically around your training for recovery and performance.</p>
{pullquote("You didn't lose weight because of intermittent fasting. You lost weight because you were eating 800 calories a day.", "Coach Dan Figueroa")}

<p>One more reason not to go too low: as you lose weight, you burn less, so the same deficit shrinks over time. The NIH built a calculator around the real math, the <a href="{BWP}" target="_blank" rel="noopener noreferrer">Body Weight Planner</a>, and it shows weight loss slowing even when you do everything right. That slowdown isn't failure. It's why we re-scan and adjust.</p>

<h2 id="food">Build the diet from food you already eat</h2>
<p>I don't hand clients a meal plan full of food they don't like. I build their nutrition program from the foods they already enjoy, because they already have a routine with those foods, and it's easier to give a routine more structure than to replace it. Then we add intention:</p>
<ul>
  <li><strong>More protein.</strong> Your goal weight in grams a day. It keeps you full and protects your muscle in a deficit.</li>
  <li><strong>More fiber.</strong> Vegetables, fruit, beans, whole grains. Fuller on fewer calories, and better for your gut.</li>
  <li><strong>Fill the common gaps.</strong> Vitamin D, magnesium, zinc and iron are the ones I see people run low on. A blood test from your doctor tells you which you actually need; iron in particular shouldn't be taken unless you're low.</li>
</ul>
<p>A diet has to be two things to last: <strong>enjoyable and flexible.</strong> If I give someone food they don't like, they won't stick to it. So I use an 80/20 approach: about 80% of your food is the structured, protein-first plan built from things you enjoy, and 20% is whatever you want. Food is emotional and psychological. Going cold turkey on everything you like is how people end up bingeing in week three. Keeping a connection to the food you love is what makes it work for a year, not a month.</p>

<h2 id="wrong">What goes wrong every January</h2>
<p>There's an old saying, usually credited to Einstein, though nobody's sure who said it first: insanity is doing the same thing over and over and expecting different results. That's January. People try the same crash diet, the same 6 a.m. cardio, the same "this time I'll just have more willpower," and expect it to work this time. If you want a different result, you have to do something completely different.</p>
<p>And you have to be logical about it, not emotional. The scale goes up a pound after a salty dinner and people throw the whole plan out. A logical person looks at the weekly average and the InBody and asks whether the trend is moving. Usually it is.</p>

<h2 id="rules">My three rules for the new year</h2>
<p><strong>1. Get a coach.</strong> I'll practice what I preach here: I've paid for mentorships at $10,000, $6,000, $5,000 and $4,000, more than five courses, and hundreds of ebooks. Every one of them saved me time, because having a proven formula and someone to guide you through it is faster than figuring it out alone. If you're a business owner, you already know this: trade your money for time, not your time for money. If building your own nutrition plan takes you four hours and you still don't know whether it'll work, that's four hours you didn't have.</p>
<p><strong>2. Get a plan.</strong> Not "eat better." A number, a set of meals you like, a training schedule, and a date we check in.</p>
<p><strong>3. Do it, even when it's not the perfect time.</strong> There is no perfect time. The best time is now. It's actually better to start when life is busy and complicated, because that's how life is going to be, and you learn to do the work when it's hard. Then when things are easy, it feels like a piece of cake. As my therapist likes to say, stuff happens. You roll with the punches. You'll learn something either way.</p>

<h2 id="track">How to tell if it's working</h2>
<ul>
  <li><strong>Weekly average weight</strong>, not daily. Weigh every morning, average the week.</li>
  <li><strong>InBody every week or two</strong> while you're dialing in, then every four to six weeks. It tells you whether what you lost was fat or muscle, which is the only number that really matters.</li>
  <li><strong>Waist measurement</strong> every two weeks.</li>
</ul>
<p>If the weekly average is dropping half a pound to a pound and the InBody says it's fat, you're done adjusting. Keep going.</p>

<h2 id="coach">Start the year with a number, not a guess</h2>
<p>If you don't know what you burn, you can't set a deficit; you can only guess. A free consult at Fig Performance includes an InBody scan, so you leave with your BMR and your real muscle and fat numbers. From there, the deficit is math.</p>
<p>Fig Performance is a <a href="/">private one-on-one personal training gym in Placentia</a>, serving <a href="/personal-trainer-yorba-linda">Yorba Linda</a>, <a href="/personal-trainer-brea">Brea</a>, <a href="/personal-trainer-fullerton">Fullerton</a> and <a href="/personal-trainer-anaheim-hills">Anaheim Hills</a>. Related: <a href="/how-to-lose-weight-after-40">how to lose weight after 40</a>, <a href="/why-am-i-not-losing-weight">why you're not losing weight</a>, <a href="/nutrition-coaching-placentia">nutrition coaching</a> and the <a href="/meal-plan-for-weight-loss">free meal plan for weight loss</a>.</p>
<p><em>Fig Performance coaches are not registered dietitians. Talk to your doctor before starting a low-calorie diet or a supplement, especially if you have a medical condition or take medication.</em></p>
{CTA}"""

faqs = [
    ("What is a good calorie deficit for weight loss after 40?",
     "For most adults over 40, 300 to 500 calories a day below what you burn, about half a pound to a pound a week. Coach Dan sets it from an InBody scan of your basal metabolic rate plus your real activity and job."),
    ("Does it matter what you eat in a calorie deficit?",
     "For weight loss, the amount matters most. A Kansas State nutrition professor lost 27 pounds in 10 weeks eating mostly snack cakes at 1,800 calories a day. For muscle, energy and sticking with it, food quality matters: protein, fiber, and food you enjoy."),
    ("Is a 1,000-calorie deficit safe?",
     "It can be done for a short stretch, with high protein and lifting, but it's not where to start, especially if you're very heavy. Expect more headaches and lower performance. Most adults over 40 do better at 300 to 500 calories a day. Talk to your doctor if you have a medical condition."),
    ("Why am I in a calorie deficit but not losing weight?",
     "Water can hold the scale still while fat comes off, then drop all at once. Give a new deficit one to two weeks, track your weekly average, and use a body-composition scan to see what changed."),
    ("Does intermittent fasting work better than a calorie deficit?",
     "No. Intermittent fasting works because it's a structured way to eat fewer calories. One 800-calorie meal a day is a big deficit, and without enough protein and lifting it often leaves people skinny fat."),
    ("What is the 80/20 rule for dieting?",
     "About 80% of your food follows the plan, built from foods you already enjoy with more protein and fiber, and 20% is whatever you want. It keeps the diet enjoyable and flexible, which is what makes it last."),
]

html = page(
    SLUG,
    "Calorie Deficit After 40: How I Set One That Works | Fig",
    "How to set a calorie deficit after 40: InBody BMR, 300 to 500 calories a day, foods you already enjoy, the 80/20 rule, and three rules for the new year.",
    "Calorie Deficit After 40: How I Set One That Actually Works",
    "Fitness after 40", "Calorie Deficit After 40: How I Set One That Works",
    "Burn more than you eat. The trick is a deficit you can live with: InBody math, food you enjoy, and three rules for the new year.",
    [("simple", "It's thermodynamics"), ("set", "How I set it"), ("low", "How aggressive?"), ("skinnyfat", "Why you look soft"), ("food", "Food you already eat"),
     ("wrong", "What goes wrong in January"), ("rules", "Three rules for the new year"), ("track", "Is it working?"), ("coach", "Start with a number")],
    body, faqs, "Calorie Deficit After 40", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
