"""Article: Are Jefferson curls safe? (from Coach Dan's voice memo, Nov 7 2026). Publish only after Dan approves."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-09"
SLUG = "jefferson-curls"
JOSPT = "https://www.jospt.org/doi/10.2519/jospt.2020.9218"
BHOF = "https://www.bonehealthandosteoporosis.org/patients/treatment/exercisesafe-movement/protecting-your-spine/"

body = f"""<p class="legal-intro">If you've been told to never round your back when you lift, the Jefferson curl looks like a mistake on purpose. You stand on a box, hold a weight, tuck your chin, and roll your spine down one vertebra at a time until you're folded over as deep as you can go. Then you unravel back up. Slowly. On purpose.</p>
<p>I Jefferson curl 205 pounds. I program the exercise for most of my clients over 40, including people who came to me with low back pain. Here's how I got there, why I think the "never round your back" rule is wrong for most people, how I teach it, and who I hold back.</p>

<h2 id="history">This isn't a new exercise</h2>
<p>The Jefferson curl has been around for a long time. I've spent years researching old-school bodybuilding for my YouTube channel, from the 1920s through the 1980s, and loaded spinal flexion shows up well before anyone put a name on it. Lifters in the 1930s were doing versions of this.</p>
<p>What's new is the attention. Ben Patrick, the Knees Over Toes Guy, brought the Jefferson curl back into the mainstream. When I first saw him doing it, my reaction was the same as everyone else's: no, that's not a good idea. Then I did what I always do with an exercise I'm skeptical of. I tested it.</p>

<h2 id="tested">What happened when I tested it</h2>
<p>I started with just the bar, for reps. Over time I added 5 pounds a side, then 10, 15, 20, 25, 30, 35, 40. At 45 a side it felt easy, so I kept going. One day I worked up to 175 and felt good, so I tested it and hit 205 pounds.</p>
{stats([("Bar", "where I started"), ("205 lb", "where I am now"), ("0", "back pain while I keep doing them")])}
<p>The number isn't the interesting part. The interesting part is what happened when I stopped. Every time I dropped Jefferson curls out of my training, my lower back started hurting. When I put them back in, the pain stopped. It was that consistent. It was amazing, honestly, and it's the thing that changed my mind.</p>

<h2 id="why">Why I think the "never round your back" rule is wrong</h2>
<p>You use your spine every day, and most of the time you use it rounded. When you pick a laundry basket off the floor, a vacuum, a bag of concrete, a toddler, you are not setting up like a powerlifter. You're bending over. That's a rounded spine under load, and you do it dozens of times a day whether you train it or not.</p>
<p>So it makes sense to train that skill, with resistance, the same way you'd train anything else. If I can pick up 205 pounds with my spine rounded, a 30-pound vacuum or a 90-pound bag of concrete is no business at all. My spine already owns that position with far more load than daily life will ever ask of it.</p>
{pullquote("You don't get hurt doing a movement your body is strong in. You get hurt doing a movement your body doesn't own.", "Coach Dan Figueroa")}
<p>That's the whole idea. Most adults over 40 have back pain because they've spent decades avoiding movement, not because they moved wrong once.</p>

<h2 id="research">What the research says</h2>
<p>The "never round your back" rule has a real origin. Lab studies on animal spines showed that repeated flexion under heavy load can damage discs. That research shaped a generation of coaching and got simplified into one line: a rounded back is a dangerous back. But those studies used dead tissue in a clamp, with no blood supply, no muscle and no ability to adapt. Your spine is living tissue that gets stronger when you load it carefully and weaker when you don't.</p>
<p>In 2020, a systematic review in the <em>Journal of Orthopaedic &amp; Sports Physical Therapy</em> looked at whether lifting with a rounded lower back is a risk factor for low back pain. It found no evidence that it is. People who lifted with more flexion were not more likely to hurt their backs than people who lifted with a "perfect" neutral spine (<a href="{JOSPT}" target="_blank" rel="noopener noreferrer">Saraceni et al., 2020</a>).</p>
<p>Two honest caveats. The studies in that review used moderate loads, not max deadlifts, so it doesn't prove that rounding under a heavy barbell is smart. And the authors rated the evidence as low quality. What it does show is that the blanket rule is too simple. Your spine bends. It's built to. Avoiding that movement for twenty years doesn't make it safer. It makes you worse at it.</p>

<h2 id="how">How I teach the Jefferson curl</h2>
<p>I start everyone with body weight. No bar, no plates. Here's the movement:</p>
<ol>
  <li><strong>Stand tall and brace.</strong> Squeeze your core and squeeze your glutes. Both stay tight the entire rep.</li>
  <li><strong>Tuck your chin</strong> and start rounding from the top of your spine down.</li>
  <li><strong>Bring your upper body toward your waistline.</strong> Past the belly button, past the waistline, past the groin, down toward the knees, and as deep as you can go with control. Glutes and core stay squeezed the whole way down.</li>
  <li><strong>At the bottom, when you feel a real stretch,</strong> reverse it. Unravel your spine slowly, lower back first, then middle back, then upper back.</li>
  <li><strong>Finish in full extension.</strong> Arch your back at the top so you've moved through both spinal flexion and spinal extension in one rep.</li>
</ol>
<p><strong>Reps:</strong> 1 to 8 per set is a good place to start. Slow on the way down, slow on the way up.</p>

<h2 id="progress">How I progress a beginner</h2>
<p>The progression is range of motion first, then load:</p>
<ul>
  <li><strong>Body weight, short range.</strong> If someone is stiff, I shorten the range. Roll down to a bench, then curl back up. That's a full rep.</li>
  <li><strong>Add range.</strong> Over weeks, the bench gets lower, then goes away. The goal is to get past the knees with control and no pain.</li>
  <li><strong>Then add load.</strong> Once the range is good, we add weight: 2.5 pounds, then 5, 10, 15, 20, and we keep going as long as the movement stays clean.</li>
</ul>
<p>There's no rush. I could have a 70-year-old do this, because the entry point is body weight to a bench, which is less load than bending over to tie a shoe.</p>
<p>One more thing: the Jefferson curl is not the whole program. The muscles that support it still need their own work. Arms, glutes, calves, neck, thoracic spine, core and hips all get trained alongside it. The spine gets strong in that range because everything around it gets strong too.</p>

<h2 id="who">Who I hold back</h2>
<p>Here's the honest answer: it depends, and you'd be surprised. Some people with a history of back pain do this with zero discomfort from day one. Others feel it right away. It comes down to how your spine responds, and the only way to find out is body weight, short range, and paying attention.</p>
<p>If it hurts at body weight, we stop and build other things first. If it doesn't, we progress. Most people are already doing 5 to 25 pounds of loaded spinal flexion every day just living their lives. We're building from there, not from zero.</p>
<p>Standard cautions still apply. Get cleared by your doctor or physical therapist first if you have a recent disc herniation, pain or numbness that runs down a leg, or you're in an acute flare. If you have diagnosed osteoporosis, loaded spinal flexion is generally advised against because of fracture risk (<a href="{BHOF}" target="_blank" rel="noopener noreferrer">Bone Health &amp; Osteoporosis Foundation</a>), so this one is a conversation with your doctor, not a default.</p>

<h2 id="jonathan">What it did for Jonathan</h2>
<p>Jonathan came to me at 43 with a back in bad shape. Stiff, achy, cranky. Bending over hurt. Touching his toes hurt. He'd stopped golfing entirely because his back wouldn't let him. He also had shoulder pain, a new son at home, and an Army background, so he was no stranger to hard training. His back just hadn't been trained in the range that was failing him.</p>
<p>We started the Jefferson curl the way I start everyone: body weight, short range, then more range, then load. Today Jonathan Jefferson curls 135 pounds. That's 135 pounds through the exact motion that used to hurt him empty-handed.</p>
{callout("Client result", "Jonathan, 43", ["Came in stiff and in pain bending over; had quit golf because of his back", "Started at body weight, short range", "Now Jefferson curls 135 pounds"])}
<p>Another client in his 40s went from 10 pounds to 45 pounds on the Jefferson curl in two months, following the same progression. Nothing fancy. Range first, then small jumps in weight, and the back adapts.</p>

<h2 id="chiro">What I'd say to a chiropractor who disagrees</h2>
<p>I'd say: look at what actually happens to a lot of people with back pain. They get an X-ray and the doctor says the bones look fine. They go to a chiropractor who adjusts the structure. If that doesn't hold, they get an MRI, and the MRI says there's no tear, no disc problem, nothing structural.</p>
<p>Now they're confused. It's not a skeletal issue. It's not a tear. So what is it?</p>
<p>Most of the time, it's a strength and weakness issue. Your spine is weak in ranges you never train. Then life asks you to lift something in one of those ranges, and that's how you get hurt. Not because the movement is dangerous. Because you don't own it.</p>
<p>A chiropractor might say the spine isn't meant to move that way. But our bodies are built to move in a lot of ways we've stopped moving. Watch a 3-year-old. Kids have incredible flexibility, including through the spine, and nobody worries about it. If their spine can do it, what's so different about training ours to do it again? We don't lose that range because it's unsafe. We lose it because we're a CFO or a sales rep or a manager, sitting most of the day, not moving much, and the body stiffens to match.</p>

<h2 id="coach">Is a Jefferson curl right for you?</h2>
<p>If you're over 40, you've avoided rounding your back for years, and your back is stiff but not injured, a Jefferson curl taught properly, starting at body weight, is one of the best things you can add. If you're not sure which category you're in, that's what the free consult is for. We look at how you move before anything gets loaded.</p>
<p>Fig Performance is a <a href="/">private one-on-one personal training gym in Placentia</a>, serving Yorba Linda, Brea, Fullerton and Anaheim Hills. Every plan starts with a free consult, an <a href="/inbody-scan-placentia">InBody scan</a> and a movement assessment. Related reading: <a href="/strength-training-for-seniors">strength training for seniors</a>, <a href="/workout-plan-for-men-over-40">the workout plan for men over 40</a> and <a href="/tib-raises">tib raises for knee and shin pain</a>. Can't make it in person? Try <a href="/online-personal-trainer">online coaching</a>.</p>
<p><em>Check with your doctor before starting a new exercise program, especially if you have osteoporosis, a disc injury, nerve symptoms, or a recent injury or surgery.</em></p>
{CTA}"""

faqs = [
    ("Are Jefferson curls bad for your back?",
     "Not when they're taught with body weight first, slow tempo and a gradual increase in range and load. A 2020 systematic review found no evidence that lifting with a rounded back is a risk factor for low back pain. People with disc injuries, nerve symptoms or osteoporosis should get cleared by a doctor first."),
    ("How much weight should I use for Jefferson curls?",
     "None to start. Begin with body weight, shorten the range to a bench if you need to, and add weight only once you can get past your knees with control. Then 2.5 pounds, 5, 10, 15, 20 and up."),
    ("How many reps of Jefferson curls should I do?",
     "Coach Dan starts clients at 1 to 8 reps per set, slow in both directions, with the core and glutes squeezed the whole time."),
    ("Can Jefferson curls help with back pain?",
     "For stiff, deconditioned backs, gradually loading flexion often reduces pain and fear of movement. Coach Dan's own back pain returns when he stops doing them. For an injured back, talk to your doctor or physical therapist first."),
    ("Are Jefferson curls safe for people over 50?",
     "Yes for most people, with the same approach: body weight first, short range if needed, then slow progress. Skip it or get cleared first if you have osteoporosis or a recent disc injury."),
    ("Who popularized the Jefferson curl?",
     "Ben Patrick, the Knees Over Toes Guy, brought it back into the mainstream, but loaded spinal flexion goes back to old-school lifters in the 1930s."),
]

html = page(
    SLUG,
    "Are Jefferson Curls Safe? A Coach's Take | Fig Performance",
    "Are Jefferson curls safe? Coach Dan Jefferson curls 205 lb and programs them for clients over 40 with back pain. How to do them, progress, and who should wait.",
    "Are Jefferson Curls Safe? My Unpopular Opinion",
    "Fitness after 40", "Are Jefferson Curls Safe? My Unpopular Opinion",
    "I Jefferson curl 205 pounds, and my back hurts when I stop. How I teach it, how to progress, and who I hold back.",
    [("history", "Not a new exercise"), ("tested", "What I found"), ("why", "Why the rule is wrong"), ("research", "What the research says"),
     ("how", "How to do it"), ("progress", "How to progress"), ("who", "Who I hold back"), ("jonathan", "Jonathan's result"),
     ("chiro", "To the chiropractors"), ("coach", "Is it right for you?")],
    body, faqs, "Are Jefferson Curls Safe?", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
