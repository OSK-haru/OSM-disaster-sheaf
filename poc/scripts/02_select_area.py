#!/usr/bin/env python3
from datetime import date

from core.config import PROCESSED_PATHS, RAW_PATHS, TARGET_CITY, TARGET_SUBREGION
from core.io_utils import normalize_feature_collection, read_geojson, write_geojson


def main() -> None:
    raw = read_geojson(RAW_PATHS['study_area'])
    features = []
    for feature in raw.get('features', []):
        props = feature.get('properties', {})
        features.append({
            'type': 'Feature',
            'properties': {
                'area_id': 'A1',
                'name': props.get('name', 'Kamisu Area'),
                'city': TARGET_CITY,
                'subregion': TARGET_SUBREGION,
                'source_dataset': props.get('source', 'unknown'),
                'ingestion_date': date.today().isoformat(),
            },
            'geometry': feature.get('geometry'),
        })
    write_geojson(PROCESSED_PATHS['study_area'], normalize_feature_collection('study_area_normalized', features))
    print(f"wrote {len(features)} study area feature -> {PROCESSED_PATHS['study_area']}")


if __name__ == '__main__':
    main()
