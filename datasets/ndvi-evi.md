# NDVI/EVI

| Field | Value |
| --- | --- |
| Status | implemented |
| Selection | selected |
| Implementation | implemented; local code reviewed |
| Entry type | derived product |
| Topics / series | Vegetation and Land Cover; series assignment unconfirmed |
| Product / version | MOD13Q1 NDVI in reviewed code; NASA product reference V061, API code does not pin collection version |
| Geographic coverage | Global product, project point/subset requests |
| Available time coverage | Terra MODIS era from 2000; reviewed bison settings 2000–2023 |
| Project time coverage | Configured 2000–2023; actual returned coverage not audited |
| Temporal interval | 16-day composites for MOD13Q1; seasonal/yearly summaries are derived |
| Native spatial resolution / scale | 250 m MOD13Q1; other NDVI/EVI sources have different grids |
| Project output resolution | Source 250 m composites; downstream 30 m habitat grid does not increase NDVI information resolution |
| Source format | Product/access-route dependent |
| Project output format | Not recorded |
| Availability checked | No live availability check in this metadata review |
| Latest observation confirmed | Not checked |
| Documentation reviewed | 2026-09-05; linked provider reference and existing documented specifications |
| Access last tested | Not tested |
| Citation / source terms | Record from the selected product before promotion to documented |

## Product and series details

Reviewed code selects 250m_16_days_NDVI, scale 0.0001. This supports NDVI implementation, not an EVI implementation claim; retain QA and actual composite dates.

[Provider specification](https://doi.org/10.5067/MODIS/MOD13Q1.061)

- [Implementation](https://github.com/olc-techsupport/pine_ridge_bison_habitat/blob/150714f7bbe6cab019a3348998e629ec08d76a79/src/constants.py): MOD13Q1 / 250m_16_days_NDVI; MODIS_START_YEAR=2000, MODIS_END_YEAR=2023; growing months May–September.

Code inspection records settings; it does not establish a successful run or complete returned coverage.

[Field definitions and review scope](../docs/metadata.md)

## Discovery and access

Provider/access location must be identified.. Choose the specific collection or layer and document a bounded download, subset query, or manual request before using it in a series.

Select the parent sensor/product and record its version, masking, compositing and calculation method. Link the series analysis code instead of treating the index as a raw source.

See the [historical catalog](../docs/original-catalog.md) for original discovery notes, which are not verified specifications. Follow [data governance](../docs/governance.md).
