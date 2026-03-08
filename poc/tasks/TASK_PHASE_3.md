# TASK_PHASE_3.md

Read `AGENTS.md` and `PROJECT_SCOPE.md` first.

## Phase 3 Goal
Apply the wheelchair feasibility rules to network edges.

## Fixed rules
- flood affected edge = blocked
- stairs = blocked
- non-walkable edge = blocked

## Tasks
1. Implement or update edge feasibility logic.
2. Annotate network edges with:
   - traversable / blocked
   - blocking reason
3. Export constrained edges in GeoJSON.
4. Save one inspection figure of blocked edges.

## Expected outputs
- constrained edges GeoJSON
- blocked_edges.png

## Acceptance criteria
- at least some edges are classified as blocked where appropriate
- blocking reasons are explicit
- logic matches the fixed project scope

## Stop after
Constrained edges are generated and inspectable.
Do not implement intervention logic in this phase.