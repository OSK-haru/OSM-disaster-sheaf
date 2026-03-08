#!/usr/bin/env python3
from datetime import date

from core.config import PROCESSED_PATHS, RAW_PATHS, TARGET_CITY, TARGET_SUBREGION
from core.io_utils import normalize_feature_collection, read_geojson, write_geojson


def main() -> None:
    raw = read_geojson(RAW_PATHS['shelters'])
    features = []
    for idx, feature in enumerate(raw.get('features', []), start=1):
        props = feature.get('properties', {})
        features.append({
            'type': 'Feature',
            'properties': {
                'shelter_id': props.get('id', f'S{idx}'),
                'name': props.get('name', f'shelter_{idx}'),
                'capacity': int(props.get('capacity', 0)),
                'city': TARGET_CITY,
                'subregion': TARGET_SUBREGION,
                'source_dataset': props.get('source', 'unknown'),
                'ingestion_date': date.today().isoformat(),
            },
            'geometry': feature.get('geometry'),
        })
    write_geojson(PROCESSED_PATHS['shelters'], normalize_feature_collection('shelters_normalized', features))
    print(f"wrote {len(features)} shelters -> {PROCESSED_PATHS['shelters']}")


if __name__ == '__main__':
    main()
