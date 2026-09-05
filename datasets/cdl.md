# USDA Cropland Data Layer (CDL)

| Field | Value |
| --- | --- |
| Status | documented |
| Product | USDA NASS Cropland Data Layer; select year and native/resampled product |
| Coverage and scale | Annual CONUS coverage from 2008; historical CDL commonly 30 m. Native resolution increased to 10 m beginning in 2024; a 30 m resampled version is also offered. |
| Source / output formats | Categorical raster downloads; retain the original GeoTIFF, class legend and year-specific metadata. NetCDF is a possible derived output, not an implemented conversion. |
| Proposed series and purpose | Agriculture and land cover (proposed). |
| Project selection | Example settings only where supplied; production extent and period unconfirmed. |
| Documentation reviewed | 2026-09-05; see linked provider sources. |
| Access last tested | Not tested unless a validation record is linked below. |

## Access

Open the NASS product page and follow National Download or CroplandCROS. Choose a year, geographic extent and resolution; retain the metadata and classification accuracy documentation. Do not compare mixed resolutions without an explicit harmonization method.

[Provider/access documentation](https://www.nass.usda.gov/Research_and_Science/Cropland/SARS1a.php) · [Citation/product reference](https://www.nass.usda.gov/Research_and_Science/Cropland/SARS1a.php)

## Reproducibility and use

Record the exact release, variables, units, dates, geographic selection, retrieval time and source citation. Retain original quality flags and metadata. Follow [data governance](../docs/governance.md); source terms apply independently of this repository's MIT license.
