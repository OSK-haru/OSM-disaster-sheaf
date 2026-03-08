#!/usr/bin/env python3
from datetime import date

from core.config import PROCESSED_PATHS, RAW_PATHS, TARGET_CITY, TARGET_SUBREGION
from core.io_utils import normalize_feature_collection, read_geojson, write_geojson


def main() -> None:
    raw = read_geojson(RAW_PATHS['flood_polygons'])
    features = []
    for idx, feature in enumerate(raw.get('features', []), start=1):
        props = feature.get('properties', {})
        features.append({
            'type': 'Feature',
            'properties': {
                'flood_id': props.get('flood_id', f'F{idx}'),
                'scenario': props.get('scenario', 'flood'),
                'flood_level_m': float(props.get('flood_level_m', 0.0)),
                'city': TARGET_CITY,
                'subregion': TARGET_SUBREGION,
                'source_dataset': props.get('source', 'unknown'),
                'ingestion_date': date.today().isoformat(),
            },
            'geometry': feature.get('geometry'),
        })
    write_geojson(PROCESSED_PATHS['flood_polygons'], normalize_feature_collection('flood_polygons_normalized', features))
    print(f"wrote {len(features)} flood polygons -> {PROCESSED_PATHS['flood_polygons']}")


if __name__ == '__main__':
    main()
