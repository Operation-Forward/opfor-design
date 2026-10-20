Settings and long forms as rows: a heading and one-line explanation on the left, the fields on the right, stacked on phones; copied from `.lms-settings-row` in `src/styles/_base.scss`.

**Markup.** `section.lms-settings-row[aria-labelledby]` with `.intro` (`h2`, `p`) and `.fields` (form fields, then `.lms-form-actions` with the filled Save button in the last row).

**Rules.**
- Never a grid of cards for settings.
- The intro says what the setting changes for people ("Your name and logo appear in the header, browser tabs, emails and certificates.").
- Fields stop at `lms-form` wide; the intro column is at most 20rem.
