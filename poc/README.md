# Kamisu Flood Evacuation Accessibility PoC

## Purpose
This repository hosts a phased PoC to test flood-time evacuation accessibility for wheelchair users in the Kamisu area of Kamisu City, Ibaraki.

## Fixed scope
- Geography: Kamisu City, Kamisu area only
- Hazard: flood only
- Flood representation: polygons
- User profile: wheelchair users only
- Wheelchair rules:
  - flood affected edge = blocked
  - stairs = blocked
  - non-walkable edge = blocked
- Output format: GeoJSON

## Non-goals
- nationwide or multi-city expansion
- multi-hazard support
- production deployment
- polished frontend
- full accessibility realism

## Phase status
- Phase 0: completed (2026-03-08)
- Phase 1: ready

## Repository layout
- `tasks/`: phase task files
- `data/raw/`: raw datasets
- `data/processed/`: normalized datasets
- `scripts/`: runnable scripts
- `core/`: reusable modules
- `outputs/geojson/`: exported GeoJSON outputs
- `outputs/figures/`: exported figures

## How to run
1. Read `AGENTS.md` and `PROJECT_SCOPE.md`.
2. Check `tasks/TASK_CURRENT.md`.
3. Run only the active phase scripts.

Example for future phases:
```bash
PYTHONPATH=. python3 scripts/<phase_script>.py
```
