A short, polite message after something happened; a static rendition of `mat-snack-bar` (12px shape, inverse colours) as `ToastService.success/info/error` shows it.

**Markup.** `.lms-toast[role=status]` with `p` and an optional text action in `lms-inverse-accent`; `.error` uses the danger container and `role="alert"`.

**Rules.**
- Say the result as a person would: "You're enrolled. Welcome aboard!", "Copied to the clipboard."
- Errors say what to do next: "Couldn't copy. Select the text and copy it manually."
- Never put the only copy of important information in a toast.
