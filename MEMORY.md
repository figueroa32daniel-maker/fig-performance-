# Project memory: Fig Performance (figperformance.com)

Read this at the start of every session, together with `_build/README.md` (how to build and publish, and Dan's rules). Add to the log at the bottom whenever something important is decided or shipped. Keep entries short and factual.

## The business
- Fig Performance: private one-on-one strength gym for adults over 40, at 1284 E. Yorba Linda Blvd, Placentia, CA 92870. Phone/text (714) 396-7178, trainat@figperformance.com.
- Owner and head coach: Daniel "Dan" Figueroa. ACSM certified personal trainer, Precision Nutrition Level 1 certified nutrition coach. Not a registered dietitian.
- Hours: Mon–Fri 5 AM–8 PM, Sat 5 AM–12 PM, closed Sunday. Grand opening Sat, Nov 14, 2026, 10 AM–1 PM.
- Service area: Placentia, Yorba Linda, Fullerton, Brea, Anaheim Hills, Villa Park. In-home training covers wider North Orange County.
- Prices: personal training $90 a session, 3-month minimum, 20% off paid in full. Online coaching $249 a month as a 3-month program, or $697 paid in full. Membership is quoted at the consult. The free consult includes an InBody scan.
- Online coaching uses the R.H.O.D.E.S. training app. It includes a weekly 1:1 video call, custom training and an 80/20 nutrition plan.
- Dan's nutrition philosophy is 80/20: about 80% nutrient-dense food and 20% food you enjoy. It's his own approach, not a study.
- Booking: Calendly https://calendly.com/trainwithcoachdan/free-consult-inbody-scan. The site's consult quiz emails Dan through formsubmit.
- Reviews: 25 on Google (5.0), 38 on Yelp (the listing is now named Fig Performance), and 12 client reviews from people Dan coached before Fig Performance. Total 75.

## Clients Dan has OK'd naming (first name only)
- Teresa, 60: shoulder injury, couldn't do bodyweight exercises. First pull-up in about 3 months. Now benches about 85 lb for reps.
- Sam, 70: deadlifts 135 lb, dumbbell benches the 45s, curls 30 lb dumbbells.
- Adriana, 48: lost 10 lb in her first month.
- Jonathan, 43: ex-Army, new son, back pain and shoulder pain. Pull-ups went from 1 to 5. Chin-ups with +35 lb, Jefferson curl 135 lb, bench 185 lb. Don't mention where he lives. Back story approved Nov 7: was stiff/achy, pain bending over, had quit golf; now golfs again.
- Thinzar (spelling confirmed by Dan Nov 7): hip thrust from 55 lb (bar + 5 each side) to 135 lb in about six weeks.

## How we work
- Dan reviews and approves every article before it goes live. He sends answers by voice memo. Write in his voice, using only facts he gave. Verify science claims and soften overstatements. Show him what changed.
- Previews go to Dan as phone-sized PDFs, rendered as one continuous page.
- Publish only from this repo (main → Vercel). On Nov 1, 2026, a deploy from another tool wiped about 20 pages.
- After publishing: update sitemap.xml and llms.txt, link the new page from the guides hub (`_build/build_articles.py`), and submit the URLs to IndexNow through OpenSEO (project c4ee5ca3-9866-446a-899b-10dc25096a6b).
- Design: keep the brand (navy, gold and cream, Montserrat and Inter). Use the ui-ux-pro-max skill in `.claude/skills/` (see CLAUDE.md).
- Article plan and draft tabs live in the Claude Docs project "Fig Performance Article Plan" (1a4c49c4-7f9b-466c-bf63-1d21fa93dc1e).
- A weekly scheduled task, "Fig weekly blog topic", runs Mondays at 11:38 AM PT. It checks site health, researches topics, drafts the next article for Dan's review, and publishes only what's marked Approved.

## Log
- 2026-11-03: Published, all approved by Dan:
  - holiday weight gain
  - online coaching page
  - beginner workout plans for women and men, plus the 3-day split hub
  - rewrites of "Why am I not losing weight" and "Strength training for women over 40"
  - meal plan for weight loss (free PDF, no email)
  - tib raises
  - women over 50
  - GLP-1 muscle loss
  - workout plan for men over 40
  - lose 10 lb in a month
- 2026-11-03: Installed the UI/UX Pro Max design skill. Dan chose "keep brand, add polish."
- 2026-11-03: In progress, not published:
  - Belly fat after menopause: LIVE Nov 7 (/how-to-lose-belly-fat-after-menopause). Researched draft + Dan's additions (progressive overload, weighted abs, creatine 5 g, magnesium/theanine/ashwagandha with doctor caveat). No client story by Dan's choice.
  - Strength training with knee pain: needs a client story.
- 2026-11-03 (superseded below): Planned design polish, waiting on Dan's photos:
  - people-first homepage hero
  - photos in articles
  - client callout boxes
  - "Nov 3, 2026" date format
  - sentence-case article headlines
  - trimmed menu (8 items plus button)
- 2026-11-03: Decided not to install claude-mem. It needs an account, stores memories on their cloud by default, and wouldn't persist in cloud sessions. This file replaces it.
- 2026-11-03: Design system chosen by Dan: Premium + Editorial. Saved at `design-system/fig-performance/MASTER.md` (navy/gold/cream, Montserrat/Inter, spacious Swiss minimal) and `pages/articles.md` (editorial: sentence-case H1, human dates, featured image, client callouts, pull quotes). Generated with ui-ux-pro-max, then adjusted to the existing brand.
- 2026-11-03: Shipped design polish (Dan-approved): human dates ("Nov 3, 2026"), title-case article H1s with balanced wrapping, client callout boxes (`callout()` in build_pages.py), pull quotes (`pullquote()`), and a 5-item menu (How it works, Pricing, Guides, Coach, Shop). Dan said to skip photos for now.
- 2026-11-03: Shipped Premium + Editorial site-wide (Dan-approved): no long ALL-CAPS H1s on any inner page, lighter article contents box, wider and larger article text, a "Key takeaways" box on every article (`TAKEAWAYS` dict in build_pages.py, keyed by slug; add one for every new article), stat highlights (`stats()`), and accessibility fixes (footer links underlined, concierge boxes no longer asides, table header label). axe audit clean, no overflow at 375/768px.
- 2026-11-07: Strength training for seniors LIVE (/strength-training-for-seniors), from Dan's memo. New approved client: Randy, 73, lawyer, shoulder arthritis, benches 135 for reps pain free. Sam, 70 = former restaurant owner (decades); lifts corrected site-wide: 50s DB bench, 40s seated DB press, 135 deadlift, 30s curls. Jefferson curl story (client in 40s, 10 lb to 45 lb in 2 months) saved for the Jefferson curl article.
- 2026-11-07: Dan's rule: FREE SEO tools only. Never spend OpenSEO credits or pay for any SEO tool. Weekly Monday task (trig_017D9k7W7JFHqW9NGDGpDBNb) now does a free rankings report: Search Console via OpenSEO (free), Google Maps check in the built-in browser, topic ideas from Google autocomplete / People also ask / Search Console. History goes in a "Rankings" tab in the article plan doc.
- 2026-11-07: Dan briefly upgraded OpenSEO ($10/mo) to price the article list, then cancelled; plan ends Dec 7, 2026 (~$9.97 credits usable until then). Backlog tab in the article plan doc now has 60 weekly articles (Nov 9, 2026 to Dec 27, 2027) with real search volumes and difficulty. Monday task (trig_017D9k7W7JFHqW9NGDGpDBNb) now drafts that week's backlog article in full every week (Dan approves before publishing) plus the free rankings report; paid OpenSEO lookups allowed lightly only until Dec 7, 2026, free-only after. Next article: Jefferson curls (needs Dan's memo).
- 2026-11-07: Local SEO fix (routine, per page-builder rules). Search Console showed "personal trainer placentia ca" split across 6 pages (home, Brea, Yorba Linda, cost, Placentia, pricing), none ranking above 41. Home page is now the single Placentia target: footer "Placentia" link and home-page area chip no longer point at /personal-training-placentia, which was retitled "How One-on-One Personal Training Works" (same URL) and is linked from the home-page Method section. City pages rebuilt with distinct content (Yorba Linda, Brea) and two added: /personal-trainer-fullerton, /personal-trainer-anaheim-hills ("personal trainer fullerton ca" was being served by the Brea page). No clients are placed in any city. Goal recorded in OpenSEO project context: #1 Placentia, top 3 N. Orange County.
- 2026-11-07: Dan sent the Jefferson curl memo. Draft 2 is in the plan doc tab "Draft: Jefferson curls" (written in his voice from the memo; open items: the 10-to-45 lb client's name and back history, OK to cite Jonathan's 135 lb, and whether to keep the standard medical cautions). Not published until Dan approves. Dan's facts: he worked up from the bar to 205 lb; back pain returned whenever he stopped and went away when he resumed; teaches body weight first, short range to a bench, then range, then 2.5 lb increments; 1-8 reps; cues = brace core + glutes, tuck chin, round down past the knees, unravel lower-mid-upper, arch to full extension; Ben Patrick popularized it; Dan's YouTube research traces loaded flexion to 1930s lifters.
- 2026-11-07: Rank tracker: the weekly schedule needs the paid plan ("plan_required"), but a manual run_rank_tracker works on credits (~198 credits, about $0.19, for 13 keywords mobile depth 40). Dan OK'd using credits for this. Added "personal trainer fullerton ca" and "personal trainer anaheim hills" to the tracker and started the first check (run 5e9aacc8). Monday task may run one manual check per week while credits last (through Dec 7, 2026).
- 2026-11-07: Jefferson curls article APPROVED by Dan and published (/jefferson-curls). Jonathan details approved: back was stiff/achy, pain bending and touching toes, had quit golf; now Jefferson curls 135 lb and golfs again. Drafts created for weeks 2 and 3 (upper belly fat, hip thrusts) awaiting Dan's memos. Dan asked to batch as many articles as possible today.
- 2026-11-07 (afternoon): Drafted weeks 2-8 in the plan doc (tabs: Upper belly fat, Hip thrusts, Women over 60, Building muscle after 50, Squat form, Hotel workout, Calorie deficit), each with DAN: gaps and a "Needs from Dan" list. Week 8 re-aimed at "calorie deficit" (not "how to lose weight after 40", which is already live) to avoid cannibalization. Dan is sending memos starting with hip thrusts. Sources chosen: Chaston & Dixon 2008 (visceral fat), Vispute 2011 (spot reduction), Contreras 2015 + Plotkin 2023 (hip thrust), Watson 2018 LIFTMOR (bone), Peterson 2011 (lean mass after 50), Hartmann 2013 (squat depth), NIH Body Weight Planner.
- 2026-11-07: Hip thrust article APPROVED by Dan and published (/hip-thrust). Dan attended Bret Contreras's 3-day seminar in Fort Lauderdale, Aug 2026; his glute template for women: 3 leg days (hip thrust + squat pattern + hinge + abduction), ~32 leg sets/week, 2 upper days. Rep range 1-30 by goal. Variations: traditional, half-rep, pulses, 1 1/4 reps, paused. Dan said: start publishing as memos come in.
