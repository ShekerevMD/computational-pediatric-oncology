# Working conventions

This is primarily a personal training repository. If it becomes shared:

- One analysis = one folder under `projects/` with its own README, config snippet, and figure list.
- No PHI, no restricted BAM/FASTQ/WSI in git.
- Prefer small, tested functions in `src/cpomp/` over notebook-only logic.
- Name branches `year01/...`, `math/...`, or `project/...`.
- Every merged change should leave `pytest -q` green.
