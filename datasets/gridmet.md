# GridMET

| Field | Value |
| --- | --- |
| Status | implemented |
| Selection | selected |
| Implementation | implemented; local code reviewed |
| Entry type | source candidate |
| Topics / series | Climate Data; series assignment unconfirmed |
| Product / version | gridMET surface meteorology; release not pinned in loader |
| Geographic coverage | CONUS; check variable-specific extent |
| Available time coverage | 1979 onward; latest delivered date must be read from returned data |
| Project time coverage | Caller supplies start_year/end_year; no universal project period |
| Temporal interval | Daily for primary meteorological variables |
| Native spatial resolution / scale | 1/24 degree (approximately 4 km) |
| Project output resolution | Point CSV from native grid; no spatial raster output established |
| Source format | NetCDF via OPeNDAP in reviewed helper |
| Project output format | Point time-series CSV |
| Availability checked | No live availability check in this metadata review |
| Latest observation confirmed | Not checked |
| Documentation reviewed | 2026-09-05; linked provider reference and existing documented specifications |
| Access last tested | Not tested |
| Citation / source terms | Record from the selected product before promotion to documented |

## Product and series details

Daily operational updates can lag. Angular cell size is not a constant distance in both directions.

[Provider specification](https://www.climatologylab.org/gridmet.html)

- [Implementation](https://github.com/olc-techsupport/data_cube_tutorial/blob/a406384bde03ffd16e392c422ffdc6b9b4fd4dd4/src/cube_utils.py): fetch_gridmet_point takes start_year/end_year and selects a nearest grid cell.

Code inspection records settings; it does not establish a successful run or complete returned coverage.

[Field definitions and review scope](../docs/metadata.md)

## Discovery and access

[Original discovery link](https://www.climatologylab.org/gridmet.html). Choose the specific collection or layer and document a bounded download, subset query, or manual request before using it in a series.

Confirm product coverage for Pine Ridge and the Northern Great Plains, authentication, source formats and terms. Provider portals can contain many unrelated products; a portal link alone is insufficient for reproducibility.

See the [historical catalog](../docs/original-catalog.md) for original discovery notes, which are not verified specifications. Follow [data governance](../docs/governance.md).
