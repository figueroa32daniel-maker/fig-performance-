"""Article: workout plan for men over 40 (from Coach Dan's voice answers, Nov 3 2026)."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote

DATE = "2026-11-03"
SLUG = "workout-plan-for-men-over-40"

body = f"""<p class="legal-intro">The best workout plan for men over 40 trains for function, not just looks. Start light, use ranges of motion you actually own, progress slowly, and fix the spots that usually hurt: neck, shoulders, lower back, hips and knees. Do that, and you stay strong enough for golf, the kids, the grandkids and the trip you've been planning, without getting hurt.</p>

<h2 id="mistake">The biggest mistake men over 40 make</h2>
<p>Most guys who walk in aren't training the right things. They train for aesthetics and forget about function. And they try to work in ranges of motion they don't own. That's how injuries happen.</p>
<p>If you've been away from exercise for a while, start with lighter weights and shorter ranges of motion, then go heavier and deeper over time. It just makes more sense.</p>

<h2 id="problem-spots">Fix the spots that usually hurt</h2>
<p>The most common pains I see in men over 40 are in the neck, traps, upper back, shoulders, hips, lower back and knees. Don't just work around them. Increase your capacity in every movement you're lacking.</p>
<ul>
  <li><strong>Shoulders and posture:</strong> if you sit at a desk all day, like most of the CEOs, CFOs and work-from-home clients I coach, your chest gets tight and your shoulders roll forward. Use face pulls, internal and external rotation work, and dumbbell pullovers to keep your shoulders and lats loose and support good posture.</li>
  <li><strong>Neck:</strong> keep it moving. As you get older, your body gets stiffer. Motion is lotion.</li>
  <li><strong>Knees:</strong> squatting isn't the enemy. You might not tolerate deep knee bending yet, but there are ways to train it pain-free. A sumo box squat uses more hip bend and less knee bend, so it often works well.</li>
  <li><strong>Hips:</strong> train them in every direction: abduction (out), adduction (in), flexion (forward) and extension (back). Healthy hips matter for golf, playing with the kids, standing at the barbecue, and that quick twist when you're running for a train in Italy.</li>
  <li><strong>Lower back:</strong> train your spine through extension, flexion and rotation, starting with safe rehab-style exercises and building up.</li>
</ul>

<h2 id="jonathan">Jonathan, 43: from back pain to a 185-pound bench</h2>
<p>Jonathan is 43, ex-Army and 6'4", and he has a brand new son he wanted to be strong for. When he came to me, he was in bad shape: low energy, poor endurance, inflamed, and dealing with lower back pain that kept coming back even after physical therapy cleared him. He also had shoulder pain that had kept him from bench pressing for 10 years. In the Army he could do a ton of pull-ups. Now he could barely do one.</p>
<p>We started with rehab-style work I knew wouldn't cause back or hip pain. As his capacity grew, we progressed: hyperextensions and Jefferson curls for spinal extension and flexion, and bent-over wood chops for rotation, which also helped his golf swing.</p>
<p>In the first three months, his inflammation came down, his belly flattened, his chest and arms got more defined, and he went from one pull-up to five in a row. Over time he kept building.</p>
{callout("Client result", "Jonathan, 43, ex-Army", ["Pull-ups: from 1 to 5 in a row", "Chin-ups with 35 pounds added", "Jefferson curls with 135 pounds", "Bench press 185 pounds, after 10 years of not benching"])}
<p>His glutes grew a lot too, thanks to all the posterior chain work. Most of all, he improved his capacity as a father and a husband.</p>

{pullquote("Motion is lotion. As you get older, your body gets stiffer. Keep it moving.")}

<h2 id="plan">What a workout plan for men over 40 looks like</h2>
<ul>
  <li><strong>3 full-body days a week,</strong> with a rest day between sessions.</li>
  <li><strong>Legs first:</strong> 2 leg exercises and 1 calf or tib exercise.</li>
  <li><strong>Upper body:</strong> chest, back and shoulders on two days, and an arm day in the middle.</li>
  <li><strong>Shoulder and posture work:</strong> face pulls, rotation work and pullovers.</li>
  <li><strong>Core:</strong> 2 sets of one core exercise a day, including rotation.</li>
  <li><strong>Start light,</strong> then add weight every week you can.</li>
  <li><strong>Walk every day.</strong></li>
</ul>
<p>Get the full plan with exact exercises, sets, reps and a warm-up: the <a href="/beginner-workout-plan-for-men">beginner workout plan for men</a>. Don't skip <a href="/tib-raises">tib raises</a>. Your knees will thank you.</p>

<h2 id="why">Why it matters</h2>
<p>The goal isn't just to look better. It's to keep every capability you have, so you can play with your kids or grandkids, golf, hike and travel without worrying about getting hurt.</p>

<h2 id="coach">Train with a coach</h2>
<p>At Fig Performance in Placentia, every plan starts with a free consult, an <a href="/inbody-scan-placentia">InBody scan</a> and an assessment of your joints, posture and how you move. If you're working with a doctor or physical therapist, I'll work alongside them. Can't make it in person? Try <a href="/online-personal-trainer">online coaching</a>.</p>
{CTA}"""

faqs = [
    ("What's the best workout plan for men over 40?",
     "Three full-body strength sessions a week that train for function, not just looks: legs first, chest, back and shoulders, an arm day, core, and shoulder and posture work. Start light, use ranges of motion you own, progress slowly, and walk daily."),
    ("How should a man over 40 start lifting again?",
     "Start with lighter weights and shorter ranges of motion, fix problem areas like shoulders, hips, lower back and knees, then add weight and range over time. Pushing range of motion you don't own is how injuries happen."),
    ("Can I lift weights with back pain after 40?",
     "Often, yes. Start with safe rehab-style exercises, then progress through spinal extension, flexion and rotation as your capacity grows. Coach Dan's client Jonathan, 43, went from recurring back pain to Jefferson curls with 135 pounds. Check with your doctor or physical therapist first."),
    ("Is squatting bad for your knees after 40?",
     "No. Squatting isn't the enemy. If deep knee bending hurts, start with a variation like a sumo box squat that uses more hip bend and less knee bend, then build up."),
    ("How many days a week should a man over 40 work out?",
     "Three full-body days a week is enough for most men, with daily walking. Pick a schedule you can keep for years."),
]

html = page(
    SLUG,
    "Workout Plan for Men Over 40 (Train for Function) | Fig Performance",
    "A workout plan for men over 40 from Coach Dan: train for function, start light, fix shoulders, hips, back and knees, and a client's 3-month story.",
    "Workout Plan for Men Over 40: Train for Function, Not Just Looks",
    "Fitness after 40", "Workout Plan for Men Over 40",
    "Train for function, not just looks. Start light, fix what hurts, and stay capable for life.",
    [("mistake", "The biggest mistake"), ("problem-spots", "Fix what hurts"), ("jonathan", "Jonathan's story"),
     ("plan", "What the plan looks like"), ("why", "Why it matters"), ("coach", "Train with a coach")],
    body, faqs, "Workout Plan for Men Over 40", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
