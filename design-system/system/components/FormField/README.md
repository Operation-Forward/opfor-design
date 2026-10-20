Outlined text fields with a visible label, a hint or an inline error; a hand-written static rendition of `mat-form-field appearance="outline"` with the 10px shape from `src/styles/_theme.scss`.

**Markup.** `.lms-field` holds `.box` (the input, optional `.suffix` button such as Show password) and the `label` after it, then `p.hint` or `p.error`. Mark an invalid field `.invalid` with `aria-invalid="true"` and `aria-describedby` pointing at the error.

**Rules.**
- Forms are `novalidate`; errors appear inline under the field and, for server errors, in a `role="alert"` summary at the top. Never a browser bubble.
- Errors say the fix in one sentence: "Enter your password."
- Use `autocomplete` tokens on every personal field; password managers and paste must work.
- Fields stop at `lms-form` (40rem) wide, even on wide screens.
- Angular: `<mat-form-field>` with `<mat-error>{{ control | fieldError }}</mat-error>`.
