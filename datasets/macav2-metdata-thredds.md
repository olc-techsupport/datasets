# MACAv2-METDATA (THREDDS)

| Field | Value |
| --- | --- |
| Status | implemented |
| Selection | selected |
| Implementation | implemented; local code reviewed |
| Entry type | source candidate |
| Topics / series | Climate Data; series assignment unconfirmed |
| Product / version | MACAv2-METDATA; CMIP5 model, realization and RCP must accompany each selection |
| Geographic coverage | CONUS |
| Available time coverage | Historical 1950–2005; projection aggregates in reviewed code 2006–2099 |
| Project time coverage | Loader: 2006–2099; habitat planning document describes 2040–2060 |
| Temporal interval | Daily products and monthly aggregates; reviewed bison loader uses monthly |
| Native spatial resolution / scale | 1/24 degree (approximately 4 km) |
| Project output resolution | Nearest grid-cell monthly CSV; no new climate spatial detail from habitat output grid |
| Source format | Monthly NetCDF via OPeNDAP |
| Project output format | Point time-series CSV |
| Availability checked | No live availability check in this metadata review |
| Latest observation confirmed | Not checked |
| Documentation reviewed | 2026-09-05; linked provider reference and existing documented specifications |
| Access last tested | Not tested |
| Citation / source terms | Record from the selected product before promotion to documented |

## Product and series details

Historical simulations and future projections are separate from observed weather. Preserve model calendar and scenario; exact periods are also evidenced by the loader URL.

[Provider specification](https://www.climatologylab.org/datasets.html)

- [Implementation](https://github.com/olc-techsupport/pine_ridge_bison_habitat/blob/150714f7bbe6cab019a3348998e629ec08d76a79/src/loaders.py): fetch_maca_monthly uses BNU-ESM by default, r1i1p1, supplied RCP, monthly 2006_2099_CONUS aggregates.

Code inspection records settings; it does not establish a successful run or complete returned coverage.

[Field definitions and review scope](../docs/metadata.md)

## Discovery and access

[Original discovery link](https://climate.northwestknowledge.net/MACA/). Choose the specific collection or layer and document a bounded download, subset query, or manual request before using it in a series.

Confirm product coverage for Pine Ridge and the Northern Great Plains, authentication, source formats and terms. Provider portals can contain many unrelated products; a portal link alone is insufficient for reproducibility.

See the [historical catalog](../docs/original-catalog.md) for original discovery notes, which are not verified specifications. Follow [data governance](../docs/governance.md).
