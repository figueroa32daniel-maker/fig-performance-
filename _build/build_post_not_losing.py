"""'Why am I not losing weight?' rewritten from Coach Dan's voice memo (Nov 3 2026)."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote

SLUG = "why-am-i-not-losing-weight"
DATE = "2026-10-30"
HAUB = "https://edition.cnn.com/2010/HEALTH/11/08/twinkie.diet.professor/index.html"
PONTZER = "https://www.nbcnews.com/news/ncna1276650"

body = f"""<p class="legal-intro">If you're not losing weight, you're almost always not in a calorie deficit. That's the honest answer. Maybe it's not enough movement, not enough strength training, too much food, too much alcohol, or a little of all of them. Here are the reasons I see most with clients over 40, and what to do about each one.</p>

<h2 id="deficit">1. You're not truly in a calorie deficit</h2>
<p>To lose weight, you have to eat fewer calories than you burn. There's no way around it. You can see it with the weight-loss medications everyone's talking about, like tirzepatide and semaglutide: a big part of how they work is turning down your appetite. You eat less, you end up in a deficit, and you lose weight.</p>
<p>If the scale isn't moving, the deficit isn't there. Usually it's one of these: not enough movement, not enough strength training, too much food, or too much alcohol.</p>

<h2 id="healthy">2. Eating healthy isn't the same as eating the right amount</h2>
<p>Say you need about 1,800 calories a day to lose weight, and you're eating 2,200 calories of salmon, avocado, nuts and smoothies. That's great food, but you won't lose weight, and you might gain.</p>
<p>In 2010, Kansas State University nutrition professor Mark Haub proved the point the other way around. He ate mostly junk food, like Twinkies, snack cakes and chips, but kept his total calories in a deficit, and he lost 27 pounds in 10 weeks (<a href="{HAUB}" target="_blank" rel="noopener noreferrer">CNN</a>). That doesn't mean you should eat junk food. You won't feel your best. But it shows that the amount you eat decides whether you lose weight.</p>
<p><strong>What to do:</strong> eat the right portion sizes, built from nutrient-dense foods. That's why I coach 80/20: about 80% whole, nutrient-dense food and 20% food you enjoy, in the right amounts.</p>

<h2 id="protein">3. You're not eating enough protein</h2>
<p>Most people think the chicken on the side of their salad, two eggs, or one scoop of protein powder, one protein bar or one protein shake is enough for the day. It isn't.</p>
<p><strong>What to do:</strong> aim for 0.7 to 1 gram of protein per pound of body weight every day, whether you're training or not. If you have a lot of weight to lose, base it on your goal weight. Build your meals around protein, and start early. Your appetite tends to drop off later in the day, so get protein in at breakfast and before you train. Your muscles need it to recover and grow.</p>

<h2 id="training">4. Your workouts aren't built to change your body</h2>
<p>Showing up to work out isn't the same as training to change your body. You need progressive overload: lifting a little more weight, or doing a few more reps, over time. That's how you build and keep muscle, and muscle keeps your metabolism up.</p>
<p><strong>What to do:</strong> lift weights at least 2 or 3 times a week, and keep getting stronger. If you need a plan, start with the beginner workout plan for <a href="/beginner-workout-plan-for-women">women</a> or <a href="/beginner-workout-plan-for-men">men</a>.</p>

<h2 id="movement">5. You sit more than you think</h2>
<p>This is the bottleneck for most of the CEOs, CFOs, business owners, managers and work-from-home clients I coach. Most people didn't gain the weight because they started eating more. They gained it because their life became sedentary.</p>
<p>And it's usually not your metabolism. A large 2021 study of more than 6,000 people found that metabolism stays fairly steady from about age 20 to 60 (<a href="{PONTZER}" target="_blank" rel="noopener noreferrer">NBC News</a>). What changes is how much we move.</p>
<p>When your body doesn't move, you get stiff. When you get stiff, you get pain. When you're in pain, you work out less, you lose abilities you used to have, and you become even more sedentary.</p>
<p><strong>What to do:</strong> walk more. My target for clients is more than 5,000 steps a day, and ideally 6,000 or more. Walk after meals, take calls on your feet, and get up from your desk every hour.</p>

<h2 id="sleep">6. You're not sleeping enough</h2>
<p>A lot of people act like they don't need sleep. Sleep is when your muscles rebuild and recover, and it affects your energy, your mood and your appetite. Sleep is just as important as working out.</p>
<p><strong>What to do:</strong> protect a consistent sleep window like you'd protect a client meeting.</p>

<h2 id="stress">7. Your stress is out of control</h2>
<p>I see a lot of clients so stressed out that they get sick often, with headaches and colds that keep coming back. Most people do a poor job of managing stress, and it gets in the way of their training, sleep and eating.</p>
<p><strong>What to do:</strong> have a go-to way to bring your stress down. Go on a walk, journal, watch your favorite show, get a massage, have the occasional glass of wine, or spend less time on your phone.</p>

<h2 id="measure">8. You're not measuring anything</h2>
{pullquote("What you don't measure, you can't manage.")}
<p>If you don't know your starting point, you can't tell what's working. The scale alone also misses a lot: if you're building muscle while losing fat, your weight can stay the same while your body improves.</p>
<p><strong>What to do:</strong> get a baseline. Get an <a href="/inbody-scan-placentia">InBody scan</a> or DEXA scan, track your weight, and find out how many calories you're eating now and how many you need. Then follow one plan, re-measure and adjust.</p>

<h2 id="medical">9. Something medical is in the mix</h2>
<p>Thyroid problems, hormone changes and some medications can affect your weight. If you think that's you, see your doctor. A good coach works alongside your doctor, not instead of them.</p>

<h2 id="plan">What actually works after 40</h2>
<p>At Fig Performance, every client follows the same loop: <strong>Scan. Plan. Train. Recover. Re-scan.</strong></p>
<ul>
  <li><strong>Scan</strong> with InBody so you know your real starting point.</li>
  <li><strong>Plan</strong> your calories, protein and training around your goals and schedule.</li>
  <li><strong>Train</strong> with coached, progressive strength sessions, and walk every day.</li>
  <li><strong>Recover</strong> with sleep, stress management, red light and vibration therapy.</li>
  <li><strong>Re-scan</strong> to see what changed, then adjust.</li>
</ul>
<p>For the step-by-step version, read <a href="/how-to-lose-weight-after-40">how to lose weight after 40</a>, or see how <a href="/nutrition-coaching-placentia">nutrition coaching</a> works. If you've been doing "everything right" and still feel stuck, your free consult will show you why, with real numbers.</p>
{CTA}"""

faqs = [
    ("Why am I not losing weight even though I eat healthy and exercise?",
     "Most likely you're not in a calorie deficit. Healthy food still has calories, and it's easy to eat more than you need. Not enough protein, not enough daily movement, too much alcohol, poor sleep and high stress also get in the way."),
    ("Can you lose weight eating junk food?",
     "Technically, yes. In 2010, Kansas State University professor Mark Haub lost 27 pounds in 10 weeks eating mostly junk food in a calorie deficit. That shows calories decide weight loss, but you'll feel and perform much better eating mostly nutrient-dense food."),
    ("How much protein should I eat to lose weight?",
     "Coach Dan recommends 0.7 to 1 gram of protein per pound of body weight daily (use your goal weight if you have a lot to lose), spread across your meals and started early in the day."),
    ("Does your metabolism slow down after 40?",
     "Not as much as people think. A large 2021 study found metabolism stays fairly stable from about 20 to 60. Most weight gain after 40 comes from moving less and losing muscle, which walking and strength training fix."),
    ("When should I see a doctor about not losing weight?",
     "If you've been consistent with a calorie deficit, training and sleep for a few months without change, or you notice other symptoms, talk to your doctor. Thyroid problems, hormone changes and some medications can affect weight."),
]

html = page(
    SLUG,
    "Why Am I Not Losing Weight After 40? | Fig Performance",
    "Not losing weight after 40? You're probably not in a true calorie deficit. Coach Dan on portions, protein, steps, sleep, stress and measuring progress.",
    "Why Am I Not Losing Weight? (When You Already Eat Well and Exercise)",
    "Fitness after 40", "Why Am I Not Losing Weight? (When You Already Eat Well and Exercise)",
    "Nine reasons the scale won't move after 40, and what to do about each one, from Coach Dan.",
    [("deficit", "Not in a deficit"), ("healthy", "Healthy isn't the right amount"), ("protein", "Not enough protein"),
     ("training", "Workouts that don't progress"), ("movement", "Sitting too much"), ("sleep", "Sleep"), ("stress", "Stress"),
     ("measure", "Not measuring"), ("medical", "Medical factors"), ("plan", "What works after 40")],
    body, faqs, "Why Am I Not Losing Weight?", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
