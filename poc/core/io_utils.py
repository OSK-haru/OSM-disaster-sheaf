import json
from pathlib import Path


def read_geojson(path: Path) -> dict:
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def write_geojson(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def normalize_feature_collection(name: str, features: list[dict]) -> dict:
    return {
        'type': 'FeatureCollection',
        'name': name,
        'crs': {
            'type': 'name',
            'properties': {'name': 'urn:ogc:def:crs:EPSG::4326'},
        },
        'features': features,
    }
