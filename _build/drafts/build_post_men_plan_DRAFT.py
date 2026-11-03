"""DRAFT until Dan approves: beginner workout plan for men (3-day full body). Exercise picks, day structure,
2 leg exercises + 1 calf per day, 2 core sets, arm day in the middle and rest times are Dan's (Nov 3 2026)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_pages import page, SITE, CTA

DATE = "2026-11-03"
SLUG = "beginner-workout-plan-for-men"
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


X = "&times;"
WARMUP = table(["Exercise", "Sets &times; reps"], [
    ("Cat-cow", f"2 {X} 10"),
    ("Bird dog", f"2 {X} 6 each side"),
    ("Front-to-back leg swing", f"2 {X} 10 each leg"),
    ("Side-to-side leg swing", f"2 {X} 10 each leg"),
    ("Glute bridge", f"2 {X} 15"),
    ("Wall slide", f"2 {X} 15"),
    ("Scapular push-up", f"2 {X} 10"),
])
COLS = ["Exercise", "Sets &times; reps"]
DAY1 = table(COLS, [
    ("Leg press", f"3 {X} 8&ndash;10"),
    ("Lying leg curl", f"3 {X} 10&ndash;12"),
    ("Seated calf raise", f"3 {X} 12&ndash;15"),
    ("Incline dumbbell press", f"3 {X} 8&ndash;10"),
    ("Underhand lat pulldown", f"3 {X} 8&ndash;10"),
    ("Cable row", f"3 {X} 10"),
    ("Lateral raise", f"3 {X} 12&ndash;15"),
    ("Cable wood chop", f"2 {X} 10 each side"),
])
DAY2 = table(COLS, [
    ("Box squat", f"3 {X} 6&ndash;8"),
    ("Barbell Romanian deadlift (RDL)", f"3 {X} 8&ndash;10"),
    ("Wall tib raise", f"3 {X} 15&ndash;20"),
    ("Seated dumbbell shoulder press", f"3 {X} 8&ndash;10"),
    ("Cross-body hammer curl", f"3 {X} 10&ndash;12 each arm"),
    ("One-arm preacher curl", f"3 {X} 10&ndash;12 each arm"),
    ("Zottman curl", f"3 {X} 10&ndash;12"),
    ("Cable overhead triceps extension", f"3 {X} 10&ndash;12"),
    ("Straight-bar pushdown", f"3 {X} 10&ndash;12"),
    ("Single-arm dumbbell skull crusher", f"3 {X} 10&ndash;12 each arm"),
    ("Weighted sit-up or cable crunch", f"2 {X} 12&ndash;15"),
])
DAY3 = table(COLS, [
    ("Dumbbell reverse lunge", f"3 {X} 8&ndash;10 each leg"),
    ("Glute bridge", f"3 {X} 10&ndash;12"),
    ("Standing calf raise", f"3 {X} 12&ndash;15"),
    ("One-arm incline dumbbell press", f"3 {X} 8&ndash;10 each arm"),
    ("Flat bench press or flat dumbbell press", f"3 {X} 6&ndash;8"),
    ("One-arm dumbbell row", f"3 {X} 10 each arm"),
    ("Lateral raise", f"3 {X} 12&ndash;15"),
    ("Hanging knee raise or bench leg raise", f"2 {X} 10&ndash;12"),
])

G = [
    ("Leg press", "Quads and glutes.", "Lets you load your legs heavy with your back supported, a safe way for beginners to build leg strength for stairs, hiking and getting up from the floor. Builds bigger, stronger legs.", "Goblet squat with a dumbbell. At home: goblet squat or bodyweight squat to a chair."),
    ("Box squat", "Quads, glutes and the muscles that keep your trunk upright.", "Sitting back to a box teaches good squat depth and control, and trains the sit-to-stand you'll use for the rest of your life. A foundation for strong, full legs.", "Sit to a higher box, or hold a dumbbell at your chest (goblet box squat). At home: squat to a chair."),
    ("Lying leg curl", "Hamstrings.", "Strong hamstrings help protect your knees and balance out the quads. Builds the back of your legs.", "Stability-ball or slider leg curl. At home: slider curls on a hardwood floor, or band leg curls."),
    ("Barbell Romanian deadlift (RDL)", "Hamstrings, glutes and the muscles along your spine.", "Teaches you to bend at the hips with a flat back, the safest way to lift things off the floor. Builds a strong back side and better posture.", "Dumbbell RDL, and only lower to mid-shin until it feels solid."),
    ("Dumbbell reverse lunge", "Quads and glutes, one leg at a time.", "Builds single-leg strength and balance, and evens out a stronger and weaker side. Stepping back is easier on the knees than walking lunges.", "Bodyweight reverse lunge holding a wall or rack."),
    ("Glute bridge", "Glutes and hamstrings.", "Strong glutes take stress off your lower back. Builds a stronger, fuller backside.", "Bodyweight bridge on the floor, then add a dumbbell on your hips."),
    ("Seated and standing calf raises", "Calves. Seated works the deeper calf muscle, and standing works the bigger one.", "Strong calves help with ankle stability, balance and walking or running without pain. Fuller lower legs.", "Bodyweight calf raises on a step, holding the wall."),
    ("Incline dumbbell press and one-arm incline press", "Upper chest, front of the shoulders and triceps.", "Pushing strength and upper body bone health. The incline builds the upper chest, which fills out the top of a T-shirt. The one-arm version also makes your core work to keep you steady.", "Incline push-up with your hands on a bench. At home: dumbbells on an adjustable bench, or the floor."),
    ("Flat bench press or flat dumbbell press", "Chest, shoulders and triceps.", "The classic test of upper body strength, and pushing power for everyday life. Builds a bigger chest.", "Dumbbell floor press, or push-ups."),
    ("Underhand lat pulldown", "Lats, upper back and biceps.", "Pulling strength and healthy shoulders, and it counteracts hours of sitting hunched at a desk. The wide back that gives you a V-taper.", "Band pulldown anchored to the top of a door."),
    ("Cable row and one-arm dumbbell row", "Mid and upper back, lats and biceps.", "Better posture and stronger shoulders, and the one-arm version evens out your sides. A thicker, more defined back.", "Chest-supported dumbbell row, or a band row anchored to a door."),
    ("Lateral raise", "Side shoulders.", "Keeps the shoulders strong and balanced. Wider shoulders make your waist look smaller.", "Lighter dumbbells, one arm at a time while holding something for support, or a band."),
    ("Seated dumbbell shoulder press", "Shoulders and triceps.", "Overhead strength for lifting things onto shelves and into the overhead bin. Rounder, fuller shoulders.", "Palms-facing-in grip, which is easier on the shoulders, with lighter dumbbells. If pressing overhead hurts, skip it for now and tell your coach."),
    ("Cross-body hammer curl, one-arm preacher curl and Zottman curl", "Biceps, forearms and grip. Hammer curls hit the forearm and the outer biceps, preacher curls keep the biceps honest with no swinging, and the Zottman works the biceps on the way up and the forearms on the way down.", "Researchers link grip strength to healthy aging, and strong arms make carrying and lifting easier. Bigger arms.", "Lighter dumbbells or band curls."),
    ("Cable overhead extension, straight-bar pushdown and single-arm skull crusher", "Triceps, from three angles: stretched overhead, straight down, and lying down.", "The triceps power every push: up off the floor, out of a chair, pressing overhead. They make up most of the size of your upper arm.", "Band pushdown anchored to a door, or a one-dumbbell overhead extension."),
    ("Core: cable wood chop, weighted sit-up or cable crunch, hanging knee raise or bench leg raise", "The whole core: rotation, crunching and lifting the legs.", "A strong core protects your lower back when you lift, twist and carry. With fat loss, it gives you a firmer midsection.", "Band chop, floor crunch, or bent-knee leg raises lying on the floor."),
]
GUIDE = "\n".join(f"""<h3>{n}</h3>
<p><strong>Works:</strong> {w}</p>
<p><strong>Why it matters:</strong> {y}</p>
<p><strong>Easier or at-home version:</strong> {r}</p>""" for n, w, y, r in G)

body = f"""<p class="legal-intro">A good beginner workout plan for men is full body, three days a week, on non-consecutive days like Monday, Wednesday and Friday. Every session starts with legs, then trains your upper body and finishes with core. Below is the exact 3-day plan Coach Dan Figueroa uses with men at Fig Performance in Placentia: 2 leg exercises and 1 calf exercise every day, chest, back and shoulders on Days 1 and 3, and an arm day in the middle.</p>

<h2 id="how">How the plan works</h2>
<ul>
  <li><strong>Legs first, every day:</strong> 2 leg exercises and 1 calf exercise. No more. That's enough to get stronger without leaving your legs too sore to train again two days later.</li>
  <li><strong>Days 1 and 3: chest, back and shoulders.</strong> Incline pressing on both days, a flat press once, and lateral raises both days.</li>
  <li><strong>Day 2: arm day,</strong> with shoulders, biceps and triceps, in between the two chest, back and shoulder days.</li>
  <li><strong>Core: 1 exercise, 2 sets,</strong> hitting a different angle each day.</li>
  <li><strong>Rest 1:15 to 2 minutes</strong> between sets.</li>
</ul>

<h2 id="warmup">The warm-up (6 to 8 minutes)</h2>
<p>Do this before every workout. It loosens your hips, back and shoulders before you load them.</p>
{WARMUP}
<p><strong>Ramp-up sets:</strong> before your first lift each day, do 1 set of 8 with about half your working weight, then 1 set of 5 with about 70%. Then start your working sets.</p>

<h2 id="plan">The 3-day plan for men</h2>
<p>Rest {REST} between sets.</p>
<h3>Day 1 (Monday): legs, chest, back and shoulders</h3>
{DAY1}
<h3>Day 2 (Wednesday): legs and arms</h3>
{DAY2}
<h3>Day 3 (Friday): legs, chest, back and shoulders</h3>
{DAY3}
<p><strong>Core swaps:</strong> rotate in a Russian twist, bent-over wood chop, dumbbell side bend or alternating elbow plank.</p>

<h2 id="tib">Why wall tib raises are in the plan</h2>
<p>The tibialis anterior is the muscle on the front of your shin. It lifts your toes every time you take a step. Almost nobody trains it, and when it's weak your toes can drag and catch, which is how a lot of trips and falls start as you get older. A strong tib also helps protect your knees and ankles and can ease shin pain. To do one, stand with your back against a wall and your feet about a foot in front of you, then lift your toes as high as you can and lower them slowly.</p>

<h2 id="exercises">What each exercise does, and easier or at-home options</h2>
<p>Every exercise in this plan has a job: keeping you strong and independent as you age, and building how you look. If an exercise doesn't work for your body or your equipment, use the easier or at-home version.</p>
{GUIDE}

<h2 id="home">Training at home</h2>
<p>You can do the whole plan with a pair of adjustable dumbbells, an adjustable bench and a long resistance band. Use the at-home versions above, keep the same sets and reps, and add weight when you hit the top of the range.</p>

<h2 id="cooldown">The cool-down stretch (5 minutes)</h2>
<p>Hold each stretch for 30 seconds and breathe slowly: hip flexor stretch, hamstring stretch, figure-four glute stretch, a chest stretch in a doorway and a lat stretch hanging from a bar or holding a rack.</p>

<h2 id="effort">How hard to push</h2>
<ul>
  <li><strong>Weeks 1 and 2:</strong> pick weights you could lift for 2 or 3 more reps than you do. Learn the movements first.</li>
  <li><strong>After that:</strong> push the last set of each exercise to about 1 rep short of failure, with good form. Box squats and bench press stay heavier, at 6 to 8 reps.</li>
</ul>

<h2 id="progress">How to progress</h2>
<ol>
  <li><strong>Write everything down.</strong> If the numbers are going up, you're getting stronger, and strength is what builds muscle.</li>
  <li><strong>Add weight when you hit the top of the range</strong> on every set, then start back at the bottom of the range.</li>
  <li><strong>Keep the same plan for 4 to 6 weeks,</strong> then change it up.</li>
</ol>

<h2 id="off-days">What to do on your off days</h2>
<p>Walk. Coach Dan's target for clients over 40 is more than 5,000 steps a day, and ideally 6,000 or more. Eat protein at every meal, and get good sleep.</p>

<h2 id="safety">Before you start</h2>
<p>If you have a medical condition, a recent injury, or you haven't exercised in a long time, check with your doctor first. Stop any exercise that causes sharp pain, and swap it for the easier version.</p>

<h2 id="coach">Want someone to set it up for you?</h2>
<p>At Fig Performance in Placentia, every plan starts with a free consult and an <a href="/inbody-scan-placentia">InBody scan</a>, and Dan builds the program around your body, including old injuries. Can't make it in person? <a href="/online-personal-trainer">Online coaching</a> puts your plan in the R.H.O.D.E.S. app, with a weekly call with Dan. Looking for the women's version? See the <a href="/beginner-workout-plan-for-women">beginner workout plan for women</a>.</p>
{CTA}"""

faqs = [
    ("What's a good beginner workout plan for men?",
     "Full body three days a week on non-consecutive days. At Fig Performance, each day starts with 2 leg exercises and 1 calf exercise, then upper body, then 1 core exercise. Days 1 and 3 train chest, back and shoulders, and Day 2 is an arm day."),
    ("Is a 3-day workout split good for beginners?",
     "Yes. Three full-body days a week trains every muscle often enough to get stronger, with a rest day between sessions to recover, and it's easy to fit around a work schedule."),
    ("How many sets and reps should a beginner do?",
     "3 sets per exercise and 2 sets for core. 6 to 8 reps on box squats and bench press, 8 to 12 on most other lifts, and 12 to 15 on calves, lateral raises and core."),
    ("How long should I rest between sets?",
     "1 minute 15 seconds to 2 minutes."),
    ("What is a wall tib raise for?",
     "It strengthens the muscle on the front of your shin that lifts your toes when you walk. A strong tib helps you avoid tripping, and supports your knees and ankles."),
    ("Can I do this plan at home?",
     "Yes. With adjustable dumbbells, an adjustable bench and a resistance band, every exercise has an at-home version."),
]

html = page(
    SLUG,
    "Beginner Workout Plan for Men: 3-Day Split | Fig Performance",
    "A beginner workout plan for men: a 3-day full-body split with legs first, an arm day in the middle, exact sets and reps, warm-up and home options.",
    "Beginner Workout Plan for Men (3-Day Full Body Split)",
    "Fitness after 40", "Beginner Workout Plan for Men",
    "A 3-day full-body split: the exact exercises, sets, reps and warm-up Coach Dan uses.",
    [("how", "How it works"), ("warmup", "Warm-up"), ("plan", "The plan"), ("tib", "Wall tib raises"),
     ("exercises", "What each exercise does"), ("home", "Training at home"), ("cooldown", "Cool-down"),
     ("effort", "How hard to push"), ("progress", "How to progress"), ("safety", "Before you start")],
    body, faqs, "Beginner Workout Plan for Men", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
