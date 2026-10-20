The catalog card for one course; copied from `src/app/catalog/course-card.ts`.

**Markup.** `article.lms-course-card` with an optional `.enrolled` badge, then `.body`: `p.eyebrow` (`.level` in clay, then the category), `h3 > a` (the whole card is this link), `p.summary` (clamped to three lines), a [Chips](#Chips) pace chip and `ul.facts` (duration, lessons, author, each with a 16px icon). A course without an image gets the generated cover (`span.lms-cover` from `course-cover.ts`: a faint diamond pattern, three chevrons and the initial; `.v1`–`.v3` switch it to teal, warning or success tints).

**Rules.**
- The title link covers the card; nothing else in the card is a separate link.
- Hover lifts the card 2px with `lms-shadow-2`; reduced motion keeps it still.
- Cards fill an `auto-fill` grid; never set card widths.
