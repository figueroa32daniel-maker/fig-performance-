"""Article: tib raises (from Coach Dan's voice answers, Nov 3 2026)."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-03"
SLUG = "tib-raises"

body = f"""<p class="legal-intro">Tib raises strengthen the tibialis anterior, the muscle on the front of your shin that lifts your toes every time you take a step. Strong tibs help absorb shock when you walk, run and jump, help protect your knees, and can help with shin splints. Almost nobody trains them. Here's why you should, and exactly how to do them.</p>

<h2 id="what">What your tibialis does</h2>
<p>Your tibialis anterior pulls your toes up toward your shin. It keeps your toes from dragging and catching when you walk, and it controls your foot as it lands. That makes it one of your body's shock absorbers. When your foot hits the ground, your feet take the load first and your tibs are next, before your knees, quads and hamstrings.</p>
<p>So if your tibs and shins are strong, your knees take less of a beating, whether you're chasing the kids around Disneyland, playing a round of golf, hiking with friends, or walking all day through Italy, Spain or Portugal.</p>

<h2 id="shin-splints">Tib raises and shin splints</h2>
<p>If you walk or run to keep your heart healthy, especially as you get older, you've probably felt shin pain at some point. Shin splints are linked to overloaded, irritated muscles along the shin.</p>
<p>Here's what I've seen in 15 years of training: a tight muscle is often a weak muscle. Stretching gives you a little more range of motion for a while, but it doesn't fix the root problem. The muscle gets tight, overworked and inflamed because it isn't strong enough for the amount of walking, running or jumping you're asking it to do. Make it stronger and it can handle the load.</p>
<p>The research on shin splints is still mixed, and shin pain has more than one cause. If you have sharp pain in one spot, pain that gets worse every time you run, or pain at night, see a doctor to rule out a stress fracture.</p>

<h2 id="how">How to do a wall tib raise</h2>
<ol>
  <li>Stand with your back and hips against a wall.</li>
  <li>Walk your feet out about a foot in front of you, keeping your legs straight.</li>
  <li>Keep your heels on the ground and lift your toes as high as you can toward your shins.</li>
  <li>Lower them slowly, without letting them slap the floor.</li>
</ol>
<p>The farther your feet are from the wall, the harder it gets.</p>

<h2 id="variations">Tib raise variations</h2>
<ul>
  <li><strong>Wall tib raise:</strong> the easiest place to start. No equipment.</li>
  <li><strong>Kettlebell toe raise:</strong> my favorite. Sit on a bench, hook a light kettlebell over the toes of one foot, and pull your toes up toward your shin. It's very effective.</li>
  <li><strong>Kettlebell tib raise:</strong> sit on a box with a kettlebell hanging from your feet and lift it by pulling your toes up.</li>
  <li><strong>Tib bar:</strong> a bar that straps onto your feet so you can load the movement with weight plates.</li>
  <li><strong>The tib machine:</strong> at Fig Performance we have a machine that trains both tibs at the same time. It's fantastic.</li>
</ul>

<h2 id="reps">Sets and reps</h2>
<p>The tibialis is a muscle like any other, so train it with a range of reps:</p>
<ul>
  <li><strong>Heavy:</strong> 5 to 10 reps, with a kettlebell, tib bar or the tib machine.</li>
  <li><strong>Most sets:</strong> 12 to 20 reps.</li>
  <li><strong>Endurance:</strong> 25 to 30 reps, great with wall tib raises.</li>
</ul>
{stats([("5&ndash;10", "reps when it's heavy"), ("12&ndash;20", "reps for most sets"), ("25&ndash;30", "reps for endurance")])}
<p>Do 2 or 3 sets, 2 or 3 times a week. Start with wall tib raises, then add weight as they get easy. You'll feel the burn fast. That's normal.</p>

<h2 id="plans">Where tib raises fit in your training</h2>
<p>Add them at the end of a leg day, or as part of your warm-up before walking or running. They're built into the <a href="/beginner-workout-plan-for-men">beginner workout plan for men</a>, and you can add them to the <a href="/beginner-workout-plan-for-women">women's plan</a> too.</p>
<p>Dealing with knee or shin pain? At Fig Performance in Placentia, every plan starts with a free consult and an assessment of your knees, hips, ankles and how you walk, so we can find the root cause.</p>
{CTA}"""

faqs = [
    ("What are tib raises good for?",
     "Tib raises strengthen the tibialis anterior on the front of your shin. That helps your feet absorb shock, keeps your toes from catching when you walk, helps protect your knees, and can help with shin pain."),
    ("Do tib raises help shin splints?",
     "They can. In Coach Dan's experience, shin pain often comes from muscles that aren't strong enough for the load, and stretching alone doesn't fix that. The research is still mixed, so see a doctor for sharp, worsening or night pain."),
    ("How many tib raises should I do?",
     "2 to 3 sets, 2 to 3 times a week. Use 5 to 10 reps when it's heavy, 12 to 20 for most sets, and 25 to 30 for endurance."),
    ("How do you do a wall tib raise?",
     "Stand with your back against a wall and your feet about a foot in front of you. Keep your heels down, lift your toes as high as you can, then lower them slowly."),
    ("What's the best tib raise exercise?",
     "Start with wall tib raises. Coach Dan's favorite is a seated kettlebell toe raise, with a light kettlebell hooked over the toes. A tib bar or tib machine lets you load it heavier."),
]

html = page(
    SLUG,
    "Tib Raises: Benefits, How-To, Sets and Reps | Fig Performance",
    "Tib raises strengthen your shins, help absorb shock, protect your knees and can help shin splints. How to do wall tib raises, variations, sets and reps.",
    "Tib Raises: Why Your Shins Need Strength, and How to Train Them",
    "Fitness after 40", "Tib Raises: Benefits, How-To, Sets and Reps",
    "The muscle almost nobody trains, and why it matters for your knees, shins and every step you take.",
    [("what", "What your tibialis does"), ("shin-splints", "Tib raises and shin splints"), ("how", "How to do a wall tib raise"),
     ("variations", "Variations"), ("reps", "Sets and reps"), ("plans", "Where they fit")],
    body, faqs, "Tib Raises", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
