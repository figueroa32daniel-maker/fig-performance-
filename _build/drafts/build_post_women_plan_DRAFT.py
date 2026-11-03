"""Article: 3-day beginner workout plan (women's plan from Coach Dan, Nov 3 2026; men's plan to follow).
DRAFT until Dan approves. Exercise choices, order and rest are Dan's. Rep ranges and warm-up style follow
common glute-focused programming (reviewed against Bret Contreras's published plans, nothing copied)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_pages import page, SITE, CTA

DATE = "2026-11-03"
SLUG = "beginner-workout-plan-for-women"
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
    ("Bent-over dumbbell wood chop", "2 &times; 10 each side"),
    ("Cable hip abduction", "3 &times; 20 each leg"),
])
DAY2 = table(["Exercise", "Sets &times; reps"], [
    ("Dumbbell sumo squat or barbell box squat", "3 &times; 10"),
    ("Barbell hip thrust with a 2-second pause", "3 &times; 10"),
    ("45-degree hyperextension (bodyweight or holding a plate)", "3 &times; 12&ndash;15"),
    ("Wide-grip cable lat pulldown", "3 &times; 10&ndash;12"),
    ("Seated dumbbell shoulder press", "3 &times; 10"),
    ("Kneeling cable crunch", "2 &times; 12&ndash;15"),
    ("Band hip abduction", "3 &times; 20&ndash;25"),
])
DAY3 = table(["Exercise", "Sets &times; reps"], [
    ("Dumbbell reverse lunge or sumo-stance leg press (machine)", "3 &times; 10 each leg / 3 &times; 12"),
    ("Supported single-leg dumbbell deadlift", "3 &times; 10 each leg"),
    ("Barbell hip thrust pulses", "3 &times; 20&ndash;30"),
    ("Dumbbell curl", "3 &times; 10&ndash;12"),
    ("Cable triceps rope pushdown", "3 &times; 12"),
    ("Bench leg raise", "2 &times; 10&ndash;12"),
    ("Machine hip abduction", "3 &times; 20&ndash;30"),
])

body = f"""<p class="legal-intro">A good 3-day beginner workout plan is full body, three times a week, on non-consecutive days like Monday, Wednesday and Friday. Every session trains your legs and glutes, your upper body and your core. Below is the exact plan Coach Dan Figueroa uses for women at Fig Performance in Placentia: 4 leg exercises, 2 upper body and 1 core each day, with a warm-up and cool-down. Looking for the men&rsquo;s version? See the <a href="/beginner-workout-plan-for-men">beginner workout plan for men</a>.</p>

<h2 id="how">How the plan works</h2>
<ul>
  <li><strong>Full body, three days a week.</strong> Chest, back, shoulders and legs all get trained, with a rest day between sessions to recover.</li>
  <li><strong>4 leg exercises every day:</strong> a squat or lunge, a hinge (RDL, hyperextension or single-leg deadlift), a hip thrust, and hip abduction. Hip thrusts are the theme all three days: regular, paused, then pulses.</li>
  <li><strong>2 upper body exercises:</strong> chest and back on Day 1, back and shoulders on Day 2, arms on Day 3.</li>
  <li><strong>1 core exercise, 2 sets,</strong> hitting a different angle each day: rotation, flexion and a leg raise.</li>
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

<h2 id="exercises">What each exercise does, and easier or at-home options</h2>
<p>Every exercise in this plan has a job: keeping you strong and independent as you age, and shaping how you look. If an exercise doesn't work for your body or your equipment, use the easier or at-home version. Same muscles, same goal.</p>
<h3>Bulgarian split squat</h3>
<p><strong>Works:</strong> Quads and glutes, one leg at a time.</p>
<p><strong>Why it matters:</strong> Builds the single-leg strength and balance you use on stairs and curbs, and evens out a stronger and weaker side. Shapes the legs and glutes.</p>
<p><strong>Easier or at-home version:</strong> Split squat with your back foot on the floor, holding a wall or rack for balance. At home: bodyweight or dumbbells, back foot on a couch or step.</p>
<h3>Hip thrusts (regular, paused and pulses)</h3>
<p><strong>Works:</strong> Glutes, the biggest muscle group in your body.</p>
<p><strong>Why it matters:</strong> Strong glutes support your lower back and power you up from a chair, up stairs and up from the floor. The pause builds control at the top, and pulses build endurance. This is the main exercise for a rounder, lifted look.</p>
<p><strong>Easier or at-home version:</strong> Glute bridge on the floor, then add a dumbbell on your hips. At home: shoulders on a couch, with a dumbbell or a band across your hips.</p>
<h3>Barbell Romanian deadlift (RDL)</h3>
<p><strong>Works:</strong> Hamstrings, glutes and the muscles along your spine.</p>
<p><strong>Why it matters:</strong> Teaches you to bend at the hips with a flat back, the safest way to pick things up off the floor. Builds the back of your legs and lifts the glutes.</p>
<p><strong>Easier or at-home version:</strong> Dumbbell or kettlebell RDL, and only lower to mid-shin until it feels solid.</p>
<h3>Dumbbell bench press</h3>
<p><strong>Works:</strong> Chest, front of the shoulders and triceps.</p>
<p><strong>Why it matters:</strong> Pushing strength: getting yourself up off the floor, pushing open a heavy door. Loading your upper body helps keep your bones strong. Firms up the chest and arms.</p>
<p><strong>Easier or at-home version:</strong> Incline push-up with your hands on a bench or counter. At home: dumbbell floor press, lying on the floor.</p>
<h3>One-arm dumbbell row</h3>
<p><strong>Works:</strong> Upper back, lats and biceps.</p>
<p><strong>Why it matters:</strong> Balances out desk posture and rounded shoulders, and helps you stand taller. Defines the back, which also makes the waist look smaller.</p>
<p><strong>Easier or at-home version:</strong> Chest-supported row, lying face-down on an incline bench. At home: band row anchored to a door.</p>
<h3>Bent-over dumbbell wood chop</h3>
<p><strong>Works:</strong> Obliques and deep core, through rotation.</p>
<p><strong>Why it matters:</strong> Trains your core to control twisting, the move behind golf swings, reaching into the back seat and turning to look behind you. Helps protect your lower back.</p>
<p><strong>Easier or at-home version:</strong> Standing band chop, or a lighter weight from a half-kneeling position.</p>
<h3>Hip abduction (cable, band and machine)</h3>
<p><strong>Works:</strong> The side glutes (glute medius).</p>
<p><strong>Why it matters:</strong> Keeps your hips stable and your knees lined up when you walk, climb stairs or stand on one leg, which matters for balance and fall prevention as you age. Shapes the upper and outer glutes.</p>
<p><strong>Easier or at-home version:</strong> Side-lying leg raise, with or without a band. At home: a mini band around your knees, seated or standing.</p>
<h3>Dumbbell sumo squat or barbell box squat</h3>
<p><strong>Works:</strong> Quads, glutes and inner thighs.</p>
<p><strong>Why it matters:</strong> The everyday sit-to-stand: chairs, cars and the toilet, without using your hands. Builds the legs and glutes.</p>
<p><strong>Easier or at-home version:</strong> Box squat to a higher box or chair, then lower it as you get stronger. At home: goblet squat with one dumbbell.</p>
<h3>45-degree hyperextension</h3>
<p><strong>Works:</strong> Lower back, glutes and hamstrings.</p>
<p><strong>Why it matters:</strong> Builds endurance in the muscles that hold you upright, for better posture and a lower back that tires less.</p>
<p><strong>Easier or at-home version:</strong> Bird dog or a floor back extension (lying face-down, lift your chest a few inches). At home: same, or over a stability ball.</p>
<h3>Wide-grip cable lat pulldown</h3>
<p><strong>Works:</strong> Lats and upper back.</p>
<p><strong>Why it matters:</strong> Pulling strength and healthy shoulders. Counteracts hours of sitting and looking down at a phone. Builds a defined back.</p>
<p><strong>Easier or at-home version:</strong> Band pulldown, or a lighter weight with a slower pace. At home: band pulldown anchored to the top of a door.</p>
<h3>Seated dumbbell shoulder press</h3>
<p><strong>Works:</strong> Shoulders and triceps.</p>
<p><strong>Why it matters:</strong> Overhead strength for putting a bag in the overhead bin or a box on a high shelf. Rounds out the shoulders.</p>
<p><strong>Easier or at-home version:</strong> Palms-facing-in grip, which is easier on the shoulders, with lighter dumbbells. If pressing overhead hurts, skip it for now and tell your coach.</p>
<h3>Kneeling cable crunch</h3>
<p><strong>Works:</strong> The front abs.</p>
<p><strong>Why it matters:</strong> Core strength to control your trunk and protect your back when you lift. Paired with fat loss, a stronger core gives you a firmer-looking midsection.</p>
<p><strong>Easier or at-home version:</strong> Floor crunch or dead bug. At home: band crunch anchored up high.</p>
<h3>Dumbbell reverse lunge or sumo-stance leg press (machine)</h3>
<p><strong>Works:</strong> Quads and glutes.</p>
<p><strong>Why it matters:</strong> Stepping back and catching yourself trains balance and control, and builds the legs.</p>
<p><strong>Easier or at-home version:</strong> Reverse lunge holding a wall or rack, bodyweight only. At home: bodyweight reverse lunge, then add dumbbells.</p>
<h3>Supported single-leg dumbbell deadlift</h3>
<p><strong>Works:</strong> Hamstrings and glutes, one side at a time, plus balance.</p>
<p><strong>Why it matters:</strong> Balance on one leg is one of the best things you can train to lower your fall risk as you age. Lifts and shapes the glutes.</p>
<p><strong>Easier or at-home version:</strong> Kickstand RDL, with the back toe touching the floor for support, holding a wall or bench. At home: same, with one dumbbell.</p>
<h3>Dumbbell curl</h3>
<p><strong>Works:</strong> Biceps and grip.</p>
<p><strong>Why it matters:</strong> Carrying groceries, kids and luggage, and grip strength, which researchers link to healthy aging. Tones the front of the arms.</p>
<p><strong>Easier or at-home version:</strong> Lighter dumbbells or a band curl.</p>
<h3>Cable triceps rope pushdown</h3>
<p><strong>Works:</strong> Triceps, the back of the arms.</p>
<p><strong>Why it matters:</strong> Helps you push up out of a chair or off the floor. Firms the back of the arms.</p>
<p><strong>Easier or at-home version:</strong> Band pushdown anchored to a door, or a one-dumbbell overhead triceps extension.</p>
<h3>Bench leg raise</h3>
<p><strong>Works:</strong> Lower abs and hip flexors.</p>
<p><strong>Why it matters:</strong> Core control and stability for everything you lift.</p>
<p><strong>Easier or at-home version:</strong> Bent-knee leg raise or dead bug, keeping your lower back pressed down.</p>

<h2 id="home">Training at home</h2>
<p>You can do the whole plan with a pair of adjustable dumbbells, a bench (or a sturdy couch), a long resistance band and a mini band. Use the at-home versions above, keep the same sets and reps, and add weight or a heavier band when you hit the top of the range.</p>

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
     "3 sets per exercise and 2 sets for core: 8 to 12 reps on squats, hip thrusts, RDLs and upper body, 12 to 15 on hyperextensions and core, and 20 to 30 on hip abduction and hip thrust pulses."),
    ("Can I do this workout plan at home?",
     "Yes. With adjustable dumbbells, a bench or couch, a long resistance band and a mini band, every exercise has an at-home version: glute bridges and couch hip thrusts, dumbbell RDLs, floor presses, band rows and pulldowns, and band abduction."),
    ("How long should I rest between sets?",
     "1 minute 15 seconds to 2 minutes."),
    ("What should I do on rest days?",
     "Walk. Aim for more than 5,000 steps a day, ideally 6,000 or more, and keep eating protein at every meal."),
]

html = page(
    SLUG,
    "Beginner Workout Plan for Women: 3-Day Full Body | Fig Performance",
    "A beginner workout plan for women: full body 3 days a week, 4 leg, 2 upper body and 1 core exercise per day, with warm-up, sets, reps and home options.",
    "Beginner Workout Plan for Women (3-Day Full Body Plan)",
    "Fitness after 40", "Beginner Workout Plan for Women",
    "Full body, three days a week: the exact exercises, sets, reps and warm-up Coach Dan uses.",
    [("how", "How it works"), ("warmup", "Warm-up"), ("plan", "The plan"), ("exercises", "What each exercise does"), ("home", "Training at home"), ("cooldown", "Cool-down"),
     ("effort", "How hard to push"), ("progress", "How to progress"), ("off-days", "Off days"), ("safety", "Before you start")],
    body, faqs, "Beginner Workout Plan for Women", kind="article", published=DATE)

if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
