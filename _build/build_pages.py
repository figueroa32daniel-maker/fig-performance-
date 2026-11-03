"""Builds Fig Performance service pages from the live site's own header/footer."""
import json, re, html
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
BASE = "https://www.figperformance.com"
pricing = (SITE / "pricing.html").read_text()

# Shared chrome copied from the pricing page so new pages match the live design.
body_start = pricing.index('<a class="skip-link"')
header = pricing[body_start: pricing.index("</header>") + len("</header>")]
header = header.replace(' aria-current="page"', "").replace('          <li><a href="/#results">Results</a></li>\n', "")
footer = pricing[pricing.index("  <!-- ============ FOOTER ============ -->"):]

CHEVRON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'


def page(slug, title, desc, og_title, kicker, h1, lede, toc, body_html, faqs, crumb, kind="service", published=None):
    url = f"{BASE}/{slug}"
    faq_html = "\n".join(
        f'          <details class="faq-item">\n            <summary><span>{html.escape(q)}</span>{CHEVRON}</summary>\n'
        f'            <div class="faq-a"><p>{a}</p></div>\n          </details>'
        for q, a in faqs
    )
    ld = [
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
                {"@type": "ListItem", "position": 2, "name": crumb, "item": url},
            ],
        },
        ({
            "@context": "https://schema.org",
            "@type": "Service",
            "name": crumb,
            "serviceType": crumb,
            "url": url,
            "areaServed": ["Placentia", "Yorba Linda", "Fullerton", "Brea", "Anaheim Hills", "Villa Park"],
            "provider": {"@id": f"{BASE}/#gym"},
        } if kind == "service" else {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": h1,
            "description": desc,
            "url": url,
            "datePublished": published,
            "dateModified": published,
            "image": f"{BASE}/assets/og-image.jpg",
            "author": {"@type": "Person", "name": "Daniel Figueroa", "jobTitle": "ACSM Certified Personal Trainer", "url": f"{BASE}/#coach"},
            "publisher": {"@id": f"{BASE}/#gym"},
        }),
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", html.unescape(a))}}
                for q, a in faqs
            ],
        },
    ]
    ld_html = "\n".join(
        f'  <script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld
    )
    byline = (f'\n        <p class="legal-meta article-byline">By Coach Dan Figueroa, ACSM certified personal trainer &middot; Updated {published}</p>' if kind == "article" else "")
    toc_html = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    e = html.escape
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#0f1f3d">

  <!-- Open Graph / social -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Fig Performance">
  <meta property="og:title" content="{e(og_title)}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{BASE}/assets/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Fig Performance: private 1:1 training in Placentia for adults over 40.">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(og_title)}">
  <meta name="twitter:description" content="{e(desc)}">
  <meta name="twitter:image" content="{BASE}/assets/og-image.jpg">

  <!-- Icons -->
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="preload" href="/assets/fonts/montserrat-latin-var.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/inter-latin-var.woff2" as="font" type="font/woff2" crossorigin>

  <link rel="stylesheet" href="/assets/styles.css?v=36">
{ld_html}
</head>
<body class="legal-page service-page">
  {header}

  <main id="main">
    <section class="legal-hero section-beige">
      <div class="container">
        <p class="kicker">{kicker}</p>
        <h1>{h1}</h1>
        <p class="legal-meta">{lede}</p>{byline}
      </div>
    </section>

    <section class="section section-cream legal-wrap">
      <div class="container legal-grid">
        <aside class="legal-toc" aria-label="On this page">
          <p class="legal-toc-title">On this page</p>
          <ol>{toc_html}</ol>
          <p class="legal-others">Ready to start? <a href="/#consult">Book a free consult</a></p>
        </aside>
        <article class="legal-body">
{body_html}
        </article>
      </div>
    </section>

    <section class="section section-cream" id="faq" aria-labelledby="faq-title">
      <div class="container">
        <div class="section-head">
          <p class="kicker">FAQ</p>
          <h2 id="faq-title">Straight answers.</h2>
        </div>
        <div class="faq-list">
{faq_html}
        </div>
        <div class="consult-explainer">
          <div>
            <h3>Start with a free consult</h3>
            <p>About an hour with Coach Dan: an InBody scan, a movement assessment, a conversation about your goals, and a game plan. No commitment.</p>
          </div>
          <a class="btn btn-primary btn-lg" href="/#consult">Book a free consult</a>
        </div>
      </div>
    </section>
  </main>

{footer}"""


CTA = ('<p class="legal-contact">Fig Performance &middot; 1284 E. Yorba Linda Blvd, Placentia, CA 92870<br>'
       'Call or text <a href="tel:+17143967178">(714) 396-7178</a> &middot; Mon&ndash;Fri, 5 AM &ndash; 8 PM; Sat, 5 AM &ndash; 12 PM<br>'
       '<a href="/#consult">Book a free consult</a></p>')

# ---------------------------------------------------------------- InBody
inbody_body = f"""<p class="legal-intro">You eat well. You exercise. You might have worked with a trainer before. But the bathroom scale barely moves, and you can't tell whether you're losing fat, losing muscle, or both. An InBody scan answers that in about a minute, so you know exactly where you stand.</p>

<h2 id="what">What an InBody scan measures</h2>
<p>InBody is a body-composition analyzer. Instead of one number, it breaks your weight down into what it's actually made of:</p>
<ul>
  <li><strong>Body fat percentage and fat mass</strong>: how much of your weight is fat.</li>
  <li><strong>Skeletal muscle mass</strong>: the muscle you build and keep with strength training.</li>
  <li><strong>Lean mass by body segment</strong>: your arms, legs and trunk, so imbalances show up.</li>
  <li><strong>Visceral fat level</strong>: the deeper fat around your organs.</li>
  <li><strong>Body water and basal metabolic rate</strong>: useful context for nutrition and recovery.</li>
</ul>

<h2 id="why-40">Why it matters after 40</h2>
<p>After 40, muscle doesn't take care of itself. It's common for the scale to stay about the same while fat slowly goes up and muscle slowly goes down. You look and feel softer, even though your weight says nothing changed.</p>
<p>That's why so many people who are "doing everything right" feel stuck. Without body-composition numbers, you can't tell whether your training and eating are moving you in the right direction. An InBody scan turns guessing into numbers you can track. (More on that in <a href="/why-am-i-not-losing-weight">why you're not losing weight</a>.)</p>
<p>A scan also catches body recomposition: fat going down and muscle going up while your weight stays the same. Coach Dan explains it in <a href="/how-to-lose-weight-after-40#scale">how to lose weight after 40</a>.</p>

<h2 id="how">How the scan works</h2>
<p>You step onto the InBody barefoot and hold the hand electrodes. The device sends a small, painless electrical signal through your body and measures how it travels through muscle, fat and water. You don't feel anything, you stay fully dressed, and the whole thing takes about a minute. You get a printout and Dan walks you through every number.</p>

<h2 id="prep">How to prepare</h2>
<p>InBody results are most useful when you test under the same conditions each time. For the most consistent numbers:</p>
<ul>
  <li>Test at about the same time of day, ideally earlier in the day.</li>
  <li>Skip eating for about two hours beforehand.</li>
  <li>Don't work out right before your scan.</li>
  <li>Use the restroom first.</li>
  <li>Remove watches, jewelry and anything metal.</li>
</ul>

<h2 id="safety">Who shouldn't use it</h2>
<p>Don't take an InBody scan if you have a pacemaker or another implanted electronic medical device, or if you're pregnant. InBody scans are for general fitness tracking. They don't diagnose or treat any condition and aren't a substitute for medical care. If you're unsure, ask your physician first. See our <a href="/disclaimer#recovery-tech">health disclaimer</a> for more.</p>

<h2 id="fig">How we use InBody at Fig Performance</h2>
<p>The scan is the first and last step of the Fig method: <strong>Scan. Plan. Train. Recover. Re-scan.</strong></p>
<ul>
  <li><strong>Scan</strong>: your first scan sets your baseline.</li>
  <li><strong>Plan</strong>: Coach Dan builds your strength training and nutrition plan around those numbers and around anything that hurts.</li>
  <li><strong>Re-scan</strong>: regular re-scans show what's changing: fat down, muscle up, and where you're making progress.</li>
</ul>
<p>Your free consult includes an InBody scan, and every member gets a complimentary scan.</p>

<h2 id="visit">Get your scan in Placentia</h2>
<p>Fig Performance is a private, coach-led strength gym on E. Yorba Linda Blvd in Placentia, a short drive from Yorba Linda, Fullerton, Brea, Anaheim Hills and Villa Park.</p>
{CTA}"""

inbody_faqs = [
    ("Is an InBody scan accurate?",
     "InBody is a reliable way to track changes in your body fat and muscle over time, as long as you test under the same conditions each time. It isn't a medical test, and numbers can shift a little with hydration and food. The trend across several scans is what matters most."),
    ("How often should I get re-scanned?",
     "Most people re-scan every 4 to 8 weeks. That's long enough for real changes in fat and muscle to show up. Coach Dan will tell you when to re-scan based on your plan."),
    ("How much does an InBody scan cost at Fig Performance?",
     "Your free consult includes an InBody scan, and every member gets a complimentary scan. Personal training clients are re-scanned as part of their program. Call or text (714) 396-7178 with any questions."),
    ("Is InBody better than a bathroom scale?",
     "A bathroom scale only tells you total weight. InBody separates that weight into fat, muscle and water, so you can see whether you're losing fat or losing muscle, even when the scale doesn't move."),
    ("Where can I get an InBody scan near Yorba Linda or Fullerton?",
     "Fig Performance is at 1284 E. Yorba Linda Blvd in Placentia, CA 92870, close to Yorba Linda, Fullerton, Brea, Anaheim Hills and Villa Park. We're open Monday through Friday, 5 AM to 8 PM, and Saturday, 5 AM to 12 PM."),
]

# ---------------------------------------------------------------- Red light
red_img = """<p><picture>
  <source type="image/webp" srcset="/assets/gym/red-light-480.webp 480w, /assets/gym/red-light.webp 900w" sizes="(min-width: 960px) 720px, 92vw">
  <img src="/assets/gym/red-light-480.jpg" srcset="/assets/gym/red-light-480.jpg 480w, /assets/gym/red-light.jpg 900w" sizes="(min-width: 960px) 720px, 92vw" width="480" height="720" loading="lazy" decoding="async" alt="Red light therapy panel at Fig Performance in Placentia, lit up with rows of red LEDs">
</picture></p>"""

red_body = f"""<p class="legal-intro">At Fig Performance, red light therapy is part of how you recover between training sessions. It's included with membership, built into the routine alongside vibration therapy, and set up so you can use it without a crowd or a wait.</p>

<h2 id="what">What red light therapy is</h2>
<p>Red light therapy uses a panel of LEDs that give off red and near-infrared light. You stand or sit in front of the panel for a short session. It doesn't use UV light, it isn't a tanning bed, and it doesn't feel like much beyond gentle warmth.</p>
{red_img}

<h2 id="research">What the research says</h2>
<p>Red light therapy is also called photobiomodulation. Researchers have studied it for muscle recovery, soreness and joint comfort, and some studies show promising results. The evidence is still developing, and results vary from person to person.</p>
<p>So we're straight with you: red light therapy is not a fat-loss tool and not a medical treatment. What changes your body after 40 is coached strength training, good nutrition and consistent recovery. Red light is one part of that recovery, not a replacement for it.</p>

<h2 id="session">What a session is like</h2>
<ul>
  <li>Coach Dan shows you how to use the panel the first time.</li>
  <li>You stand or sit in front of the panel for a few minutes.</li>
  <li>Don't stare directly into the lights.</li>
  <li>Many members use it after training, on the same visit.</li>
</ul>

<h2 id="safety">Who should check with a doctor first</h2>
<p>Talk to your physician before using red light therapy if you're pregnant, have a light-sensitive condition, take medication that makes you sensitive to light, or have an implanted medical device. Red light therapy is offered for general wellness. It doesn't diagnose, treat, cure or prevent any disease. See our <a href="/disclaimer#recovery-tech">health disclaimer</a> for more.</p>

<h2 id="access">How to use it at Fig Performance</h2>
<p>Red light therapy is included with a Fig Performance membership, along with <a href="/vibration-therapy-placentia">vibration therapy</a>, classes, a complimentary InBody scan and a one-time trainer consult. See <a href="/pricing">plans and pricing</a>, or ask about it at your free consult.</p>

<h2 id="cost">How much does red light therapy cost?</h2>
<p>Standalone red light sessions at wellness studios are usually sold per visit or as a monthly package. At Fig Performance, red light therapy comes with membership instead, so you get recovery, training space and coaching in one place. Membership is quoted at your <a href="/free-consult-placentia">free consult</a>.</p>

<h2 id="visit">Red light therapy in Placentia</h2>
<p>We're a private, coach-led strength gym on E. Yorba Linda Blvd in Placentia, a short drive from <a href="/personal-trainer-yorba-linda">Yorba Linda</a>, Fullerton, <a href="/personal-trainer-brea">Brea</a>, Anaheim Hills and Villa Park. Coming from Fullerton, we're a few minutes up Placentia Ave or the 57.</p>
{CTA}"""

red_faqs = [
    ("Is red light therapy included with membership?",
     "Yes. A Fig Performance membership includes red light therapy, vibration therapy, classes up to 2 to 3 times a week, a complimentary InBody scan and a one-time trainer consult."),
    ("Does red light therapy help with fat loss?",
     "Don't count on it. The research on red light therapy for fat loss isn't strong. Fat loss after 40 comes from strength training, nutrition and consistency. We use red light as part of recovery."),
    ("Does red light therapy help muscle recovery?",
     "Some studies show it may help with muscle soreness and recovery, but the evidence is still developing and results vary. We treat it as one helpful part of a recovery routine, not a cure."),
    ("Is red light therapy safe?",
     "Red light therapy doesn't use UV light and is generally considered low risk. Don't stare into the panel, and check with your physician first if you're pregnant, sensitive to light, take light-sensitizing medication, or have an implanted medical device."),
    ("How much does red light therapy cost in Placentia?",
     "At Fig Performance, red light therapy is included with membership, along with vibration therapy, classes, a complimentary InBody scan and a one-time trainer consult. Membership is quoted at your free consult."),
    ("Where can I find red light therapy near Fullerton, Yorba Linda or Brea?",
     "Fig Performance is at 1284 E. Yorba Linda Blvd in Placentia, CA 92870, close to Yorba Linda, Fullerton, Brea, Anaheim Hills and Villa Park. We're open Monday through Friday, 5 AM to 8 PM, and Saturday, 5 AM to 12 PM."),
]

pages = {
    "inbody-scan-placentia.html": page(
        "inbody-scan-placentia",
        "InBody Scan in Placentia, CA | Fig Performance",
        "Get an InBody body-composition scan in Placentia. See your body fat, muscle and visceral fat, not just your weight. Included free with your consult.",
        "InBody Body-Composition Scan in Placentia | Fig Performance",
        "InBody scan", "InBody Scan in Placentia, CA",
        "Body-composition testing for adults over 40 who want real numbers, not guesses. Included with your free consult.",
        [("what", "What it measures"), ("why-40", "Why it matters after 40"), ("how", "How it works"),
         ("prep", "How to prepare"), ("safety", "Who shouldn't use it"), ("fig", "How we use it"),
         ("visit", "Get your scan")],
        inbody_body, inbody_faqs, "InBody Scan"),
    "red-light-therapy-placentia.html": page(
        "red-light-therapy-placentia",
        "Red Light Therapy in Placentia, CA | Fig Performance",
        "Red light therapy in Placentia, near Fullerton and Yorba Linda. Included with Fig Performance membership, with vibration therapy. Cost, safety and what to expect.",
        "Red Light Therapy in Placentia | Fig Performance",
        "Recovery", "Red Light Therapy in Placentia, CA",
        "Part of the recovery routine at Fig Performance. Included with membership.",
        [("what", "What it is"), ("research", "What the research says"), ("session", "What a session is like"),
         ("safety", "Check with a doctor"), ("access", "How to use it"), ("cost", "Cost"), ("visit", "Visit us")],
        red_body, red_faqs, "Red Light Therapy"),
}

if __name__ == "__main__":
  for name, content in pages.items():
    (SITE / name).write_text(content)
    print("wrote", name, len(content))
