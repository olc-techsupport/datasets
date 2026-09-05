# Metadata definitions and implementation review

Reviewed 2026-09-05. All 51 records use separate fields for product/version, provider time coverage, project time coverage, temporal interval, native spatial resolution or mapping scale, output resolution, source/output format and availability checks. `catalog.json` stores the same values.

Provider coverage describes the source archive. Project coverage describes configured requests or analysis windows. Actual returned dates and gaps require a data/manifest inspection; a code date filter alone is not evidence of complete coverage. Satellite revisit interval differs from usable cloud-free acquisitions and composite windows. A static map's acquisition/publication date is not an annual time series. Geographic degree spacing differs from a constant meter grid.

Selection, implementation and live validation are independent. Owner-reported implementations are retained, with missing repository links stated explicitly. Existing Daymet live validation is retained. Other pipelines were inspected as text, not run. No new service-wide latest-observation dates were asserted.

## Local code inspected

- `data_cube_tutorial`: gridMET point helper, MOD13Q1 settings and TIGER2023 Pine Ridge boundary loader.
- `pine_ridge_bison_habitat`: NLCD 2021 loader, MOD13Q1 2000–2023 settings, SRTM tile reader, monthly MACA loader and 30 m EPSG:5070 target grid.
- `tribal_water_monitoring`: analysis configuration and groundwater request defaults.
- `Geology-soils-geology`: SSURGO implementation and third-party source descriptions.

Dataset implementation links use the configured GitHub remote and reviewed local HEAD. They identify local code evidence; remote page availability was not tested. User-reported Landsat, Sentinel-2, GBIF, OSM, BIA and SDGS implementations were not assigned invented repository links. Census boundary code was not attributed to BIA; USGS state geology was not attributed to SDGS.

## Review findings to carry into series work

- Bison SRTM loader enforces one-arc-second tiles while comments elsewhere describe GL3/90 m. The catalog records executable settings and flags the mismatch; cached data should be checked in that repository.
- Bison NLCD is a 2021 snapshot, not Annual NLCD. A product-family description must preserve that distinction.
- Bison climate loader uses monthly MACA aggregates. A monthly input cannot by itself establish counts of individual daily heat events.
- MOD13Q1 supplies 250 m, 16-day composites. The 30 m habitat output target does not add fine-scale NDVI information.
- Water configuration specifies 2000–2024, but the groundwater loader defaults to 1980 onward. Each notebook's actual call and returned site coverage determine its series.

Unselected portals and local resources retain product-dependent fields rather than fabricated date ranges or meter resolutions. Prior detailed Daymet/PRISM/SMAP/CDL/USGS descriptions remain available; new source references accompany the added specifications.
