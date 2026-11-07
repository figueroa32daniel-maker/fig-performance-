"""Article: how to lose belly fat after menopause (researched draft, Dan's additions, approved Nov 7 2026)."""
import sys
from build_pages import page, SITE, CTA, callout, pullquote, stats

DATE = "2026-11-07"
SLUG = "how-to-lose-belly-fat-after-menopause"
SWAN = "https://divisionofresearch.kaiserpermanente.org/publications/changes-in-body-composition-and-weight-during-the-menopause-transition/"
KHALAFI = "https://frontiersin.org/articles/10.3389/fendo.2023.1183765/full"
BAJERSKA = "https://doaj.org/article/a0fa51e647314598b1a0261d300a4fdb"
PROTAGE = "https://researchexperts.utmb.edu/en/publications/evidence-based-recommendations-for-optimal-dietary-protein-intake/"
MENONOTE = "https://menopause.org/wp-content/uploads/for-women/MenoNote-Weight-Gain.pdf"
MAYO = "https://www.amerikanhastanesi.org/mayo-clinic-care-network/mayo-clinic-health-information-library/first-aid/belly-fat-in-women-taking-mdash-and-keeping-mdash-it-off"
IMS = "https://www.healthday.com/health-news/nutrition/menopause-won-t-spur-weight-gain-but-may-boost-belly-fat-review-669773.html"
CREATINE = "https://supplysidesj.com/healthy-living/review-shows-creatine-preserves-muscle-mass-in-older-women"
ASHWA = "https://doaj.org/article/045a897c2d174ebda9c3b1c622383cc9"
MSD = "https://www.msdmanuals.com/professional/special-subjects/dietary-supplements/ashwagandha"


def a(href, text):
    return f'<a href="{href}" target="_blank" rel="noopener noreferrer">{text}</a>'


body = f"""<p class="legal-intro">If your belly got bigger around menopause even though you're eating and moving the same as always, you're not imagining it. Menopause changes where your body stores fat. The good news: the research is clear on what helps. Strength training with progressive overload, enough protein, a modest calorie deficit built on whole, fiber-rich foods, and daily movement. Here's what the studies and doctors say, and how I put it into practice with clients over 40.</p>

<h2 id="why">Why belly fat shows up at menopause</h2>
<p>As estrogen drops, fat storage shifts toward your midsection. The Mayo Clinic notes many women see this even without gaining weight on the scale ({a(MAYO, "Mayo Clinic")}).</p>
<p>At the same time, you lose muscle. The Menopause Society says women lose 3% to 8% of their muscle mass per decade after 30, and less muscle means you burn fewer calories at rest ({a(MENONOTE, "The Menopause Society")}).</p>
<p>The large SWAN study tracked women through menopause with body scans. Once the menopause transition started, the rate of fat gain roughly doubled and lean mass started to drop. Both kept going until about two years after the final period, then leveled off ({a(SWAN, "Greendale et al., 2019")}). So this is a window, and what you do during it matters.</p>
<p>Menopause itself doesn't seem to cause most of the weight gain. A review by the International Menopause Society found midlife women gain about a pound a year on average, mostly from aging and lifestyle. What menopause changes is where the fat goes ({a(IMS, "International Menopause Society review")}).</p>
{stats([("3&ndash;8%", "of muscle lost per decade after 30"), ("~2x", "faster fat gain during the menopause transition"), ("35 in", "waist size Mayo Clinic flags as unhealthy")])}

<h2 id="lift">1. Lift weights 2 to 3 times a week</h2>
<p>This is the big one. A 2023 review of 101 randomized trials and 5,697 postmenopausal women found exercise training lowered body fat percentage, fat mass, waist size and visceral fat, the deep belly fat around your organs. Resistance training was the type that added lean mass, about 0.9 kg of fat-free mass on average ({a(KHALAFI, "Khalafi et al., 2023")}).</p>
<p>Muscle is what you're losing during menopause, so it's what you need to build back. Train your whole body, focus on big lifts like squats, hinges, presses and rows, and add weight over time. Start with the <a href="/beginner-workout-plan-for-women">beginner workout plan for women</a>.</p>
<p><strong>Get stronger every week.</strong> This is called progressive overload, and it's the part most people skip. Every week, try to add a little weight or a rep or two. Say you squat 100 pounds for 8 reps this month. Two or three months from now, that should be anywhere from 110 to 150 pounds for the same 8 reps. Muscle is a byproduct of getting stronger, so track your lifts and make sure the numbers go up.</p>
<p><strong>Add weighted ab exercises.</strong> Cable crunches, weighted dead bugs, and planks or carries with weight build a stronger core and more definition. Train your abs like any other muscle, with weight you add over time. One honest note: no ab exercise burns fat off your belly on its own. Ab work builds the muscle underneath, and the calorie deficit, protein and the rest of your training take the fat off on top of it. Together, that's what shows definition.</p>

<h2 id="eat">2. Eat in a small calorie deficit, built on whole foods</h2>
<p>To lose fat anywhere, including your belly, you need to burn more than you eat. What you eat inside that deficit matters too.</p>
<p>In a 16-week trial of 144 postmenopausal women with belly fat, two calorie-controlled diets (a Mediterranean diet and a high-fiber Central European diet) both cut waist size by about 7% and visceral fat by about 25%. The women who stuck to their diet best lost the most, and more fiber was linked to more visceral fat loss ({a(BAJERSKA, "Bajerska et al., 2018")}).</p>
<p>In practice: build meals around vegetables, fruit, beans, whole grains, lean protein, fish, nuts and olive oil. These are nutrient-dense foods, with lots of vitamins, minerals and fiber for the calories, and they keep you full. Cut back on sugary drinks, processed snacks and eating out. Use the <a href="/meal-plan-for-weight-loss">free meal plan for weight loss</a> as a template.</p>

<h2 id="protein">3. Get enough protein</h2>
<p>Protein protects your muscle while you lose fat. The Menopause Society recommends about 1.2 grams of protein per kilogram of body weight a day, and the PROT-AGE expert group recommends at least 1.0 to 1.2 g/kg for older adults, and at least 1.2 for those who exercise ({a(PROTAGE, "Bauer et al., 2013")}).</p>
<p>For most of my clients, I aim a little higher: about your goal body weight in grams of protein a day. Get protein at every meal, starting with breakfast.</p>
<p><strong>Consider creatine.</strong> Creatine is one of the most studied supplements there is. A 2026 meta-analysis in the Journal of the International Society of Sports Nutrition looked at 7 trials with 608 menopausal and postmenopausal women. Taking 5 grams or more a day while strength training gave a small but real boost in lean mass and leg strength. Lower doses, or creatine without lifting, did nothing ({a(CREATINE, "JISSN meta-analysis")}). Take 5 grams of creatine monohydrate a day, every day.</p>

<h2 id="walk">4. Walk every day</h2>
<p>Aim for at least 150 minutes a week of moderate activity like brisk walking, which is what both the Mayo Clinic and the Menopause Society recommend. Daily steps add up and help you stay in a calorie deficit without more gym time.</p>

<h2 id="sleep">5. Protect your sleep and manage stress</h2>
<p>Hot flashes, night sweats and stress can wreck your sleep, and poor sleep makes it harder to control your appetite and recover from training. The Menopause Society lists sleep and stress management as part of managing weight at midlife. Cutting back on alcohol helps here too.</p>
<p>If you're having a hard time sleeping, these are worth asking your doctor about:</p>
<ul>
  <li><strong>Magnesium</strong>, taken in the evening</li>
  <li><strong>L-theanine</strong>, an amino acid found in tea</li>
  <li><strong>Ashwagandha:</strong> a 2021 review of 5 trials found a small improvement in sleep, mostly at 600 mg a day or more for at least 8 weeks ({a(ASHWA, "Cheah et al., 2021")}). Don't take it if you're pregnant or breastfeeding, and check with your doctor first if you have liver or thyroid problems or take thyroid, blood pressure, diabetes or sleep medication ({a(MSD, "MSD Manual")}).</li>
</ul>
<p>Supplements help around the edges. A cool, dark room, a set bedtime and less alcohol at night come first.</p>

<h2 id="hrt">6. Talk to your doctor about hormone therapy</h2>
<p>Hormone therapy is not a weight-loss treatment. But according to the Menopause Society, some studies suggest it may slightly reduce belly fat and help preserve muscle, and the International Menopause Society found estrogen therapy doesn't cause weight gain. Whether it's right for you is a conversation for your doctor.</p>

<h2 id="struggles">What women say they're struggling with</h2>
<p>On women's lifting and menopause forums, the same story comes up again and again: "I'm doing everything I used to, and my waist keeps growing." One woman on a strength training forum had been lifting for four months, getting stronger, and still couldn't lose the belly. The coaches' answer was the same as this article: keep lifting, eat enough protein, and add a modest calorie deficit. Strength training alone builds muscle, but you still need the deficit to lose the fat on top of it.</p>

<h2 id="measure">Measure your waist, not just your weight</h2>
<p>The Mayo Clinic says a waist over 35 inches points to an unhealthy amount of belly fat. Measure around your bare stomach just above your hip bones, relaxed. Because you may be building muscle while losing fat, the scale can stall while your waist shrinks. An <a href="/inbody-scan-placentia">InBody scan</a> shows you fat and muscle separately.</p>
<p>If you're in North Orange County, get an InBody scan at Fig Performance in Placentia. It shows exactly how much fat and muscle you have, so you'll know the weight coming off is fat, not muscle.</p>

<h2 id="coach">Get help in Placentia</h2>
<p>At Fig Performance, every plan starts with a free consult and an InBody scan. We build your strength training, protein and calorie targets, and track your waist and body composition. Read more in <a href="/strength-training-for-women-over-50">strength training for women over 50</a>. Can't make it in person? Try <a href="/online-personal-trainer">online coaching</a>.</p>
<p><em>This article is general fitness and nutrition guidance, not medical advice. Talk to your doctor about menopause symptoms, supplements and hormone therapy.</em></p>
{CTA}"""

faqs = [
    ("Why is it so hard to lose belly fat after menopause?",
     "Lower estrogen shifts fat toward your midsection, and you lose muscle, so you burn fewer calories. The fix is strength training with progressive overload, enough protein and a modest calorie deficit."),
    ("What's the best exercise for menopause belly fat?",
     "Strength training 2 to 3 times a week, getting stronger every week, plus daily walking. A review of 101 trials found exercise lowered waist size and visceral fat in postmenopausal women, and resistance training added lean mass."),
    ("How much protein do I need after menopause?",
     "At least 1.2 grams per kilogram of body weight a day, per the Menopause Society. Coach Dan aims for about your goal body weight in grams."),
    ("Should I take creatine after menopause?",
     "It can help. A 2026 meta-analysis found 5 grams a day plus strength training gave a small boost in lean mass and leg strength in menopausal and postmenopausal women. Without lifting, it didn't help."),
    ("Does hormone therapy help with belly fat?",
     "It's not a weight-loss treatment, but some studies suggest it may slightly reduce belly fat. Ask your doctor."),
    ("Can ab exercises get rid of belly fat?",
     "Not on their own. You can't spot-reduce fat. Weighted ab exercises build core strength and definition, while a calorie deficit, strength training and daily movement take the fat off."),
]

html = page(
    SLUG,
    "How to Lose Belly Fat After Menopause | Fig Performance",
    "How to lose belly fat after menopause: what studies and doctors say about strength training, protein, creatine, diet, sleep and hormone therapy.",
    "How to Lose Belly Fat After Menopause: What the Research Says",
    "Fitness after 40", "How to Lose Belly Fat After Menopause",
    "Why the midsection changes, and the six things the research says actually help.",
    [("why", "Why it happens"), ("lift", "Lift weights"), ("eat", "Eat in a deficit"), ("protein", "Protein and creatine"),
     ("walk", "Walk daily"), ("sleep", "Sleep and stress"), ("hrt", "Hormone therapy"), ("measure", "Measure your waist")],
    body, faqs, "Belly Fat After Menopause", kind="article", published=DATE)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else str(SITE / f"{SLUG}.html")
    open(out, "w").write(html)
    print("wrote", out, len(html))
