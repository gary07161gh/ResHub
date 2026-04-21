# Resolution Hub UI Polish

## Summary

Refine the existing single-file app into a cleaner, more restrained workspace UI while keeping every feature, the localStorage data model, and the no-dependency Chrome-on-Windows-11 runtime intact. The redesign will be shadcn-inspired in feel, but implemented entirely inside `Resolution Hub.html` with the current React CDN, Tailwind CDN, and Babel setup.

## Key Changes

- Rebuild the visual system around a tighter neutral palette, softer surfaces, and more consistent spacing so the app feels less heavy and more intentional.
- Simplify the shell:
  - lighten the sidebar treatment
  - reduce competing accents
  - make the primary workspace read more clearly at a glance
- Polish the dashboard:
  - restyle KPI cards into a more understated metrics row
  - tighten the filter/search toolbar
  - improve table and kanban readability with cleaner row, column, and empty-state treatment
- Polish case detail:
  - strengthen section hierarchy for customer data, status, notes, and latest action
  - reduce border noise
  - make the action blocks feel more polished and less dense
- Bring dialogs and the tasks panel into the same visual system so settings, history, delete confirmation, and personal tasks feel like part of one product rather than separate fragments.
- Keep dark mode, print, import/export, and all existing workflows unchanged.

## Test Plan

- Open the app in Google Chrome on Windows 11 and verify the app loads with no console errors.
- Smoke test these flows:
  - dashboard search, status filtering, and view switching
  - table and kanban modes
  - case detail editing and navigation back to queue
  - settings, history, delete confirmation, and tasks panel
  - import/export, CSV export, and print preview
  - dark mode persistence across refresh
- Check empty-state rendering and a populated-case state to make sure the new layout still works when data is sparse or dense.
- Confirm the updated spacing, contrast, and controls remain usable at common desktop widths and do not introduce overflow or clipping.

## Assumptions

- The requested change is a conservative polish, not a full brand redesign.
- No new packages, fonts, or assets will be added.
- The app should stay as one HTML file and continue relying only on the current CDN-based React/Tailwind/Babel setup.
- The goal is visual cleanup and hierarchy, not feature rework or data-model changes.
