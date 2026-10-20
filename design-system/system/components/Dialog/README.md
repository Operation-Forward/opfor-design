Confirm before acting, and short tasks; a static rendition of `mat-dialog` with the 20px shape and a Fraunces title, as `ConfirmService.confirm()` builds it.

**Markup.** A native `dialog.lms-dialog` (`role="alertdialog"` for confirms) with `h2`, `.content` and `.actions` (Cancel as a text button, then the action).

**Rules.**
- Never `confirm()`, `alert()` or `prompt()`.
- The title asks the action as a question ("Sign out of all other devices?"); the message says what happens and what stays.
- The confirm button repeats the verb ("Sign out others"); destructive ones are `danger` and start with focus on Cancel.
