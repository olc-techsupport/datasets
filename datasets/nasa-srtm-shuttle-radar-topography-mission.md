# NASA SRTM (Shuttle Radar Topography Mission)

| Field | Value |
| --- | --- |
| Status | implemented |
| Selection | selected |
| Implementation | implemented; local code reviewed |
| Entry type | source candidate |
| Topics / series | Elevation and Topography; series assignment unconfirmed |
| Product / version | SRTM 1 Arc-Second Global; local loader reads AWS Skadi HGT tiles |
| Geographic coverage | Approximately 60 N to 56 S |
| Available time coverage | Acquisition February 11–22, 2000; record distribution/reprocessing version separately |
| Project time coverage | February 2000 acquisition; downloaded tile revision not recorded here |
| Temporal interval | Static elevation surface |
| Native spatial resolution / scale | 1 arc-second (approximately 30 m); 3 arc-second products are separate |
| Project output resolution | Loader mosaic EPSG:4326 at 1 arc-second; downstream target 30 m EPSG:5070 |
| Source format | Compressed HGT tiles in reviewed loader |
| Project output format | GeoTIFF mosaic |
| Latest observation confirmed | Not checked |
| Documentation reviewed | 2026-09-05; linked provider reference and existing documented specifications |
| Access last tested | Not tested |
| Citation / source terms | Record from the selected product before promotion to documented |

## Product and series details

Loader enforces 3601 × 3601 samples per one-degree tile. Its constants/provenance comments mentioning GL3/90 m disagree with the executable loader; confirm cached raster metadata before analysis.

[Provider specification](https://doi.org/10.5066/F7PR7TFT)

- [Implementation](https://github.com/olc-techsupport/pine_ridge_bison_habitat/blob/150714f7bbe6cab019a3348998e629ec08d76a79/src/loaders.py): load_srtm_dem validates 3601-sample tiles and 1/3600-degree spacing.

Code inspection records settings; it does not establish a successful run or complete returned coverage.

[Field definitions and review scope](../docs/metadata.md)

## Discovery and access

[Original discovery link](https://www.earthdata.nasa.gov/data/instruments/srtm). Choose the specific collection or layer and document a bounded download, subset query, or manual request before using it in a series.

Confirm product coverage for Pine Ridge and the Northern Great Plains, authentication, source formats and terms. Provider portals can contain many unrelated products; a portal link alone is insufficient for reproducibility.

See the [historical catalog](../docs/original-catalog.md) for original discovery notes, which are not verified specifications. Follow [data governance](../docs/governance.md).
