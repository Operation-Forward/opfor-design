The page's title block: an optional eyebrow, the one `h1`, a lead, and actions on the right; copied from `src/app/shared/page-header.ts` (`lms-page-header`).

**Markup.** `.lms-page-header > .text` (`p.eyebrow`, `h1`, `p.lead`) and `.actions`. Add `.hero` and `span.motif` with three `<i>` for the landing form: a surface card with three faded clay chevrons at 8%, 14% and 22%.

**Rules.**
- One `h1` per page; focus moves to it after every navigation.
- The eyebrow names the area in uppercase `lms-accent` ("Catalog", "Teach"); the lead is one or two sentences in `lms-muted` at `lms-text-md`.
- Use `.hero` only on landing pages (catalog, sign-in). The chevrons hide under 600px.
- Angular: `<lms-page-header eyebrow="Catalog" heading="Find your next step" lead="…" hero>` with `[actions]` projected.
