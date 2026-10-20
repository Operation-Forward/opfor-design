Filter chips for narrowing a list, and the pace chips on course cards; a static rendition of `mat-chip-option` (catalog filters in `src/app/catalog/catalog.html`) plus `.pace` copied from `course-card.ts`.

**Markup.** A group label `p.lms-filter-label`, then `.lms-chips[role=listbox]` of `button.lms-chip[role=option]` with `aria-selected`; counts go in `.n`. Pace: `.lms-pace` ("Self-paced", on `lms-well`) or `.lms-pace.classes` ("By scheduled class", on `lms-secondary-container`).

**Rules.**
- One selected chip per group; selecting again clears it. Filters live in the URL.
- Chip labels are the values people search by, as the data has them ("command line", "linux").
