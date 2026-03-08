# AGENTS.md
## Kamisu City Flood Evacuation Accessibility PoC

This file defines the global context, goals, constraints, execution principles, and phase structure for this project.

All agents must read this file first.

---

# 1. Project identity

## Project title
Flood-time evacuation accessibility PoC for wheelchair users in Kamisu City (Kamisu area), Ibaraki.

## Core question
Can publicly available local data already reveal zones in Kamisu City where wheelchair users cannot feasibly reach evacuation shelters during flood conditions?

## Short answer we want to test
Yes: by combining shelter data, road/walkable network data, and flood polygons, it should be possible to compute reachable and unreachable zones, explain why unreachable zones occur, and show how a simple intervention changes the result.

---

# 2. Background and motivation

In disaster planning, many local datasets are already publicly available:
- evacuation shelters
- hazard maps
- road and path networks
- accessibility-relevant edge properties

However, these data are usually published separately.
Even if each local dataset is individually useful, this does not automatically mean that evacuation is globally feasible for a given mobility profile.

This project focuses on the following practical gap:

A city may publish shelters and hazard information, but wheelchair users may still be unable to reach any shelter under flood conditions because:
- flood-affected edges become impassable
- stairs break continuity
- non-walkable network segments interrupt routes
- local feasible fragments do not combine into a globally feasible evacuation path

This PoC is not merely a map viewer.
It is a diagnostic prototype for evacuation feasibility.

Its value lies in:
- detecting unreachable zones
- explaining why they are unreachable
- supporting planning and prioritization
- demonstrating that public local data can already expose structural evacuation failures

---

# 3. Why this project matters

The point is not just to say “this place is dangerous.”
The point is to compute:

- whether a wheelchair user can actually reach a shelter
- where the city-wide structure fails
- which constraint causes failure
- whether a simple intervention reduces the failure

This is closer to an evacuation feasibility audit tool than to a consumer navigation app.

---

# 4. Fixed scope decisions

These decisions are already fixed and must not be changed unless explicitly instructed by the user.

## Geography
- City: Kamisu City, Ibaraki
- Sub-region: Kamisu area only
- Do not expand to all Japan
- Do not expand to multiple cities
- Start from a smaller study area if necessary

## Hazard type
- Flood only

## Flood representation
- Use flood polygons because they are easier to handle in this PoC

## Mobility profile
- Wheelchair users only

## Wheelchair feasibility rules
Use the following minimal rules exactly unless explicitly revised later:
- flood affected edge = blocked
- stairs = blocked
- non-walkable edge = blocked

## Output format
- GeoJSON is the primary output format

---

# 5. Research hypotheses

## Main hypothesis
Using public data in Kamisu City (Kamisu area), it is possible to detect zones where wheelchair users cannot reach evacuation shelters during flood conditions.

## Secondary hypothesis
These unreachable zones can be explained by concrete local constraints that fail to combine into globally feasible evacuation paths.

## Intervention hypothesis
A simple hypothetical intervention can measurably reduce the number or spatial extent of unreachable zones.

---

# 6. Non-goals

The following are explicitly out of scope for the current PoC:
- nationwide support
- multiple hazard types
- real-time disaster operations
- production deployment
- mobile app distribution
- polished frontend
- fully rigorous mathematical sheaf implementation
- perfect accessibility realism
- full population simulation
- legal or official evacuation advice
- complete barrier-free semantics for every edge

If a task drifts toward these, deprioritize it.

---

# 7. Definition of success

The PoC is successful if all of the following are achieved:

1. A study area in Kamisu area is selected and documented.
2. Shelter data is loaded and normalized.
3. A walkable/road network is constructed for the study area.
4. Flood polygons are spatially aligned with the network.
5. Wheelchair feasibility rules are applied to edges.
6. Reachability to shelters is computed from sampled origins.
7. Reachable and unreachable outputs are exported in GeoJSON.
8. At least 3 failure reason categories are produced.
9. One simple intervention scenario is compared with baseline.

Optional but beneficial:
- static figures
- concise report
- small local API or lightweight viewer

---

# 8. Execution principles

## Work incrementally
Do not build the full system at once.
Each phase must be independently runnable and produce persistent artifacts.

## Preserve artifacts
Every phase must leave behind inspectable outputs:
- processed data
- GeoJSONs
- figures
- reports
- logs or summary text if helpful

## Prefer explicitness
If assumptions are simplified, document them explicitly.
Do not silently invent domain logic.

## Prefer reproducibility
Use scripts and modules instead of relying only on notebooks.

## Stop cleanly
If blocked, stop at the nearest coherent phase boundary, report what works, and preserve outputs.

---

# 9. Data and modeling assumptions

## Required data types
- Shelter data
- Flood polygons
- Road/walkable network

## Minimal accessibility model
The first version should use exactly these rules:
- flood affected edge = blocked
- stairs = blocked
- non-walkable edge = blocked

Do not add complex slope, curb, or surface models in early phases unless the user explicitly asks for it.

## Reachability model
Use a simple and explainable graph-based reachability model.
It is acceptable to sample origins using:
- regular grid points
- sampled nodes
- representative origin points

Do not wait for a perfect demand model.

---

# 10. Output requirements

## Required GeoJSON outputs
At minimum, produce:
- normalized shelters GeoJSON
- study area GeoJSON
- network edges GeoJSON
- constrained/annotated network edges GeoJSON
- reachability results GeoJSON
- failure reason GeoJSON
- intervention comparison GeoJSON if applicable

## Suggested figures
- shelters over network
- network with flood overlay
- blocked edges
- reachable/unreachable map
- failure reason map
- intervention comparison map

## Suggested report
- one concise markdown or html summary

---

# 11. Phase structure

This project must be executed in phases.
Do not skip ahead unless an earlier phase is already complete.

## Phase 0
Bootstrap repository and freeze scope.

## Phase 1
Load and normalize data:
- shelters
- study area
- network
- flood polygons

## Phase 2
Create baseline visualization and data sanity checks.

## Phase 3
Apply wheelchair feasibility rules to network edges.

## Phase 4
Compute shelter reachability from origins.

## Phase 5
Explain failure reasons.

## Phase 6
Run one simple intervention scenario.

## Phase 7
Package outputs for inspection.

---

# 12. Stop conditions and fallback behavior

## If flood polygon ingestion is hard
Use a documented intermediate representation, but remain polygon-based.

## If the first study area is trivial
If everything is reachable or everything is unreachable:
- inspect assumptions
- inspect shelter filtering
- inspect blocked-edge logic
- minimally adjust the study area or assumptions
- document the change

Do not manipulate results dishonestly.

## If time runs short
Priority order:
1. shelters
2. network
3. flood polygons
4. feasibility rules
5. reachability
6. failure reasons
7. intervention
8. packaging
9. API/frontend

---

# 13. Recommended project structure

poc/
  AGENTS.md
  PROJECT_SCOPE.md
  README.md
  tasks/
    TASK_CURRENT.md
    TASK_PHASE_0.md
    TASK_PHASE_1.md
    TASK_PHASE_2.md
    TASK_PHASE_3.md
    TASK_PHASE_4.md
    TASK_PHASE_5.md
    TASK_PHASE_6.md
    TASK_PHASE_7.md
  data/
    raw/
    processed/
  notebooks/
  scripts/
  core/
  api/
  frontend/
  outputs/
    figures/
    geojson/

---

# 14. Engineering expectations

Prefer creating or using files like:
- scripts/01_load_shelters.py
- scripts/02_select_area.py
- scripts/03_build_network.py
- scripts/04_prepare_flood_polygons.py
- scripts/05_plot_baseline.py
- scripts/06_apply_feasibility.py
- scripts/07_compute_reachability.py
- scripts/08_explain_failures.py
- scripts/09_run_intervention.py

Core modules may include:
- core/config.py
- core/io_utils.py
- core/feasibility.py
- core/reachability.py
- core/explanations.py
- core/plotting.py

This file list is guidance, not a rigid mandate.

---

# 15. Final expected story of the PoC

By the end of this project, the outputs should support the following narrative:

- We selected a study area in Kamisu area, Kamisu City.
- We loaded shelter data, flood polygons, and a walkable network.
- We modeled wheelchair movement under flood conditions with explicit simple rules.
- We computed which origins can or cannot reach shelters.
- We exported GeoJSON outputs showing reachable and unreachable zones.
- We categorized the reasons for failure.
- We demonstrated one simple intervention that changes the result.

If this story is supported by artifacts, the PoC is successful.

---