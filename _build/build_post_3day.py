"""/3-day-beginner-workout-plan becomes a short hub that sends readers to the
women's and men's plans and targets '3 day workout split' / '3 day workout plan'."""
import sys
from build_pages import page, SITE, CTA

DATE = "2026-11-03"
SLUG = "3-day-beginner-workout-plan"

body = f"""<p class="legal-intro">The best 3-day workout split for beginners is full body, three times a week, on non-consecutive days like Monday, Wednesday and Friday. You train every major muscle each session, rest a day in between, and get stronger fast without living in the gym. Coach Dan Figueroa builds it differently for women and men, so pick your plan below.</p>

<h2 id="plans">Pick your plan</h2>
<ul>
  <li><a href="/beginner-workout-plan-for-women"><strong>Beginner workout plan for women</strong></a>: 4 leg and glute exercises a day (a squat or lunge, a hinge, a hip thrust and hip abduction), 2 upper body exercises and 1 core exercise.</li>
  <li><a href="/beginner-workout-plan-for-men"><strong>Beginner workout plan for men</strong></a>: 2 leg exercises and 1 calf exercise a day, chest, back and shoulders on Days 1 and 3, and an arm day in the middle.</li>
</ul>

<h2 id="why">Why a 3-day full-body split works for beginners</h2>
<ul>
  <li><strong>You train each muscle three times a week,</strong> which is plenty to build strength and muscle when you're starting out.</li>
  <li><strong>You get a rest day between sessions</strong> to recover, so you show up fresh.</li>
  <li><strong>It fits a busy schedule.</strong> Three sessions a week is easy to keep, even with a demanding job.</li>
  <li><strong>Miss a day and you've still trained everything</strong> that week, which isn't true of a body-part split.</li>
</ul>

<h2 id="both">What both plans have in common</h2>
<ul>
  <li>A 6 to 8 minute warm-up and ramp-up sets before your first lift.</li>
  <li>3 sets on most exercises, 2 sets on core, and 1:15 to 2 minutes of rest between sets.</li>
  <li>A cool-down stretch at the end.</li>
  <li>Easier and at-home versions of every exercise.</li>
  <li>Walking on your off days: more than 5,000 steps, ideally 6,000 or more.</li>
</ul>

<h2 id="coach">Want a plan built for you?</h2>
<p>At Fig Performance in Placentia, every plan starts with a free consult and an <a href="/inbody-scan-placentia">InBody scan</a>. Can't make it in person? <a href="/online-personal-trainer">Online coaching</a> puts your plan in the R.H.O.D.E.S. app, with a weekly call with Dan.</p>
{CTA}"""

faqs = [
    ("What is the best 3-day workout split for beginners?",
     "Full body three days a week on non-consecutive days, like Monday, Wednesday and Friday. You train every major muscle each session with a rest day in between."),
    ("Is 3 days a week enough to build muscle?",
     "Yes, for beginners. Three full-body sessions train each muscle three times a week, which is enough to build strength and muscle when you push each session and add weight over time."),
    ("Should men and women train differently?",
     "The basics are the same, but Coach Dan builds the plans differently: more leg and glute work each day for women, and more upper body volume with an arm day for men."),
]

html = page(
    SLUG,
    "3-Day Workout Split for Beginners (Women & Men) | Fig Performance",
    "The best 3-day workout split for beginners: full body, 3 days a week. Pick the women's or men's plan from Coach Dan, with exact exercises, sets and reps.",
    "3-Day Workout Split for Beginners: Plans for Women and Men",
    "Fitness after 40", "3-Day Workout Split for Beginners",
    "Full body, three days a week. Pick the plan for women or for men.",
    [("plans", "Pick your plan"), ("why", "Why it works"), ("both", "What both plans share"), ("coach", "Get a plan built for you")],
    body, faqs, "3-Day Workout Split", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
