"""Article: GLP-1s and muscle loss (from Coach Dan's voice answers, Nov 3 2026)."""
import sys
from build_pages import page, SITE, CTA

DATE = "2026-11-03"
SLUG = "glp-1-muscle-loss"
STEP1 = "https://pmc.ncbi.nlm.nih.gov/articles/PMC8089287/"
STEP1X = "https://pubmed.ncbi.nlm.nih.gov/35441470/"

body = f"""<p class="legal-intro">GLP-1 medications like semaglutide (Ozempic, Wegovy) and tirzepatide (Mounjaro, Zepbound) work largely by turning down your appetite, so you eat less and lose weight. The catch: a big share of that weight can come from muscle, and when you're barely hungry it's hard to eat enough protein to keep it. Here's how to keep your muscle on a GLP-1, from a coach who has trained clients using them.</p>

<h2 id="tool">A GLP-1 is a tool. Your habits keep the results.</h2>
<p>There's nothing wrong with using one of these medications to get an edge, under your doctor's care. They're prescription drugs, so be mindful of the side effects and work with your doctor.</p>
<p>But the medication is the tool, and your habits are what keep the results. If you ever stop or switch medications, you want to be lifting a few times a week, eating a high-protein diet, eating enough to keep your muscle, and moving every day, so you keep what you worked for.</p>

<h2 id="muscle">Why muscle loss is the real risk</h2>
<p>To keep muscle, your body needs protein and enough fuel. When your appetite is suppressed, both get hard. In one large semaglutide trial, about 40% of the weight people lost was lean mass, which includes muscle (<a href="{STEP1}" target="_blank" rel="noopener noreferrer">STEP 1 body-composition substudy</a>). Some studies also suggest rapid weight loss can affect bone density.</p>
<p>Lose too much muscle and you lose strength, you burn fewer calories at rest, and everyday things get harder. For some people, that trade isn't worth it.</p>
<p>My honest take: if your doctor says you're at high risk of heart disease or another serious condition, these medications can make a lot of sense. For most people, go in with a plan to protect your muscle.</p>

<h2 id="protein">1. Hit your protein, even when you're not hungry</h2>
<ul>
  <li>Aim for at least your goal body weight in grams of protein a day, or 0.7 to 1 gram per pound.</li>
  <li>Eat protein first at every meal, before anything else fills you up.</li>
  <li>Use protein shakes, Greek yogurt and protein bars. Liquid and soft protein is easier to get down when your appetite is low.</li>
  <li>Spread it through the day, starting at breakfast.</li>
</ul>

<h2 id="lift">2. Lift weights 2 to 3 times a week</h2>
<p>Strength training tells your body to keep its muscle while you lose fat. Train full body, track your lifts, and keep getting stronger over time. Hitting personal records while you lose weight is a great sign you're losing fat, not muscle. Start with the beginner workout plan for <a href="/beginner-workout-plan-for-women">women</a> or <a href="/beginner-workout-plan-for-men">men</a>.</p>

<h2 id="fuel">3. Eat enough to keep your muscle</h2>
<p>Don't let the medication drive your calories so low that you can't recover or train hard. Losing weight slower and keeping your muscle beats losing it fast and losing your strength with it.</p>

<h2 id="move">4. Move every day</h2>
<p>Walk daily. Aim for more than 5,000 steps a day, ideally 6,000 or more. It's one of the habits that keeps the weight off later.</p>

<h2 id="stopping">5. Plan for coming off</h2>
<p>When people stop these medications, they often regain much of the weight. In the STEP 1 trial extension, people regained about two-thirds of the weight they'd lost within a year of stopping semaglutide (<a href="{STEP1X}" target="_blank" rel="noopener noreferrer">Wilding et al., 2022</a>). The people who keep their results are the ones who built the habits while they were on it: lifting, high protein, enough food and daily movement.</p>

<h2 id="measure">Measure muscle, not just weight</h2>
<p>The scale can't tell you whether you're losing fat or muscle. An <a href="/inbody-scan-placentia">InBody scan</a> can. At Fig Performance in Placentia, we scan, build your training and protein plan, and re-scan to make sure the weight coming off is fat. Can't make it in person? Try <a href="/online-personal-trainer">online coaching</a>.</p>
<p>This article is general fitness and nutrition guidance, not medical advice. Talk to your doctor before starting, stopping or changing any medication.</p>
{CTA}"""

faqs = [
    ("Do you lose muscle on GLP-1s like Ozempic or Zepbound?",
     "You can. In a large semaglutide trial, about 40% of the weight lost was lean mass, which includes muscle. Eating enough protein and strength training 2 to 3 times a week helps you keep it."),
    ("How much protein should I eat on a GLP-1?",
     "Aim for at least your goal body weight in grams a day, or 0.7 to 1 gram per pound. Eat protein first, and use shakes, Greek yogurt and protein bars when your appetite is low."),
    ("How do I keep muscle on Ozempic?",
     "Hit your protein target, lift weights 2 to 3 times a week and get stronger over time, eat enough to recover, walk daily, and track your body composition with something like an InBody scan."),
    ("What happens when you stop a GLP-1?",
     "Many people regain much of the weight. In the STEP 1 extension, people regained about two-thirds of their weight loss within a year of stopping semaglutide. Building strength, protein and movement habits while you're on it helps you keep your results."),
    ("Should I take a GLP-1 to lose weight?",
     "That's a decision for you and your doctor. They can make a lot of sense when your health risk is high. Either way, protect your muscle with protein and strength training."),
]

html = page(
    SLUG,
    "GLP-1 Muscle Loss: How to Keep Muscle on Ozempic | Fig Performance",
    "GLP-1s like Ozempic and Zepbound can cost you muscle. Coach Dan on protein, strength training, eating enough and keeping your results after you stop.",
    "GLP-1s and Muscle Loss: How to Keep Your Muscle on Ozempic or Zepbound",
    "Fitness after 40", "GLP-1s and Muscle Loss: How to Keep Your Muscle",
    "The medication is a tool. Your habits keep the results. How to protect your muscle on Ozempic, Wegovy, Mounjaro or Zepbound.",
    [("tool", "A tool, not the answer"), ("muscle", "Why muscle loss matters"), ("protein", "Hit your protein"), ("lift", "Lift weights"),
     ("fuel", "Eat enough"), ("move", "Move every day"), ("stopping", "Plan for coming off"), ("measure", "Measure muscle")],
    body, faqs, "GLP-1s and Muscle Loss", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
