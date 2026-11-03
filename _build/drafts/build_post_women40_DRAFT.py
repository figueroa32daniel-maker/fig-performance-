"""DRAFT until Dan approves: 'Strength training for women over 40' rewritten from Coach Dan's voice memo (Nov 3 2026).
On approval: remove the strength-training-for-women-over-40 entry from build_articles.py and promote this file to _build/."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_pages import page, SITE, CTA

SLUG = "strength-training-for-women-over-40"
DATE = "2026-10-30"

body = f"""<p class="legal-intro">Strength training after 40 isn't just about looking toned. It's about keeping everything you can do: getting up off the floor, getting off the toilet without your hands, climbing a flight of stairs without getting winded, getting out of the car, and picking yourself up if you fall. Here's why it matters, how often to lift, how heavy to go, and how to train around a bad knee, back or shoulder.</p>

<h2 id="why">Why strength training matters after 40</h2>
<p>The goal is to keep every capability you have: to jump, run, hike, walk up stairs, pick things up and get yourself off the ground. When you start losing those, you slowly become the person everyone has to work around. "We can't take her on the hike." "Her knees hurt after a little walking." "She gets tired so fast." That isn't fair to you or the people you love, and it takes away your ability to enjoy life with them.</p>
<p>Lifting also makes your bones stronger, and it gives you the defined, toned look most women want: more muscle and less fat.</p>

<h2 id="bulky">"Won't lifting make me bulky?"</h2>
<p>No. Your muscles will get a little bigger and more defined, but you won't look like a bodybuilder. Getting bulky takes years of eating on purpose to gain size, like 200 grams of protein and 2,500 to 3,000 calories a day, and usually performance-enhancing drugs. Most people will never get anywhere near that. What you'll actually see is a firmer shape, better posture and more strength.</p>

<h2 id="how-often">How often should you lift?</h2>
<p>Two to three full-body sessions a week, every other day: Monday, Wednesday and Friday, or Tuesday, Thursday and Saturday. That leaves you at least four days of rest a week, which is plenty.</p>
<p>Walk every day, at least 30 minutes, and work your way up to about 90 minutes a day.</p>
<p>You only need about 3 days of training. If you want to do 4, that's fine. But the best program isn't the hardest one. It's the one you can keep doing for years. Can you see yourself training 4 or 5 days a week for the next 10 years? If the answer is no, train 3. Do what you can actually do, and get really consistent at it. Consistency is the biggest driver of results. <strong>Chase progress, not perfection.</strong></p>

<h2 id="exercises">The movements to focus on</h2>
<p>You don't need fancy exercises. A good program covers five basic movements:</p>
<ul>
  <li><strong>Squat:</strong> goblet squats, box squats, leg press.</li>
  <li><strong>Hinge:</strong> Romanian deadlifts, hip thrusts, hyperextensions.</li>
  <li><strong>Push:</strong> incline push-ups, dumbbell presses.</li>
  <li><strong>Pull:</strong> rows, lat pulldowns, assisted pull-ups.</li>
  <li><strong>Single-leg:</strong> split squats, step-ups, reverse lunges.</li>
</ul>
<p>Want the exact exercises, sets and reps? Use the <a href="/beginner-workout-plan-for-women">beginner workout plan for women</a>.</p>

<h2 id="heavy">How heavy should you go?</h2>
<p>Heavier than you think, but not all at once. Your bones and muscles adapt over time when you slowly lift heavier and heavier weights. Go too heavy too soon and you'll get hurt. Progress gradually, and lifting is very safe. That's called progressive overload.</p>
<p>Teresa, 60, is a good example. She came to me with a shoulder injury and couldn't do a single bodyweight exercise. About three months later she did her first pull-up, and today she bench presses about 85 pounds for reps. She didn't start there. We built up to it slowly. <a href="/build-muscle-after-60">Read how she progressed, month by month</a>.</p>

<h2 id="aches">Training around your knees, back and shoulders</h2>
<p>First figure out what the symptom is, then find the root cause. Don't just avoid the area. You still use every one of these movements in daily life: you squat to sit on the toilet, and you stand on one leg every time you step out of the car or walk up stairs. The goal is to train them back to strong, starting with easier versions and progressing slowly.</p>
<ul>
  <li><strong>Shoulders:</strong> your shoulder flexes, extends and rotates, so figure out which motion hurts. One exercise I use with a lot of clients with shoulder pain is the two-arm dumbbell pullover. It's been a game changer.</li>
  <li><strong>Back:</strong> sometimes it's posture, and sometimes it's tight chest muscles or lats. I like the reverse-grip lat pulldown because it also trains the lower traps, which help hold your posture. Add an extension or hinge exercise to strengthen your lower back, and train the muscles around your spine, like your quadratus lumborum and your abs.</li>
  <li><strong>Knees:</strong> knees get very strong when you train them properly. Warm them up, start with step-ups, step-downs and leg extensions, then slowly add weight over time.</li>
</ul>
<p>If you're under a doctor's or physical therapist's care for an injury, check with them first.</p>

<h2 id="nutrition">Protein and recovery</h2>
<p>Eat at least your goal body weight in grams of protein every day. If your goal is 140 pounds, aim for at least 140 grams.</p>
<p>And make recovery a priority, because you're not a machine. Think of your body like a Mercedes or a BMW, whatever your favorite car is. The more you drive it, the more maintenance it needs: gas, oil changes, new parts. Your body is an expensive car with a lot of expensive parts. Eat well, sleep, stretch and keep your flexibility, so the whole thing keeps running and nothing breaks down.</p>

<h2 id="sample">A simple sample week</h2>
<ul>
  <li><strong>Monday:</strong> full-body strength.</li>
  <li><strong>Tuesday:</strong> walk 30 to 90 minutes.</li>
  <li><strong>Wednesday:</strong> full-body strength.</li>
  <li><strong>Thursday:</strong> walk, stretch or light mobility.</li>
  <li><strong>Friday:</strong> full-body strength.</li>
  <li><strong>Weekend:</strong> walk, stay active and rest.</li>
</ul>
<p>Prefer Tuesday, Thursday and Saturday? That works just as well. Check with your physician before starting a new exercise program, especially if you have a medical condition.</p>

<h2 id="coach">When a coach makes the difference</h2>
<p>Many women over 40 have tried classes, apps or a trainer who handed out random workouts. What works better is one plan built around you, coached rep by rep, and measured with real numbers. At Fig Performance in Placentia, every plan starts with a free consult and an <a href="/inbody-scan-placentia">InBody scan</a>. Can't make it in person? Try <a href="/online-personal-trainer">online coaching</a>.</p>
{CTA}"""

faqs = [
    ("Is strength training good for women over 40?",
     "Yes. It keeps you capable in everyday life: getting off the floor, climbing stairs, getting out of the car and picking yourself up if you fall. It also strengthens your bones and gives you a firmer, more defined shape."),
    ("Will lifting weights make women over 40 bulky?",
     "No. Your muscles get a little bigger and more defined, but getting bulky takes years of eating to gain size and usually performance-enhancing drugs. Most women see a firmer shape, better posture and more strength."),
    ("How many days a week should a woman over 40 lift weights?",
     "Two to three full-body sessions a week, every other day, with at least four rest days. Walk every day for at least 30 minutes, working up to about 90. The best plan is the one you can stay consistent with for years."),
    ("How much protein should a woman over 40 eat?",
     "Coach Dan recommends at least your goal body weight in grams of protein a day. If your goal is 140 pounds, aim for at least 140 grams."),
    ("Can I strength train with knee, back or shoulder pain?",
     "Usually, yes. Find the symptom and its cause, start with easier versions and progress slowly instead of avoiding the movement. If you're under a doctor's or physical therapist's care for an injury, check with them first."),
    ("Where can I find a personal trainer for women over 40 near Placentia?",
     "Fig Performance offers private one-on-one strength training for adults over 40 at 1284 E. Yorba Linda Blvd in Placentia, close to Yorba Linda, Fullerton, Brea, Anaheim Hills and Villa Park. Your first consult is free."),
]

html = page(
    SLUG,
    "Strength Training for Women Over 40 | Fig Performance",
    "Strength training for women over 40, from Coach Dan: why it keeps you capable, how often to lift, how heavy, and how to train around knees, back and shoulders.",
    "Strength Training for Women Over 40: Where to Start",
    "Fitness after 40", "Strength Training for Women Over 40: Where to Start",
    "Keep every capability you have. How often to lift, how heavy, and how to train around aches.",
    [("why", "Why it matters"), ("bulky", "Will it make me bulky?"), ("how-often", "How often"),
     ("exercises", "The movements"), ("heavy", "How heavy"), ("aches", "Knees, back and shoulders"),
     ("nutrition", "Protein and recovery"), ("sample", "Sample week"), ("coach", "When a coach helps")],
    body, faqs, "Strength Training for Women Over 40", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
