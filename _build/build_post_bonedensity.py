"""Article: Lifting for bone density after 50. Approved by Dan and PUBLISHED Nov 25 2026.
Source links added (LIFTMOR trial verified via PubMed, PMID 28975661, doi 10.1002/jbmr.3284).
[DAN] A client with a documented DEXA improvement would strengthen this page further."""
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-25"
SLUG = "strength-training-for-bone-density"

body = f"""<p class="legal-intro">If you have been told you have osteopenia or osteoporosis, you have probably also been told to walk, swim and be careful. Walking and swimming are good for you. Neither one does much for your bones. The exercise that does is the one most women over 50 are quietly steered away from: picking up heavy things. There is a well-known trial on exactly this.</p>

<h2 id="why">Why walking does not build bone</h2>
<p>Bone responds to load. Specifically, it responds to strain that is larger than what it already handles, applied quickly. That is the signal that tells bone-building cells to get to work.</p>
<p>Walking does not provide it. Your bones handled walking yesterday and the day before. Swimming and cycling are worse for this purpose, because the water or the bike takes your body weight. They are excellent for your heart and your joints. They are not a bone stimulus, and telling a woman with low bone density to swim more is, for her bones, close to telling her to do nothing.</p>
<p>What provides the signal is heavy resistance training and impact. Loading the skeleton through the spine and hips, hard enough that it is genuinely difficult.</p>

<h2 id="liftmor">The LIFTMOR trial</h2>
<p>The trial is called <a href="https://doi.org/10.1002/jbmr.3284" target="_blank" rel="noopener noreferrer">LIFTMOR</a>. Researchers in Australia took 101 postmenopausal women with low bone mass, a T-score below minus 1.0, and randomised them. One group did a home-based, low-intensity exercise program. The other did supervised heavy lifting.</p>
<p>The heavy group trained twice a week for 30 minutes, for eight months. Four exercises: deadlift, back squat, overhead press, and a jumping chin-up with a drop landing for impact. Five sets of five reps, above 85 percent of their one-rep maximum. The first month was bodyweight and light loads to learn the movements before any of that weight went on the bar.</p>
<p>The heavy group improved bone mineral density at the lumbar spine and the femoral neck, which is the top of the thigh bone and one of the places a hip fracture happens. They also improved on physical function tests. The low-intensity group did not keep pace.</p>
{callout("The LIFTMOR protocol", "What the women in the trial actually did", ["Twice a week, 30 minutes, supervised", "Deadlift, back squat, overhead press, jumping chin-up", "5 sets of 5 above 85% of their one-rep max", "First month was light, to learn the movements", "Eight months total"])}
<p>The other finding is the one I would underline. It was safe. These were women with osteopenia and osteoporosis, lifting heavy, and across the eight months the trial logged a single minor adverse event, a back spasm. The fear that heavy lifting will break a fragile spine is the exact thing the study was designed to test, and it did not happen.</p>
{pullquote("Thirty minutes, twice a week, for eight months. That is less time than most people spend on cardio they do not enjoy and their bones do not notice.")}

<h2 id="meaning">What that does and does not mean for you</h2>
<p>A few honest caveats, because this is a medical topic and you deserve the full picture.</p>
<ul>
  <li><strong>It was supervised.</strong> Every session, by people who knew what they were doing. That is not incidental to the result. Five sets of five at 85 percent of maximum is not something to teach yourself from a video.</li>
  <li><strong>Participants were screened.</strong> Women with recent fractures, severe curvature of the upper spine, and certain neurological conditions were excluded. Not everyone with low bone density is a candidate for this exact program.</li>
  <li><strong>It is one trial.</strong> A good one, widely cited, and supported by other work on resistance training and bone, but bone density changes slowly and no single study settles a question.</li>
  <li><strong>Your doctor comes first.</strong> If you have osteoporosis, a history of fracture, or you are on medication for your bones, that conversation happens before you touch a barbell. I am an ACSM certified personal trainer, not a doctor.</li>
</ul>

<h2 id="start">How we would start you</h2>
<p>Nobody walks into Fig Performance and loads a bar to 85 percent of their maximum. Neither did the women in the trial. Here is the honest sequence.</p>
<ol>
  <li><strong>Assessment first.</strong> A movement screen and an InBody scan at the free consultation. If you have a recent DEXA result, bring it.</li>
  <li><strong>Learn the patterns with almost no weight.</strong> Hinge, squat, press. Usually four to six weeks, which is roughly what the trial did.</li>
  <li><strong>Add load slowly and write it down.</strong> The weight goes up when the movement is solid, not on a schedule.</li>
  <li><strong>Add impact only when it fits.</strong> Jumping and landing is a real part of the bone stimulus, but it is the last thing we add, not the first.</li>
  <li><strong>Measure something.</strong> Strength numbers monthly, and a DEXA through your doctor on whatever interval they recommend. Bone changes over years, not weeks.</li>
</ol>
<p>Teresa started here at 60 and could not do a single bodyweight exercise. About three months later she did her first pull-up. That is not a bone density claim, and I am not making one about her. It is the point about where people start: nowhere near a heavy barbell, and that was fine.</p>
{stats([("101", "postmenopausal women in LIFTMOR"), ("2 x 30 min", "a week, for eight months"), ("4", "exercises in the whole program")])}

<h2 id="also">The things that also matter</h2>
<p>Lifting is the lever with the most under it, but it is not the only one. Enough protein, enough calcium and vitamin D, not smoking, and balance work to reduce the odds of a fall in the first place. A fracture needs both a fragile bone and a fall. Training helps with both sides of that.</p>
<p><a href="/how-much-protein-after-40">How much protein you need after 40</a> covers the nutrition side. <a href="/strength-training-for-women-over-50">Strength training for women over 50</a> is the broader starting point.</p>
{CTA}"""

faqs = [
    ("Can you rebuild bone density after 50?",
     "Bone responds to heavy load at any age. In the LIFTMOR trial, postmenopausal women with low bone mass who did supervised heavy lifting twice a week for eight months improved bone mineral density at the spine and hip, while a low-intensity group did not keep pace."),
    ("Is heavy lifting safe with osteoporosis?",
     "The LIFTMOR trial tested exactly that in women with osteopenia and osteoporosis and reported it as safe. It was supervised throughout, and women with recent fractures and certain other conditions were screened out. Talk to your doctor before you start."),
    ("Does walking help osteoporosis?",
     "Walking is good for your health and your balance, but it does not load bone much beyond what it already handles, so it is a weak stimulus for building bone. Heavy resistance training and impact are what the research points to."),
    ("How often do I need to lift for bone health?",
     "The LIFTMOR program was twice a week for 30 minutes. That was enough to change bone mineral density over eight months, which is less time than most people spend on cardio."),
    ("What exercises are best for bone density?",
     "The ones that load the spine and hips: deadlift, back squat and overhead press, plus a controlled impact movement. That was the entire LIFTMOR program, four exercises."),
]

html = page(
    SLUG,
    "Lifting for Bone Density After 50 | Fig Performance",
    "Walking doesn't build bone. What the LIFTMOR trial found about heavy lifting for postmenopausal women with osteopenia, and how to start safely in Placentia, CA.",
    "Strength Training for Bone Density After 50",
    "Fitness after 40", "Walking will not build your bones. This might.",
    "What the LIFTMOR trial found, and how we would start you.",
    [("why", "Why walking does not build bone"), ("liftmor", "The LIFTMOR trial"), ("meaning", "What it means for you"),
     ("start", "How we would start you"), ("also", "What else matters")],
    body, faqs, "Strength training for bone density", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
