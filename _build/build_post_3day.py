"""Article: 3-day beginner workout plan for adults over 40 (built from Coach Dan's documented methods)."""
from build_pages import page, SITE, CTA

DATE = "2026-11-03"
SLUG = "3-day-beginner-workout-plan"


def day(title, rows):
    trs = "\n".join(f"    <tr><td>{e}</td><td>{s}</td><td>{r}</td></tr>" for e, s, r in rows)
    return f"""<h3>{title}</h3>
<div class="price-table-wrap"><table class="price-table compare-table">
  <thead><tr><th>Exercise</th><th>Sets</th><th>Reps</th></tr></thead>
  <tbody>
{trs}
  </tbody>
</table></div>"""


DAY1 = day("Day 1 (Monday): full body A", [
    ("Goblet squat", "3", "8&ndash;12"),
    ("One-arm dumbbell row", "3", "8&ndash;12 each arm"),
    ("Dumbbell bench press", "3", "8&ndash;12"),
    ("Dumbbell Romanian deadlift", "3", "8&ndash;12"),
    ("Plank", "2", "20&ndash;40 seconds"),
])
DAY2 = day("Day 2 (Wednesday): full body B", [
    ("Split squat", "3", "8&ndash;12 each leg"),
    ("One-arm lat pulldown", "3", "8&ndash;12 each arm"),
    ("Seated dumbbell shoulder press", "3", "8&ndash;12"),
    ("Glute bridge", "3", "10&ndash;15"),
    ("Dead bug", "2", "8 each side"),
])
DAY3 = day("Day 3 (Friday): full body C", [
    ("Dumbbell or trap bar deadlift", "3", "8&ndash;12"),
    ("Incline push-up (hands on a bench)", "3", "8&ndash;12"),
    ("One-arm dumbbell row", "3", "8&ndash;12 each arm"),
    ("Step-up", "3", "8&ndash;10 each leg"),
    ("Farmer carry", "3", "30&ndash;40 steps"),
])

body = f"""<p class="legal-intro">A good 3-day beginner workout plan is three full-body sessions a week, on non-consecutive days like Monday, Wednesday and Friday. Each one has a warm-up, five exercises for 3 sets of 8 to 12 reps, and a cool-down stretch. Start lighter than you think, add weight once you hit 12 reps on every set, and walk on your off days. Here's the exact plan, built the way Coach Dan Figueroa starts new clients over 40 at Fig Performance.</p>

<h2 id="how">How the plan works</h2>
<ul>
  <li><strong>3 days a week, full body each time.</strong> Every muscle gets trained three times a week, with a rest day in between to recover.</li>
  <li><strong>One-arm and one-leg exercises.</strong> Everybody has one side that's stronger or more stable. Training each side on its own evens that out and builds a stable base before you go heavy. It's how Dan started Teresa, who did her first pull-up at 60.</li>
  <li><strong>8 to 12 reps a set.</strong> Pick a weight you could lift for 2 or 3 more reps than you do. Lighter weights and more reps give your joints, tendons and technique time to catch up.</li>
  <li><strong>Warm-up, workout, cool-down.</strong> Every session, no skipping. It keeps you flexible and helps prevent pain and injury.</li>
</ul>

<h2 id="warmup">The warm-up (5 to 8 minutes)</h2>
<ol>
  <li>3 to 5 minutes of easy cardio: bike, rower or a brisk walk.</li>
  <li>10 bodyweight squats, 10 glute bridges and 10 arm circles each way.</li>
  <li>One light set of your first exercise.</li>
</ol>

<h2 id="plan">The 3-day beginner workout plan</h2>
<p>Rest 60 to 90 seconds between sets. Each session takes about 45 minutes.</p>
{DAY1}
{DAY2}
{DAY3}

<h2 id="cooldown">The cool-down stretch (5 minutes)</h2>
<p>Hold each stretch for 30 seconds and breathe slowly: hip flexor stretch, hamstring stretch, chest stretch in a doorway, child's pose, and a figure-four glute stretch.</p>

<h2 id="progress">How to progress</h2>
<ol>
  <li><strong>Write everything down.</strong> Every exercise, weight and rep. If the numbers are going up, you're building strength, and strength is what builds muscle.</li>
  <li><strong>Add weight when you hit 12.</strong> When you get 12 reps on every set of an exercise, go up a little the next session and start back at 8.</li>
  <li><strong>After about a month, drop the reps.</strong> Once your technique is solid, move to 6 to 8 reps with heavier weight. Later, 3 to 5. That's the same progression Dan used with Teresa: 8&ndash;12, then 6&ndash;8, then 3&ndash;5.</li>
  <li><strong>Swap in harder versions.</strong> Incline push-ups become floor push-ups. Split squats become rear-foot-elevated split squats.</li>
</ol>

<h2 id="off-days">What to do on your off days</h2>
<p>Walk. Coach Dan's target for clients over 40 is more than 5,000 steps a day, and ideally 6,000 or more. That everyday movement burns more calories than most people realize, and it helps you recover. Eat protein at every meal, and get good sleep.</p>

<h2 id="safety">Before you start</h2>
<p>If you have a medical condition, a recent injury, or you haven't exercised in a long time, check with your doctor first. Stop any exercise that causes sharp pain. If an exercise bothers an old injury, swap it for one that doesn't: a coach can show you what works for your body.</p>

<h2 id="coach">Want someone to set it up for you?</h2>
<p>At Fig Performance in Placentia, every plan starts with a free consult and an <a href="/inbody-scan-placentia">InBody scan</a>, and Dan builds the program around your body, including old injuries. Can't make it in person? <a href="/online-personal-trainer">Online coaching</a> puts a plan like this in the R.H.O.D.E.S. app, with a weekly call with Dan. See also <a href="/build-muscle-after-60">how to build muscle after 60</a> and <a href="/strength-training-for-women-over-40">strength training for women over 40</a>.</p>
{CTA}"""

faqs = [
    ("Is a 3-day workout plan good for beginners?",
     "Yes. Three full-body sessions a week on non-consecutive days trains every muscle often enough to get stronger, with a rest day between sessions to recover. It's one of the easiest schedules to stick to."),
    ("How many sets and reps should a beginner do?",
     "Start with 3 sets of 8 to 12 reps, using a weight you could lift for 2 or 3 more reps. When you hit 12 reps on every set, add a little weight and start back at 8."),
    ("How long should a beginner workout take?",
     "About 45 minutes: a 5 to 8 minute warm-up, five exercises, and a 5-minute cool-down stretch."),
    ("Is this plan OK for someone over 40?",
     "Yes. It starts light, uses one-arm and one-leg exercises to fix imbalances, and progresses gradually. Check with your doctor first if you have a medical condition or recent injury."),
    ("What should I do on rest days?",
     "Walk. Aim for more than 5,000 steps a day, ideally 6,000 or more, and keep eating protein at every meal."),
]

html = page(
    SLUG,
    "3-Day Beginner Workout Plan (Full Body, Over 40) | Fig Performance",
    "A 3-day beginner workout plan: three full-body days, 3 sets of 8-12 reps, warm-up and cool-down, and how to progress. Built by Coach Dan for adults over 40.",
    "3-Day Beginner Workout Plan for Adults Over 40",
    "Fitness after 40", "3-Day Beginner Workout Plan",
    "Three full-body days a week, the exact exercises, and how to progress. Built for adults over 40.",
    [("how", "How it works"), ("warmup", "Warm-up"), ("plan", "The plan"), ("cooldown", "Cool-down"),
     ("progress", "How to progress"), ("off-days", "Off days"), ("safety", "Before you start")],
    body, faqs, "3-Day Beginner Workout Plan", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
