# USGS Water Data for the Nation

| Field | Value |
| --- | --- |
| Status | documented |
| Product | USGS Water Data modern OGC APIs; collection selected by observation type |
| Coverage and scale | Monitoring locations across the US; temporal coverage varies by station, parameter and collection. The old 2010 start was a project suggestion, not source-wide coverage. |
| Source / output formats | OGC responses: GeoJSON/JSON. Parquet time series and separate site GeoJSON would be project outputs; no conversion pipeline is provided here. |
| Proposed series and purpose | Water monitoring (proposed; existing local implementation identified). |
| Project selection | Example settings only where supplied; production extent and period unconfirmed. |
| Documentation reviewed | 2026-09-05; see linked provider sources. |
| Access last tested | Not tested unless a validation record is linked below. |

## Access

Use time-series metadata to select a station and parameter, then daily or continuous collections for those observations. Discrete groundwater measurements use field-measurements. Water quality requires the appropriate samples service/Water Quality Portal. Start with one station and a bounded date interval; follow pagination. Optional API keys enable higher rate limits; keep keys outside Git.

[Provider/access documentation](https://api.waterdata.usgs.gov/) · [Citation/product reference](https://api.waterdata.usgs.gov/docs/ogcapi/migration/)

## Reproducibility and use

Record the exact release, variables, units, dates, geographic selection, retrieval time and source citation. Retain original quality flags and metadata. Follow [data governance](../docs/governance.md); source terms apply independently of this repository's MIT license.

Existing local code: `C:/Users/gekek/Documents/tribal_water_monitoring/src/loaders.py`, functions `load_usgs_groundwater_levels` and `_get_usgs_ogc_features`. This is a local cross-reference, not a portable dependency or a claim that the external implementation was tested here. Reuse it in that series; avoid duplicating its full pipeline in this catalog.
