"""Press / media page for Fig Performance."""
from build_pages import page, SITE

SLUG = "press"

body = """<p class="legal-intro">For interview requests, expert quotes or photos, email <a href="mailto:trainat@figperformance.com">trainat@figperformance.com</a> or text <a href="sms:+17143967178">(714) 396-7178</a>. Coach Dan replies within 24 hours.</p>

<h2 id="about">About Fig Performance</h2>
<p>Fig Performance is a private, one-on-one strength gym in Placentia, California, built for adults over 40 who want to lose fat, build muscle and get stronger. Every client starts with an InBody body-composition scan, so progress is measured, not guessed. Recovery is built in with red light and vibration therapy. The gym opens officially on Saturday, November 14, 2026, at 1284 E. Yorba Linda Blvd, Placentia, CA 92870.</p>

<h2 id="dan">About Coach Dan Figueroa</h2>
<p>Daniel Figueroa is the owner and head coach of Fig Performance. He is an ACSM certified personal trainer, a Precision Nutrition Level 1 certified nutrition coach, certified in CPR, AED and first aid, and a former lifeguard. He has trained since age 15&frac12; and placed first and second in bodybuilding competitions. Before opening Fig Performance, he coached clients through Train With Dan, his coaching business, which holds a 5.0 rating across 38 Yelp reviews.</p>
<p><img src="/assets/dan.jpg" width="800" height="1000" loading="lazy" decoding="async" alt="Coach Dan Figueroa, owner of Fig Performance in Placentia"></p>
<p><a href="/assets/dan.jpg" download>Download headshot</a> &middot; <a href="/assets/logo.png" download>Download logo</a></p>

<h2 id="topics">Topics Dan can speak on</h2>
<ul>
  <li>Losing weight after 40 with a desk job: steps, protein and twice-a-week strength training</li>
  <li>Building muscle in your 60s and 70s, with real client examples</li>
  <li>Strength training for women through and after menopause</li>
  <li>Body recomposition: why the scale can stay flat while you lose fat</li>
  <li>InBody scans and measuring progress beyond body weight</li>
  <li>Training around old injuries, back pain and stiff shoulders</li>
  <li>Opening a small, private gym as an independent coach</li>
</ul>

<h2 id="facts">Fast facts</h2>
<ul>
  <li><strong>Location:</strong> Placentia, CA (Orange County), serving Yorba Linda, Brea, Fullerton, Anaheim Hills and Villa Park</li>
  <li><strong>Facility:</strong> private 1,500 sq ft strength gym</li>
  <li><strong>Grand opening:</strong> Saturday, November 14, 2026</li>
  <li><strong>Reviews:</strong> 5.0 on Google and 5.0 on Yelp</li>
  <li><strong>Website:</strong> <a href="/">figperformance.com</a> &middot; <a href="https://www.instagram.com/figperformance/" target="_blank" rel="noopener noreferrer">Instagram</a> &middot; <a href="https://www.linkedin.com/company/figperformance/" target="_blank" rel="noopener noreferrer">LinkedIn</a></li>
</ul>

<h2 id="guides">Recent guides by Coach Dan</h2>
<ul>
  <li><a href="/is-belly-fat-the-last-to-go">Is belly fat the last to go?</a></li>
  <li><a href="/hip-thrust">Hip thrust form for women over 40</a></li>
  <li><a href="/jefferson-curls">Are Jefferson curls safe?</a></li>
  <li><a href="/strength-training-for-seniors">Strength training for seniors</a></li>
  <li><a href="/how-to-lose-belly-fat-after-menopause">How to lose belly fat after menopause</a></li>
  <li><a href="/meal-plan-for-weight-loss">Simple meal plan for weight loss</a></li>
  <li><a href="/glp-1-muscle-loss">GLP-1s and muscle loss</a></li>
  <li><a href="/strength-training-for-women-over-50">Strength training for women over 50</a></li>
  <li><a href="/workout-plan-for-men-over-40">Workout plan for men over 40</a></li>
  <li><a href="/beginner-workout-plan-for-women">Beginner workout plan for women</a></li>
  <li><a href="/beginner-workout-plan-for-men">Beginner workout plan for men</a></li>
  <li><a href="/how-to-avoid-holiday-weight-gain">How to avoid holiday weight gain after 40</a></li>
  <li><a href="/how-to-lose-weight-after-40">How to lose weight after 40</a></li>
  <li><a href="/build-muscle-after-60">Can you build muscle after 60?</a></li>
  <li><a href="/why-am-i-not-losing-weight">Why am I not losing weight?</a></li>
  <li><a href="/strength-training-for-women-over-40">Strength training for women over 40</a></li>
</ul>

<h2 id="contact">Press contact</h2>
<p class="legal-contact">Daniel Figueroa, Owner &amp; Head Coach<br><a href="mailto:trainat@figperformance.com">trainat@figperformance.com</a> &middot; <a href="tel:+17143967178">(714) 396-7178</a></p>"""

faqs = [
    ("How do I request an interview or quote from Coach Dan?",
     "Email trainat@figperformance.com or text (714) 396-7178 with your outlet, topic and deadline. Coach Dan replies within 24 hours."),
    ("Can I use photos of Coach Dan and the gym?",
     "Yes, for editorial coverage of Fig Performance. Download the headshot and logo from this page, or ask for gym photos."),
]

html = page(SLUG, "Press & Media | Fig Performance, Placentia",
            "Press kit for Fig Performance: about the gym, Coach Dan Figueroa's bio, headshot and logo, topics he speaks on, and how to request an interview.",
            "Press & Media: Fig Performance and Coach Dan Figueroa", "Press", "Press &amp; Media",
            "Expert quotes on fitness after 40 from Coach Dan Figueroa, ACSM certified personal trainer.",
            [("about", "About Fig Performance"), ("dan", "About Coach Dan"), ("topics", "Topics"), ("facts", "Fast facts"), ("contact", "Press contact")],
            body, faqs, "Press", kind="article", published="2026-10-31")

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", len(html))
