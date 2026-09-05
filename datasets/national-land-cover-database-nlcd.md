# National Land Cover Database (NLCD)

| Field | Value |
| --- | --- |
| Status | implemented |
| Selection | selected |
| Implementation | implemented; local code reviewed |
| Entry type | source candidate |
| Topics / series | Vegetation and Land Cover; series assignment unconfirmed |
| Product / version | NLCD 2021 Land Cover L48 in bison series; Annual NLCD is a separate product option |
| Geographic coverage | CONUS for reviewed L48 product |
| Available time coverage | Implemented snapshot: 2021. Annual NLCD initially spans 1985–2023; later releases require their own endpoint/version check |
| Project time coverage | 2021 snapshot |
| Temporal interval | Legacy selected years; Annual NLCD yearly |
| Native spatial resolution / scale | 30 m categorical raster |
| Project output resolution | Source GeoTIFF; downstream habitat target is 30 m EPSG:5070 (constants.py) |
| Source format | GeoTIFF via WCS in reviewed loader |
| Project output format | GeoTIFF subset and downstream habitat outputs |
| Latest observation confirmed | Not checked |
| Documentation reviewed | 2026-09-05; linked provider reference and existing documented specifications |
| Access last tested | Not tested |
| Citation / source terms | Record from the selected product before promotion to documented |

## Product and series details

Do not infer an annual series from the legacy 2021 endpoint. Preserve class legend and categorical resampling method.

[Provider specification](https://www.usgs.gov/centers/eros/science/about-annual-nlcd)

- [Implementation](https://github.com/olc-techsupport/pine_ridge_bison_habitat/blob/150714f7bbe6cab019a3348998e629ec08d76a79/src/loaders.py): load_nlcd_bbox requests NLCD_2021_Land_Cover_L48.

Code inspection records settings; it does not establish a successful run or complete returned coverage.

[Field definitions and review scope](../docs/metadata.md)

## Discovery and access

[Original discovery link](https://www.mrlc.gov/data). Choose the specific collection or layer and document a bounded download, subset query, or manual request before using it in a series.

Confirm product coverage for Pine Ridge and the Northern Great Plains, authentication, source formats and terms. Provider portals can contain many unrelated products; a portal link alone is insufficient for reproducibility.

See the [historical catalog](../docs/original-catalog.md) for original discovery notes, which are not verified specifications. Follow [data governance](../docs/governance.md).
