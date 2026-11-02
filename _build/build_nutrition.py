"""Service page: nutrition coaching in Placentia (part of personal training)."""
from build_pages import page, SITE, CTA

SLUG = "nutrition-coaching-placentia"
CAL = "https://calendly.com/trainwithcoachdan/free-consult-inbody-scan"

body = f"""<p class="legal-intro">At Fig Performance in Placentia, nutrition coaching comes with one-on-one personal training. Coach Dan, your trainer and nutrition coach, takes the foods you already like, raises your protein, sets your calories, and gives you a simple plan with rotating options. No obsessive tracking, no cutting out the foods you love, and your InBody scans show whether it's working.</p>

<h2 id="how">How nutrition coaching works</h2>
<ol>
  <li><strong>Nutrition questionnaire.</strong> Which proteins, carbs and fats you like, the foods you actually enjoy, and what a normal day of eating looks like for you.</li>
  <li><strong>Structure what you already eat.</strong> Coach Dan raises your protein, sets your calories and builds a calorie deficit you can live with if fat loss is the goal.</li>
  <li><strong>Your plan, with options.</strong> Breakfast A or B, lunch A or B, snack A or B, and so on. You don't need an app. If you like tracking, that's fine too.</li>
  <li><strong>Measure with InBody.</strong> Body fat, muscle and visceral fat, not just your weight, so you know you're losing fat and keeping muscle.</li>
  <li><strong>Adjust.</strong> Every week in your sessions, you talk through what's working and what isn't, and the plan changes with you.</li>
</ol>

<h2 id="after-40">Why nutrition changes after 40</h2>
<p>After 40, you lose muscle more easily, and a desk job cuts how much you move. When you eat less to lose fat, your body can give up muscle along with it. Protein is what helps you keep it. That's why the plan starts with protein at every meal, pairs it with strength training, and adds daily walking (over 5,000 steps, ideally 6,000 or more). Read more in <a href="/how-to-lose-weight-after-40">how to lose weight after 40</a> and <a href="/why-am-i-not-losing-weight">why am I not losing weight?</a></p>

<h2 id="clients">What clients say</h2>
<blockquote><p>&ldquo;What stood out was how he explained his approach to nutrition too, no crazy tracking or cutting out foods, just a realistic plan that actually fits into real life.&rdquo;</p><p>Lauren T., client of Coach Dan</p></blockquote>
<blockquote><p>&ldquo;He has also worked with me on my nutrition&hellip; In just four weeks, I have lost 10 pounds.&rdquo;</p><p>Adriana M., client of Coach Dan</p></blockquote>

<h2 id="dietitian">Nutrition coach or registered dietitian?</h2>
<p>Coach Dan is a Precision Nutrition Level 1 certified nutrition coach and an ACSM certified personal trainer. He isn't a registered dietitian. Nutrition coaching at Fig Performance is for healthy adults who want to lose fat, build muscle and eat with more structure. It isn't medical nutrition therapy.</p>
<p>See a registered dietitian (RD) or your doctor if you have diabetes, kidney disease, a food allergy, a digestive condition, an eating disorder, or you're pregnant, or if your doctor has prescribed a special diet. Many clients work with both: their RD or doctor for the medical side, and Coach Dan for training, protein, habits and accountability.</p>

<h2 id="price">Cost</h2>
<p>Nutrition coaching is included with personal training at Fig Performance: $90 a session with Coach Dan, 3-month minimum, and 20% off when you pay 3 months in full. See <a href="/pricing">plans and pricing</a> or <a href="/personal-training-cost-placentia">how much personal training costs in Placentia</a>.</p>

<h2 id="start">Start with a free consult</h2>
<p>Your consult and <a href="/inbody-scan-placentia">InBody scan</a> are free, with no commitment. You'll leave with your numbers and a plan. We're at 1284 E. Yorba Linda Blvd, Placentia, close to <a href="/personal-trainer-yorba-linda">Yorba Linda</a>, Fullerton, <a href="/personal-trainer-brea">Brea</a>, Anaheim Hills and Villa Park.</p>
<p><a class="btn btn-gold" href="{CAL}" target="_blank" rel="noopener">Book your free consult online</a></p>
{CTA}"""

faqs = [
    ("Do you offer nutrition coaching in Placentia?",
     "Yes. Fig Performance includes nutrition coaching with one-on-one personal training: a nutrition questionnaire, more protein, set calories, and a simple plan with rotating meal options, checked with InBody body-composition scans."),
    ("Do I have to track calories or macros?",
     "No. Most clients follow a plan with rotating options, like breakfast A or B, built from foods they already like. If you enjoy tracking, you can."),
    ("Is Coach Dan a nutrition coach or a dietitian?",
     "Coach Dan is a Precision Nutrition Level 1 certified nutrition coach and ACSM certified personal trainer, not a registered dietitian. He coaches nutrition for healthy adults who want to lose fat and build muscle. For a medical condition, a food allergy, an eating disorder, pregnancy or a prescribed diet, see a registered dietitian or your doctor."),
    ("How much does nutrition coaching cost?",
     "It's included with personal training at Fig Performance, which is $90 a session with a 3-month minimum and 20% off when you pay 3 months in full. The first consult and InBody scan are free."),
    ("How much protein should I eat after 40?",
     "Enough to keep the muscle you have while you lose fat. Start by putting a solid protein source in every meal. Your exact target depends on your body size, goals and health, which Coach Dan sets at your consult."),
]

html = page(SLUG,
    "Nutrition Coaching in Placentia, CA for Adults 40+ | Fig Performance",
    "Nutrition coaching in Placentia with Coach Dan, PN1 certified: more protein, a simple plan from foods you like, no obsessive tracking. Included with training.",
    "Nutrition Coaching in Placentia, CA | Fig Performance",
    "Nutrition", "Nutrition Coaching in Placentia, CA",
    "A simple plan built from foods you already like, for adults over 40. Included with personal training.",
    [("how", "How it works"), ("after-40", "Why it changes after 40"), ("clients", "What clients say"),
     ("dietitian", "Coach or dietitian?"), ("price", "Cost"), ("start", "Free consult")],
    body, faqs, "Nutrition Coaching")

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", len(html))
