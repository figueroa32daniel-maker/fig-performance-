"""Article: dumbbell workout for beginners over 50 (from Coach Dan's voice memo, Nov 16 2026). Publish only after Dan approves."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-16"
SLUG = "dumbbell-workout-for-beginners-over-50"

STARTING_WEIGHTS = """<h2 id="weights">How heavy should you start?</h2>
<p>[DAN: starting weights pending]</p>"""

body = f"""<p class="legal-intro">If you're over 50 and starting to lift, or starting again after years away, you don't need a gym full of machines. You need a set of dumbbells and an adjustable bench. That's it. With those two things you can train every muscle in your body, two or three days a week, around a full life.</p>
<p>Here's the plan I'd give you: how many days, what to do on them, how hard to push, how to know when to go up in weight, and what to swap in if your shoulder, knee or back has opinions.</p>

<h2 id="days">How many days a week?</h2>
<p>Everybody needs a minimum of two workouts a week. You can go up to five, but you don't need to. Two or three is what actually works, and it's built for a real life: friends, family, the things you like to do outside of work, a high-pressure job or a business to run. For a successful, busy adult over 50, three days a week is plenty.</p>
<p>There are three good ways to set up the week:</p>
<ul>
  <li><strong>Full body, three times a week</strong>, every other day. Monday, Wednesday, Friday. My default for beginners.</li>
  <li><strong>Full body, twice a week.</strong> The minimum, and it still works.</li>
  <li><strong>Upper / lower.</strong> Upper body one day, lower body the next. You can run it every other day, or three days on and a day off.</li>
</ul>
{stats([("2", "workouts a week, minimum"), ("3", "is plenty"), ("2", "pieces of equipment")])}

<h2 id="equipment">The equipment: dumbbells and an adjustable bench</h2>
<p>You can get by with just dumbbells, but a bench is what lets you do multiple things: inclines, rows, step-ups, presses, core work. Make it an <strong>adjustable</strong> bench, so you can go flat, incline and upright.</p>

<h2 id="menu">The exercise menu</h2>
<p>Here's everything you can do with a bench and dumbbells, by muscle group. Pick one or two from each group per workout.</p>
<p><strong>Back:</strong> chest-supported row, one-arm row, dumbbell row. <strong>Traps:</strong> shrugs.</p>
<p><strong>Chest:</strong> incline dumbbell press, flat dumbbell press, floor press, one-arm press.</p>
<p><strong>Shoulders:</strong> Arnold press, seated dumbbell press, lateral raise, rear-delt fly.</p>
<p><strong>Glutes and hamstrings:</strong> dumbbell Romanian deadlift (RDL), single-leg RDL holding the bench, single-leg deadlift.</p>
<p><strong>Quads:</strong> goblet squat, reverse lunge, Bulgarian split squat.</p>
<p><strong>Calves and shins:</strong> standing calf raise, seated calf raise, wall <a href="/tib-raises">tib raise</a>.</p>
<p><strong>Core:</strong> bench leg raise, weighted crunch with your feet up on the bench, dumbbell side bend, Russian twist, alternating elbow plank.</p>
<p><strong>Forearms and grip:</strong> suitcase carry, farmer's carry, dumbbell wrist curls and wrist extensions.</p>
<p><strong>Biceps:</strong> hammer curl, incline dumbbell curl, one-arm preacher curl over the bench.</p>
<p><strong>Triceps:</strong> overhead dumbbell extension (two-arm or one-arm), skull crushers, dumbbell kickbacks.</p>
<p><strong>Neck:</strong> if you've got tech neck from years at a screen, gentle neck rotations, neck curls and neck extensions.</p>

<h2 id="sample">A sample full-body week</h2>
<p>Three days, every other day. Alternate workout A and workout B.</p>
<p><strong>Workout A</strong></p>
<ol>
  <li>Goblet squat</li>
  <li>Incline dumbbell press</li>
  <li>Chest-supported row</li>
  <li>Dumbbell RDL</li>
  <li>Lateral raise</li>
  <li>Bench leg raise</li>
  <li>Farmer's carry</li>
</ol>
<p><strong>Workout B</strong></p>
<ol>
  <li>Reverse lunge</li>
  <li>Seated dumbbell press</li>
  <li>One-arm row</li>
  <li>Single-leg RDL holding the bench</li>
  <li>Hammer curl and overhead dumbbell extension</li>
  <li>Dumbbell side bend</li>
  <li>Standing calf raise</li>
</ol>
<p>Two to three sets of each. Rest about a minute to a minute and a half between sets.</p>

<h2 id="hard">How hard should it feel? The 1 to 10 scale</h2>
<p>How many reps you do depends on how heavy your dumbbells are. What matters more is that you get <strong>close to failure</strong>: close to the point where you couldn't do one more good rep. Here's the easiest way to measure it.</p>
<p>Imagine you're carrying a heavy backpack up a hill. At the end of every set, ask yourself one question: <strong>"How many more could I have done?"</strong> That answer is your score, on a scale coaches call RPE, rate of perceived exertion.</p>
<ul>
  <li><strong>10:</strong> I couldn't do even one more. Totally out of gas.</li>
  <li><strong>9:</strong> I had one more in me. Maybe.</li>
  <li><strong>8:</strong> I had two more. It was hard, but I was still in control.</li>
  <li><strong>7:</strong> I had three more. Getting tough.</li>
  <li><strong>5 or 6:</strong> I could have kept going for a while. A warm-up.</li>
  <li><strong>1 to 4:</strong> Like walking to the mailbox.</li>
</ul>
<p><strong>Aim for 7 to 9 on your work sets.</strong> If you finish a set and honestly could have done five more, it was too light. If your form fell apart, it was too heavy. The sweet spot is the last two reps being hard, slow and still clean.</p>
{callout("The one question", "How many more could you have done?", ["3 more = 7", "2 more = 8", "1 more = 9", "Aim for 7 to 9 on every work set"])}

{STARTING_WEIGHTS}

<h2 id="progress">When to go up in weight</h2>
<p>My clients add <strong>two reps or five pounds to every exercise, every week.</strong> If you did 10 reps with 20 pounds last week, this week you do 12 with 20, or 10 with 25. That's how I get bodies to adapt faster.</p>
<p>But that's a target, not a law. You go up when you're ready to go up. Part of being ready is technique: you've got the movement down and you're confident in it. Part of it is mental. A lot of beginners psych themselves out when the weight gets heavier. So I deliberately rotate clients through light, medium and heavy weights to desensitize them, so a heavy dumbbell stops looking scary.</p>
{pullquote("Strength is a skill. Once the technique is there and the confidence is there, the weight goes up fast.", "Coach Dan Figueroa")}

<h2 id="sam">Sam's story: dumbbells first, then the barbell</h2>
<p>Sam is 70. He started with me on dumbbells. We ran different rep ranges on purpose: 15 reps for a month, then 5 reps the next month, then the middle, 6 to 10. Here's why that works. If he can do 15 reps with 35 pounds, imagine what he can do for 5. Then next time we have two data points: what he did at high reps, and what he did at low reps. When we land in the middle, he feels the jump in weight for himself.</p>
<p>That built his technique, and the technique built his confidence. Before long he was doing barbell work on his own. Today Sam deadlifts 135 pounds, dumbbell benches the 45s and curls 30-pound dumbbells. Muscle is a byproduct of strength, and strength is a byproduct of doing it consistently with good form.</p>
{stats([("70", "Sam's age"), ("135 lb", "deadlift"), ("45s", "dumbbell bench")])}

<h2 id="swaps">If something hurts: shoulder, knee, back</h2>
<p>Pain is case by case: where it hurts, how long you've had it, and how bad it is. If it's sharp, getting worse, or there's a history of surgery, see your doctor or a physical therapist first. For the usual aches I see, here's what I swap in.</p>
<p><strong>Bad shoulder.</strong> Neutral-grip work is almost always safe on the shoulders: neutral-grip press, single-arm neutral-grip press, neutral-grip row. Add two-arm dumbbell pullovers on the bench, lateral raises and face pulls, which are usually fine, and prone shoulder extensions. I'll also add trap and neck work, because a lot of shoulder pain gets better when the muscles around it get stronger.</p>
<p><strong>Bad knee.</strong> Step-ups are very safe on the knees, probably a better choice than any squat. Box squats are super safe too, and reverse lunges are gentler than forward lunges. At that point I put more focus on the hamstrings and glutes: single-leg RDL, dumbbell RDL, bench-supported RDL, glute bridge, hip thrust. Then exercises that help knee mobility and stability: terminal knee extensions with a band, lateral band walks, standing hip abduction. If you have access to machines, leg extensions, leg curls, abduction and adduction are all knee-friendly.</p>
<p><strong>Bad back.</strong> Depends where. For <strong>upper-back pain</strong>, strengthen your posture. I used to get upper-back pain myself; what fixed it was dumbbell pullovers, scapular elevation and depression (shrugging up and pulling your shoulders down), thoracic spine rotations, and cat-cows. For <strong>lower-back pain</strong>, [DAN: confirm the lower-back rule] until it settles, then build it back gradually.</p>

<h2 id="month">What the first months look like</h2>
<ul>
  <li><strong>Month 1:</strong> higher reps, around 12 to 15. Learn every movement, find your starting weights, live at 7 to 8 on the scale.</li>
  <li><strong>Month 2:</strong> lower reps, around 5, with heavier dumbbells. This is where you find out you're stronger than you think.</li>
  <li><strong>Month 3:</strong> the middle, 6 to 10. With data from both ends, the weight jumps are obvious.</li>
</ul>
<p>Every week, two more reps or five more pounds, when you're ready. Strength comes first. Muscle follows a couple of months behind it, and by month three the InBody shows it.</p>

<h2 id="coach">Want someone to set it up with you?</h2>
<p>This plan works on your own. It works faster with a coach checking your form for the first few weeks, because technique is what unlocks the weight. At a free consult at Fig Performance we'll do an InBody scan, watch how you move, and pick your starting weights together.</p>
<p>Fig Performance is a <a href="/">private one-on-one personal training gym in Placentia</a>, serving Yorba Linda, Brea, Fullerton and Anaheim Hills. Related: <a href="/building-muscle-after-50">building muscle after 50</a>, the <a href="/3-day-beginner-workout-plan">3-day beginner workout plan</a>, <a href="/strength-training-for-seniors">strength training for seniors</a> and <a href="/hotel-workout">the hotel workout</a>. Can't make it in person? Try <a href="/online-personal-trainer">online coaching</a>.</p>
<p><em>Check with your doctor before starting a new exercise program, especially if you have a heart condition, joint pain, or a recent injury or surgery.</em></p>
{CTA}"""

faqs = [
    ("What is a good dumbbell workout for a beginner over 50?",
     "Two to three full-body workouts a week with dumbbells and an adjustable bench: a squat or lunge, a press, a row, an RDL, a shoulder exercise, core and a carry. Two to three sets each, close to failure."),
    ("How many days a week should a beginner over 50 lift?",
     "At least two. Three is plenty for most busy adults. Full body every other day, full body twice a week, or an upper/lower split all work."),
    ("How do I know if I'm lifting heavy enough?",
     "At the end of each set, ask how many more reps you could have done. Two or three more is about right (7 to 8 on the 1 to 10 scale). Five or more means too light. Broken form means too heavy."),
    ("When should I increase the weight?",
     "Coach Dan's clients add two reps or five pounds to every exercise each week, when their technique and confidence are ready."),
    ("What dumbbell exercises are safe for bad shoulders?",
     "Neutral-grip presses and rows, lateral raises, dumbbell pullovers and face pulls are usually shoulder-friendly. Pain is case by case; see a doctor or physical therapist if it's sharp or worsening."),
    ("What exercises are safe for bad knees?",
     "Step-ups, box squats, reverse lunges, RDLs, glute bridges and hip thrusts, plus terminal knee extensions and lateral band walks for stability."),
]

html = page(
    SLUG,
    "Dumbbell Workout for Beginners Over 50 | Fig Performance",
    "Dumbbell workout for beginners over 50: 2 to 3 days a week with dumbbells and a bench, how hard to push, when to add weight, and swaps for bad joints.",
    "Dumbbell Workout for Beginners Over 50: The Whole Plan",
    "Fitness after 40", "Dumbbell Workout for Beginners Over 50",
    "Dumbbells, an adjustable bench, two or three days a week. What to do, how hard to push, and what to swap if something hurts.",
    [("days", "How many days"), ("equipment", "The equipment"), ("menu", "The exercise menu"), ("sample", "A sample week"),
     ("hard", "How hard? The 1-10 scale"), ("weights", "Starting weights"), ("progress", "When to go up"), ("sam", "Sam's story"),
     ("swaps", "Shoulder, knee, back swaps"), ("month", "The first months"), ("coach", "Get set up")],
    body, faqs, "Dumbbell Workout for Beginners Over 50", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
