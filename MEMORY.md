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
- Jonathan, 43: ex-Army, new son, back pain and shoulder pain. Pull-ups went from 1 to 5. Chin-ups with +35 lb, Jefferson curl 135 lb, bench 185 lb. Don't mention where he lives.

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
  - Belly fat after menopause: content gathered, needs a draft and Dan's review.
  - Strength training with knee pain: needs a client story.
- 2026-11-03: Planned design polish, waiting on Dan's photos:
  - people-first homepage hero
  - photos in articles
  - client callout boxes
  - "Nov 3, 2026" date format
  - sentence-case article headlines
  - trimmed menu (8 items plus button)
- 2026-11-03: Decided not to install claude-mem. It needs an account, stores memories on their cloud by default, and wouldn't persist in cloud sessions. This file replaces it.
