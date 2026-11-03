"""Article: Can you build muscle after 60? (from Coach Dan's interview answers, Oct 30 2026)."""
from build_pages import page, SITE, CTA, callout, pullquote

DATE = "2026-10-30"
SLUG = "build-muscle-after-60"

body = f"""<p class="legal-intro">Yes, you can build muscle after 60. I see it every week. Teresa started with me at 60, unable to do a single bodyweight exercise, and did her first pull-up about three months later. Sam is 70 and deadlifts 135 pounds for reps. Neither of them started strong. They started slow, got coached, and kept showing up. Here's exactly how we did it.</p>

<h2 id="teresa">How a 60-year-old did her first pull-up in about 3 months</h2>
<p><strong>Teresa, 60, trains with Coach Dan at Fig Performance in Placentia.</strong></p>
<p>When Teresa came in, she hadn't lifted in a year or two. She had a shoulder injury, not much upper-body strength and not much overall strength. No pull-ups, nothing close.</p>
<p><strong>Month 1: build the base.</strong> We started with what I thought would work best for her body: one-arm (unilateral) exercises for her back and arms, plus leg work. Everybody has imbalances, one side stronger or more stable than the other. Training each side on its own starts to even that out, so you build a stable, symmetrical base before you load up. We worked around her shoulder, not through it, and used 8 to 12 reps per set.</p>
<p><strong>Months 2 and 3: fewer reps, more weight.</strong> As she got stronger, we brought the reps down and the weight up: from 8 to 12 reps, to 6 to 8, then 3 to 5, and eventually heavy sets of 1 to 3. When she got good at something, we made it harder. She worked up to a one-arm dumbbell bench press with 25 pounds. Then we added eccentric chin-ups: she jumps up to the bar and lowers herself as slowly as she can. That slow lowering builds the strength you need to pull yourself up.</p>
<p><strong>Where she is now:</strong></p>
<ul>
  <li>Her first pull-up, and now multiple reps with the lightest assistance band</li>
  <li>Weighted planks with about 75 pounds on her back</li>
  <li>Curls with 30-pound dumbbells</li>
  <li>Bench press around 85 pounds for reps</li>
</ul>
<p>Every step was based on what I saw from her in person: what looked safe, and what she was ready for.</p>
{callout("Client result", "Teresa, 60: from zero bodyweight exercises to pull-ups", ["Started with a shoulder injury", "First pull-up in about 3 months", "Bench press about 85 pounds for reps", "Curls with 30-pound dumbbells"])}

<h2 id="sam">Sam, 70: deadlifting 135 pounds for reps</h2>
<p>Sam is 70, and he's a badass. Right now he's doing:</p>
<ul>
  <li>Deadlifts with about 135 pounds for reps</li>
  <li>Dumbbell bench press with the 45s for reps</li>
  <li>Seated dumbbell shoulder press with 45-pound dumbbells</li>
  <li>One-arm lat pulldown with 90-plus pounds</li>
  <li>Decline sit-ups and decline leg raises</li>
</ul>
<p>He didn't start there. Same formula as Teresa: we took it slow, used lighter weight for more reps, and over time gradually lowered the reps and raised the weight until he got to numbers that surprise people half his age.</p>

<h2 id="how">How to build muscle after 60: the formula</h2>
<ol>
  <li><strong>Start where your body is.</strong> Old injuries, imbalances, how long it's been since you trained. The plan works around them.</li>
  <li><strong>Fix imbalances first.</strong> One-arm and one-leg exercises build an even, stable base.</li>
  <li><strong>Start light, with more reps.</strong> About 8 to 12 reps a set while your joints, tendons and technique catch up.</li>
  <li><strong>Progressively overload.</strong> As you get stronger, fewer reps with more weight (8&ndash;12, then 6&ndash;8, then 3&ndash;5, then 1&ndash;3), or a harder version of the movement.</li>
  <li><strong>Track your strength.</strong> Write it down. If the numbers are going up, you're building muscle.</li>
  <li><strong>Recover like it's part of training.</strong> Enough protein, good sleep and smart intensity. More isn't always better.</li>
</ol>
<p>For the nutrition side, especially protein, see <a href="/how-to-lose-weight-after-40">how to lose weight after 40</a>.</p>

<h2 id="safe">Is lifting weights safe after 60?</h2>
<p>This is the number one worry I hear: "I'm going to get hurt." Weightlifting is very safe when your coach is paying attention. I've been coaching for more than 10 years. I can tell when someone is in pain, when they're uncomfortable, and when a movement isn't right for them that day, and we adjust on the spot.</p>
<p>And the payoff is big. Strength training is good for your bones, and people who do it regularly often notice better mood, sleep, energy, focus and sex drive. If you have a medical condition or a recent injury, talk to your doctor before you start, then get coached.</p>

<h2 id="skills">Keep every skill you have</h2>
<p>I work with people over 60 who tell me, "I don't want to jump anymore." OK, but at some point you'll need to. You'll have to hop over something, catch yourself, or move fast. You can't just never jump again.</p>
<p>The goal is to keep every skill you had when you were younger:</p>
<ul>
  <li>Getting up off the floor</li>
  <li>Getting off the toilet or a low chair without using your hands</li>
  <li>Bending over to pick up a sock</li>
  <li>Jumping over something in your way</li>
  <li>Pushing yourself up off the ground</li>
</ul>
<p>Use them or lose them. Training is how you keep them.</p>

<h2 id="late">Is it too late to start at 60 or 70?</h2>
<p>It's never too late. You'll never know how good you can get unless you try, and you have to give yourself some grace.</p>
<p>Plenty of people hit their stride late. Samuel L. Jackson became a household name in his mid-40s. Colonel Sanders started franchising Kentucky Fried Chicken in his 60s. They didn't wait for the perfect time. They just started.</p>
<p>You don't need to be in great shape to begin. You don't need perfect mobility, stability or strength. Take imperfect action.</p>
{pullquote("Chase progress, not perfection.")}

<h2 id="start">How to start</h2>
<p>At Fig Performance in Placentia, every new client starts with a free consult: an <a href="/inbody-scan-placentia">InBody scan</a> to see your muscle and body fat, a strength assessment, and a plan built around your body, including any old injuries. Sessions are one-on-one with me, so every set is watched and adjusted.</p>
<p>Women over 40 can also read our guide to <a href="/strength-training-for-women-over-40">strength training for women over 40</a>.</p>
{CTA}"""

faqs = [
    ("Can you build muscle after 60?",
     "Yes. With progressive strength training, enough protein and good recovery, people in their 60s and 70s build muscle and strength. Teresa started at 60 unable to do bodyweight exercises and did her first pull-up about three months later. Sam, 70, deadlifts about 135 pounds for reps."),
    ("How do you build muscle after 60?",
     "Start light with about 8 to 12 reps, fix side-to-side imbalances with one-arm and one-leg exercises, then gradually lower the reps and raise the weight every few weeks. Track your strength, eat enough protein and prioritize sleep."),
    ("Is weight lifting safe for people over 60?",
     "Yes, when it's coached well and progressed gradually. A good coach watches for pain or discomfort and adjusts on the spot. Check with your doctor first if you have a medical condition or recent injury."),
    ("Is it too late to start lifting weights at 60 or 70?",
     "No. It's never too late. You don't need to be in shape to start. Begin light, get coached, and chase progress, not perfection."),
    ("How long does it take to get stronger after 60?",
     "Strength usually improves within the first few weeks. Teresa went from no bodyweight exercises to her first pull-up in about three months of coached, progressive training."),
]

html = page(
    SLUG,
    "Build Muscle After 60: Her First Pull-Up in 3 Months | Fig Performance",
    "Yes, you can build muscle after 60. How a 60-year-old got her first pull-up in 3 months and a 70-year-old deadlifts 135 lb, from Coach Dan.",
    "How a 60-Year-Old Did Her First Pull-Up in 3 Months (Placentia, CA)",
    "Fitness after 40", "Can You Build Muscle After 60?",
    "Yes. Two real clients, the exact progression we used, and how to start safely.",
    [("teresa", "Teresa, 60: her first pull-up"), ("sam", "Sam, 70: 135-pound deadlifts"), ("how", "The formula"),
     ("safe", "Is it safe after 60?"), ("skills", "Keep every skill you have"), ("late", "Is it too late?"), ("start", "How to start")],
    body, faqs, "Build Muscle After 60", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
