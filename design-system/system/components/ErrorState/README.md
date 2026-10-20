What a page shows when it can't load, and the lock notice for content that isn't open yet; copied from `src/app/shared/error-state.ts` (`lms-error-state`) and `offline-banner.ts`.

**Markup.** `.lms-error-state[role=alert]` with `.icon` and the text (`h2`, `p`, `.actions` with Try again and `.ref`, the request id for support). `.gate` turns it into a lock notice in clay ("Your class hasn't started yet"). `.lms-offline[role=status]` is the full-width banner under the header while the browser is offline.

**Rules.**
- Say what failed in plain words and keep the rest of the page usable. Always show the request id on load failures.
- A locked lesson names the day it opens; it is text, never a dead link.
