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