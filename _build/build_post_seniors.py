"""Article: strength training for seniors (from Coach Dan's voice memo, approved Nov 7 2026)."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-07"
SLUG = "strength-training-for-seniors"
CDC = "https://cdc.gov/physical-activity-basics/guidelines/older-adults.html"

body = f"""<p class="legal-intro">Here's my unpopular opinion: a lot of trainers treat older adults like they're made of glass. They won't let them squat, deadlift, press overhead or do pull-ups because they're afraid they'll get hurt. Honestly, I think some of those coaches either don't know how to coach those lifts or aren't screening their clients properly. Your body is very adaptable at any age. With the right starting point and steady progress, people over 65 can do a lot more than they think.</p>

<h2 id="results">You're not too old to lift heavy</h2>
<p>Here's what some of my clients over 60 are doing:</p>
<ul>
  <li><strong>Randy, 73,</strong> is a lawyer with arthritis in his shoulder. He bench presses 135 pounds for reps, pain free.</li>
  <li><strong>Sam, 70,</strong> is a former restaurant owner who ran his own business for decades. He dumbbell bench presses the 50s and does a seated dumbbell shoulder press with 40s.</li>
  <li><strong>Teresa, 60,</strong> does bodyweight pull-ups.</li>
  <li>A 60-year-old man did pull-ups with 45 pounds hanging from his belt, at his first consultation.</li>
</ul>
{callout("Client results", "Age didn't decide their program", ["Randy, 73: bench presses 135 pounds for reps with shoulder arthritis, pain free", "Sam, 70: dumbbell bench press with the 50s, seated press with the 40s", "Teresa, 60: bodyweight pull-ups"])}
<p>I'm not saying you'll start there. We don't start with anything crazy. But I don't treat a 65-year-old like they're 90. When I give clients something challenging, they often ask, "Are you sure I can do this?" I tell them: trust me, I've seen it work. Then they do it, and they're surprised they had it in them.</p>

<h2 id="senior">Who counts as a senior?</h2>
<p>At Fig Performance, I'd say anyone 65 and up. But honestly, I don't train seniors any differently. My philosophy is the same for everyone. What changes is the starting point and the goals. That's why every plan starts with an assessment: your joints, mobility, injuries and history. If you've had surgery or finished physical therapy, I like to work with your doctor or therapist's notes too.</p>
<p>The CDC recommends that adults 65 and older do muscle-strengthening activities at least 2 days a week, plus 150 minutes a week of moderate activity like brisk walking, and balance work (<a href="{CDC}" target="_blank" rel="noopener noreferrer">CDC</a>).</p>

<h2 id="movements">The 6 movements every older adult should train</h2>
<p>These are the skills that keep you independent:</p>
<ol>
  <li><strong>Push:</strong> a flat or incline dumbbell press. The strength to push yourself up off the floor.</li>
  <li><strong>Pull:</strong> a reverse-grip lat pulldown or chest-supported row. Pulling a door, a suitcase, yourself.</li>
  <li><strong>Squat:</strong> a box squat. Getting up from a chair or the toilet without your hands.</li>
  <li><strong>Hinge:</strong> a Romanian deadlift. Picking things up off the floor without hurting your back.</li>
  <li><strong>Carry:</strong> a farmer's carry with dumbbells. Carrying groceries.</li>
  <li><strong>Overhead:</strong> a dumbbell overhead press. Putting a box on a high shelf, or lifting your granddaughter up to put the star on the Christmas tree.</li>
</ol>
<p>I'd add core and rotation work too, so your spine can twist without throwing your back out. And I don't stray away from any of these unless there's a real mobility problem. If your knees hurt every time you squat, there's an easier version of the squat. We regress, we don't skip.</p>

<h2 id="start">How to start if you've never lifted</h2>
<p>Dumbbells are a safe place to start. At the gym we have dumbbells from 5 to 100 pounds, so there's a starting point for everyone. A first program might be:</p>
<ul>
  <li>Box squat</li>
  <li>Dumbbell Romanian deadlift</li>
  <li>Flat or incline dumbbell bench press</li>
  <li>Reverse-grip lat pulldown</li>
  <li>Farmer's carry</li>
</ul>
<p>The same goes for harder lifts. To work up to a pull-up, you might go: reverse-grip lat pulldown, then band-assisted chin-ups, then slow eccentric (lowering-only) chin-ups, then bodyweight pull-ups for a few reps.</p>

<h2 id="reps">Sets, reps and how to progress safely</h2>
<p>It depends on the person, but here's an example of how I often run it:</p>
{stats([("8&ndash;10", "reps per set in month 1"), ("5&ndash;6", "reps per set in month 2"), ("1&ndash;5", "reps per set in month 3")])}
<p>Starting with 8 to 10 reps gives you practice with the movement while you still build strength and muscle. Then the reps come down and the weight goes up.</p>
<p>Every week, we either add 2 reps to each exercise or add 2.5 to 5 pounds, sometimes even 10. If you can do a lat pulldown with 70 pounds for 10 reps, by the time we drop to 5 reps you should be using 110 to 120 pounds.</p>

<h2 id="safe">"Won't I get hurt?"</h2>
<p>Anything in weightlifting is safe as long as it's done progressively over time. People get hurt when they skip the screening, add too much weight too fast, or try things their body isn't ready for. With a proper assessment and a coach who knows the body, you can train with confidence, even with arthritis, after rehab or after surgery. Randy has arthritis in his shoulder, and he benches pain free.</p>
{pullquote("Your body is very adaptable at any age. Find the right starting point, then get a little stronger every week.", "Coach Dan Figueroa")}

<h2 id="coach">Train with a coach in Placentia</h2>
<p>At Fig Performance, every plan starts with a free consult, an <a href="/inbody-scan-placentia">InBody scan</a> and an assessment. Then we find your starting point and build from there. Read more: <a href="/build-muscle-after-60">build muscle after 60</a>, <a href="/strength-training-for-women-over-50">strength training for women over 50</a> and the <a href="/workout-plan-for-men-over-40">workout plan for men over 40</a>. Can't make it in person? Try <a href="/online-personal-trainer">online coaching</a>.</p>
<p><em>Check with your doctor before starting a new exercise program, especially if you have a heart condition, osteoporosis, or a recent injury or surgery.</em></p>
{CTA}"""

faqs = [
    ("Is strength training safe for seniors?",
     "Yes, when it starts with an assessment and progresses gradually. Coach Dan's client Randy, 73, has shoulder arthritis and bench presses 135 pounds pain free."),
    ("What exercises should seniors do?",
     "A push, a pull, a squat, a hinge, a carry and an overhead press, plus core work. These keep you strong for everyday life."),
    ("How often should seniors lift weights?",
     "At least 2 days a week, per the CDC. Many of Coach Dan's clients train 2 to 3 times a week."),
    ("How many reps should seniors do?",
     "Start with 8 to 10 reps to learn the movements, then lower the reps and raise the weight over the next few months, adding 2 reps or 2.5 to 5 pounds a week."),
    ("Can you build muscle after 65?",
     "Yes. Muscle is a byproduct of getting stronger, and the body adapts at any age when you progress steadily."),
]

html = page(
    SLUG,
    "Strength Training for Seniors: How to Start | Fig Performance",
    "Strength training for seniors from Coach Dan: the 6 movements to train, how to start, sets and reps, and why older adults can lift more than they think.",
    "Strength Training for Seniors: Stop Treating Older Adults Like They're Fragile",
    "Fitness after 40", "Strength Training for Seniors",
    "Your body is adaptable at any age. The 6 movements to train, how to start, and how to progress safely.",
    [("results", "Not too old to lift"), ("senior", "Who counts as a senior"), ("movements", "The 6 movements"),
     ("start", "How to start"), ("reps", "Sets and reps"), ("safe", "Won't I get hurt?"), ("coach", "Train with a coach")],
    body, faqs, "Strength Training for Seniors", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
