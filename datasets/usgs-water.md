# USGS Water Data for the Nation

| Field | Value |
| --- | --- |
| Status | implemented |
| Selection | selected |
| Implementation | implemented; local code reviewed |
| Entry type | product / product family |
| Topics / series | Water monitoring (proposed; existing local implementation identified). |
| Product / version | USGS modern Water Data API collections; station, parameter and statistic define a series |
| Geographic coverage | US monitoring network; project selects Tribal-region sites |
| Available time coverage | Station/parameter specific; report actual returned minimum/maximum separately from request bounds |
| Project time coverage | Configured analysis 2000–2024; groundwater loader default 1980 onward; actual site coverage varies |
| Temporal interval | Continuous/daily series or irregular field measurements, depending on collection |
| Native spatial resolution / scale | Monitoring-location points; no raster cell size |
| Project output resolution | Point observations/time-series tables; no native raster resolution |
| Source format | Product/access-route dependent |
| Project output format | Not recorded |
| Availability checked | No live availability check in this metadata review |
| Latest observation confirmed | Not checked |
| Documentation reviewed | 2026-09-05; linked provider reference and existing documented specifications |
| Access last tested | Not tested unless a validation record is linked below. |

## Product and series details

Retain units, qualifiers and missing intervals. A configured analysis period does not prove uninterrupted station coverage.

Format details: OGC responses: GeoJSON/JSON. Parquet time series and separate site GeoJSON would be project outputs; no conversion pipeline is provided here.

[Provider specification](https://api.waterdata.usgs.gov/)

- [Implementation](https://github.com/daearconsulting/tribal_water_monitoring/blob/54d191e189c26260ca93b300966333dd88e696d4/config/config.yaml): Analysis years 2000–2024; base period 2000–2020. Groundwater loader separately defaults to 1980 onward.
- [Implementation](https://github.com/daearconsulting/tribal_water_monitoring/blob/54d191e189c26260ca93b300966333dd88e696d4/src/loaders.py): load_usgs_groundwater_levels defaults to 1980-01-01; field-measurements query is open-ended.

Code inspection records settings; it does not establish a successful run or complete returned coverage.

[Field definitions and review scope](../docs/metadata.md)

## Access

Use time-series metadata to select a station and parameter, then daily or continuous collections for those observations. Discrete groundwater measurements use field-measurements. Water quality requires the appropriate samples service/Water Quality Portal. Start with one station and a bounded date interval; follow pagination. Optional API keys enable higher rate limits; keep keys outside Git.

[Provider/access documentation](https://api.waterdata.usgs.gov/) · [Citation/product reference](https://api.waterdata.usgs.gov/docs/ogcapi/migration/)

## Reproducibility and use

Record the exact release, variables, units, dates, geographic selection, retrieval time and source citation. Retain original quality flags and metadata. Follow [data governance](../docs/governance.md); source terms apply independently of this repository's MIT license.

Existing local code: `C:/Users/gekek/Documents/tribal_water_monitoring/src/loaders.py`, functions `load_usgs_groundwater_levels` and `_get_usgs_ogc_features`. This is a local cross-reference, not a portable dependency or a claim that the external implementation was tested here. Reuse it in that series; avoid duplicating its full pipeline in this catalog.
