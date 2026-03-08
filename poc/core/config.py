from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT_DIR / 'data' / 'raw'
PROCESSED_DIR = ROOT_DIR / 'data' / 'processed'

TARGET_CITY = 'Kamisu City, Ibaraki'
TARGET_SUBREGION = 'Kamisu area'

RAW_PATHS = {
    'shelters': RAW_DIR / 'shelters' / 'shelters_seed.geojson',
    'study_area': RAW_DIR / 'study_area' / 'study_area_seed.geojson',
    'network': RAW_DIR / 'network' / 'network_seed.geojson',
    'flood_polygons': RAW_DIR / 'flood_polygons' / 'flood_seed.geojson',
}

PROCESSED_PATHS = {
    'shelters': PROCESSED_DIR / 'shelters.geojson',
    'study_area': PROCESSED_DIR / 'study_area.geojson',
    'network_edges': PROCESSED_DIR / 'network_edges.geojson',
    'flood_polygons': PROCESSED_DIR / 'flood_polygons.geojson',
}
