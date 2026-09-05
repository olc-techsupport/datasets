# DayMET

| Field | Value |
| --- | --- |
| Status | access tested |
| Selection | selected |
| Implementation | implemented; tested example in this repository |
| Entry type | product / product family |
| Topics / series | Climate and drought (proposed); cross-series weather covariates. |
| Product / version | Daymet Version 4 R1, DOI 10.3334/ORNLDAAC/2129 |
| Geographic coverage | North America for this record; other regional archives differ |
| Available time coverage | North America from 1980; latest returned date recorded per request |
| Project time coverage | Example: 2020-01-01 through 2020-01-31 at 43.03, -102.56 |
| Temporal interval | Daily; leap day retained, December 31 omitted in leap years |
| Native spatial resolution / scale | 1 km grid; sample is one grid-cell time series |
| Project output resolution | One native grid-cell sample; no resampling |
| Source format | CSV with provider metadata; gridded products use NetCDF |
| Project output format | Unmodified CSV and provenance JSON |
| Availability checked | 2026-09-05; bounded sample passed (prior validation) |
| Latest observation confirmed | 2020-01-31 within the sample; service-wide latest date not checked |
| Documentation reviewed | 2026-09-05; linked provider reference and existing documented specifications |
| Access last tested | 2026-09-05; 31 daily records validated; see validation record below. |

## Product and series details

Live sample checked 2026-09-05. Endpoint URL is not version-pinned; response citation and checksum are retained.

Format details: Single-pixel service: CSV with metadata preamble. Gridded delivery: NetCDF; Zarr would be a derived project output.

[Provider specification](https://daymet.ornl.gov/overview)

- [Implementation](../examples/daymet_sample.py): Bounded standard-library sample; see docs/validation.md

Code inspection records settings; it does not establish a successful run or complete returned coverage.

[Field definitions and review scope](../docs/metadata.md)

## Access

Use the single-pixel tool to choose coordinates, variables and dates. The example retrieves January 2020 at 43.03, -102.56, an illustrative point near Pine Ridge; it is not a reservation-wide average.

[Provider/access documentation](https://daymet.ornl.gov/single-pixel/) · [Citation/product reference](https://doi.org/10.3334/ORNLDAAC/2129)

## Reproducibility and use

Record the exact release, variables, units, dates, geographic selection, retrieval time and source citation. Retain original quality flags and metadata. Follow [data governance](../docs/governance.md); source terms apply independently of this repository's MIT license.

[Runnable example](../examples/daymet_sample.py) · [Instructions](../examples/README.md) · [Validation](../docs/validation.md). The live service is not version-pinned by URL; the example checks its returned V4 R1 citation and saves the exact response plus checksum. Daymet uses a 365-day calendar: do not silently treat day-of-year as an ordinary Gregorian series in leap years.
