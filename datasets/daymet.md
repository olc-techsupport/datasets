# DayMET

| Field | Value |
| --- | --- |
| Status | access tested |
| Product | Daymet Version 4 R1 daily surface weather |
| Coverage and scale | North America; 1 km grid; daily from 1980, with end year checked at retrieval. |
| Source / output formats | Single-pixel service: CSV with metadata preamble. Gridded delivery: NetCDF; Zarr would be a derived project output. |
| Proposed series and purpose | Climate and drought (proposed); cross-series weather covariates. |
| Project selection | Example settings only where supplied; production extent and period unconfirmed. |
| Documentation reviewed | 2026-09-05; see linked provider sources. |
| Access last tested | 2026-09-05; 31 daily records validated; see validation record below. |

## Access

Use the single-pixel tool to choose coordinates, variables and dates. The example retrieves January 2020 at 43.03, -102.56, an illustrative point near Pine Ridge; it is not a reservation-wide average.

[Provider/access documentation](https://daymet.ornl.gov/single-pixel/) · [Citation/product reference](https://doi.org/10.3334/ORNLDAAC/2129)

## Reproducibility and use

Record the exact release, variables, units, dates, geographic selection, retrieval time and source citation. Retain original quality flags and metadata. Follow [data governance](../docs/governance.md); source terms apply independently of this repository's MIT license.

[Runnable example](../examples/daymet_sample.py) · [Instructions](../examples/README.md) · [Validation](../docs/validation.md). The live service is not version-pinned by URL; the example checks its returned V4 R1 citation and saves the exact response plus checksum. Daymet uses a 365-day calendar: do not silently treat day-of-year as an ordinary Gregorian series in leap years.
