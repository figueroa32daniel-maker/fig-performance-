"""Article: hotel / travel workout (from Coach Dan's voice memo, Nov 15 2026). Publish only after Dan approves."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-15"
SLUG = "hotel-workout"

body = f"""<p class="legal-intro">I've trained in Switzerland, Italy, Greece, Poland, Norway, Costa Rica and Brazil, and all over the US: Florida, Texas, North Carolina, Las Vegas, Oregon. Here's the thing nobody tells you about the "hotel workout": the best one is usually not in your hotel. It's at the gym down the street, and there is always a gym down the street.</p>
<p>This is how I keep training when I travel, what I look for in a gym, the workout I do when the equipment is limited, a room-only fallback for when there's truly nothing nearby, and the one habit that matters more than any of it over the holidays.</p>

<h2 id="why">Why I don't skip workouts on the road</h2>
<p>We're creatures of habit. The reason I train on vacation isn't that one missed week ruins anything. It doesn't. It's that routine is what keeps you from falling off. The more consistent you are with something, the better it sticks and the better the results. Break the routine for a two-week trip and the first week back is twice as hard. Keep it, even at half the dose, and you walk back into the gym like you never left.</p>
<p>So the target is low and non-negotiable: <strong>one or two workouts a week while traveling.</strong> One is good enough. Two is better. Three is fantastic. On a vacation trip I'll get at least one or two. On a longer work trip, two weeks or more, I buy a week pass and train like I'm home.</p>
{pullquote("Even in Brazil, the nearest gym was twenty minutes away. I took an Uber. Routine is worth a twenty-minute ride.", "Coach Dan Figueroa")}

<h2 id="gym">Step one: find a gym and buy the day pass</h2>
<p>Before you work out in a hotel room with a towel and a chair, search for a gym within a short ride of where you're staying. There's almost always one. Buy the day pass, or the week pass if you're there a while. It's the best money you'll spend on the trip.</p>
<p>You don't need a fancy gym. Here's my whole checklist:</p>
<ul>
  <li><strong>Dumbbells</strong></li>
  <li><strong>A bench</strong></li>
  <li><strong>A cable machine</strong></li>
  <li><strong>A pull-up bar</strong> is a bonus, not a requirement</li>
</ul>
<p>That's it. With dumbbells, a bench and cables you can train every muscle in the body, and the cable machine alone covers a dozen exercises. If a gym has those three things, you're set.</p>

<h2 id="workout">The travel gym workout</h2>
<p>One full-body session, built from what every small gym has. Pick six to eight of these, one or two per movement, and go:</p>
<p><strong>Push</strong></p>
<ul>
  <li>Dumbbell bench press</li>
  <li>Dumbbell lateral raises</li>
  <li>Cable triceps pressdown</li>
</ul>
<p><strong>Pull</strong></p>
<ul>
  <li>Chest-supported dumbbell row</li>
  <li>Cable reverse fly</li>
  <li>Cable curl</li>
  <li>Pull-ups, if there's a bar and you've got the strength. Nothing builds the upper back faster.</li>
</ul>
<p><strong>Legs</strong></p>
<ul>
  <li>Dumbbell goblet squat</li>
  <li>Reverse lunges</li>
  <li>Single-leg glute bridge</li>
</ul>
<p><strong>Core</strong></p>
<ul>
  <li>Cable crunches</li>
  <li>Bench leg raises</li>
</ul>
<p><strong>How heavy, how many reps:</strong> it depends on what the gym has. If the dumbbells only go up to 25 pounds, go higher rep, 12 to 25 per set, and make the last few hard. If they go up to 50 or more, train the way you would at home, 6 to 12 reps. Either way, you're keeping the habit and giving the muscle a reason to stay.</p>
{callout("The travel gym checklist", "All you need", ["Dumbbells, a bench, a cable machine", "A pull-up bar if you're lucky", "A day pass or a week pass", "One or two sessions a week, full body"])}

<h2 id="room">If there's truly no gym: the room-only fallback</h2>
<p>Rare, but it happens. Twenty minutes, no equipment, three rounds:</p>
<ol>
  <li><strong>Squat</strong> to the edge of the bed or a chair, 15 reps</li>
  <li><strong>Reverse lunges</strong>, 10 per side</li>
  <li><strong>Push-ups</strong>, hands on the floor or on the desk, 10 to 15</li>
  <li><strong>Single-leg glute bridge</strong>, 10 per side</li>
  <li><strong>Suitcase carry</strong>: pick up your actual suitcase, walk the hall and back, switch hands</li>
  <li><strong>Plank</strong>, 30 to 45 seconds</li>
</ol>
<p>It's not a replacement for lifting. It's a placeholder that keeps the routine alive until you're back under a bar.</p>

<h2 id="pack">What I pack</h2>
<p>Gym clothes. That's it. Nothing crazy, no bands, no gadgets. I train in the same walking shoes I wear to explore the city. If you pack workout clothes, you'll work out. If you don't, you've already decided not to.</p>

<h2 id="protein">The habit that matters more than the workout: protein</h2>
<p>Here's the trick I figured out from traveling a lot. The workouts keep you in the routine, but <strong>protein is what protects your muscle and keeps your appetite from running the trip.</strong> Prioritize protein at every chance you get. The moment you land, before you do anything else, go to a grocery store and stock up: protein shakes, protein bars, protein snacks. Keep them in the room and in your bag.</p>
<p>Then at every meal, protein first. Vacation food is bread, pasta, dessert and drinks with a little protein on the side. Flip it. Eat the fish, the steak, the eggs first. You'll enjoy the rest more and eat less of it without trying.</p>
<p>The rule I give clients: your goal weight in grams of protein a day, even on vacation. Want to weigh 170? Aim for about 170 grams. The shakes and bars make it possible on a travel day when meals are unpredictable.</p>

<h2 id="holidays">Holiday travel specifically</h2>
<p>Everything above applies, plus three things, because the holidays stack food, alcohol and no movement for two or three weeks straight:</p>
<ol>
  <li><strong>Walk.</strong> Airports, downtowns, the neighborhood after dinner. A long walk every day is the most valuable thing you can do on a travel day, and it gets you out of the house.</li>
  <li><strong>Pick your drinking nights.</strong> Two or three, not every night. Alcohol is the thing that stacks up fastest over a holiday week, and it wrecks the sleep you need to recover.</li>
  <li><strong>Book the first session back before you leave.</strong> The trip ends; the routine doesn't. Having a time on the calendar is what makes that true.</li>
</ol>

<h2 id="coach">When you get home</h2>
<p>Your first session back feels rusty for about one workout. Don't make up for lost time by going heavier than you left off. Pick up where you were, and by the second session you're back. If you've been meaning to start a real plan and the holidays are the excuse, come in for a free consult when you're home. We'll do an InBody scan and build the routine that travels with you.</p>
<p>Fig Performance is a <a href="/">private one-on-one personal training gym in Placentia</a>, serving Yorba Linda, Brea, Fullerton and Anaheim Hills. Related: <a href="/how-to-avoid-holiday-weight-gain">how to avoid holiday weight gain after 40</a>, the <a href="/3-day-beginner-workout-plan">3-day beginner workout plan</a> and <a href="/online-personal-trainer">online coaching</a>, which comes with you wherever you go.</p>
<p><em>Check with your doctor before starting a new exercise program, especially if you have a heart condition or a recent injury or surgery.</em></p>
{CTA}"""

faqs = [
    ("What's the best hotel workout?",
     "The gym near your hotel. Coach Dan searches for a gym within a short ride, buys a day or week pass, and trains with dumbbells, a bench and a cable machine. A room-only bodyweight circuit is the fallback when there's truly no gym nearby."),
    ("How many workouts should I do while traveling?",
     "One or two a week keeps the routine alive. One is good enough, two is better, three is fantastic. On long work trips, buy a week pass and train like you're home."),
    ("What equipment does a travel gym need?",
     "Dumbbells, a bench and a cable machine cover every muscle. A pull-up bar is a bonus. Adjust reps to the weights available: 12 to 25 reps with light dumbbells, 6 to 12 with heavier ones."),
    ("Will I lose muscle if I skip the gym for a week?",
     "No. Strength and muscle hold for weeks. The risk isn't the missed week; it's breaking the routine so the first week back is twice as hard."),
    ("What should I pack to work out while traveling?",
     "Gym clothes. Coach Dan trains in the same walking shoes he explores in. No bands or gadgets required."),
    ("How do I eat healthy while traveling?",
     "Protein first at every meal, and stock up on protein shakes, bars and snacks at a grocery store as soon as you arrive. Aim for your goal weight in grams of protein a day, even on vacation."),
]

html = page(
    SLUG,
    "Hotel Workout: How I Train in Any Country | Fig Performance",
    "The best hotel workout is the gym down the street. How Coach Dan trains on the road, the dumbbell-and-cable session, a room-only fallback, and the protein rule.",
    "Hotel Workout: How I Train in Any Country (and Why It's Usually Not in the Hotel)",
    "Fitness after 40", "The Hotel Workout, From Someone Who Travels a Lot",
    "Find the gym, buy the day pass, pack gym clothes, stock up on protein. One or two sessions a week keeps the routine alive.",
    [("why", "Why I don't skip"), ("gym", "Find a gym"), ("workout", "The travel workout"), ("room", "Room-only fallback"),
     ("pack", "What I pack"), ("protein", "Protein on the road"), ("holidays", "Holiday travel"), ("coach", "When you get home")],
    body, faqs, "Hotel Workout", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
