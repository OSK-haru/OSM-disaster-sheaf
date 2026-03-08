#!/usr/bin/env bash
set -euo pipefail

PYTHONPATH=. python3 scripts/01_load_shelters.py
PYTHONPATH=. python3 scripts/02_select_area.py
PYTHONPATH=. python3 scripts/03_build_network.py
PYTHONPATH=. python3 scripts/04_prepare_flood_polygons.py

echo "Phase 1 outputs generated under data/processed"
