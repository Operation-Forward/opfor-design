Course progress: a pill track with a clay fill that ends in a forward point; copied from `src/app/shared/progress.ts` (`lms-progress`).

**Markup.** `progress.lms-progress` with `value` from 0 to 1 and a text fallback, under a `.lms-progress-label` that says the progress in words ("3 of 4 lessons", "Week 2 of 4"). The app sets the fill width inline; a `<progress>` element does the same without inline style.

**Rules.**
- Always pair the bar with words; the bar alone is decoration.
- Track `lms-well` ringed by `lms-outline`; fill `lms-accent`.
