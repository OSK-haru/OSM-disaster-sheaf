# TASK_PHASE_1.md

Read `AGENTS.md` and `PROJECT_SCOPE.md` first.

## Phase 1 Goal
Load and normalize the minimum datasets for the Kamisu area PoC.

## Required datasets
- shelter data
- flood polygons
- road/walkable network

## Tasks
1. Implement shelter loading and normalization.
2. Define and save the study area.
3. Build or download the road/walkable network for the study area.
4. Load and prepare flood polygons.
5. Align coordinate reference systems.

## Expected outputs
- normalized shelters GeoJSON
- study area GeoJSON
- network artifact
- flood polygon artifact

## Acceptance criteria
- shelter points are spatially usable
- study area is defined
- network is constructed for the study area
- flood polygons are spatially aligned with the network

## Stop after
The required datasets are available in usable form.
Do not begin failure reasoning or intervention here.

## Execution Log
- Status: completed
- Completion date: 2026-03-08
- Method: local seed data normalization
- Scripts used:
  - `scripts/01_load_shelters.py`
  - `scripts/02_select_area.py`
  - `scripts/03_build_network.py`
  - `scripts/04_prepare_flood_polygons.py`
  - `scripts/run_phase1.sh`
- Outputs:
  - `data/processed/shelters.geojson`
  - `data/processed/study_area.geojson`
  - `data/processed/network_edges.geojson`
  - `data/processed/flood_polygons.geojson`
