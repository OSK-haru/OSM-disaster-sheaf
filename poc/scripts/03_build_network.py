#!/usr/bin/env python3
from datetime import date

from core.config import PROCESSED_PATHS, RAW_PATHS, TARGET_CITY, TARGET_SUBREGION
from core.io_utils import normalize_feature_collection, read_geojson, write_geojson


def main() -> None:
    raw = read_geojson(RAW_PATHS['network'])
    features = []
    for idx, feature in enumerate(raw.get('features', []), start=1):
        props = feature.get('properties', {})
        features.append({
            'type': 'Feature',
            'properties': {
                'edge_id': props.get('edge_id', f'E{idx}'),
                'highway': props.get('highway', 'unknown'),
                'walkable': props.get('walkable', 'unknown'),
                'stairs': props.get('stairs', 'unknown'),
                'city': TARGET_CITY,
                'subregion': TARGET_SUBREGION,
                'source_dataset': props.get('source', 'unknown'),
                'ingestion_date': date.today().isoformat(),
            },
            'geometry': feature.get('geometry'),
        })
    write_geojson(PROCESSED_PATHS['network_edges'], normalize_feature_collection('network_edges_normalized', features))
    print(f"wrote {len(features)} network edges -> {PROCESSED_PATHS['network_edges']}")


if __name__ == '__main__':
    main()
