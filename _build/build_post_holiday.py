"""Article: How to avoid holiday weight gain after 40 (from Coach Dan's answers, Nov 3 2026)."""
from build_pages import page, SITE, CTA

DATE = "2026-11-03"
SLUG = "how-to-avoid-holiday-weight-gain"
STUDY = "https://pubmed.ncbi.nlm.nih.gov/10727591/"

body = f"""<p class="legal-intro">To avoid holiday weight gain: eat protein first, fill up on vegetables, leave room for the dessert you actually want, keep training, and go easy on the drinks. Most of all, keep the holidays to the holidays. Thanksgiving is a couple of days, not all of November. Here's exactly what I tell my clients over 40, and what I do myself.</p>

<h2 id="why">Why the holidays matter more than one pound</h2>
<p>In a well-known study in the <em>New England Journal of Medicine</em>, adults gained a little under a pound on average over the holiday season, and most of them still hadn't lost it by the next fall (<a href="{STUDY}" target="_blank" rel="noopener noreferrer">Yanovski et al., 2000</a>). One pound sounds like nothing. But after 40, when muscle is easier to lose and a desk job keeps you sitting, a pound a year turns into 10 pounds a decade. The people in that study who were more active gained less.</p>

<h2 id="mindset">Live a little, but act like you have goals</h2>
<p>The holidays are for family. We use food to bond with the people we love, and there's nothing wrong with that. Live a little.</p>
<p>But if you have goals, you have to act in accordance with those goals. That doesn't mean skipping the meal or saying no to dessert. It means you decide what matters to you before you sit down, instead of letting the table decide for you.</p>

<h2 id="plate">How to build your holiday plate</h2>
<p>This is what I tell every client before Thanksgiving: <strong>protein first, as much as you can.</strong> Then your vegetables and fiber. Protein and fiber fill you up fast, so you naturally have less room for the stuff that doesn't support your goals.</p>
<p>The clients who get through the holidays well do exactly that. Most of their plate is protein, and the rest is vegetables. They skip the rolls and the stuffing on purpose, to save room for a piece of pie.</p>
<p>That's how I eat too. At family dinner I stack up on protein and vegetables, add a little bit of carbs, and leave room for dessert. I don't skip dessert. I like dessert.</p>

<h2 id="eighty-twenty">Why I eat 80/20, even in December</h2>
<p>My diet is 80/20: about 80% clean, nutrient-dense food, and 20% food I just enjoy. For your nutrition to be sustainable, it has to be flexible, and it has to be enjoyable. If your plan doesn't have room for your mom's pie, you won't stick to it. Build the pie in.</p>

<h2 id="training">I still train on Thanksgiving</h2>
<p>I train on Thanksgiving Day. You have to have balance: if you're going to eat that much food, balance it out with some exercise. On Christmas morning, I'll train if I have time. But spending time with family comes first.</p>
<p>The rest of the season, keep your normal training (new to it? try a 3-day plan for <a href="/beginner-workout-plan-for-women">women</a> or <a href="/beginner-workout-plan-for-men">men</a>) and your daily walking. For my clients over 40 that's usually two strength sessions a week and more than 5,000 steps a day, ideally 6,000 or more. If your week gets packed, shorten the sessions instead of skipping them.</p>

<h2 id="mistakes">The biggest holiday mistakes I see after 40</h2>
<h3>1. Drinking way too much</h3>
<p>This is the big one. Drinking every weekend leading up to Thanksgiving, and every weekend after, all the way through New Year's. Alcohol adds a lot of calories, wrecks your sleep, and makes late-night snacking more likely. Set hard boundaries before the season starts: which nights you'll drink, and how much.</p>
<h3>2. Dragging the holidays out for weeks</h3>
<p>Thanksgiving is a couple of days. Christmas is a couple of days. Give each one a week at most, then move on. It's not supposed to be two months of holiday food, drinking and poor habits. Everybody's doing great in October, then they have no boundaries for eight weeks, and they're upset about their holiday weight in January.</p>
<h3>3. Giving in to peer pressure</h3>
<p>Somebody will say, "Come on, live a little, it's the holidays." You're allowed to say no. If you have goals, you need personal boundaries, and you need the self-control to stick to them. Have discipline. Be firm.</p>

<h2 id="travel">Traveling for the holidays</h2>
<p>When my clients travel, I give them a program they can do in a hotel room. I tell them to get as much movement as they can, keep prioritizing protein and fiber, and bring their supplements so they're still getting their micronutrients. If they need support, they message me.</p>
<p>Here's a simple 20-minute version you can do anywhere. Do 3 rounds, resting about a minute between rounds:</p>
<ul>
  <li>Bodyweight squats or split squats: 10 to 15 reps (each leg for split squats)</li>
  <li>Push-ups, on the floor or with hands on the bed or a desk: 8 to 15 reps</li>
  <li>Glute bridges: 15 reps</li>
  <li>Plank: 20 to 40 seconds</li>
  <li>Reverse lunges: 8 to 10 reps each leg</li>
</ul>
<p>Then go for a walk. Stop anything that causes pain, and check with your doctor first if you have a medical condition or a recent injury.</p>

<h2 id="january">Why you shouldn't wait for January</h2>
<p>Habits take time to build. If you wait for January 1st, you're starting from zero.</p>
<p>November and December are the hardest months of the year. It's cold, it's raining, everyone's busy and stressed, you're shopping and traveling. If you learn to stay on track now, when it's hard, it gets easy when things calm down. You learn discipline, self-control and how to set boundaries, and by the time January, February and March come around, you're already in a routine that carries you all the way to summer.</p>
<p>At Fig Performance in Placentia, every client starts with a free consult and an <a href="/inbody-scan-placentia">InBody scan</a>, so you know your real body fat and muscle going into the holidays and can see what changed after. Read more in <a href="/how-to-lose-weight-after-40">how to lose weight after 40</a> and <a href="/nutrition-coaching-placentia">how nutrition coaching works</a>.</p>
{CTA}"""

faqs = [
    ("How do I avoid gaining weight over the holidays?",
     "Eat protein first and fill up on vegetables, leave room for the one dessert you really want, keep training and walking, limit drinks, and keep each holiday to a few days instead of letting it stretch through November and December."),
    ("What should I eat first at Thanksgiving dinner?",
     "Protein, as much as you can, then vegetables and fiber. They fill you up fast, so you have less room for the foods that don't support your goals. Skipping the rolls and stuffing is an easy way to save room for pie."),
    ("Should I skip dessert over the holidays?",
     "No. Coach Dan eats 80/20: about 80% nutrient-dense food and 20% food he enjoys. Nutrition only works long term if it's flexible and enjoyable, so plan your dessert in."),
    ("How much weight do people gain over the holidays?",
     "Less than most people think. A study in the New England Journal of Medicine found adults gained a little under a pound on average over the holiday season. The problem is most didn't lose it afterward, so it adds up year after year."),
    ("Is it better to start now or wait until January?",
     "Start now. November and December are the hardest months, so if you build the habits now, January and the rest of the year get much easier."),
    ("How can I work out while traveling for the holidays?",
     "Do a 20-minute bodyweight circuit in your room: squats or split squats, push-ups, glute bridges, a plank and reverse lunges, 3 rounds. Then walk as much as you can, and keep prioritizing protein and fiber."),
]

html = page(
    SLUG,
    "How to Avoid Holiday Weight Gain After 40 | Fig Performance",
    "How to avoid holiday weight gain after 40, from Coach Dan: protein first, room for dessert, train on Thanksgiving, set drink boundaries, and a hotel workout.",
    "How to Avoid Holiday Weight Gain After 40 (A Coach's Rules)",
    "Fitness after 40", "How to Avoid Holiday Weight Gain After 40",
    "Live a little, keep your goals. What Coach Dan tells clients, and what he does himself.",
    [("why", "Why it matters"), ("mindset", "Live a little, keep your goals"), ("plate", "Your holiday plate"),
     ("eighty-twenty", "Eating 80/20"), ("training", "Training on Thanksgiving"), ("mistakes", "Biggest mistakes"),
     ("travel", "Traveling"), ("january", "Don't wait for January")],
    body, faqs, "Holiday Weight Gain", kind="article", published=DATE)

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", SLUG, len(html))
