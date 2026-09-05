# USDA Cropland Data Layer (CDL)

| Field | Value |
| --- | --- |
| Status | documented |
| Selection | candidate |
| Implementation | not implemented; none recorded |
| Entry type | product / product family |
| Topics / series | Agriculture and land cover (proposed). |
| Product / version | USDA NASS Cropland Data Layer; identify year and native/resampled product |
| Geographic coverage | CONUS for this selection |
| Available time coverage | Annual CONUS coverage from 2008; latest release not newly checked |
| Project time coverage | Series-specific dates not recorded |
| Temporal interval | Annual crop classifications |
| Native spatial resolution / scale | 30 m historical; 10 m native beginning 2024, with 30 m resampled option |
| Project output resolution | Not recorded; retain separately from source resolution |
| Source format | Product/access-route dependent |
| Project output format | Not recorded |
| Availability checked | No live availability check in this metadata review |
| Latest observation confirmed | Not checked |
| Documentation reviewed | 2026-09-05; linked provider reference and existing documented specifications |
| Access last tested | Not tested unless a validation record is linked below. |

## Product and series details

Keep year-specific legend and accuracy metadata; do not silently mix 10 m and 30 m products. Earlier provider review retained.

Format details: Categorical raster downloads; retain the original GeoTIFF, class legend and year-specific metadata. NetCDF is a possible derived output, not an implemented conversion.

[Provider specification](https://www.nass.usda.gov/Research_and_Science/Cropland/SARS1a.php)

[Field definitions and review scope](../docs/metadata.md)

## Access

Open the NASS product page and follow National Download or CroplandCROS. Choose a year, geographic extent and resolution; retain the metadata and classification accuracy documentation. Do not compare mixed resolutions without an explicit harmonization method.

[Provider/access documentation](https://www.nass.usda.gov/Research_and_Science/Cropland/SARS1a.php) · [Citation/product reference](https://www.nass.usda.gov/Research_and_Science/Cropland/SARS1a.php)

## Reproducibility and use

Record the exact release, variables, units, dates, geographic selection, retrieval time and source citation. Retain original quality flags and metadata. Follow [data governance](../docs/governance.md); source terms apply independently of this repository's MIT license.
