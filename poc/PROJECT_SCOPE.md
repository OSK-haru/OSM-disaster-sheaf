# PROJECT_SCOPE.md

## Fixed scope for the current PoC

### Geography
- Target city: Kamisu City, Ibaraki
- Target sub-region: Kamisu area only

### Hazard
- Flood only

### Flood representation
- Use flood polygons

### User profile
- Wheelchair users only

### Wheelchair edge rules
- flood affected edge = blocked
- stairs = blocked
- non-walkable edge = blocked

### Primary objective
Determine whether wheelchair users can reach evacuation shelters during flood conditions,
and identify unreachable zones and their causes.

### Required output format
- GeoJSON

### Minimum successful outputs
1. Shelter GeoJSON
2. Study area GeoJSON
3. Network edges GeoJSON
4. Flood-overlaid constrained edges GeoJSON
5. Reachability result GeoJSON
6. Failure reason GeoJSON
7. One intervention comparison GeoJSON

### Current non-goals
- nationwide support
- multi-hazard support
- polished frontend
- production deployment
- full accessibility realism