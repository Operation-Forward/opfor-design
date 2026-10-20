The one paginator for every list: range, page size, "Page n of m", Previous and Next; copied from `src/app/shared/pager.ts` (`lms-pager`).

**Markup.** `nav.lms-pager[aria-label]` with the range in a polite live region, `label.size` with a `select` (and a hidden note that changing it returns to page 1), and `.buttons` with outlined Previous / Next.

**Rules.**
- Page and size live in the URL (`?page=&per_page=`), defaults omitted.
- Lists paginate; nothing scrolls inside the page.
