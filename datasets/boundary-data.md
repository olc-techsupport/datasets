# Boundary Data

| Field | Value |
| --- | --- |
| Status | implemented |
| Selection | selected |
| Implementation | implemented; local code reviewed |
| Entry type | local / governed resource |
| Topics / series | Geographic and Spatial Data; series assignment unconfirmed |
| Product / version | Census TIGER/Line 2023 AIANNH in the tutorial |
| Geographic coverage | US AIANNH source filtered to Pine Ridge |
| Available time coverage | Annual boundary vintage; reviewed code selects 2023 |
| Project time coverage | TIGER/Line 2023 vintage; not a measurement time series |
| Temporal interval | Boundary snapshot |
| Native spatial resolution / scale | Vector polygons; positional accuracy is not pixel resolution |
| Project output resolution | Dissolved polygon GeoJSON, EPSG:4326; no pixel size |
| Source format | TIGER/Line zipped Shapefile |
| Project output format | GeoJSON |
| Latest observation confirmed | Not checked |
| Documentation reviewed | Field structure reviewed 2026-09-05; source specifications require the selected product metadata |
| Access last tested | Not tested |
| Citation / source terms | Record from the selected product before promotion to documented |

## Product and series details

Statistical boundary representation must not be equated with an authoritative jurisdictional determination.

- [Implementation](https://github.com/olc-techsupport/data_cube_tutorial/blob/a406384bde03ffd16e392c422ffdc6b9b4fd4dd4/src/cube_utils.py): load_pine_ridge_boundary uses Census TIGER2023 AIANNH, filtered to Pine Ridge. This is not evidence of a BIA layer.

Code inspection records settings; it does not establish a successful run or complete returned coverage.

[Field definitions and review scope](../docs/metadata.md)

## Discovery and access

Provider/access location must be identified. Choose the specific collection or layer and document a bounded download, subset query, or manual request before using it in a series.

Identify the authorized custodian and approved access process. Keep restricted coordinates, credentials, cultural site details and private download links outside this public repository. For reservation boundaries, record the authoritative source, date and intended interpretation before exporting a GIS layer.

See the [historical catalog](../docs/original-catalog.md) for original discovery notes, which are not verified specifications. Follow [data governance](../docs/governance.md).
