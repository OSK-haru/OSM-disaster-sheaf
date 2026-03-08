#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
PROCESSED = ROOT / 'data' / 'processed'
FIGURES = ROOT / 'outputs' / 'figures'


def load_geojson(path: Path) -> dict:
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def crs_name(fc: dict) -> str:
    return fc.get('crs', {}).get('properties', {}).get('name', '')


def plot_points(ax, features: list[dict], color: str, label: str) -> None:
    xs, ys = [], []
    for ft in features:
        geom = ft.get('geometry', {})
        if geom.get('type') != 'Point':
            continue
        x, y = geom.get('coordinates', [None, None])
        if x is not None and y is not None:
            xs.append(x)
            ys.append(y)
    if xs:
        ax.scatter(xs, ys, c=color, s=35, label=label, zorder=3)


def plot_lines(ax, features: list[dict], color: str, label: str) -> None:
    has = False
    for ft in features:
        geom = ft.get('geometry', {})
        if geom.get('type') != 'LineString':
            continue
        coords = geom.get('coordinates', [])
        if len(coords) < 2:
            continue
        xs = [c[0] for c in coords]
        ys = [c[1] for c in coords]
        ax.plot(xs, ys, color=color, linewidth=1.3, alpha=0.9, zorder=2)
        has = True
    if has:
        ax.plot([], [], color=color, linewidth=2, label=label)


def plot_polygons(ax, features: list[dict], edge: str, face: str, label: str) -> None:
    has = False
    for ft in features:
        geom = ft.get('geometry', {})
        if geom.get('type') != 'Polygon':
            continue
        rings = geom.get('coordinates', [])
        if not rings:
            continue
        ring = rings[0]
        xs = [c[0] for c in ring]
        ys = [c[1] for c in ring]
        ax.fill(xs, ys, facecolor=face, edgecolor=edge, alpha=0.25, linewidth=1.2, zorder=1)
        has = True
    if has:
        ax.plot([], [], color=edge, linewidth=2, label=label)


def save_report(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main() -> None:
    shelters = load_geojson(PROCESSED / 'shelters.geojson')
    study_area = load_geojson(PROCESSED / 'study_area.geojson')
    network = load_geojson(PROCESSED / 'network_edges.geojson')
    floods = load_geojson(PROCESSED / 'flood_polygons.geojson')

    FIGURES.mkdir(parents=True, exist_ok=True)

    fig1, ax1 = plt.subplots(figsize=(8, 6))
    plot_polygons(ax1, study_area.get('features', []), edge='#0B3C5D', face='#9FD3C7', label='study area')
    plot_lines(ax1, network.get('features', []), color='#1D7874', label='network')
    plot_points(ax1, shelters.get('features', []), color='#D7263D', label='shelters')
    ax1.set_title('Baseline: Shelters over Network')
    ax1.set_xlabel('Longitude')
    ax1.set_ylabel('Latitude')
    ax1.grid(True, linestyle=':', alpha=0.4)
    ax1.legend(loc='best')
    fig1.tight_layout()
    fig1_path = FIGURES / 'baseline_shelters_network.png'
    fig1.savefig(fig1_path, dpi=180)
    plt.close(fig1)

    fig2, ax2 = plt.subplots(figsize=(8, 6))
    plot_lines(ax2, network.get('features', []), color='#264653', label='network')
    plot_polygons(ax2, floods.get('features', []), edge='#9D0208', face='#F4A261', label='flood polygons')
    plot_points(ax2, shelters.get('features', []), color='#3A86FF', label='shelters')
    ax2.set_title('Baseline: Network with Flood Overlay')
    ax2.set_xlabel('Longitude')
    ax2.set_ylabel('Latitude')
    ax2.grid(True, linestyle=':', alpha=0.4)
    ax2.legend(loc='best')
    fig2.tight_layout()
    fig2_path = FIGURES / 'baseline_network_flood.png'
    fig2.savefig(fig2_path, dpi=180)
    plt.close(fig2)

    expected_crs = 'urn:ogc:def:crs:EPSG::4326'
    checks = {
        'shelters': crs_name(shelters),
        'study_area': crs_name(study_area),
        'network_edges': crs_name(network),
        'flood_polygons': crs_name(floods),
    }
    mismatches = {k: v for k, v in checks.items() if v != expected_crs}

    report = [
        '# Phase 2 Sanity Report',
        '',
        '## Geometry counts',
        f"- shelters: {len(shelters.get('features', []))}",
        f"- study_area: {len(study_area.get('features', []))}",
        f"- network_edges: {len(network.get('features', []))}",
        f"- flood_polygons: {len(floods.get('features', []))}",
        '',
        '## CRS checks',
        f"- expected: {expected_crs}",
    ]
    for k, v in checks.items():
        report.append(f"- {k}: {v}")
    report.append('')
    report.append(f"- CRS consistent: {'yes' if not mismatches else 'no'}")

    report_path = FIGURES / 'phase2_sanity_report.md'
    save_report(report_path, report)

    print(f'wrote: {fig1_path}')
    print(f'wrote: {fig2_path}')
    print(f'wrote: {report_path}')


if __name__ == '__main__':
    main()
