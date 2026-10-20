Operation Forward is a charity, and Operation Forward Learning is its free learning platform. This system is the charity's look, taken from the live learning platform and the logo kit: warm Paper grounds, Ink text, Forward Clay for action, Forward Teal for support, Fraunces headings with Atkinson Hyperlegible for reading, generous space and soft 16px cards. Use it for the LMS, the charity website, emails, certificates, slides and print. In the Angular app the same values arrive as `--lms-*` custom properties and Material's `--mat-sys-*`; elsewhere, load `tokens.css` and `components/bundle.css` and use the `.lms-*` classes.

## Content fundamentals

**Voice: warm, plain, encouraging.** Talk to one adult learner who may be new to tech and short on time. Say what happens and what to do next. Celebrate progress without hype.

- Address the reader as "you"; the charity is "we" ("We've sent a new confirmation link. Check your inbox.").
- Sentence case everywhere, including buttons and headings. No jargon a beginner wouldn't know; when a technical word matters, use it and explain it once.
- Friendly beats formal, but never cute at the reader's expense: "Your learning starts here", "Welcome back. Pick up where you left off.", "You're enrolled. Welcome aboard!"
- Errors say what failed and the fix, never blame: "Couldn't copy. Select the text and copy it manually.", "Enter your password."
- Dates and times in the reader's words: "Starts in 12 days", "Week 2 of 4", "Your class starts Nov 3, 2026."
- One exclamation mark at most, and only for a real welcome or a finished course.

| Do | Don't |
|---|---|
| "Free, practical courses that build real skills, one friendly lesson at a time." | "Unlock your potential with our cutting-edge curriculum!" |
| "Anyone using your account elsewhere will need to sign in again. You'll stay signed in here." | "This action cannot be undone. Proceed?" |
| "Try other words, or clear the filters to see everything." | "0 results." |

**Buttons** are a verb and its object ("Create account", "Download certificate", "Sign out others"); the confirm button repeats the verb. **Eyebrows** name the area in two words or fewer ("Catalog", "Teach"). **The tagline** is "Skills that move people forward."

## Logo

The logo is two forward chevrons, Forward Teal then Forward Clay, beside "Operation Forward" in Fraunces. Files and rules are in the Logos asset group. In product headers the mark is drawn in CSS (`.lms-mark`, two clipped chevrons in `lms-secondary` and `lms-accent`) so it follows the theme; the site name beside it is set in the `wordmark` style. The chevron is the charity's motif: three fading clay chevrons mark hero headers, the header band ends in a forward cut, and the progress fill points forward. Use it as a direction, never as decoration on every surface.

## Visual foundations

### Colour roles

| Brand name | Token | Light | Dark |
|---|---|---|---|
| Paper | `lms-paper` | `#FBF8F3` | `#13171B` |
| Ink / Bone | `lms-ink` | `#1F2A33` | `#ECE7E0` |
| Forward Clay / Light Clay | `lms-accent` | `#B4532A` | `#E58E6C` |
| Forward Teal / Light Teal | `lms-secondary` | `#1F5E5B` | `#7FC6BF` |

- Pages sit on `lms-paper`; cards and fields on `lms-surface`; menus and dialogs on `lms-raised`; tracks and quiet chips on `lms-well`.
- Text is `lms-ink`; leads, summaries and metadata are `lms-muted`. Both hold 4.5:1 on paper, surface, raised and well in both themes (the app's `palette.spec.ts` checks every pair).
- `lms-accent` (clay) is the one action colour: filled buttons, links, eyebrows, the header band, focus rings, progress. `lms-accent-container` is the soft clay ground of the sign-in panel and empty-state badges.
- `lms-secondary` (teal) supports: the first chevron, the band's tail, tonal buttons, selected chips, the scheduled-class pace chip.
- Status: `lms-success`, `lms-warning`, `lms-danger`, each with a `-container` ground. Never rely on colour alone; every status has words or an icon.
- Dividers are `lms-hairline`; control borders are `lms-outline` (3:1).
- The accent is set by an admin at runtime; the app derives `on-accent` and the containers so contrast holds whatever colour is chosen. Write `lms-accent`, never `#B4532A`.

### Light and dark

Both are first-class, plus "match my device" (the default). Dark keeps the warmth: Ink becomes the ground, Bone the text, and clay and teal lighten (`#E58E6C`, `#7FC6BF`) with dark text on filled clay (`lms-on-accent`). Never hard-code white on `lms-accent`.

### Type

- **Fraunces** (variable, 300–800, `'SOFT' 100`) at weight 600 for headings, line height 1.15, letter-spacing −0.012em, balanced wrapping: `h1` 32–42px fluid, `h2` 26–30px, `h3` 24px, `h4` 20px; `display` 40–56px for hero statements; `wordmark` 650 at 20px.
- **Atkinson Hyperlegible Next** (variable, with italic) for all reading: `body` 16px at 1.6, `lead` 18px, `small` 14px, `caption` 13px bold uppercase for card eyebrows; `eyebrow` 14px 600 uppercase at 0.08em in clay. Chosen for low-vision readers: 1, l and I, and 0 and O, stay distinct.
- **Atkinson Hyperlegible Mono** for code and keys at 0.95em.
- Prose stops at `lms-measure` (72ch). The root size steps up once (17px) at 2400px wide.

### Space, shape, depth

- A 4px grid: `lms-space-1` (4) to `lms-space-16` (64). Cards pad 24px; page headers 32px above, 24px below.
- Corners are soft: `lms-radius-card` 16px for cards and panels, 12px (`button-shape`) for buttons, menus and toasts, `lms-radius-control` 10px for fields and selects, 20px (`dialog-shape`) for dialogs, `pill` for chips and progress.
- Depth is gentle: cards carry `lms-shadow-1` and a `lms-hairline` border; hover and the sign-in card use `lms-shadow-2`.

### Layout

- Width tiers, never per-page widths: `lms-measure` for prose, `lms-form` (40rem) for fields, `lms-task` (76rem) for one focused task, `lms-page` (1200 to 2200px, growing with the screen) by default, and full width for data-dense pages. Gutters grow 16 → 24 → 32 → 48 → 64px.
- One scroll: the window is the only vertical scroller. Lists paginate with the [Pager](#Pager); long lessons split into pages.
- Wide screens add columns (a side rail, an outline beside "About"), never longer lines.

### Motion

Restrained: 150ms, 200ms and 250ms on `cubic-bezier(0.2, 0, 0, 1)` for hover, cards lifting 2px and drawers sliding in. Everything stops under `prefers-reduced-motion`.

### Focus

A 3px `lms-focus` (clay) outline with a 2px offset on every control; Material controls use the same ring with 8px corners.

## Iconography

Material Symbols Rounded (Apache 2.0) on a 24px grid, filled outlines, `currentColor`. In the app: `<mat-icon svgIcon="name" />` from the same-origin sprite `public/icons/symbols.svg`. Icons sit before labels and never replace them, except icon buttons, which carry an `aria-label`. 16px icons in card facts and chips, 20px in navigation, 24px elsewhere. No emoji in the interface.

## House rules

- No `alert`, `confirm`, `prompt` or `beforeunload`; confirms use the in-app [Dialog](#Dialog).
- Forms are `novalidate` with inline errors; no `title=` tooltips; no inline `style=""` (the app runs under a strict CSP).
- One overflow menu (`more_vert`) per table row; settings use [SettingsRow](#SettingsRow).
- Every list paginates; nothing scrolls inside the page.
- One `h1` per page; focus moves to it after every navigation.

## Accessibility

Target WCAG 2.2 AA for people on screen readers, keyboards, phones on slow connections and low-vision settings. Every colour pair is tested in both themes and for any runtime accent; axe runs on every route in light and dark. Targets are at least 44×44px; layouts reflow to 320px without sideways scrolling; status changes are announced politely and errors assertively; destructive confirms are `role="alertdialog"` with focus on Cancel.

## Not synced

- Taken from `Operation-Forward/opfor-lms-frontend@8ac8485` and the logo kit: every colour token (`src/app/core/theme/palette.ts`), type sizes, spacing, radii, shadows and widths (`src/styles/_theme.scss`), the four font files, 12 logo SVGs, and 32 of 122 icons.
- Skipped: `--lms-player` and the `--mat-sys-*` mapping (they reference other variables), motion values (kept in `components/bundle.css`), lesson typography (`src/styles/_prose.scss`, written in Sass), the PNG logo exports and `favicon.ico`.
- Components are static renditions: Header, PageHeader, EmptyState, ErrorState, Progress, Pager, CourseCard and SettingsRow copy the app's own CSS; Button, FormField, Chips, Dialog and Toast are hand-written renditions of the Angular Material components with the app's overrides. The Angular app itself is not bundled.
