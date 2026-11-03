"""Article: 3-day beginner workout plan (women's plan from Coach Dan, Nov 3 2026; men's plan to follow).
DRAFT until Dan approves. Exercise choices, order and rest are Dan's. Rep ranges and warm-up style follow
common glute-focused programming (reviewed against Bret Contreras's published plans, nothing copied)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_pages import page, SITE, CTA

DATE = "2026-11-03"
SLUG = "3-day-beginner-workout-plan"
REST = "1:15&ndash;2 min"


def table(cols, rows):
    head = "".join(f"<th>{c}</th>" for c in cols)
    trs = "\n".join("    <tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"""<div class="price-table-wrap"><table class="price-table compare-table">
  <thead><tr>{head}</tr></thead>
  <tbody>
{trs}
  </tbody>
</table></div>"""


WARMUP = table(["Exercise", "Sets &times; reps"], [
    ("Cat-cow", "2 &times; 10"),
    ("Bird dog", "2 &times; 6 each side"),
    ("Front-to-back leg swing", "2 &times; 10 each leg"),
    ("Side-to-side leg swing", "2 &times; 10 each leg"),
    ("Banded glute bridge", "2 &times; 15"),
    ("Lateral band walk", "2 &times; 10 each way"),
])
UPPER_WARMUP = table(["Exercise", "Sets &times; reps"], [
    ("Wall slide", "2 &times; 15"),
    ("Scapular push-up", "2 &times; 10"),
])

DAY1 = table(["Exercise", "Sets &times; reps"], [
    ("Bulgarian split squat", "3 &times; 8&ndash;10 each leg"),
    ("Barbell hip thrust", "3 &times; 8&ndash;12"),
    ("Barbell Romanian deadlift (RDL)", "3 &times; 10&ndash;12"),
    ("Dumbbell bench press", "3 &times; 10"),
    ("One-arm dumbbell row", "3 &times; 10 each arm"),
    ("Bent-over wood chop", "3 &times; 10 each side"),
    ("Cable hip abduction", "3 &times; 20 each leg"),
])
DAY2 = table(["Exercise", "Sets &times; reps"], [
    ("Sumo squat or box squat", "3 &times; 10"),
    ("Barbell hip thrust with a 2-second pause", "3 &times; 10"),
    ("Hyperextension", "3 &times; 12&ndash;15"),
    ("Lat pulldown", "3 &times; 10&ndash;12"),
    ("Seated dumbbell shoulder press", "3 &times; 10"),
    ("Cable crunch", "3 &times; 12&ndash;15"),
    ("Band hip abduction", "3 &times; 20&ndash;25"),
])
DAY3 = table(["Exercise", "Sets &times; reps"], [
    ("Dumbbell reverse lunge or sumo leg press", "3 &times; 10 each leg / 3 &times; 12"),
    ("Supported single-leg dumbbell deadlift", "3 &times; 10 each leg"),
    ("Barbell hip thrust pulses", "3 &times; 20&ndash;30"),
    ("Dumbbell curl", "3 &times; 10&ndash;12"),
    ("Triceps rope pushdown", "3 &times; 12"),
    ("Bench leg raise", "3 &times; 10&ndash;12"),
    ("Machine hip abduction", "3 &times; 20&ndash;30"),
])

body = f"""<p class="legal-intro">A good 3-day beginner workout plan is full body, three times a week, on non-consecutive days like Monday, Wednesday and Friday. Every session trains your legs and glutes, your upper body and your core. Below is the exact plan Coach Dan Figueroa uses for women at Fig Performance in Placentia: 4 leg exercises, 2 upper body and 1 core each day, with a warm-up and cool-down. A separate plan for men is coming.</p>

<h2 id="how">How the plan works</h2>
<ul>
  <li><strong>Full body, three days a week.</strong> Chest, back, shoulders and legs all get trained, with a rest day between sessions to recover.</li>
  <li><strong>4 leg exercises every day:</strong> a squat or lunge, a hinge (RDL, hyperextension or single-leg deadlift), a hip thrust, and hip abduction. Hip thrusts are the theme all three days: regular, paused, then pulses.</li>
  <li><strong>2 upper body exercises:</strong> chest and back on Day 1, back and shoulders on Day 2, arms on Day 3.</li>
  <li><strong>1 core exercise,</strong> hitting a different angle each day: rotation, flexion and a leg raise.</li>
  <li><strong>Abduction always goes last,</strong> with a different tool each day: cable, band, then machine.</li>
  <li><strong>Rest 1:15 to 2 minutes</strong> between sets.</li>
</ul>

<h2 id="warmup">The warm-up (6 to 8 minutes)</h2>
<p>Do this before every workout. It loosens your hips and wakes up your glutes before you load them.</p>
{WARMUP}
<p>On Days 1 and 2, add these for your shoulders and upper back:</p>
{UPPER_WARMUP}
<p><strong>Ramp-up sets:</strong> before your first lift each day, do 1 set of 8 with about half your working weight, then 1 set of 5 with about 70%. Then start your working sets.</p>

<h2 id="plan">The 3-day plan for women</h2>
<p>Rest {REST} between sets. Each session takes about 50 to 60 minutes with the warm-up.</p>
<h3>Day 1 (Monday): legs, chest and back</h3>
{DAY1}
<h3>Day 2 (Wednesday): legs, back and shoulders</h3>
{DAY2}
<h3>Day 3 (Friday): legs and arms</h3>
{DAY3}

<h2 id="cooldown">The cool-down stretch (5 minutes)</h2>
<p>Hold each stretch for 30 seconds and breathe slowly: hip flexor stretch, hamstring stretch, figure-four glute stretch, and a chest stretch in a doorway.</p>

<h2 id="effort">How hard to push</h2>
<ul>
  <li><strong>Weeks 1 and 2:</strong> pick weights you could lift for 2 or 3 more reps than you do. Learn the movements first.</li>
  <li><strong>After that:</strong> push the last set of each exercise to about 1 rep short of failure, with good form.</li>
  <li><strong>On abduction and hip thrust pulses,</strong> go for the burn. High reps are the point.</li>
</ul>

<h2 id="progress">How to progress</h2>
<ol>
  <li><strong>Write everything down.</strong> Every exercise, weight and rep. If the numbers are going up, you're getting stronger, and strength is what builds muscle.</li>
  <li><strong>Add weight when you hit the top of the range.</strong> When you hit the top of the rep range on every set, go up a little next time and start back at the bottom of the range.</li>
  <li><strong>Keep the same plan for 4 to 6 weeks</strong> so you can see your lifts climb, then change it up.</li>
</ol>

<h2 id="off-days">What to do on your off days</h2>
<p>Walk. Coach Dan's target for clients over 40 is more than 5,000 steps a day, and ideally 6,000 or more. Eat protein at every meal, and get good sleep.</p>

<h2 id="safety">Before you start</h2>
<p>If you have a medical condition, a recent injury, or you haven't exercised in a long time, check with your doctor first. Stop any exercise that causes sharp pain. If an exercise bothers an old injury, swap it for one that doesn't. A coach can show you what works for your body.</p>

<h2 id="coach">Want someone to set it up for you?</h2>
<p>At Fig Performance in Placentia, every plan starts with a free consult and an <a href="/inbody-scan-placentia">InBody scan</a>, and Dan builds the program around your body, including old injuries. Can't make it in person? <a href="/online-personal-trainer">Online coaching</a> puts your plan in the R.H.O.D.E.S. app, with a weekly call with Dan. See also <a href="/strength-training-for-women-over-40">strength training for women over 40</a>.</p>
{CTA}"""

faqs = [
    ("Is a 3-day workout plan good for beginners?",
     "Yes. Three full-body sessions a week on non-consecutive days trains every muscle often enough to get stronger, with a rest day between sessions to recover."),
    ("What should a 3-day workout plan for women include?",
     "At Fig Performance, each day has 4 leg and glute exercises (a squat or lunge, a hinge, a hip thrust and hip abduction), 2 upper body exercises and 1 core exercise, plus a warm-up and cool-down stretch."),
    ("How many sets and reps should a beginner do?",
     "3 sets per exercise: 8 to 12 reps on squats, hip thrusts, RDLs and upper body, 12 to 15 on hyperextensions and core, and 20 to 30 on hip abduction and hip thrust pulses."),
    ("How long should I rest between sets?",
     "1 minute 15 seconds to 2 minutes."),
    ("What should I do on rest days?",
     "Walk. Aim for more than 5,000 steps a day, ideally 6,000 or more, and keep eating protein at every meal."),
]

html = page(
    SLUG,
    "3-Day Beginner Workout Plan for Women (Full Body) | Fig Performance",
    "A 3-day beginner workout plan for women: full body 3x a week with 4 leg, 2 upper body and 1 core exercise per day, warm-up, sets, reps and rest.",
    "3-Day Beginner Workout Plan for Women (Full Body)",
    "Fitness after 40", "3-Day Beginner Workout Plan for Women",
    "Full body, three days a week: the exact exercises, sets, reps and warm-up Coach Dan uses.",
    [("how", "How it works"), ("warmup", "Warm-up"), ("plan", "The plan"), ("cooldown", "Cool-down"),
     ("effort", "How hard to push"), ("progress", "How to progress"), ("off-days", "Off days"), ("safety", "Before you start")],
    body, faqs, "3-Day Beginner Workout Plan", kind="article", published=DATE)

if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
