"""Article: hip thrust form and programming for women over 40 (from Coach Dan's voice memo, Nov 7 2026). Publish only after Dan approves."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-07"
SLUG = "hip-thrust"
EMG = "https://doi.org/10.1123/jab.2014-0301"
PLOTKIN = "https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2023.1279170"

body = f"""<p class="legal-intro">This past August I spent three days in Fort Lauderdale at a seminar run by Bret Contreras, the coach who invented the barbell hip thrust. Three days of current research, technique, programming, and the machines he's built for his own gym. I came home with a notebook full of changes to how I coach the glutes, and this article is most of it.</p>
<p>The hip thrust is the one exercise I wish every woman over 40 had been taught at 30. It builds the glutes directly, it's easier on the knees and back than a squat, and it's the single best fix I know for the posterior chain that years of sitting shut down. Here's how to set it up, the mistakes I fix every week, and how I program it.</p>

<h2 id="why">Why the glutes, and why now</h2>
<p>The glutes are the muscle group you most want strong and well developed after 40, and I mean that for two reasons that matter equally. Posterior chain strength is longevity: it's how you get up from a chair at 75, climb stairs without a rail, and protect your knees and lower back in everything else you do. And it's aesthetics. Nobody's embarrassed about that, and they shouldn't be. Rebuilding the glutes is the fastest visible change most women get from lifting.</p>
<p>The hip thrust does both faster than anything else because, as Bret has shown and I've watched in my gym, it's very easy to scale. You can add weight almost every session for months. That builds confidence as fast as it builds muscle.</p>

<h2 id="setup">The setup: get these four things right</h2>
<ol>
  <li><strong>The bench.</strong> 12 to 24 inches high. An adjustable bench works. I use a hip thrust box; a 12-inch plyo box is fine. Your shoulder blades rest on the edge, not your whole back and not just your neck. Too much back on the bench or too little is the first thing I fix on almost everyone.</li>
  <li><strong>The bar.</strong> It sits right above your hip bone, at the crease of your hips. Use a pad. A 2- to 4-inch bar pad to start, and as the weight goes up, a thick balance pad, because the heavier you go the more the bar digs in. Hip bone pain is the number one reason people quit this exercise, and it's completely avoidable.</li>
  <li><strong>Your feet.</strong> Position them so that at the top of the rep your knees are bent at 90 degrees, shins vertical. Too far out and it becomes a hamstring exercise.</li>
  <li><strong>A deadlift jack.</strong> Not required, but if you set up your own bar, a deadlift jack lets you slide plates on and off in seconds. It's the most useful accessory for this lift.</li>
</ol>

<h2 id="how">How to do the hip thrust</h2>
<ol>
  <li>Sit on the floor with your shoulder blades against the bench and the bar across your hips.</li>
  <li>Brace your core. Tuck your chin slightly so your eyes stay forward, not at the ceiling.</li>
  <li>Drive through your heels and thrust up until your hips are fully extended: a straight line from shoulders to knees, knees at 90 degrees.</li>
  <li>Squeeze the glutes hard at the top.</li>
  <li>Lower under control and go again. Push up with power. The way down can be quicker; more on that below.</li>
</ol>
<p>My own rule, and it's a little different from how most people coach it: <strong>squeeze the glutes the whole rep, down and up.</strong> Bret is right that there's very little tension on the glutes at the bottom. But I want you to keep the connection the whole time. That mind-to-muscle connection is a big part of what makes a muscle grow, and it's a habit I want on every exercise, not just this one.</p>

<h2 id="power">Power up, don't crawl down</h2>
<p>One thing I changed after the seminar. At the bottom of a hip thrust the glutes lose most of their tension, so there's no reason to lower the bar in slow motion. Bret's cue is to focus on exploding upward with force and not worry about a slow negative. He coaches the deadlift the same way. The power on the way up is what matters.</p>
<p>That's also why some women do better with a shorter version: pulsing in the top half of the rep instead of coming all the way down, so the glutes stay under tension the entire set. If full-range reps aren't giving you the burn where you want it, try it.</p>
{pullquote("Lower the weight, find what full hip extension actually looks like, and work your hip mobility. More range means more glute, and faster results.", "Coach Dan Figueroa")}

<h2 id="mistakes">The mistakes I fix most</h2>
<ul>
  <li><strong>Spine position on the bench.</strong> Too much back on the bench, or not enough. Shoulder blades on the edge, chin tucked, ribs down.</li>
  <li><strong>Not reaching full hip extension.</strong> This is the big one. A lot of women have never tested how much hip extension they actually have, so they thrust up to where it feels normal and stop short. It's like doing a curl and never reaching the top. Lower the weight, find what full extension looks like, and work on your hip mobility, especially your hip flexors. More range means more glute fibers working, a more efficient rep, and faster results.</li>
  <li><strong>Feet in the wrong place.</strong> Knees should be at 90 degrees at the top. Adjust until they are.</li>
  <li><strong>Arching the lower back to fake the top.</strong> Ribs down, squeeze the glutes, don't arch.</li>
</ul>

<h2 id="beginner">How I start a beginner</h2>
<p>With the barbell. Not a dumbbell, not a bodyweight bridge for weeks. I had a client start with the empty bar and a 5-pound plate on each side, 55 pounds total. About a month and a half later she was hip thrusting 135 pounds.</p>
{stats([("55 lb", "where she started"), ("135 lb", "six weeks later"), ("3&times;", "a week, on leg days")])}
<p>That's not unusual. You can't load a dumbbell glute bridge or a single-leg hip thrust anywhere near what you can load a barbell, and the barbell is the most accessible option because not everyone has a hip thrust machine. Yes, it's more setup than most exercises. That's one of the things a coach is for.</p>

<h2 id="program">How I program the glutes now</h2>
<p>This is the part that changed most after Fort Lauderdale. Bret's recommendation for women who want to build the glutes is roughly <strong>32 working sets a week for the legs</strong>, structured like this. Everybody's different, but this is the template I'm using:</p>
<p><strong>Three leg days a week (Monday, Wednesday, Friday), four exercises each:</strong></p>
<ol>
  <li><strong>Hip thrust.</strong> Every leg day.</li>
  <li><strong>A squat pattern.</strong> Both legs or single leg: barbell back squat, Bulgarian split squat, or sumo leg press.</li>
  <li><strong>A hinge.</strong> Barbell Romanian deadlift, single-leg deadlift, or back extension.</li>
  <li><strong>Abduction, to finish every workout.</strong> Band, cable or machine. I use the machine most because it's the fastest to set up. Cable abduction is the one people skip and shouldn't: it trains each side on its own, and you'll feel right away if one hip is weaker. And I still do a lot of band work. Bret's been recommending bands for about twenty years, and he still does.</li>
</ol>
<p><strong>Two upper body days:</strong> one for chest, back and shoulders; one for back and arms.</p>
{callout("The weekly template", "Glutes, three days a week", ["Mon / Wed / Fri: hip thrust, a squat pattern, a hinge, then abduction", "Two upper body days: chest, back and shoulders; back and arms", "About 32 working sets a week for the legs"])}
<p><strong>Reps:</strong> for a new client I run the hip thrust the way I run most lifts: 8 to 10 reps per set the first month, then 5 to 6 with more weight, then heavier still. The rest of the leg day lives in the 8 to 12 range. Add weight whenever the form holds.</p>

<h2 id="vs">Hip thrust vs. squat</h2>
<p>People ask which is better for the glutes. Both work. A 2015 EMG study found the barbell hip thrust activated the glutes much more than a back squat at the same relative load (<a href="{EMG}" target="_blank" rel="noopener noreferrer">Contreras et al., 2015</a>). A 2023 training study that followed people for nine weeks found squats and hip thrusts built similar glute size, with squats adding more quad and inner-thigh size (<a href="{PLOTKIN}" target="_blank" rel="noopener noreferrer">Plotkin et al., 2023</a>). That's why the template above has both: a squat pattern and a hip thrust on every leg day. The hip thrust lets you load the glutes hard without your spine or knees being the limit, which is exactly what a 50-year-old with a cranky back needs.</p>

<h2 id="coach">Start here</h2>
<p>If you've never hip thrusted, set up a bench and the empty bar, find full hip extension with no weight first, then add 5 pounds a side. If you want someone to set up the bar and watch your form, that's what the free consult is for.</p>
<p>Fig Performance is a <a href="/">private one-on-one personal training gym in Placentia</a>, serving Yorba Linda, Brea, Fullerton and Anaheim Hills. Related: <a href="/strength-training-for-women-over-50">strength training for women over 50</a>, <a href="/strength-training-for-women-over-40">strength training for women over 40</a> and <a href="/how-to-lose-belly-fat-after-menopause">how to lose belly fat after menopause</a>. Can't make it in person? Try <a href="/online-personal-trainer">online coaching</a>.</p>
<p><em>Check with your doctor before starting a new exercise program, especially if you have a hip or back injury or a recent surgery.</em></p>
{CTA}"""

faqs = [
    ("What muscles do hip thrusts work?",
     "Mainly the gluteus maximus, with the hamstrings assisting."),
    ("How heavy should a woman hip thrust?",
     "Start with the empty bar plus 5 pounds a side. Many women reach 135 pounds within two months; the glutes are strong and this lift scales fast."),
    ("Where should the bar sit for hip thrusts?",
     "Right above the hip bone, at the hip crease, with a thick pad. Hip bone pain is the top reason people quit, and a balance pad fixes it."),
    ("How high should the bench be for hip thrusts?",
     "12 to 24 inches. A 12-inch plyo box or an adjustable bench works. Shoulder blades on the edge, not your whole back."),
    ("Should I lower slowly on hip thrusts?",
     "No. There's little glute tension at the bottom, so focus on driving up with power. Coach Dan still cues a glute squeeze through the whole rep for mind-to-muscle connection."),
    ("How often should I do hip thrusts?",
     "Three times a week on leg days, alongside a squat pattern, a hinge and an abduction exercise, following Bret Contreras's programming for women building the glutes."),
]

html = page(
    SLUG,
    "Hip Thrust Form for Women Over 40 | Fig Performance",
    "Hip thrust form from a coach who trained with Bret Contreras: bench height, bar placement, the mistakes to fix, and a 3-day glute program for women over 40.",
    "Hip Thrust Form: How to Do It and Why Women Over 40 Need It",
    "Fitness after 40", "Hip Thrust Form: How to Do It and Why Women Over 40 Need It",
    "What I learned from the coach who invented the hip thrust, and how I program it for women over 40.",
    [("why", "Why the glutes"), ("setup", "The setup"), ("how", "How to do it"), ("power", "Power up"),
     ("mistakes", "Mistakes I fix"), ("beginner", "Starting a beginner"), ("program", "The weekly program"),
     ("vs", "Hip thrust vs. squat"), ("coach", "Start here")],
    body, faqs, "Hip Thrust Form", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
