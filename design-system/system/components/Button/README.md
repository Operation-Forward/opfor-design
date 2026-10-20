Buttons as the LMS themes Angular Material: 12px corners, `lms-text-sm` at weight 600, filled clay for the main action; a hand-written static rendition of `mat-flat-button`, `mat-stroked-button`, `mat-button` and tonal buttons with the overrides in `src/styles/_theme.scss`.

**Markup.** `.lms-btn` plus `filled`, `outlined`, `tonal` (teal container) or `text`; `danger` with `filled` or `outlined` for destructive actions (the app's `.lms-danger-button`); `block` for the full-width form button. Icon-only actions use `.lms-icon-btn` (44px circle) with an `aria-label` naming the action and its object.

**Rules.**
- One filled button per view: the action the page exists for ("Create account", "Sign in", "Save settings").
- Labels are sentence case, a verb and its object. Confirm buttons repeat the verb; Cancel is a text button.
- Targets are at least 44×44px in the app (40px tall buttons sit in 44px rows).
- Angular: `<button mat-flat-button>`; never restyle Material buttons per page.
