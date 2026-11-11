"""Article: building muscle after 50 (from Coach Dan's voice memo; approved by Dan Nov 11 2026)."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-11"
SLUG = "building-muscle-after-50"
PETERSON = "https://pmc.ncbi.nlm.nih.gov/articles/PMC2995836"
PROTAGE = "https://doi.org/10.1016/j.jamda.2013.05.021"
CREATINE_QA = "https://pmc.ncbi.nlm.nih.gov/articles/PMC7871530"
CREATINE_ISSN = "https://doi.org/10.1186/s12970-017-0173-z"

body = f"""<p class="legal-intro">Here's the question I get from almost every new client in their 50s, usually asked a little sheepishly: "Can I still build muscle, or am I just slowing things down?"</p>
<p>You can build muscle. Not "maintain." Build. How much depends on where you're starting, and I'll give you honest numbers below. But the people doing it in my gym are 50, 60, 70 and 73, and the research backs them up. Here's what changes after 50, what doesn't, and exactly how I'd approach it.</p>

<h2 id="howmuch">How much muscle can you build after 50? It depends on one thing</h2>
<p>Have you ever trained hard? Not "gone to the gym." Trained. Followed a real strength phase, pushed sets close to failure, added weight week after week for months. Most people over 50 never have, and that's good news, because the biggest gains in life go to people doing proper strength training for the first time.</p>
<p>If you've never done a proper strength phase, I think you can put on a pound of muscle a month, maybe a couple, in the early going, as long as you're training close to failure and progressing the weight. If you've been lifting seriously for years, it's slower, and the wins are more about holding what you've got and adding strength.</p>
<p>The research lands in the same place. The largest review on this pooled 49 studies and 1,328 adults aged 50 and older doing supervised, whole-body strength training. On average they gained about 2.4 pounds of lean mass in roughly 20 weeks, and the people doing higher-volume programs gained more (<a href="{PETERSON}" target="_blank" rel="noopener noreferrer">Peterson et al., 2011</a>). That's the average across every kind of program, including gentle ones. Train the way I'm about to describe and you're aiming for the top of that range, not the middle.</p>
{stats([("~2.4 lb", "average lean mass gained in 20 weeks, adults 50+ (49 studies)"), ("1 lb/mo", "a realistic early target if you've never trained hard"), ("3&ndash;8%", "muscle lost per decade if you don't lift")])}
<p>For context, a sedentary adult over 50 loses roughly 3% to 8% of their muscle per decade. A few months of real training doesn't just stop that. It reverses several years of it.</p>

<h2 id="changes">What changes after 50</h2>
<p>Your body isn't 20 anymore. It's changed, and pretending otherwise is how people over 50 get hurt or burn out. Three things are real:</p>
<ul>
  <li><strong>Recovery takes longer.</strong> You need more time between hard sessions than you did in your 20s and 30s. You can't do what you did then and bounce back by Tuesday.</li>
  <li><strong>Protein matters more.</strong> You start losing muscle with age, and your muscle responds less to each meal than it used to. The fix is more of the signal, not less.</li>
  <li><strong>Sleep, nutrition and supplementation stop being optional.</strong> At 25 you could get away with sloppy. At 55 you have to be on top of them to get results.</li>
</ul>
{pullquote("Your body doesn't recover the way it did in your 20s. That's not a reason to train less. It's a reason to recover better.", "Coach Dan Figueroa")}

<h2 id="method">The method: get stronger, and muscle follows</h2>
<p>Muscle is a byproduct of getting stronger. I don't chase a pump or soreness. I chase a number going up every week on six movements:</p>
<ol>
  <li><strong>Push:</strong> dumbbell bench press</li>
  <li><strong>Pull:</strong> lat pulldown or row</li>
  <li><strong>Squat:</strong> box squat or goblet squat</li>
  <li><strong>Hinge:</strong> Romanian deadlift</li>
  <li><strong>Carry:</strong> farmer's carry</li>
  <li><strong>Overhead:</strong> dumbbell overhead press</li>
</ol>
<p>Here's how the reps run. Month one, 8 to 10 reps per set to learn the lifts. Month two, 5 to 6 reps, heavier. Month three, 1 to 5 reps, heavy. Every week we add two reps or 2.5 to 5 pounds. And the sets have to get close to failure. Not to failure every time, but close enough that the last two reps are hard. That's the part most people over 50 have never done, and it's the part that builds muscle.</p>

<h2 id="rest">Rest days are part of the program</h2>
<p>I highly recommend them. After 50, more recovery between workouts is not a luxury, it's how you maximize results. My default for clients over 50:</p>
<ul>
  <li><strong>Two to three lifting days a week</strong>, never back to back.</li>
  <li><strong>Walk on the off days.</strong> Movement without recovery debt.</li>
  <li><strong>Sleep seven hours or more.</strong> Growth hormone is released while you sleep. Short sleep means less muscle from the same workout, more appetite, and worse food choices.</li>
</ul>
<p>If you feel beat up going into a session, that's information. Pull the weight back 10% that day and keep the habit. Consistency over months is what builds muscle after 50, not heroics in one week.</p>

<h2 id="protein">Protein: keep it as high as you can</h2>
<p>As you get older you start losing muscle, so protein is how you hold onto it. My rule: eat your goal weight in grams of protein every day. Want to weigh 180? About 180 grams. Spread it over three or four meals, 30 to 40 grams each, because after 50 your muscle needs a bigger dose per meal to get the signal.</p>
<p>For context, the expert group on protein and aging recommends at least 1.0 to 1.2 grams per kilogram of body weight for older adults, and 1.2 or more for those who exercise (<a href="{PROTAGE}" target="_blank" rel="noopener noreferrer">Bauer et al., 2013</a>). The goal-weight rule puts you well above that, which is where I want you. Most of my clients are shocked at how little protein they were actually eating once they track it for three days.</p>

<h2 id="creatine">Creatine: if you can take it, your grandma can take it</h2>
<p>I highly recommend creatine monohydrate to almost everyone over 50. It's great for building muscle and strength, and it's the most studied supplement in sports science. Here's what the research says:</p>
<ul>
  <li><strong>It's safe.</strong> A 2021 review by the leading creatine researchers went through the common fears one by one: kidney damage, hair loss, dehydration, cramping. None hold up in healthy people at normal doses. The kidney myth traces back to a single 1998 case report of a man who already had kidney disease (<a href="{CREATINE_QA}" target="_blank" rel="noopener noreferrer">Antonio et al., 2021</a>). The International Society of Sports Nutrition's position stand says the same (<a href="{CREATINE_ISSN}" target="_blank" rel="noopener noreferrer">Kreider et al., 2017</a>).</li>
  <li><strong>It works for older adults.</strong> The same review found accumulating evidence of benefits in older populations, especially combined with strength training.</li>
  <li><strong>It may help your brain, too.</strong> Research on creatine and cognition is newer, but it points to benefits for memory, especially in older adults.</li>
  <li><strong>The dose:</strong> 3 to 5 grams a day is the researched standard. I use 5 to 10 grams a day with clients. No loading phase needed. Monohydrate, the cheap kind. The only people who need to check with a doctor first are those with existing kidney disease.</li>
</ul>
{callout("Supplements worth it after 50", "Short list", ["Creatine monohydrate, 5 to 10 g a day", "Protein powder only if you can't hit your number with food", "Everything else is a conversation at your consult, not a default"])}

<h2 id="expect">What to expect, month by month</h2>
<p>Strength comes fast. In the first three months most clients over 50 add a lot to their main lifts, because the nervous system learns the movements before the muscle catches up. Visible muscle lags strength by a couple of months. By month three the InBody shows it moving; by month six it's obvious in the mirror and in your clothes.</p>
<p>That's why I scan every client every four to six weeks. The scale can't tell you whether you gained muscle or fat. The InBody can, and watching skeletal muscle mass climb is the most motivating number in the gym.</p>

<h2 id="coach">Start this week</h2>
<p>If you're over 50 and you've been "maintaining," you've been leaving the best part on the table. Come in for a free consult. The InBody will tell you your skeletal muscle mass today, and in three months we'll scan again and you'll see it move.</p>
<p>Fig Performance is a <a href="/">private one-on-one personal training gym in Placentia</a>, serving Yorba Linda, Brea, Fullerton and Anaheim Hills. Related: <a href="/build-muscle-after-60">can you build muscle after 60?</a>, <a href="/workout-plan-for-men-over-40">workout plan for men over 40</a>, <a href="/strength-training-for-women-over-50">strength training for women over 50</a> and <a href="/strength-training-for-women-over-60">strength training for women over 60</a>. Can't make it in person? Try <a href="/online-personal-trainer">online coaching</a>.</p>
<p><em>Check with your doctor before starting a new exercise or supplement program, especially if you have kidney disease, a heart condition, or a recent injury or surgery.</em></p>
{CTA}"""

faqs = [
    ("Can you really build muscle after 50?",
     "Yes. A review of 49 studies found adults over 50 gained about 2.4 pounds of lean mass in roughly 20 weeks of strength training. People who have never trained hard can gain faster, around a pound a month early on."),
    ("How fast can you build muscle after 50?",
     "If you've never done a proper strength phase, about a pound of muscle a month is a realistic early target, provided you train close to failure and add weight weekly. Experienced lifters gain more slowly."),
    ("How many rest days do you need after 50?",
     "Lift two to three days a week, never back to back, and walk on the off days. Recovery takes longer after 50, and sleep of seven hours or more is part of the program."),
    ("How much protein do I need to build muscle after 50?",
     "Coach Dan's rule: your goal weight in grams per day, spread over three or four meals. Experts recommend at least 1.2 g per kilogram for older adults who exercise; the goal-weight rule lands above that."),
    ("Is creatine safe for people over 50?",
     "Yes for healthy adults. A 2021 expert review found no support for the kidney, hair loss or cramping fears at normal doses, and benefits for older adults. Coach Dan uses 5 to 10 grams of creatine monohydrate a day. Check with your doctor if you have kidney disease."),
    ("How long until I see results?",
     "Strength improves within weeks. The InBody usually shows muscle moving by three months, and it's obvious in the mirror by six."),
]

html = page(
    SLUG,
    "Building Muscle After 50: What Really Works | Fig",
    "Building muscle after 50: how much you can realistically gain, why recovery and protein matter more, the training method, and the research on creatine's safety.",
    "Building Muscle After 50: What Really Works",
    "Fitness after 40", "Building Muscle After 50",
    "Yes, you can build it. How much depends on whether you've ever trained hard. Honest numbers, the method, and creatine.",
    [("howmuch", "How much can you build?"), ("changes", "What changes after 50"), ("method", "The method"), ("rest", "Rest days"),
     ("protein", "Protein"), ("creatine", "Creatine"), ("expect", "What to expect"), ("coach", "Start this week")],
    body, faqs, "Building Muscle After 50", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
