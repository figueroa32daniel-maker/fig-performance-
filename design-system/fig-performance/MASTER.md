# Design System Master File: Fig Performance

> **How to use:** before changing any page's look, read this file. If `design-system/fig-performance/pages/<page>.md` exists, its rules override this file for that page. Generated with the UI/UX Pro Max skill (Luxury/Premium Brand, variance 4, density 3), then adjusted by hand to Fig Performance's existing brand. Chosen by Dan on Nov 3, 2026: **Premium + Editorial**.

**Direction:** premium, calm, confident. Swiss-style minimalism on the homepage and service pages (strong grid, lots of space, few elements, one clear action per section). Editorial / magazine style on articles (see `pages/articles.md`). Feels like a high-end private coach, not a big-box gym or a startup.

**Audience:** adults over 40, busy professionals, many with old injuries. They want trust, clarity and real results, not hype.

---

## Color (use the CSS variables in `assets/styles.css`, never raw hex in new components)

| Role | Variable | Hex | Use |
|------|----------|-----|-----|
| Primary / brand | `--navy` | `#0f1f3d` | Primary buttons, headings, dark sections |
| Primary hover | `--navy-2` | `#172a4f` | Hover on navy |
| Deep navy | `--navy-3` | `#0a1530` | Footer, deepest backgrounds |
| Accent (decorative) | `--gold` | `#b88939` | Rules, dots, icons, borders only. Never body text |
| Gold text on light | `--gold-text` | `#7a5a1e` | Small labels and kickers on cream/white (passes AA) |
| Gold on navy | `--gold-light` | `#d1a65a` | Labels, links and the gold button on navy |
| Background | `--cream` | `#f5f0e8` | Default page background |
| Alt background | `--beige` | `#ede6da` | Hero and alternating sections |
| Card | `--white` | `#ffffff` | Cards, article body |
| Text | `--text` | `#1a1f2b` | Body text on light |
| Muted text | `--muted` | `#4a4f5c` | Secondary text (6.6:1 on beige) |
| Hairline | `--line` | `#ddd4c4` | Borders and dividers on light |
| Text on navy | `--on-navy` / `--on-navy-muted` | `#e9e4da` / `#b9c1d1` | Copy on navy sections |

Rules: one accent (gold), used sparingly. No new colors without Dan's approval. Contrast 4.5:1 minimum for text.

## Typography

- **Headings:** Montserrat (`--font-head`), self-hosted variable font. Bold weights.
- **Body:** Inter (`--font-body`), self-hosted. Base 16px or larger, line-height 1.5 to 1.65.
- **Kickers / labels:** Montserrat, small, uppercase, wide letter-spacing, gold, with the short gold rule before them. This is a signature brand element; keep it.
- **Headline case:** ALL CAPS only for short headlines (about 6 words or fewer, like the homepage hero). Longer headlines, including every article H1, use sentence case.
- No third typeface. Don't load Google Fonts; the fonts are self-hosted.

## Spacing (spacious, density 3/10)

| Token | Value | Use |
|-------|-------|-----|
| xs | 4px | Tight gaps |
| sm | 8px | Icon and inline gaps |
| md | 24px | Card padding |
| lg | 32px | Group spacing |
| xl | 48px | Between blocks inside a section |
| 2xl | 64px | Section padding (mobile) |
| 3xl | 96px | Section padding (desktop), hero |

Generous white space is part of the premium feel. When in doubt, add space and remove elements.

## Shape and depth

- Radius: `--radius` 6px on buttons, cards and inputs. Don't mix in pill or 16px+ radii.
- Shadows: soft navy-tinted (`--shadow`, `--shadow-sm`). Use on hero media and featured cards only.
- Borders: 1px `--line` hairlines. Gold top border (3px) marks featured cards and tables.

## Components

- **Primary button:** navy fill, white text (`.btn .btn-primary`). One per section.
- **Secondary button:** outline (`.btn .btn-secondary`).
- **Gold button:** on navy backgrounds only (`.btn .btn-gold`).
- **Cards:** white, 1px line border or soft shadow, 24px padding. Hover may lift 2px; no scale transforms.
- **Tables:** `.price-table` (with `.compare-table` when text needs to wrap on phones).
- **Icons:** inline SVG, single consistent line style. Never emoji.

## Imagery (the biggest upgrade still to make)

- Lead with people: Dan coaching a client, real clients training (with written OK), the gym and equipment. Real photos only. No stock photos of models.
- Warm, natural light, slightly desaturated so the photos sit with navy and cream. Avoid blown-out or washed-out images.
- Every image needs width/height set, WebP plus JPG fallback, lazy loading below the fold, and descriptive alt text.

## Motion

- Subtle only: 150–300ms ease transitions, gentle fade/rise on scroll. No parallax, no bouncy or fast animation.
- Respect `prefers-reduced-motion` (show everything in its final state).

## Page pattern (homepage and service pages)

Hero (value prop and one primary action) → proof (results, reviews) → how it works → offer and pricing → coach → FAQ → final CTA. Keep the CTA visible: header button, after the offer, and at the bottom. Navigation: about 5 items plus the Book button.

## Avoid

- Cheap-looking visuals, stock photos, clip art, emoji icons
- Busy layouts, too many colors, gradients, glassmorphism or "liquid glass" effects
- Fast or flashy animation, layout-shifting hovers
- Long ALL CAPS headlines
- Computer-style dates ("2026-11-03"). Write "Nov 3, 2026"
- Low-contrast gray-on-gray text, invisible focus states

## Pre-delivery checklist

- [ ] Uses the variables above; no new colors or fonts
- [ ] Text contrast 4.5:1 or better; visible focus states; `cursor: pointer` on clickable elements
- [ ] Touch targets at least 44×44px
- [ ] Hover and transitions 150–300ms; `prefers-reduced-motion` respected
- [ ] Images sized, compressed (WebP), lazy-loaded, with alt text; no layout shift
- [ ] Checked at 375px, 768px, 1024px and 1440px; no horizontal scroll on phones
- [ ] Nothing hidden behind the sticky header
- [ ] Dan approved the change before it goes live
