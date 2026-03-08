# TASK_PHASE_2.md

Read `AGENTS.md` and `PROJECT_SCOPE.md` first.

## Phase 2 Goal
Create baseline visualizations and verify spatial alignment.

## Tasks
1. Plot shelters over the network.
2. Plot network with flood polygons.
3. Save quick inspection figures.
4. Confirm CRS consistency and plausible geometry.

## Expected outputs
- baseline_shelters_network.png
- baseline_network_flood.png

## Acceptance criteria
- a human can visually confirm that shelters, network, and flood polygons align plausibly
- obvious data alignment issues are resolved or documented

## Stop after
Baseline spatial sanity checks are complete.
Do not yet compute full reachability if baseline alignment is still broken.

## Execution Log
- Status: completed
- Completion date: 2026-03-08
- Environment: WSL local Python (`.venv/bin/python`)
- Script used:
  - `scripts/05_plot_baseline.py`
- Outputs:
  - `outputs/figures/baseline_shelters_network.png`
  - `outputs/figures/baseline_network_flood.png`
  - `outputs/figures/phase2_sanity_report.md`
