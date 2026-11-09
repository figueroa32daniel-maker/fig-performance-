# Fig Performance website

Static site deployed to Vercel from `main`. Read `MEMORY.md` first (project memory: business facts, approved client names, decisions and a log; add to its log when something important is decided or shipped). Then read `_build/README.md` for how pages are built and published, and for Dan's rules. The most important rule: never publish an article until Dan has approved it.

## Design

- Use the `ui-ux-pro-max` skill in `.claude/skills/ui-ux-pro-max/` for all UI design work: new pages, layout changes, components, and design reviews.
- Before changing any page's look, read `design-system/fig-performance/MASTER.md`. If `design-system/fig-performance/pages/<page>.md` exists, its rules override the master file.
- Keep the Fig Performance brand: navy, gold and cream, the logo, and Montserrat headings with Inter body text, unless Dan approves a change.
- To use the skill's search tool, run `python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain>` from the repo root (the SKILL.md path uses ${CLAUDE_PLUGIN_ROOT}, which is the repo root here). Treat results as suggestions; the brand rules in MASTER.md win.
- Run the skill's pre-delivery checklist (`references/quick-reference.md` and the checklist in its output) before publishing any design change. Check every change on a phone-sized screen too.

## Design skills for the website rebuild (added Nov 9, 2026)

Free, open-source design skills Dan asked for, kept in `.claude/skills/` (licenses inside each folder). Use them together with ui-ux-pro-max; Fig's brand rules in MASTER.md still win (navy, gold, cream, logo; Dan approves any change), and Dan's content rules in MEMORY.md and _build/README.md always apply.

- `impeccable` (Paul Bakaus): design, critique, audit and polish commands that strip "AI slop" from pages. Its launcher scripts were left out on purpose (they download and run a binary), so follow its "Launcher unavailable" path and read PRODUCT.md / DESIGN.md / MASTER.md directly.
- `design-taste-frontend` (taste-skill): layout variety, motion and density rules for company sites. Its stock photo library and its automatic Stop hook were removed. Fig uses real photos of the gym and clients only, never stock or stand-in photos.
- `oil-ui`: builds several design directions side by side to pick from (instructions mostly in Chinese; `README.en.md` is English). Its scripts were left out; never use oiloil image credits (paid).
- `emil-*` (Emil Kowalski): motion and animation rules (`emil-design-eng`, `emil-animate`, reviews, performance, Apple-style design). Keep motion subtle and respect reduced-motion.
- `brand-identity`: logo, type and palette as one system. Only for reviewing or documenting Fig's existing brand, never for replacing it without Dan's approval.
- `dimensional-drawing`: draws components as technical spec sheets (useful for design handoff docs, not for the public site).

Not vendored: Benji Taylor's Stageshow (no license in its repo; install it yourself with `npx skills add https://github.com/benjitaylor/skills --skill stageshow` if needed) and the Awwwards MCP server (an add-on Dan would install in Claude Code himself).

