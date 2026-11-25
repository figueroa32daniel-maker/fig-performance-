"""Definitional pages for the four Nov 22 AI-Overview gaps.

Each is a plain informational page that defines a service or concept answer-first,
so AI engines (AI Overviews, ChatGPT, Perplexity) can lift a self-contained
definition and cite us. Not commercial city pages; those are separate. Facts are
limited to Fig's real method and the published offers. No invented outcomes.
"""
from build_pages import page, SITE, CTA

PAGES = []

# 1. Placentia 40+
PAGES.append(dict(
    slug="what-is-personal-training-for-adults-over-40",
    title="What Is Personal Training for Adults Over 40?",
    desc="Personal training for adults over 40 is coaching built around how the body changes with age: muscle, recovery and measured progress, not a generic gym program.",
    og="What Is Personal Training for Adults Over 40? | Fig Performance",
    kicker="Guide",
    h1="What Is Personal Training for Adults Over 40?",
    lede="A plain definition, and what a good program over 40 actually includes.",
    crumb="Personal Training Over 40",
    toc=[("definition","The short answer"),("different","Why over 40 is different"),("includes","What a good program includes"),("measure","How progress is measured"),("start","Where to start")],
    body="""<p class="legal-intro">Personal training for adults over 40 is one-on-one coaching built around how the body changes with age. It is not the same program a 25-year-old gets with the volume turned down. It accounts for slower recovery, the muscle loss that begins in the 40s, joints that have some history, and a schedule full of work and family. The goal is to build strength and lose fat in a way that holds, and to measure it rather than guess.</p>

<h2 id="different">Why training over 40 is different</h2>
<p>Three things change after 40. Muscle mass starts to decline, a process called sarcopenia, unless strength training pushes back against it. Recovery slows, so the right amount of training matters more than the maximum amount. And most people over 40 have an old injury or a cranky joint, so movements have to be chosen and loaded carefully. A program that ignores these spends your effort in the wrong places. A program built around them is why people who felt stuck for years start changing again.</p>

<h2 id="includes">What a good program includes</h2>
<p>Four things separate real coaching from supervised workouts:</p>
<ul>
  <li><strong>An assessment first.</strong> What you can do now, what hurts, and where you actually are, so the plan is built for you rather than pulled off a shelf.</li>
  <li><strong>Progressive overload.</strong> Strength comes from gradually asking the body to do slightly more over time. Without it, a program stops working however hard the sessions feel. <a href="/building-muscle-after-50">Here is how that looks after 50.</a></li>
  <li><strong>A small number of movements, trained well.</strong> The compound lifts that move the most muscle, loaded in rep ranges that build both size and strength, rather than a different machine every visit.</li>
  <li><strong>Nutrition that supports it.</strong> Enough protein to hold and build muscle while losing fat, which for most people means aiming for their goal bodyweight in grams of protein a day.</li>
</ul>

<h2 id="measure">How progress is measured</h2>
<p>The scale cannot tell fat from muscle, which is why it is a poor judge of training over 40. At <a href="/">Fig Performance in Placentia</a>, every client starts with an <a href="/inbody-scan-placentia">InBody body-composition scan</a> and is re-scanned regularly, so fat loss and muscle gain show up as separate numbers. It is common in the first months to see the scale barely move while fat drops and muscle rises, a change the scan catches and the mirror misses. Our <a href="/body-composition-glossary">glossary</a> explains each number.</p>

<h2 id="start">Where to start</h2>
<p>If you are over 40, already train, and cannot tell whether your effort is working, a scan answers it in about a minute and the first consult is free. Personal training is $60 to $90 a session with a 3-month minimum, and the <a href="/fitness-after-40">fitness after 40</a> guide covers the training side in more depth.</p>
""",
    faqs=[
        ("What is personal training for adults over 40?","It is one-on-one coaching built around how the body changes with age: slower recovery, age-related muscle loss, and existing joint history. The program is designed to build strength and lose fat in a way that lasts, with progress measured by body-composition scans rather than the scale."),
        ("Is it too late to start strength training at 40, 50 or 60?","No. Muscle responds to progressive strength training at every age studied, including into the 80s. Starting later means being more deliberate about recovery and movement choice, not training less hard. Most people see measurable change within the first few months."),
        ("How is this different from a regular gym membership?","A gym gives you equipment. Personal training gives you a program built for your body, coaching on every rep, and a way to measure whether it is working. For people who have equipment and still feel stuck, the missing piece was never the gym; it was the plan and the measure."),
        ("How often do I need to train?","Most adults over 40 train twice a week in one-on-one sessions and add daily walking. Some train three or four times. The right number is set at the free consult based on your schedule and goals."),
        ("How much does personal training for adults over 40 cost?","At Fig Performance it is $60 to $90 a session, billed weekly or monthly, with a 3-month minimum. Your exact rate is set at the free consult. The first consult and InBody scan are free."),
    ],
))

# 2. Fullerton over 50
PAGES.append(dict(
    slug="strength-training-after-50",
    title="Strength Training After 50: What It Is and Why It Matters",
    desc="Strength training after 50 rebuilds the muscle and bone that age takes away. What it is, why it matters, and what a safe program looks like.",
    og="Strength Training After 50: What It Is and Why It Matters | Fig Performance",
    kicker="Guide",
    h1="Strength Training After 50: What It Is and Why It Matters",
    lede="A plain definition, the science in short, and what a safe program looks like.",
    crumb="Strength Training After 50",
    toc=[("definition","The short answer"),("why","Why it matters after 50"),("looks","What it looks like"),("safe","Is it safe"),("start","Where to start")],
    body="""<p class="legal-intro">Strength training after 50 is resistance exercise, using weights, machines or your own bodyweight, that rebuilds the muscle and bone the body loses with age. After 50 it is the single most important kind of exercise most people can do, because it is the only one that directly reverses age-related muscle loss. Done with coaching and sensible loading, it is also one of the safest.</p>

<h2 id="why">Why it matters after 50</h2>
<p>From around the 40s, adults lose muscle each decade unless they train against it, and the rate climbs after 50. That lost muscle is why strength fades, why metabolism slows, and why balance and bone density decline. Strength training is what turns that around. It rebuilds muscle, loads the bones that keep them dense, and restores the power you use to stand from a chair, carry bags and keep your footing. Cardio is good for the heart; it does not rebuild the muscle, and after 50 that is the thing most worth protecting.</p>

<h2 id="looks">What it looks like</h2>
<p>A good program after 50 is built on a few principles, not a long list of exercises:</p>
<ul>
  <li><strong>Compound movements.</strong> A small number of lifts that train the big muscles of the legs, hips, back and shoulders, where most of the body's muscle lives.</li>
  <li><strong>Progressive overload.</strong> Gradually adding weight, reps or control over time. This is what produces change; without it, the same routine stops working.</li>
  <li><strong>Enough recovery.</strong> Two to three sessions a week is plenty for most people over 50, because recovery, not session count, is the limit.</li>
  <li><strong>Protein.</strong> Older muscle needs more protein to rebuild. A common target is your goal bodyweight in grams of protein a day.</li>
</ul>
<p>Our guides on <a href="/building-muscle-after-50">building muscle after 50</a> and <a href="/strength-training-for-women-over-50">strength training for women over 50</a> go deeper.</p>

<h2 id="safe">Is it safe after 50?</h2>
<p>For most people, yes, and safer than the alternative of losing strength. The risk comes from poor form and loading too fast, which is exactly what coaching removes. At <a href="/personal-trainer-fullerton">Fig Performance, serving Fullerton</a> from the Placentia studio, every program starts with an assessment of what you can do now and anything that hurts, and the load is built up from there. If you have a heart condition or a recent injury, we work with your doctor's guidance.</p>

<h2 id="start">Where to start</h2>
<p>Start with an assessment and an <a href="/inbody-scan-placentia">InBody scan</a> so you have a baseline to train from. The first consult and scan are free. One-on-one training is $60 to $90 a session with a 3-month minimum.</p>
""",
    faqs=[
        ("What is strength training after 50?","It is resistance exercise, using weights, machines or bodyweight, that rebuilds the muscle and bone lost with age. After 50 it is the most important kind of exercise for most people, because it is the only one that directly reverses age-related muscle loss."),
        ("Is strength training safe after 50?","For most people, yes, and safer than losing strength. The risk is poor form and loading too fast, which coaching removes by starting from an assessment and building load gradually. People with a heart condition or recent injury should train with their doctor's guidance."),
        ("How often should someone over 50 lift weights?","Two to three sessions a week is enough for most people, because recovery is the limiting factor after 50, not the number of sessions. Daily walking on top of that is ideal."),
        ("Can you build muscle after 50 or 60?","Yes. Muscle responds to progressive strength training at every age that has been studied. It takes consistency and enough protein, and progress is slower than at 25, but it is real and measurable."),
        ("Where can I do strength training after 50 near Fullerton?","Fig Performance offers private one-on-one strength training for adults over 40 and 50 at 1284 E. Yorba Linda Blvd in Placentia, a short drive from Fullerton. Every session is coached by Dan Figueroa, an ACSM certified personal trainer."),
    ],
))

# 3. Yorba Linda private training
PAGES.append(dict(
    slug="what-is-private-personal-training",
    title="What Is Private Personal Training?",
    desc="Private personal training is one-on-one coaching by appointment in a private facility, with no crowd and no shared floor. Here is what it is and who it suits.",
    og="What Is Private Personal Training? | Fig Performance",
    kicker="Guide",
    h1="What Is Private Personal Training?",
    lede="What it means, how it differs from a big-box gym, and who it is for.",
    crumb="Private Personal Training",
    toc=[("definition","The short answer"),("versus","How it compares"),("suits","Who it suits"),("expect","What to expect"),("start","Where to start")],
    body="""<p class="legal-intro">Private personal training is one-on-one coaching that takes place by appointment in a private facility, rather than on the open floor of a public gym. You train with a coach who is working only with you, in a space without a crowd, waiting for equipment, or anyone watching. It is the most focused way to train, and for people who value their time and their privacy, it is often the one that finally sticks.</p>

<h2 id="versus">How private training compares</h2>
<p>There are four common ways to train with help, and they are genuinely different:</p>
<ul>
  <li><strong>Big-box gym with a trainer.</strong> One-on-one coaching, but on a busy public floor. You share equipment and space with everyone there that hour.</li>
  <li><strong>Semi-private training.</strong> A coach working with a small group, usually two to four people, each on their own program. More affordable, less individual attention.</li>
  <li><strong>Online coaching.</strong> A program and check-ins delivered remotely. Flexible and cheaper, but no one is in the room to correct a lift or adjust a weight.</li>
  <li><strong>Private personal training.</strong> One coach, one client, in a private room, by appointment. The most individual attention and the most privacy, at a higher price than the others.</li>
</ul>

<h2 id="suits">Who private training suits</h2>
<p>Private training fits people who are self-conscious about training in front of others, who have a schedule that will not tolerate waiting for a rack, who want every rep coached rather than a program handed over, or who simply train better without a crowd. It tends to suit professionals and business owners over 40, which is who <a href="/personal-trainer-yorba-linda">Fig Performance, serving Yorba Linda</a>, is built for.</p>

<h2 id="expect">What to expect</h2>
<p>A good private session is not just a workout with company. It starts from an assessment and an <a href="/inbody-scan-placentia">InBody scan</a>, runs on a program built for your body with <a href="/what-is-personal-training-for-adults-over-40">progressive overload</a>, and is measured with regular re-scans so you can see fat and muscle change separately. At Fig Performance that also includes nutrition coaching and recovery tools, all in a private studio.</p>

<h2 id="start">Where to start</h2>
<p>The first consult and InBody scan are free, so you can see the space and the approach before deciding. Private one-on-one training is $60 to $90 a session with a 3-month minimum; <a href="/pricing">semi-private</a> is a lower-cost option if you are comfortable training in a small group.</p>
""",
    faqs=[
        ("What is private personal training?","It is one-on-one coaching by appointment in a private facility, rather than on the open floor of a public gym. One coach works only with you, with no crowd, no waiting for equipment, and no one watching."),
        ("What is the difference between private and semi-private training?","Private training is one coach and one client. Semi-private is one coach working with a small group, usually two to four people, each on their own program. Private gives more individual attention and privacy; semi-private costs less."),
        ("Is private personal training worth the cost?","It depends on what has stopped you before. If equipment and information were never the problem, and consistency and attention were, the privacy and one-on-one coaching are usually what makes training finally stick. If you will train reliably on your own, a cheaper option may fit better."),
        ("Is private training better for beginners?","Often, yes. Beginners benefit most from having every lift coached and from not feeling watched while they learn. A private setting removes the intimidation that keeps a lot of people from starting."),
        ("Where can I find private personal training near Yorba Linda?","Fig Performance is a private one-on-one studio at 1284 E. Yorba Linda Blvd in Placentia, minutes from Yorba Linda. Sessions are by appointment with Dan Figueroa, an ACSM certified personal trainer."),
    ],
))

# 4. Brea strength + weight loss
PAGES.append(dict(
    slug="strength-training-for-weight-loss",
    title="Strength Training for Weight Loss: How It Actually Works",
    desc="Strength training drives weight loss by holding onto muscle in a calorie deficit, so what you lose is fat. Here is why lifting beats cardio alone for fat loss.",
    og="Strength Training for Weight Loss: How It Works | Fig Performance",
    kicker="Guide",
    h1="Strength Training for Weight Loss: How It Actually Works",
    lede="Why lifting, not just cardio, is what changes how your body looks.",
    crumb="Strength Training for Weight Loss",
    toc=[("definition","The short answer"),("why","Why it beats cardio alone"),("recomp","Why the scale lies"),("looks","What it looks like"),("start","Where to start")],
    body="""<p class="legal-intro">Strength training drives weight loss by protecting your muscle while you lose weight, so that what comes off is fat rather than a mix of fat and muscle. A calorie deficit is what makes you lose weight; strength training is what decides whether you end up smaller and soft or leaner and stronger. For changing how your body actually looks, lifting does more than cardio alone.</p>

<h2 id="why">Why it beats cardio alone</h2>
<p>When you eat in a deficit, the body pulls energy from both fat and muscle. Cardio burns calories but does nothing to tell the body to keep its muscle, so people who only do cardio often lose weight and still look soft, because they lost muscle along with the fat. Strength training sends the opposite signal: it tells the body the muscle is needed, so the deficit comes out of fat instead. The result is the same scale weight with a very different body underneath. Muscle also keeps your metabolism higher, which makes the fat loss easier to hold.</p>

<h2 id="recomp">Why the scale lies during fat loss</h2>
<p>Because strength training can build a little muscle while you lose fat, the scale often moves slowly even as your body changes, a process called <a href="/body-composition-glossary">body recomposition</a>. This is why we measure with an <a href="/inbody-scan-placentia">InBody scan</a> rather than the scale: it shows fat mass and muscle mass as separate numbers, so a month where the scale barely moved can turn out to be a month where you lost eight pounds of fat and built two of muscle. Our guide on <a href="/why-am-i-not-losing-weight">why the scale is not moving</a> covers this in depth.</p>

<h2 id="looks">What it looks like</h2>
<p>Fat loss that lasts is built on three things, none of them extreme:</p>
<ul>
  <li><strong>A modest calorie deficit</strong> you can actually sustain, not a crash diet that costs you muscle.</li>
  <li><strong>Strength training two to three times a week,</strong> built on compound lifts and <a href="/what-is-personal-training-for-adults-over-40">progressive overload</a>.</li>
  <li><strong>Enough protein,</strong> usually around your goal bodyweight in grams a day, which protects muscle and keeps you full.</li>
</ul>
<p>Daily walking on top of that does more for fat loss over time than punishing cardio sessions.</p>

<h2 id="start">Where to start</h2>
<p>At <a href="/personal-trainer-brea">Fig Performance, serving Brea</a> from the Placentia studio, every client starts with a free consult and InBody scan, so fat loss is tracked honestly from day one. Personal training is $60 to $90 a session with a 3-month minimum.</p>
""",
    faqs=[
        ("Does strength training help with weight loss?","Yes, in a specific way. A calorie deficit is what makes you lose weight, and strength training is what makes the weight you lose come from fat instead of muscle. That is the difference between ending up smaller and soft or leaner and stronger."),
        ("Is strength training or cardio better for fat loss?","Strength training does more to change how your body looks, because it protects muscle in a deficit so you lose fat rather than muscle, and it keeps metabolism higher. Cardio and daily walking help burn calories on top of that. The best fat-loss plans use both, with lifting at the core."),
        ("Why is the scale not moving even though I'm training?","Because strength training can build muscle while you lose fat, so the scale moves slowly even as your body changes shape. This is called body recomposition. A body-composition scan shows fat and muscle as separate numbers, which the scale cannot."),
        ("How much protein do I need for fat loss?","A common target is your goal bodyweight in grams of protein a day. Enough protein protects muscle while you are in a calorie deficit and keeps you fuller, which makes the deficit easier to hold."),
        ("Where can I train for strength and weight loss near Brea?","Fig Performance offers private one-on-one training for adults over 40 at 1284 E. Yorba Linda Blvd in Placentia, a short drive from Brea. Every client starts with a free consult and InBody scan to track fat loss honestly."),
    ],
))

pages = {}
for d in PAGES:
    toc = d["toc"]
    pages[f"{d['slug']}.html"] = page(
        d["slug"], d["title"], d["desc"], d["og"], d["kicker"], d["h1"], d["lede"],
        toc, d["body"], d["faqs"], d["crumb"], kind="article",
        published="2026-11-24", updated="2026-11-24")

if __name__ == "__main__":
    for name, content in pages.items():
        (SITE / name).write_text(content)
        print("wrote", name, len(content))
