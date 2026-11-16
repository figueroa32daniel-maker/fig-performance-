"""Article: hotel / travel workout (from Coach Dan's voice memo, Nov 15 2026). Publish only after Dan approves."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-15"
SLUG = "hotel-workout"

body = f"""<p class="legal-intro">I've trained in Switzerland, Italy, Greece, Poland, Norway, Portugal, Costa Rica and Brazil, and all over the US: Florida, Texas, North Carolina, Las Vegas, Oregon. Here's what I've learned about the "hotel workout": the gym is wherever you can find one, the workout doesn't have to be long, and the only mistake is doing nothing because the setup isn't perfect.</p>
<p>This is how I keep training when I travel, in this order: the hotel gym if there is one, a gym nearby if there isn't, bands if there's neither, and a room-only circuit as the last resort. Plus the one habit that matters more than any of it over the holidays.</p>

<h2 id="why">Why I don't skip workouts on the road</h2>
<p>We're creatures of habit. The reason I train on vacation isn't that one missed week ruins anything. It doesn't. It's that routine is what keeps you from falling off. The more consistent you are with something, the better it sticks and the better the results. Break the routine for a two-week trip and the first week back is twice as hard. Keep it, even at half the dose, and you walk back in like you never left.</p>
<p>The clients of mine who succeed the most on the road are not the ones with the best hotel gym. They're the ones who just keep the routine. That's really it. So before any trip, I give clients three things: one or two workouts a week, lots of steps (a given when you're traveling), and protein at every single meal.</p>
<p>And the workout dose is small. You only need <strong>one or two workouts a week to maintain muscle and keep your conditioning.</strong> Muscle atrophies faster than people think when you stop using it, but it takes very little to tell it to stay. One session is good enough. Two is better. Three is fantastic. On a vacation trip I'll get at least one or two. On a work trip of two weeks or more, I buy a week pass and train like I'm home.</p>
{pullquote("Twenty minutes of something is better than nothing. Messy action beats no action, every time.", "Coach Dan Figueroa")}

<h2 id="gym">Step one: use the hotel gym, if there is one</h2>
<p>If the hotel has a weight room, I use it. I don't always book the hotel with the gym, though. When I'm traveling for fun I'd rather be in the right part of town than near a treadmill, and the hotels with real gyms aren't always where I want to stay. So I don't count on it. If it's there, fantastic.</p>
<p>What makes a hotel gym usable? <strong>Dumbbells.</strong> That's the minimum. No bench, fine. A row of dumbbells that goes up to at least 25 pounds and I can get a real workout. The best case, in a hotel or anywhere, is three things:</p>
<ul>
  <li><strong>Dumbbells</strong></li>
  <li><strong>A bench</strong></li>
  <li><strong>A cable machine</strong></li>
</ul>
<p>With those three you can train every muscle in the body. A pull-up bar is a bonus. Nothing builds the upper back faster.</p>

<h2 id="nearby">Step two: find a gym nearby and buy the day pass</h2>
<p>No hotel gym, or just a treadmill in a closet? Search for a gym within a short ride and buy the day pass, or the week pass if you're there a while. It's the best money you'll spend on the trip. Even in Brazil, the nearest gym was twenty minutes away. I took an Uber.</p>
<p>One honest note: fitness isn't as big everywhere as it is in the US. In Lisbon there was one really good big gym near me and five or ten small boot-camp-style studios that didn't do walk-in memberships. So it depends on the city. Look before you go, and if the only option is a small studio with a day rate, take it.</p>

<h2 id="workout">The travel workout</h2>
<p>One full-body session, built from whatever the gym has. Pick one exercise from each line and go. Twenty minutes is plenty. An hour is not required.</p>
<ol>
  <li><strong>Push:</strong> dumbbell bench press or dumbbell overhead press</li>
  <li><strong>Squat:</strong> goblet squat or reverse lunges</li>
  <li><strong>Pull:</strong> lat pulldown, one-arm dumbbell row, or pull-ups if there's a bar</li>
  <li><strong>Core:</strong> dumbbell side bend, bent-over wood chopper, weighted sit-up, or bench leg raises</li>
  <li><strong>Carry or arms:</strong> hold the heaviest dumbbells you can find for 30 seconds to a minute (grip strength counts), or swap in arms: dumbbell curls, lateral raises, skull crushers. With cables: cable curls, rope or straight-bar pressdowns, cable overhead rows.</li>
</ol>
<p><strong>How heavy, how many reps:</strong> it depends on what's there. If the dumbbells top out at 25 pounds, go higher rep, 12 to 25 per set, and make the last few hard. If they go to 50 or more, train the way you would at home, 6 to 12 reps. Either way, you're keeping the habit and giving the muscle a reason to stay.</p>
{callout("The travel workout", "Five lines, twenty minutes", ["Push, squat, pull, core, carry or arms", "One exercise per line, 2 to 3 sets", "12 to 25 reps with light dumbbells, 6 to 12 with heavy"])}

<h2 id="bands">Step three: bands, when there's no gym at all</h2>
<p>If you want one piece of gear in your bag, make it a set of bands. They weigh nothing and they go anywhere, and even three exercises with a band keeps the routine alive. Band pull-aparts and shoulder dislocations for the upper back and shoulders. Banded push-ups and banded squats. Banded Romanian deadlifts. A booty band for glute bridges, single-leg glute bridges, kickbacks and fire hydrants.</p>
<p>It's not the same as a bar on your back. It's not supposed to be. It's three or four exercises, done, routine intact.</p>

<h2 id="room">Last resort: the room-only circuit</h2>
<p>No gym, no bands, twenty minutes, three rounds:</p>
<ol>
  <li><strong>Squat</strong> to the edge of the bed or a chair, 15 reps</li>
  <li><strong>Reverse lunges</strong>, 10 per side</li>
  <li><strong>Push-ups</strong>, hands on the floor or on the desk, 10 to 15</li>
  <li><strong>Single-leg glute bridge</strong>, 10 per side</li>
  <li><strong>Suitcase carry</strong>: pick up your actual suitcase, walk the hall and back, switch hands</li>
  <li><strong>Plank</strong>, 30 to 45 seconds</li>
</ol>

<h2 id="perfect">Stop chasing the perfect scenario</h2>
<p>Some people think that if they can't get a full hour in, it isn't worth doing. It's the opposite. A 20-minute circuit is better than nothing, and nothing is what you get when you wait for ideal. Life gets crazy. Stuff happens. You roll with it and do what you can. If I land somewhere with no gym nearby and a hotel with no weight room, I settle for band work, and I don't feel bad about it, because the point was never to be perfect. The point was to keep doing it.</p>

<h2 id="pack">What I pack</h2>
<p>Gym clothes. That's it. I train in the same walking shoes I wear to explore the city. If you pack workout clothes, you'll work out. If you don't, you've already decided not to. Bands are optional and worth it.</p>

<h2 id="protein">The habit that matters more than the workout: protein</h2>
<p>Here's the trick I figured out from traveling a lot. The workouts keep you in the routine, but <strong>protein is what protects your muscle and keeps your appetite from running the trip.</strong> Prioritize protein at every chance you get. The moment you land, before you do anything else, go to a grocery store and stock up: protein shakes, protein bars, protein snacks. Keep them in the room and in your bag.</p>
<p>Here's the simple travel version I give clients:</p>
<ul>
  <li><strong>Two protein shakes a day.</strong></li>
  <li><strong>One protein bar, or a couple of cups of Greek yogurt.</strong></li>
  <li><strong>A dinner with protein and fiber.</strong> Fish, steak, chicken, eggs, plus vegetables.</li>
</ul>
<p>That gets you to the floor I want on travel days: <strong>at least 100 grams of protein a day for men and at least 80 for women.</strong> Those are minimums, not targets. If you carry more muscle or you're heavier, your number is higher, and if you're used to eating more, stay there. Plenty of my female clients eat 100 or more. At home the rule is your goal weight in grams; on the road, hold the floor and you'll come back without having lost anything.</p>
<p>And at every meal, protein first. Vacation food is bread, pasta, dessert and drinks with a little protein on the side. Flip it. Eat the fish, the steak, the eggs first. You'll enjoy the rest more and eat less of it without trying.</p>

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
     "Use the hotel gym if it has dumbbells. If not, find a gym nearby and buy a day pass. If there's neither, bands. Last resort, a 20-minute room circuit. A full-body session of push, squat, pull, core and a carry covers everything."),
    ("How many workouts should I do while traveling?",
     "One or two a week is enough to maintain muscle and conditioning. Twenty minutes counts. On long work trips, buy a week pass and train like you're home."),
    ("What equipment does a travel gym need?",
     "Dumbbells, a bench and a cable machine cover every muscle. A pull-up bar is a bonus. Adjust reps to the weights available: 12 to 25 reps with light dumbbells, 6 to 12 with heavier ones."),
    ("Will I lose muscle if I skip the gym for a week?",
     "No. Strength and muscle hold for weeks. The risk isn't the missed week; it's breaking the routine so the first week back is twice as hard."),
    ("What should I pack to work out while traveling?",
     "Gym clothes, and optionally a set of bands, which weigh nothing and cover pull-aparts, squats, Romanian deadlifts and glute work when there's no gym. Coach Dan trains in the same walking shoes he explores in."),
    ("How much protein should I eat while traveling?",
     "At least 100 grams a day for men and 80 for women, more if you carry more muscle. Coach Dan's travel version: two protein shakes, a protein bar or a couple of Greek yogurts, and a dinner with protein and fiber. Stock up at a grocery store the day you land."),
]

html = page(
    SLUG,
    "Hotel Workout: How I Train in Any Country | Fig Performance",
    "Hotel gym, a gym nearby, bands, or a 20-minute room circuit: how Coach Dan trains on the road in any country, the travel workout, and the protein rule.",
    "Hotel Workout: How I Train in Any Country (Gym or No Gym)",
    "Fitness after 40", "The Hotel Workout, From Someone Who Travels a Lot",
    "Hotel gym, gym nearby, bands, or a room circuit. Twenty minutes beats nothing, and one or two sessions a week keeps the routine alive.",
    [("why", "Why I don't skip"), ("gym", "The hotel gym"), ("nearby", "A gym nearby"), ("workout", "The travel workout"), ("bands", "Bands"),
     ("room", "Room-only circuit"), ("perfect", "Stop chasing perfect"), ("pack", "What I pack"), ("protein", "Protein on the road"), ("holidays", "Holiday travel"), ("coach", "When you get home")],
    body, faqs, "Hotel Workout", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
