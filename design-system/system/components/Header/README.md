The sticky site header with the clay-and-teal band, and the site footer; copied from `src/app/layout/shell.scss` (shell.ts).

**Markup.** `header.lms-header > .bar` holds `a.lms-brand` (the CSS chevron mark `span.lms-mark` and `span.lms-wordmark`), `nav.lms-nav` with the current link marked `aria-current="page"`, and `.actions` (theme, notifications, account as 44px icon buttons with `aria-label`s that carry state: "Notifications, 2 unread"). `footer.lms-footer > .inner` holds `.brand` with `.lms-mark.small` and the `.tagline`, then `.meta`.

**Rules.**
- The band is the signature: `lms-accent` for 72% of the width, a forward cut, then `lms-secondary`. Never recolour it outside the tokens.
- The header is sticky at `lms-header-h` (69px) and translucent `lms-paper`; sticky offsets and `scroll-padding-top` use that token.
- Header and footer follow the page's width tier (`.lms-container`, `.full`, `.task`).
- In the Angular app use `lms-shell`; this markup is for sites built without Angular.
