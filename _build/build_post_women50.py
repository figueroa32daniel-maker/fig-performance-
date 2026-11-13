"""Article: strength training for women over 50 (from Coach Dan's voice answers, Nov 3 2026)."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote

DATE = "2026-11-03"
SLUG = "strength-training-for-women-over-50"
LIFTMOR = "https://pubmed.ncbi.nlm.nih.gov/28975661/"

body = f"""<p class="legal-intro">Strength training for women over 50 isn't a gentler, watered-down version of training. Your age doesn't decide your program. Your body does: your injuries, your mobility, your strength and your goals. I have a 37-year-old client who can't do a pull-up, and a 60-year-old who can. Here's how I train women over 50 at Fig Performance, and what changes during and after menopause.</p>

<h2 id="age">Your age doesn't decide your program</h2>
<p>I don't treat a 60-year-old like she's 90, or a 40-year-old like she's 60. Every client gets the same effective coaching, because I want all my clients to feel strong, confident, capable and powerful.</p>
<p>Teresa started with me at 60 with a shoulder injury, unable to do a single bodyweight exercise. About three months later she did her first pull-up, and today she bench presses about 85 pounds for reps. <a href="/build-muscle-after-60">Read how she progressed, month by month</a>. Sam is 70: he curls 30-pound dumbbells, presses the 50s on the dumbbell bench, and deadlifts 135 pounds.</p>
{callout("Client results", "Age didn't decide their program", ["Teresa, 60: first pull-up in about 3 months, now benches about 85 pounds for reps", "Sam, 70: deadlifts 135 pounds, dumbbell benches the 50s, curls 30-pound dumbbells"])}
<p>Everybody gets strong. Everybody keeps the ability to jump, run, pick things up, set them down and lift them overhead.</p>

<h2 id="assessment">It starts with an assessment</h2>
<p>Before we train, I assess everything that matters:</p>
<ul>
  <li>Knees, hips and ankles</li>
  <li>Your gait (how you walk) and your posture</li>
  <li>Neck mobility, shoulder mobility and hip flexibility</li>
</ul>
<p>Then we talk: your activity level, your current fitness, your background, past injuries and anything you're struggling with now. That gives us both objective and subjective information, so the training and nutrition plan fit you.</p>
<p>If you're working with a physician, physical therapist or chiropractor, their notes are really appreciated. I like to work alongside them so we're all on the same page, and so I stay within my scope as a coach.</p>
<p>From there, we work on your injuries and limitations, your flexibility and mobility, and your strength. Then we build your capacity.</p>

<h2 id="menopause">What changes during and after menopause</h2>
<p>As estrogen drops, women tend to lose bone and muscle faster. Strength training is one of the best tools you have to slow both.</p>
<ul>
  <li><strong>Bones:</strong> lifting heavy can help. In the LIFTMOR trial, postmenopausal women with low bone mass did supervised, progressively heavy lifting twice a week for 8 months and improved their bone density, with no increase in injuries (<a href="{LIFTMOR}" target="_blank" rel="noopener noreferrer">Watson et al., 2018</a>). The key word is progressive: you build up to heavy, you don't start there.</li>
  <li><strong>Muscle:</strong> progressive strength training is how you keep and build it. Track your lifts so you know you're getting stronger.</li>
  <li><strong>Belly fat:</strong> fat tends to shift toward the midsection after menopause. The fix is the same as always: a calorie deficit, enough protein, strength training and daily walking. Read <a href="/how-to-lose-belly-fat-after-menopause">how to lose belly fat after menopause</a>.</li>
  <li><strong>Protein:</strong> needs go up a little with age. Aim for at least your goal body weight in grams of protein a day.</li>
  <li><strong>Sleep and hot flashes:</strong> exercise can help sleep and mood, but hormone questions belong with your doctor.</li>
</ul>

<h2 id="how-often">How often to lift</h2>
<p>Three full-body sessions a week, every other day: Monday, Wednesday and Friday, or Tuesday, Thursday and Saturday. Walk every day, at least 30 minutes, working up to about 90. Pick a schedule you can keep for years, because consistency beats everything. <strong>Chase progress, not perfection.</strong></p>
<p>For the exact exercises, sets and reps, use the <a href="/beginner-workout-plan-for-women">beginner workout plan for women</a>. For more on the basics, read <a href="/strength-training-for-women-over-40">strength training for women over 40</a>.</p>

<h2 id="safety">Before you start</h2>
<p>If you have osteoporosis, a heart condition, a recent injury or surgery, check with your doctor first. Heavy lifting with low bone density should be supervised and built up gradually.</p>

<h2 id="coach">Train with a coach in Placentia</h2>
<p>At Fig Performance, every plan starts with a free consult, an <a href="/inbody-scan-placentia">InBody scan</a> and the assessment above. Can't make it in person? Try <a href="/online-personal-trainer">online coaching</a>.</p>
{CTA}"""

faqs = [
    ("Is it safe for women over 50 to lift heavy weights?",
     "Yes, when you build up gradually and train with good form. In the LIFTMOR trial, postmenopausal women with low bone mass improved bone density with supervised, progressively heavy lifting. Check with your doctor first if you have osteoporosis or another condition."),
    ("How should a woman over 50 start strength training?",
     "Start with an assessment of your joints, mobility and injuries, then train full body three times a week, starting light and adding weight over time. Walk daily, and eat at least your goal weight in grams of protein."),
    ("Does strength training help with menopause?",
     "It helps slow the bone and muscle loss that speeds up after menopause, and it can help with weight, sleep and mood. For hot flashes and hormone questions, talk to your doctor."),
    ("Can a woman over 50 build muscle?",
     "Yes. At Fig Performance, Teresa did her first pull-up at 60 and now bench presses about 85 pounds for reps. Progressive strength training builds muscle at any age."),
    ("How often should a woman over 50 lift weights?",
     "Three full-body sessions a week, every other day, plus at least 30 minutes of walking daily."),
]

html = page(
    SLUG,
    "Strength Training for Women Over 50 & Menopause | Fig Performance",
    "Strength training for women over 50, from Coach Dan: why age doesn't decide your program, the assessment, menopause, bone density and how often to lift.",
    "Strength Training for Women Over 50: Age Doesn't Decide Your Program",
    "Fitness after 40", "Strength Training for Women Over 50",
    "Your body decides your program, not your age. The assessment, menopause, and how often to lift.",
    [("age", "Age doesn't decide it"), ("assessment", "The assessment"), ("menopause", "Menopause"),
     ("how-often", "How often to lift"), ("safety", "Before you start"), ("coach", "Train with a coach")],
    body, faqs, "Strength Training for Women Over 50", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
