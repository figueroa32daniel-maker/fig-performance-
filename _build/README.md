# Fig Performance site builders

These scripts generate the guide, service and city pages. `_build/` is excluded from the Vercel deploy (see `.vercelignore`). Run every script from this folder: `cd _build && python3 build_x.py`. Each script writes its page into the repo root and pulls the header and footer from `pricing.html`.

- `build_pages.py`: `page()` template, InBody and red light pages, CSS version
- `build_articles.py`: fitness-after-40 hub and older articles
- `build_post_*.py`: one file per article written from Coach Dan's answers
- `build_cities.py`, `build_local.py`, `build_cost.py`, `build_vibration.py`, `build_nutrition.py`, `build_press.py`: service and local pages
- `*.md`: Dan's raw answers and notes for the articles

## Publishing a new article

1. Copy `build_post_muscle60.py` to `build_post_<slug>.py`. Write the article from Dan's own answers. Use `kind="article"` and `published="YYYY-MM-DD"`.
2. Run it. Add the article to:
   - the hub at `fitness-after-40` (in `build_articles.py`)
   - the homepage guides strip (`#guides` in `index.html`), if it's a top article
   - `sitemap.xml`
   - `llms.txt` under "Guides for adults over 40"
   - the press page guide list (in `build_press.py`)
3. Link it from 1 or 2 related existing pages.
4. Commit and push to `main`. Vercel deploys automatically.
5. Check that the page is live, then submit the new and changed URLs to IndexNow through OpenSEO (project `c4ee5ca3-9866-446a-899b-10dc25096a6b`).

## Rules from Dan (never break these)

- Never publish an article until Dan has reviewed it and approved it. He adds his own suggestions to every article first. Drafts go in the article plan doc (Claude Docs project 1a4c49c4-7f9b-466c-bf63-1d21fa93dc1e) for his review.

- Prices: use only what the website already shows. That's $90 a session; the 1–4 sessions-a-week table ($387, $774, $1,161, $1,548 a month); 20% off when paid 3 months in full; a 3-month minimum; and a free consult. Online coaching is $249 a month as a 3-month program ($747), or $697 paid in full. The membership price is quoted at the consult.
- Never mention Crunch on Dan's own marketing, except the sourced price comparison on the cost guide.
- No "$150 value" claims.
- The 12 extra reviews are "client reviews" from people Dan coached before Fig Performance. Never call them text-message reviews.
- Never invent client stories, numbers or quotes. Use first names only, and only ones Dan has given.
- Dan is an ACSM certified personal trainer and a Precision Nutrition Level 1 certified nutrition coach. He is not a registered dietitian.
- Hours: Mon–Fri 5 AM–8 PM, Sat 5 AM–12 PM, closed Sunday.
- Publish only from this repo. A deploy from any other tool wipes these pages (this happened on Nov 1, 2026).
