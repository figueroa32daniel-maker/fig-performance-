"""Service page: vibration therapy in Placentia (answers Google 'People also ask')."""
from build_pages import page, SITE, CTA

SLUG = "vibration-therapy-placentia"
MAYO = "https://www.mayoclinic.org/healthy-lifestyle/fitness/expert-answers/whole-body-vibration/faq-20057958"

body = f"""<p class="legal-intro">At Fig Performance in Placentia, vibration therapy is part of the recovery routine, included with membership alongside red light therapy. Here's what it is, what the research actually says, who should skip it, and how we use it with adults over 40.</p>

<h2 id="what">What vibration therapy is</h2>
<p>Whole-body vibration therapy means standing, sitting or holding a position on a platform that vibrates quickly. The vibration makes your muscles contract and relax many times a second. You can stand still on it, or do simple moves like a squat or a calf raise while it runs.</p>

<h2 id="work">Does vibration therapy actually work?</h2>
<p>It can help a little, but it isn't magic. According to the <a href="{MAYO}" target="_blank" rel="noopener noreferrer">Mayo Clinic</a>, some research suggests whole-body vibration may help muscle strength, balance in older adults, back pain and bone loss, and may support weight loss when paired with eating less. The research is limited, though, and it's not clear that it's as good for you as regular exercise.</p>
<p>So we're straight with you: a vibration plate won't build muscle or burn fat on its own. Coached strength training, good nutrition and daily walking do that. Vibration therapy is one part of recovery, not a shortcut.</p>

<h2 id="ten-minutes">What is 10 minutes on a vibration plate equivalent to?</h2>
<p>There's no reliable answer. Claims like "10 minutes equals an hour at the gym" come from marketing, not research. Ten minutes on a plate is ten minutes of light muscle work. Treat it as a warm-up or a recovery tool, and keep your real training.</p>

<h2 id="who-not">Who should not do vibration therapy?</h2>
<p>Skip it, or get your doctor's OK first, if any of these apply to you:</p>
<ul>
  <li>You're pregnant.</li>
  <li>You have a pacemaker, defibrillator or other implanted electronic device.</li>
  <li>You have a heart condition, an arrhythmia or uncontrolled high blood pressure.</li>
  <li>You've had recent surgery, especially a joint replacement or spine surgery.</li>
  <li>You have a blood clot, deep vein thrombosis or a clotting disorder.</li>
</ul>
<p>If you're not sure, ask your physician. Vibration therapy is offered for general wellness. It doesn't diagnose, treat, cure or prevent any disease. See our <a href="/disclaimer#recovery-tech">health disclaimer</a>.</p>

<h2 id="session">How we use it at Fig Performance</h2>
<ul>
  <li>Coach Dan shows you how to use the platform the first time, and sets the intensity for you.</li>
  <li>Most members use it for a few minutes after training, often with <a href="/red-light-therapy-placentia">red light therapy</a> on the same visit.</li>
  <li>Stop if anything feels wrong: dizziness, pain, or numbness.</li>
</ul>

<h2 id="access">Vibration therapy in Placentia</h2>
<p>Vibration therapy is included with a Fig Performance membership, along with red light therapy, classes, a complimentary InBody scan and a one-time trainer consult. Semi-private membership is $199 to $345 a month. See <a href="/pricing">plans and pricing</a>.</p>
<p>We're at 1284 E. Yorba Linda Blvd, Placentia, a short drive from <a href="/personal-trainer-yorba-linda">Yorba Linda</a>, Fullerton, <a href="/personal-trainer-brea">Brea</a>, Anaheim Hills and Villa Park.</p>
{CTA}"""

faqs = [
    ("Does vibration therapy actually work?",
     "Some research suggests whole-body vibration may help muscle strength, balance in older adults and bone loss, but the research is limited and it isn't as proven as regular exercise. At Fig Performance we use it as part of recovery, not as a replacement for strength training."),
    ("Who should not do vibration therapy?",
     "People who are pregnant, have a pacemaker or other implanted device, have a heart condition or uncontrolled high blood pressure, have had recent surgery such as a joint replacement, or have a blood clot or clotting disorder should skip it or get their doctor's OK first."),
    ("What is 10 minutes on a vibration plate equivalent to?",
     "There's no reliable equivalent. Claims that 10 minutes on a plate equals a full workout come from marketing, not research. Use it as a warm-up or recovery tool alongside real training."),
    ("Can vibration therapy help you lose weight?",
     "Not on its own. Some studies show it may support weight loss when combined with eating fewer calories, but fat loss after 40 comes from strength training, nutrition and daily activity."),
    ("Where can I find vibration therapy near Placentia?",
     "Fig Performance at 1284 E. Yorba Linda Blvd in Placentia includes vibration therapy and red light therapy with membership. It's close to Yorba Linda, Fullerton, Brea, Anaheim Hills and Villa Park."),
]

html = page(SLUG,
    "Vibration Therapy in Placentia, CA: Does It Work? | Fig Performance",
    "Vibration therapy in Placentia, included with Fig Performance membership. Does it actually work, who should skip it, and how we use it for recovery after 40.",
    "Vibration Therapy in Placentia: Does It Actually Work?",
    "Recovery", "Vibration Therapy in Placentia, CA",
    "What it is, what the research says, and who should skip it. Included with membership.",
    [("what", "What it is"), ("work", "Does it work?"), ("ten-minutes", "Is 10 minutes a workout?"),
     ("who-not", "Who should skip it"), ("session", "How we use it"), ("access", "Vibration therapy in Placentia")],
    body, faqs, "Vibration Therapy")

if __name__ == "__main__":
    (SITE / f"{SLUG}.html").write_text(html)
    print("wrote", len(html))
