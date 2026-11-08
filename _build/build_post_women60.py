"""Article: strength training for women over 60 (from Coach Dan's voice memos; approved by Dan Nov 7 2026)."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-07"
SLUG = "strength-training-for-women-over-60"
LIFTMOR = "https://doi.org/10.1002/jbmr.3284"
COCHRANE = "https://doi.org/10.1136/bjsports-2019-101512"
PROTAGE = "https://doi.org/10.1016/j.jamda.2013.05.021"
DGA = "https://www.dietaryguidelines.gov/"
CDC = "https://cdc.gov/physical-activity-basics/guidelines/older-adults.html"

body = f"""<p class="legal-intro">Teresa came to me at 60 with a shoulder injury. She couldn't do a single bodyweight exercise. About three months later she did her first pull-up. Today she bench presses about 85 pounds for reps.</p>
<p>I'm not telling you that to impress you. I'm telling you because almost every woman over 60 who walks into my gym assumes that kind of progress is for someone else. It isn't. Here's how I train women over 60, what the research says about bone, balance and muscle at this age, and what I'd tell you if you've been told to take it easy.</p>

<h2 id="same">The formula doesn't change at 60</h2>
<p>Here's my honest answer to "how is training a woman at 60 different from training one at 50?" It isn't, really. The formula is the same for everyone who walks through my door: progressive weight training, the six movements, enough protein, enough sleep. I don't treat anyone differently because of a number.</p>
<p>What I do is listen to the body in front of me. If a client is still cycling or dealing with menopause symptoms, we train through it and adjust: a little less intensity on a rough day, a little more food that week, and we keep the routine. Consistency beats perfection every time. For women past menopause, the hormones have settled, and the only thing that changes is the starting point.</p>
{pullquote("I don't train a 60-year-old differently. I find her starting point, then we get a little stronger every week.", "Coach Dan Figueroa")}

<h2 id="bone">Lift heavy for your bones</h2>
<p>The standard advice to women with low bone density has been light weights and caution. In 2018, Australian researchers tested the opposite. The LIFTMOR trial took 101 postmenopausal women, average age 65, all with low bone mass, and had half of them lift heavy under supervision twice a week for eight months: deadlifts, overhead presses and back squats, five sets of five at more than 85% of their max. The other half did a gentle home program.</p>
<p>The heavy-lifting group gained 2.9% bone density in the lumbar spine while the gentle group lost 1.2%. They improved on every functional test and even stood taller. Across eight months, there was one adverse event, a minor back spasm (<a href="{LIFTMOR}" target="_blank" rel="noopener noreferrer">Watson et al., 2018</a>).</p>
<p>Five sets of five is a good program. It sits in the middle: it builds muscle and it builds strength. I'll also take clients even lower, to sets of one, two or three reps, because that unlocks a different kind of strength. You're desensitizing your body to heavy resistance and teaching it to handle more and more. That's exactly what bone responds to.</p>
<p>Is there anything I avoid with women over 60? Honestly, no. There are so many exercises and so many variations that there's always a way to build more muscle: grip, traps, glutes, internal and external rotation, knee flexion, the hinge, even the neck, which protects you from whiplash and tech neck. We regress when we need to. We don't skip.</p>

<h2 id="balance">Balance and falls: it's strength, not a wobble board</h2>
<p>Falls are what end independence, and the research on preventing them is strong. A Cochrane review of 108 trials found exercise reduces the rate of falls in older adults by 23%, and programs that combine balance and functional work with resistance training cut falls by about a third (<a href="{COCHRANE}" target="_blank" rel="noopener noreferrer">Sherrington et al., 2019</a>). The CDC recommends balance work alongside strength training at least two days a week for adults 65 and older (<a href="{CDC}" target="_blank" rel="noopener noreferrer">CDC</a>).</p>
<p>Here's how I approach it. A few months ago Danielle came in for a consultation. She'd been in a car accident and had been tripping and falling ever since. She'd seen three doctors. I told her we needed to re-establish the signal between her brain and her muscles, and I walked her through how I'd do it, three ways:</p>
<ol>
  <li><strong>Isometrics.</strong> Holding positions under load. They rebuild the brain-to-muscle connection and they're about as safe as strength training gets.</li>
  <li><strong>Eccentrics.</strong> Slow lowering. Eccentric work builds stability and strength fast, with very low risk.</li>
  <li><strong>Unilateral work.</strong> Training one side at a time, mostly legs: single-leg hip thrusts, single-leg deadlifts, Bulgarian split squats, reverse lunges, single-leg extensions and curls, cable kickbacks, single-leg abduction. Each side has to stabilize on its own, and the weaker side can't hide.</li>
</ol>
<p>Danielle told me it was the first advice she'd been given that felt practical, something she could actually go do rather than a prescription or a list of things to stop doing. That's the point of training balance this way: it's a plan, not a warning.</p>
<p>Then there's the stabilizers. The muscles that hold your knee steady, especially the abductors on the outside of the hip, do a lot of the work of not falling. Train them and your balance improves without ever standing on a foam pad. Stability is really just strength plus flexibility, which together give you mobility, and mobility is what keeps you on your feet.</p>
{callout("How I train balance", "Three tools, all low risk", ["Isometric holds to rebuild the brain-to-muscle signal", "Slow eccentrics for stability and strength", "Unilateral leg work so each side learns to stand on its own"])}

<h2 id="movements">The six movements, same as everyone</h2>
<p>I don't have a separate program for women over 60. I have a separate starting point. The movements are the same ones I give a 45-year-old executive:</p>
<ol>
  <li><strong>Push:</strong> flat or incline dumbbell press</li>
  <li><strong>Pull:</strong> reverse-grip lat pulldown or chest-supported row</li>
  <li><strong>Squat:</strong> box squat</li>
  <li><strong>Hinge:</strong> Romanian deadlift</li>
  <li><strong>Carry:</strong> farmer's carry</li>
  <li><strong>Overhead:</strong> dumbbell overhead press</li>
</ol>
<p>Plus core, rotation and the unilateral work above. If a movement hurts, there's an easier version.</p>

<h2 id="first">How the first three months look</h2>
<p>Teresa's first month was finding what she could do with a bad shoulder and building from there. The pattern I use for her and almost everyone:</p>
{stats([("8&ndash;10", "reps per set in month 1"), ("5&ndash;6", "reps per set in month 2"), ("1&ndash;5", "reps per set in month 3")])}
<p>Every week, we add two reps or 2.5 to 5 pounds to each lift. That's it. It sounds slow. Over three months it added up to Teresa's first pull-up.</p>

<h2 id="recover">Sleep, protein and fiber</h2>
<p><strong>Sleep first.</strong> Prioritize sleep and recovery over almost everything else, because that's where muscle is built. Your body releases growth hormone while you sleep. Sleep regulates your appetite and your stress, and when you're short on it you reach for junk. Hormones fluctuate at this stage of life; the routine shouldn't.</p>
<p><strong>Protein: your goal weight in grams.</strong> If you want to weigh 140, eat about 140 grams a day. For context, the expert group on protein and aging recommends at least 1.0 to 1.2 grams per kilogram of body weight for people over 65, and at least 1.2 for those who exercise (<a href="{PROTAGE}" target="_blank" rel="noopener noreferrer">Bauer et al., 2013</a>). The goal-weight rule lands well above that, which is where I want you, because after 60 your body needs a bigger dose of protein per meal to get the signal. Aim for 25 to 30 grams at each meal.</p>
<p><strong>Fiber: at least 22 grams a day.</strong> That's the Dietary Guidelines figure for women 51 and older (<a href="{DGA}" target="_blank" rel="noopener noreferrer">Dietary Guidelines for Americans</a>), and most women get far less. Fiber keeps your gut healthy, keeps you full, and makes the protein target easier to hit without feeling stuffed.</p>

<h2 id="teresa">Teresa's story</h2>
<p>Teresa, 60, came in with a shoulder injury and couldn't do a bodyweight exercise. We found her starting point and worked up from there. About three months in, she did her first pull-up. Today she bench presses about 85 pounds for reps. She's the reason I don't let anyone tell me what a woman over 60 can't do.</p>

<h2 id="late">Is it too late to start at 60? 65? 70?</h2>
<p>No. Randy, 73, came to me with arthritis in his shoulder and bench presses 135 pounds for reps, pain free. Sam started with me at 70 and deadlifts 135. The body adapts at every age. The only thing that changes is how carefully we pick the starting point.</p>
<p>If you're a woman over 60 in Placentia, Yorba Linda, Brea, Fullerton or Anaheim Hills and you've been told to take it easy, come in for a free consult. We'll do an InBody scan, see how you move, and I'll show you what your starting point actually is.</p>
<p>Fig Performance is a <a href="/">private one-on-one personal training gym in Placentia</a>. Related: <a href="/strength-training-for-women-over-50">strength training for women over 50</a>, <a href="/strength-training-for-seniors">strength training for seniors</a>, <a href="/build-muscle-after-60">can you build muscle after 60?</a> and <a href="/hip-thrust">hip thrust form</a>. Can't make it in person? Try <a href="/online-personal-trainer">online coaching</a>.</p>
<p><em>Check with your doctor before starting a new exercise program, especially if you have osteoporosis, a heart condition, or a recent injury or surgery.</em></p>
{CTA}"""

faqs = [
    ("Is strength training safe for women over 60?",
     "Yes, with an assessment first and gradual progress. In the LIFTMOR trial, women over 60 with low bone mass lifted heavy twice a week for eight months with one minor adverse event, and gained spine bone density."),
    ("How often should a woman over 60 lift weights?",
     "At least two days a week, per the CDC, with balance work included. Many of Coach Dan's clients train two or three times a week."),
    ("Can women over 60 build muscle?",
     "Yes. Teresa, 60, went from no bodyweight exercises to a pull-up in about three months and now benches about 85 pounds for reps."),
    ("What exercises improve balance for women over 60?",
     "Isometric holds, slow eccentrics, and single-leg work like split squats, single-leg deadlifts and single-leg hip thrusts, plus hip abduction for the stabilizers. Research shows combining balance work with strength training cuts falls by about a third."),
    ("Does lifting weights help osteoporosis?",
     "Heavy, supervised resistance training improved spine bone density by about 3% in eight months in postmenopausal women with low bone mass, while a gentle program lost bone. Talk to your doctor about your specific situation."),
    ("How much protein and fiber does a woman over 60 need?",
     "Coach Dan's rule: your goal weight in grams of protein per day, 25 to 30 grams per meal. Fiber: at least 22 grams a day, the Dietary Guidelines figure for women 51 and older."),
]

html = page(
    SLUG,
    "Strength Training for Women Over 60: How to Start | Fig",
    "Strength training for women over 60: why the formula doesn't change, lifting heavy for bone, training balance, protein and fiber, and Teresa's first pull-up.",
    "Strength Training for Women Over 60: How to Start and How Far You Can Go",
    "Fitness after 40", "Strength Training for Women Over 60",
    "The formula doesn't change at 60. Your starting point does. Bone, balance, protein, and Teresa's first pull-up.",
    [("same", "The formula doesn't change"), ("bone", "Lift heavy for your bones"), ("balance", "Balance and falls"), ("movements", "The six movements"),
     ("first", "The first three months"), ("recover", "Sleep, protein, fiber"), ("teresa", "Teresa's story"), ("late", "Too late to start?")],
    body, faqs, "Strength Training for Women Over 60", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
