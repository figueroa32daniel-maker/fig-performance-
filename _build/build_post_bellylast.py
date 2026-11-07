"""Article: Is belly fat the last to go? (from Coach Dan's voice memo; approved by Dan Nov 7 2026)."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-07"
SLUG = "is-belly-fat-the-last-to-go"
CHASTON = "https://pubmed.ncbi.nlm.nih.gov/18180786/"
WAHRENBERG = "https://pubmed.ncbi.nlm.nih.gov/2503539/"
GALITZKY = "https://www.jci.org/articles/view/116421"
EPEL = "https://pubmed.ncbi.nlm.nih.gov/11020091/"
VISPUTE = "https://doi.org/10.1519/JSC.0b013e3181fb4a46"

body = f"""<p class="legal-intro">Yes. Belly fat really is the last to go, and the lower belly in particular. I see it with almost every client. The face leans out, the arms change, the pants get loose in the legs, and the lower stomach hangs on. Here's why your body does that, what the research says about it, and what actually gets it moving, including a client who went from an inflamed, bloated stomach to flat in under three months after 42.</p>

<h2 id="why">Why the belly is where your body keeps its reserves</h2>
<p>Think about where your organs are. Your body stores a lot of its fat around the midsection because that's where the organs it most wants to protect are, and because fat stored there is a resource it can pull from quickly. For most of human history, a reserve of energy you could tap during a hard winter or a long stretch without food was the difference between surviving and not. The belly is that reserve. The body is built to fill it first and empty it last, because that's what kept your ancestors alive.</p>
<p>The modern science lines up with the old logic in a way that's worth understanding, because it changes how you attack the problem.</p>

<h2 id="two">Two kinds of belly fat, and they don't behave the same</h2>
<ul>
  <li><strong>Visceral fat</strong> sits deep, around the organs, behind the abdominal wall. It's the fat that makes the upper belly feel hard and pushed out, and it's the kind linked to heart disease, type 2 diabetes and fatty liver.</li>
  <li><strong>Subcutaneous fat</strong> sits under the skin. It's what you can pinch. The lower belly pooch, the one almost everyone carries, is mostly this kind. It's not dangerous. It's just stubborn.</li>
</ul>
<p>Here's the part most people get backwards: the dangerous deep fat is the <em>first</em> to go. A systematic review of weight-loss studies found that with modest weight loss, visceral fat is lost preferentially, meaning a small amount of total fat loss removes a larger share of the deep fat than the pinchable fat (<a href="{CHASTON}" target="_blank" rel="noopener noreferrer">Chaston &amp; Dixon, 2008</a>). Your body gives up the reserve that's closest to the bloodstream first.</p>
<p>The lower belly is the opposite. Fat cells in different parts of the body have different mixes of receptors. Some receptors tell the cell to release fat; others tell it to hold on. Lower-body and lower-abdominal fat cells carry more of the "hold on" receptors, and that fat tissue gets less blood flow, so even when the rest of you is burning fat, those cells release it slowly (<a href="{WAHRENBERG}" target="_blank" rel="noopener noreferrer">Wahrenberg et al., 1989</a>; <a href="{GALITZKY}" target="_blank" rel="noopener noreferrer">Galitzky et al., 1993</a>). That's the biology behind "the last to go." It isn't that you're doing something wrong. It's that those cells are built to be stubborn.</p>

<h2 id="cortisol">Where cortisol fits</h2>
<p>Stress matters here too. Cortisol, the stress hormone, pushes fat storage toward the middle. A study of women at Yale found that the ones who carried their fat centrally secreted more cortisol in response to stress and kept secreting it when the same stress came back, even when they were otherwise lean (<a href="{EPEL}" target="_blank" rel="noopener noreferrer">Epel et al., 2000</a>). I see the lifestyle version of this all the time: a client under a lot of stress, not sleeping, eating junk and drinking, and the stomach is inflamed and bloated on top of whatever fat is there. Fix the stress, the sleep and the food, and a surprising amount of that belly goes away before you've lost much fat at all.</p>
{pullquote("The deep fat that threatens your health leaves first. The lower belly you can pinch leaves last. Judge your progress by the right one.", "Coach Dan Figueroa")}

<h2 id="inbody">What the InBody shows that the mirror can't</h2>
<p>This is why I scan every client. The InBody gives a visceral fat level. On our scale, I want clients under 6. Below that, you're clear of the health problems that come with high visceral fat, whatever the lower belly is doing. A client can look almost the same in the mirror after a month while that number drops, and that is real progress, the kind that matters most for your health.</p>
{callout("Visceral fat on the InBody", "Under 6 is the target", ["Visceral fat is the deep fat around the organs, the kind tied to heart disease and diabetes", "It leaves first with a modest deficit, often before the mirror changes", "We re-scan every four to six weeks to watch it move"])}

<h2 id="crunches">Do crunches burn belly fat?</h2>
<p>No, and yes. Crunches don't burn the fat sitting over your abs. A controlled study put people through six weeks of abdominal training, seven exercises, five days a week, and found no change in belly fat or waist size compared with a group that did nothing (<a href="{VISPUTE}" target="_blank" rel="noopener noreferrer">Vispute et al., 2011</a>). Fat comes off the whole body in a calorie deficit, in the order your genetics decide.</p>
<p>But core training absolutely works for what it's actually for. Train the stomach with weight and it gets stronger, and strength is muscle tissue. A stronger, thicker core shows more definition even at a higher body fat percentage. So I train the core hard, from every angle:</p>
<ul>
  <li>Bench leg raises, hanging knee raises, hanging leg raises, hanging side knee raises</li>
  <li>Kneeling wood choppers, Pallof presses, Russian twists</li>
  <li>Dumbbell side bends and Smith machine side bends</li>
  <li>Reverse crunches and full-body sit-ups</li>
  <li>Hyperextensions, reverse hyperextensions and glute-ham raises for the back side of the core</li>
</ul>
<p>Weighted, progressed, from all angles. That builds the muscle. The deficit uncovers it.</p>

<h2 id="moves">What actually moves belly fat, and how fast</h2>
<p>Three things, dialed in, and you can see the visceral fat number and the waist move week to week:</p>
<ol>
  <li><strong>Walk 30 minutes every day.</strong> Not optional. This is the cheapest fat burner there is and it costs you no recovery.</li>
  <li><strong>Strength train at least twice a week.</strong> Heavy enough to get stronger. Muscle is what makes a leaner midsection look tight instead of deflated.</li>
  <li><strong>Eat your goal weight in grams of protein.</strong> Want to weigh 160? About 160 grams a day. It protects muscle and kills the snacking that fills the deficit back in.</li>
</ol>
<p>Then the honest extras: sleep, stress, and alcohol. All three land on the belly. Alcohol is the one I'd look at first if your stomach is bloated and inflamed, because it's empty calories, it wrecks sleep, and your body burns it before it touches stored fat.</p>
<p>The deep fat moves fast with this. The lower belly is slower, often the last few months of a fat-loss phase. That's normal. It isn't a sign the plan stopped working.</p>

<h2 id="priscilla">Priscilla's stomach</h2>
<p>Priscilla came to me over 42 with a stomach that was really inflamed. She was drinking, eating a lot of junk, and it showed exactly where you'd expect. She stopped the drinking and the junk, followed the diet, did her cardio, and trained with me three times a week. Her stomach got flat fast. Within about two to three months it was very flat, and she lost 20 pounds along the way.</p>
{stats([("20 lb", "lost"), ("2&ndash;3", "months to a flat stomach"), ("3&times;", "a week with me")])}
<p>I'm not going to pretend that's easy. It took dedication, focus, good time management and good stress management. But it's absolutely possible after 40, and the stomach is often the first thing to change once the inflammation comes down, even while the last of the lower belly fat is still on its way out.</p>

<h2 id="coach">Find out which fat you're actually carrying</h2>
<p>If your stomach feels hard and pushed out above the navel, that's visceral fat, and it's the one worth going after first. If it's a soft lower pooch, it'll come, last, and chasing it with crunches won't speed it up. Either way, the InBody tells you where you stand in about a minute, and the free consult includes one.</p>
<p>Fig Performance is a <a href="/">private one-on-one personal training gym in Placentia</a>, serving Yorba Linda, Brea, Fullerton and Anaheim Hills. Related: <a href="/how-to-lose-belly-fat-after-menopause">how to lose belly fat after menopause</a>, <a href="/how-to-lose-weight-after-40">how to lose weight after 40</a> and <a href="/why-am-i-not-losing-weight">why you're not losing weight</a>. Can't make it in person? Try <a href="/online-personal-trainer">online coaching</a>.</p>
<p><em>Check with your doctor before starting a new exercise or nutrition program, especially if you have a heart condition, diabetes or a recent injury.</em></p>
{CTA}"""

faqs = [
    ("Is belly fat really the last to go?",
     "The pinchable lower belly fat usually is. Those fat cells carry more of the receptors that block fat release and get less blood flow. The deeper visceral fat behind upper belly fat is often the first to go with modest weight loss."),
    ("What causes upper belly fat?",
     "Mostly visceral fat around the organs, plus some fat under the skin. It's linked to stress, poor sleep, alcohol and a calorie surplus, and it's the kind tied to heart disease and diabetes."),
    ("What is a good visceral fat level on the InBody?",
     "Coach Dan's target for clients is under 6 on the InBody's visceral fat scale. Below that, you're clear of the health problems tied to high visceral fat."),
    ("Do crunches burn belly fat?",
     "No. Six weeks of daily abdominal training didn't change belly fat in a controlled study. Fat comes off the whole body in a calorie deficit. Weighted core training builds the muscle underneath so the abs show more once the fat comes off."),
    ("How fast can you lose belly fat?",
     "The deep visceral fat moves within weeks with daily walking, two strength sessions a week and enough protein. The lower belly is slower and is usually the last to flatten, often over two to three months or more."),
    ("Does cortisol cause belly fat?",
     "Cortisol pushes fat storage toward the middle, and women who carry fat centrally secrete more cortisol under stress. Sleep, stress management and cutting back alcohol help, along with the training and food."),
]

html = page(
    SLUG,
    "Is Belly Fat the Last to Go? Why, and What Works | Fig",
    "Is belly fat the last to go? Yes. The science of why the body keeps it, why the lower belly is stubborn, and what flattened one client's stomach in 3 months.",
    "Is Belly Fat the Last to Go? Why Your Body Keeps It, and What Moves It",
    "Fitness after 40", "Is Belly Fat the Last to Go? Why Your Body Keeps It, and What Moves It",
    "Yes. Here's why, which belly fat leaves first, and how Priscilla got a flat stomach after 42.",
    [("why", "Why the belly"), ("two", "Two kinds of belly fat"), ("cortisol", "Where cortisol fits"), ("inbody", "What the InBody shows"),
     ("crunches", "Do crunches work?"), ("moves", "What moves it"), ("priscilla", "Priscilla's story"), ("coach", "Which fat are you carrying?")],
    body, faqs, "Is Belly Fat the Last to Go?", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
