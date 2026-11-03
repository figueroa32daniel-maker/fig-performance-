"""Article: How to avoid holiday weight gain after 40 (Nov 2026, seasonal)."""
from build_pages import page, SITE, CTA

DATE = "2026-11-03"
SLUG = "how-to-avoid-holiday-weight-gain"
STUDY = "https://pubmed.ncbi.nlm.nih.gov/10727591/"

body = f"""<p class="legal-intro">To avoid holiday weight gain, don't try to lose weight between Thanksgiving and New Year's. Aim to hold steady: keep your daily steps up, keep two strength sessions a week, eat protein first, go easy on the drinks, and get back to normal at your very next meal. The holidays are a handful of days, not six weeks.</p>

<h2 id="why">Why the holidays matter more than one pound</h2>
<p>In a well-known study in the <em>New England Journal of Medicine</em>, adults gained on average a little under a pound over the holiday season, and most of them hadn't lost it by the next fall (<a href="{STUDY}" target="_blank" rel="noopener noreferrer">Yanovski et al., 2000</a>). One pound sounds like nothing. But after 40, when muscle is easier to lose and a desk job keeps you sitting, a pound a year adds up to 10 pounds a decade. The people in that study who reported being more active gained less.</p>
<p>So the goal for the next six weeks is simple: <strong>maintain</strong>. If you come out of New Year's at the same weight, with the same strength, you're ahead of most people.</p>

<h2 id="plan">9 ways to avoid holiday weight gain</h2>

<h3>1. Aim to maintain, not lose</h3>
<p>Trying to diet through December usually backfires. You feel deprived at every party, then overdo it. Eat at maintenance on normal days and enjoy the actual holiday meals without guilt.</p>

<h3>2. Keep your daily steps up</h3>
<p>Coach Dan's target for clients over 40 is more than 5,000 steps a day, and ideally 6,000 or more. Everyday movement burns more calories than most people realize, and it's the first thing to disappear when it's cold, dark and busy. Walk after the big meal. Park farther away. Take calls on your feet.</p>

<h3>3. Don't drop your strength training</h3>
<p>Two sessions a week is enough to keep your muscle and your progress through the holidays. Muscle keeps your metabolism up, so this is the habit to protect. If your week gets packed, shorten the sessions instead of skipping them.</p>

<h3>4. Eat protein first</h3>
<p>Start every plate with protein: turkey, ham, roast, shrimp, eggs. Protein fills you up and helps you keep muscle. You'll naturally eat less of the stuff that's easy to overdo.</p>

<h3>5. Treat the holiday as a day, not a season</h3>
<p>Thanksgiving is one day. Christmas Eve and Christmas are two. The office party is one evening. Enjoy those, then go back to your normal meals in between. Having a few go-to options for regular days, like breakfast A or B and lunch A or B, makes that easy because you don't have to think about it.</p>

<h3>6. Go easy on the drinks</h3>
<p>Alcohol is where a lot of holiday calories hide, and it makes late-night snacking more likely. Decide how many drinks you'll have before you get there, and have a glass of water between each one.</p>

<h3>7. Don't skip meals to "save up"</h3>
<p>Showing up to a party starving is how one plate turns into three. Eat a normal, protein-heavy meal earlier in the day.</p>

<h3>8. Protect your sleep</h3>
<p>Late nights make you hungrier and less likely to train the next day. Keep your wake-up time steady, even when bedtime moves.</p>

<h3>9. Get back on plan at the next meal</h3>
<p>One big meal doesn't undo your progress, and the scale jump the next morning is mostly water and salt. Don't wait for Monday or January. Your next meal is the fresh start.</p>

<h2 id="travel">Traveling? A 20-minute hotel workout</h2>
<p>No gym needed. Do 3 rounds, resting about a minute between rounds:</p>
<ul>
  <li>Bodyweight squats or split squats: 10 to 15 reps (each leg for split squats)</li>
  <li>Push-ups, on the floor or with hands on the bed or a desk: 8 to 15 reps</li>
  <li>Glute bridges: 15 reps</li>
  <li>Plank: 20 to 40 seconds</li>
  <li>Reverse lunges: 8 to 10 reps each leg</li>
</ul>
<p>Then go for a walk. Stop anything that causes pain, and check with your doctor first if you have a medical condition or recent injury.</p>

<h2 id="january">Start before January</h2>
<p>Most people wait for January 1st, start too hard, and quit by February. If you start now, you walk into the new year already in a routine. At Fig Performance in Placentia, every client starts with a free consult and an <a href="/inbody-scan-placentia">InBody scan</a>, so you know your real body fat and muscle before the holidays and can see what changed after. Read more in <a href="/how-to-lose-weight-after-40">how to lose weight after 40</a> and <a href="/nutrition-coaching-placentia">how nutrition coaching works</a>.</p>
{CTA}"""

faqs = [
    ("How much weight do people gain over the holidays?",
     "Less than most people think. A study in the New England Journal of Medicine found adults gained a little under a pound on average over the holiday season. The problem is most didn't lose it afterward, so it adds up year after year."),
    ("How do I avoid gaining weight over the holidays?",
     "Aim to maintain rather than lose. Keep your daily steps above 5,000 (ideally 6,000 or more), keep two strength sessions a week, eat protein first, limit drinks, and go back to your normal meals right after each holiday meal."),
    ("Is it better to start a diet now or wait until January?",
     "Start building habits now. Aim to hold your weight through the holidays while you keep training, so you start January already in a routine instead of starting from scratch."),
    ("Will one big holiday meal make me gain weight?",
     "Not much fat. The scale jump the next morning is mostly water and salt. Go back to your normal eating at your next meal and it usually comes back down within a few days."),
    ("How can I work out while traveling for the holidays?",
     "Do a 20-minute bodyweight circuit in your room: squats or split squats, push-ups, glute bridges, a plank and reverse lunges, 3 rounds. Then go for a walk."),
]

html = page(
    SLUG,
    "How to Avoid Holiday Weight Gain After 40 | Fig Performance",
    "How to avoid holiday weight gain after 40: aim to maintain, keep your steps and strength training, eat protein first, and a 20-minute hotel workout.",
    "How to Avoid Holiday Weight Gain (After 40)",
    "Fitness after 40", "How to Avoid Holiday Weight Gain After 40",
    "Hold steady from Thanksgiving to New Year's, without skipping the good parts.",
    [("why", "Why it matters"), ("plan", "9 ways to avoid it"), ("travel", "20-minute hotel workout"), ("january", "Start before January")],
    body, faqs, "Holiday Weight Gain", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
