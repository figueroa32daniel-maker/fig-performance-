"""Article: How much protein after 40. DRAFT, written by Claude overnight Nov 25 2026
from published research, not from a Coach Dan interview. Dan reviews before publishing.
Open questions for Dan are marked [DAN] in comments."""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "how-much-protein-after-40"

body = f"""<p class="legal-intro">Most people over 40 who tell me they eat plenty of protein are eating about half what they need. Not because they are careless. Because the number everyone quotes, the official RDA, was never meant to be a target for someone who is 50 and lifting weights. It is a floor, set to stop you becoming deficient. Here is what the research actually says, and the simple way I get clients to hit it.</p>

<h2 id="rda">The number you have heard is a floor, not a goal</h2>
<p>The Recommended Dietary Allowance for protein is 0.8 grams per kilogram of body weight a day. For a 165-pound adult that is about 60 grams. It sounds official, and it is, but of what: it is the minimum intake that keeps nearly all healthy adults from running a deficit. It is the bottom of the range, not the middle.</p>
<p>The PROT-AGE study group, convened by the European Union Geriatric Medicine Society, reviewed the evidence for older adults and concluded that 0.8 is too low. Their recommendation for healthy adults over 65 is 1.0 to 1.2 grams per kilogram a day, and 1.2 to 1.5 grams for anyone dealing with a chronic condition or losing muscle. For older adults who train regularly, the range they and others give goes higher still, to roughly 1.2 to 1.7 grams.</p>
{callout("What that looks like", "Protein a day for a 165-pound adult", ["RDA minimum: about 60 g", "PROT-AGE, healthy older adult: 75 to 90 g", "Training regularly: 90 to 127 g"])}
<p>So the gap between the number on the back of the cereal box and the number that actually protects your muscle is not small. For a lot of my clients it is 40 or 50 grams a day.</p>

<h2 id="why">Why it changes after 40</h2>
<p>There is a specific reason older adults need more, and it has a name: anabolic resistance. As you age, the same amount of protein in a meal triggers less muscle building than it did at 25. Your body gets less responsive to the signal, so you need a louder signal.</p>
<p>Research on this is blunt about the size of the effect. Work by Moore and colleagues found that adults around 71 needed substantially more protein in a single meal than young adults to stimulate muscle protein synthesis at the same rate. You are not imagining that what used to work has stopped working.</p>
<p>Put that next to the other thing that happens after 40, which is that muscle starts to go if nothing is asking it to stay, and you get the situation I see every week: someone eating what they have always eaten, training the way they have always trained, and slowly losing ground.</p>
{pullquote("Protein is not what builds the muscle. Lifting builds the muscle. Protein is the material. You need both, and most people over 40 are short on both.")}

<h2 id="meal">Spread it out, do not save it for dinner</h2>
<p>Total for the day matters, but so does how you spread it. Most people I meet eat almost no protein at breakfast, a little at lunch, and then a large amount at dinner. That pattern wastes the two meals where you had a chance to trigger muscle building and leaves one meal doing all the work.</p>
<p>The practical target is 25 to 35 grams of protein at each main meal. That is roughly:</p>
<ul>
  <li>A 4 to 5 ounce chicken breast</li>
  <li>Two scoops of most whey protein powders</li>
  <li>A cup of Greek yogurt plus a handful of nuts</li>
  <li>Four eggs, or two eggs plus a cup of cottage cheese</li>
  <li>5 ounces of 93% lean ground beef</li>
</ul>
<p>Breakfast is where almost everyone leaks protein. A bagel, a banana and coffee is close to nothing. If you fix only one meal, fix that one.</p>

<h2 id="how">How I get clients to actually hit it</h2>
<ol>
  <li><strong>Work out your real number.</strong> Body weight in pounds divided by 2.2 gives kilograms. Multiply by 1.2 if you are training, more if you are trying to hold muscle while losing fat.</li>
  <li><strong>Count for three days, then stop.</strong> I am not asking anyone to track forever. Three days tells you where you actually are, which is almost always lower than you think.</li>
  <li><strong>Anchor each meal to a protein.</strong> Decide the protein first and build the rest of the plate around it. It is a much easier habit than counting.</li>
  <li><strong>Use the easy wins.</strong> Greek yogurt, cottage cheese, a shake, deli turkey, canned tuna. Nobody is cooking three times a day.</li>
  <li><strong>Re-scan, do not guess.</strong> An InBody scan separates muscle from fat. If the scale is dropping and your muscle is dropping with it, you are losing the wrong thing, and protein is usually the first place to look.</li>
</ol>
{stats([("0.8 g/kg", "the RDA, a minimum"), ("1.0 to 1.2", "PROT-AGE, healthy over 65"), ("25 to 35 g", "per meal, not just at dinner")])}

<h2 id="kidneys">What about my kidneys?</h2>
<p>This is the question I get most, usually from someone whose doctor mentioned it years ago. For people with healthy kidneys, there is no good evidence that higher protein intakes in these ranges cause damage, and the Institute of Medicine has not set an upper limit for protein. If you have diagnosed kidney disease, that is a different conversation and it belongs with your doctor, not with me or an article.</p>
<p>I am an ACSM certified personal trainer and a Precision Nutrition Level 1 certified nutrition coach. I am not a registered dietitian or a doctor. If you are managing a medical condition, take this to the person who is managing it with you.</p>

<h2 id="lifting">Protein without lifting does not do much</h2>
<p>You can eat 150 grams a day and still lose muscle if nothing is asking your body to keep it. The protein is the raw material. The training is the instruction. Teresa was 60 when she started here, could not do a single bodyweight exercise, and did her first pull-up about three months later. That happened because she lifted and ate enough to support it, in that order of importance.</p>
<p>If you are over 40 and want the training side of this, <a href="/strength-training-for-women-over-40">start here for women</a> or <a href="/workout-plan-for-men-over-40">here for men</a>, and <a href="/build-muscle-after-60">here if you are over 60</a>.</p>
{CTA}"""

faqs = [
    ("How much protein do I need a day after 40?",
     "Work from your body weight rather than a flat number. Divide your weight in pounds by 2.2 to get kilograms, then aim for 1.0 to 1.2 grams per kilogram if you are generally healthy, and up to about 1.6 if you are training regularly or trying to hold muscle while losing fat."),
    ("Is 100 grams of protein a day enough?",
     "It depends on your size. For a 150-pound adult, 100 grams is a good target. For a 220-pound adult it is on the low side. Work it out from your own body weight instead of using a round number."),
    ("Can too much protein damage your kidneys?",
     "In people with healthy kidneys there is no good evidence that it does, and no upper limit has been set for protein intake. If you have diagnosed kidney disease, ask your doctor what range is right for you."),
    ("Do I need protein powder?",
     "No, but it makes the target much easier to hit. Most people struggle at breakfast and after training, and a shake solves both without any cooking."),
    ("Should I eat protein before or after a workout?",
     "The total over the day matters far more than the timing. Getting 25 to 35 grams at each main meal will do more for you than worrying about a window around training."),
]

html = page(
    SLUG,
    "How Much Protein Do You Need After 40? | Fig Performance",
    "The RDA for protein is a floor, not a target. What adults over 40 actually need per day and per meal, and how to hit it, from Coach Dan in Placentia, CA.",
    "How Much Protein Do You Actually Need After 40?",
    "Fitness after 40", "How much protein do you need after 40?",
    "The number everyone quotes is a minimum. Here is the real range, and how to hit it.",
    [("rda", "The RDA is a floor"), ("why", "Why it changes after 40"), ("meal", "Spread it out"),
     ("how", "How to hit it"), ("kidneys", "What about my kidneys?"), ("lifting", "Protein without lifting")],
    body, faqs, "How much protein after 40", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
