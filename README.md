# OLC NIFA Geospatial Datasets

A shared catalog and practical access guide for environmental, geospatial and socio-cultural sources supporting Oglala Lakota College research, education and land stewardship in Pine Ridge and the Northern Great Plains.

This repository combines the dataset inventory and the former Geospatial-data_ingestion documentation. It contains candidate sources, product notes and one runnable Daymet sample. Full series analyses remain in their own repositories.

## Start here

- [Run the Daymet sample](examples/README.md): one month at an illustrative point near Pine Ridge.
- [Proposed series mapping](docs/series.md): planning assignments, not confirmed project commitments.
- [Contribution guide](CONTRIBUTING.md), [governance and citation](docs/governance.md), and [validation record](docs/validation.md).
- [Consolidation notes](docs/consolidation.md) and original documentation snapshots preserve the earlier inventories.

## Catalog

`candidate`: discovery lead, specifications/access unverified. `documented`: product and access notes reviewed, download not necessarily tested. `access tested`: the linked bounded example succeeded on its recorded date, not a production readiness guarantee. `retired`: retained for provenance. No entry is labeled in use without series evidence.

Each row links to its dataset record. Broad portals, derived products and governed local resources are identified separately from specific products. Duplicate OpenStreetMap entries share one record; overlapping discovery resources remain visible until exact products are chosen.

| Dataset or resource | Topics / proposed use | Status | Type |
| --- | --- | --- | --- |
| [USGS Protected Areas Database (PAD-US)](datasets/usgs-protected-areas-database-pad-us.md) | Geographic and Spatial Data | candidate | source candidate |
| [OpenStreetMap (OSM)](datasets/openstreetmap-osm.md) | Geographic and Spatial Data; Infrastructure Data | candidate | source candidate |
| [Boundary Data](datasets/boundary-data.md) | Geographic and Spatial Data | candidate | local / governed resource |
| [POLARIS Soil Dataset](datasets/polaris-soil-dataset.md) | Geology and Soils Data | candidate | source candidate |
| [USDA NRCS Web Soil Survey](datasets/usda-nrcs-web-soil-survey.md) | Geology and Soils Data | candidate | source candidate |
| [SSURGO Downloader (NRCS)](datasets/ssurgo-downloader-nrcs.md) | Geology and Soils Data | candidate | source candidate |
| [SoilGrids (ISRIC)](datasets/soilgrids-isric.md) | Geology and Soils Data | candidate | source candidate |
| [South Dakota Geological Survey (SDGS)](datasets/south-dakota-geological-survey-sdgs.md) | Geology and Soils Data | candidate | source candidate |
| [USGS National Elevation Dataset (NED)](datasets/usgs-national-elevation-dataset-ned.md) | Elevation and Topography | candidate | source candidate |
| [NASA SRTM (Shuttle Radar Topography Mission)](datasets/nasa-srtm-shuttle-radar-topography-mission.md) | Elevation and Topography | candidate | source candidate |
| [MACAv2-METDATA (THREDDS)](datasets/macav2-metdata-thredds.md) | Climate Data | candidate | source candidate |
| [NOAA Climate Data (NCEI)](datasets/noaa-climate-data-ncei.md) | Climate Data | candidate | portal / resource |
| [PRISM Climate Data](datasets/prism.md) | Climate Data | documented | product / product family |
| [GridMET](datasets/gridmet.md) | Climate Data | candidate | source candidate |
| [Daymet](datasets/daymet.md) | Climate Data | access tested | product / product family |
| [NASA EarthData EOSDIS](datasets/nasa-earthdata-eosdis.md) | Climate Data | candidate | portal / resource |
| [NASA Global Climate Change - Vital Signs of the Planet](datasets/nasa-global-climate-change-vital-signs-of-the-planet.md) | Climate Data | candidate | portal / resource |
| [ESA Climate Change Initiative (ESA CCI)](datasets/esa-climate-change-initiative-esa-cci.md) | Climate Data | candidate | source candidate |
| [National Land Cover Database (NLCD)](datasets/national-land-cover-database-nlcd.md) | Vegetation and Land Cover | candidate | source candidate |
| [MODIS Land Cover (MOD12)](datasets/modis-land-cover-mod12.md) | Vegetation and Land Cover | candidate | source candidate |
| [BONAP (Biota of North America Program)](datasets/bonap-biota-of-north-america-program.md) | Vegetation and Land Cover | candidate | source candidate |
| [USGS Species Viewer](datasets/usgs-species-viewer.md) | Vegetation and Land Cover | candidate | source candidate |
| [USFS National Grasslands](datasets/usfs-national-grasslands.md) | Vegetation and Land Cover | candidate | portal / resource |
| [NDVI/EVI](datasets/ndvi-evi.md) | Vegetation and Land Cover | candidate | derived product |
| [USGS National Hydrography Dataset (NHDPlus HR)](datasets/usgs-national-hydrography-dataset-nhdplus-hr.md) | Hydrology | candidate | source candidate |
| [NASA GRACE (Groundwater Data)](datasets/nasa-grace-groundwater-data.md) | Hydrology | candidate | source candidate |
| [USGS Water Data for the Nation](datasets/usgs-water.md) | Hydrology | documented | product / product family |
| [Global Runoff Data Centre (GRDC)](datasets/global-runoff-data-centre-grdc.md) | Hydrology | candidate | source candidate |
| [Landsat (USGS)](datasets/landsat-usgs.md) | Satellite and Remote Sensing Data | candidate | source candidate |
| [Sentinel-2 (ESA Copernicus)](datasets/sentinel-2-esa-copernicus.md) | Satellite and Remote Sensing Data | candidate | source candidate |
| [Planet / Maxar (optional)](datasets/planet-maxar-optional.md) | Satellite and Remote Sensing Data | candidate | source candidate |
| [World Database on Protected Areas (WDPA)](datasets/world-database-on-protected-areas-wdpa.md) | Conservation and Wildlife Data | candidate | source candidate |
| [eBird (Cornell Lab of Ornithology)](datasets/ebird-cornell-lab-of-ornithology.md) | Conservation and Wildlife Data | candidate | source candidate |
| [GBIF (Global Biodiversity Information Facility)](datasets/gbif-global-biodiversity-information-facility.md) | Conservation and Wildlife Data | candidate | source candidate |
| [USGS Protected Areas and Species Distributions](datasets/usgs-protected-areas-and-species-distributions.md) | Conservation and Wildlife Data | candidate | source candidate |
| [USDA NASS](datasets/usda-nass.md) | Agricultural Data | candidate | portal / resource |
| [FAO GIEWS](datasets/fao-giews.md) | Agricultural Data | candidate | source candidate |
| [EPA Air Quality System (AQS)](datasets/epa-air-quality-system-aqs.md) | Environmental Monitoring Data | candidate | source candidate |
| [USGS BioData](datasets/usgs-biodata.md) | Environmental Monitoring Data | candidate | source candidate |
| [Homeland Infrastructure Foundation-Level Data (HIFLD)](datasets/homeland-infrastructure-foundation-level-data-hifld.md) | Infrastructure Data | candidate | source candidate |
| [Local GIS Resources](datasets/local-gis-resources.md) | Infrastructure Data | candidate | local / governed resource |
| [USGS LANDFIRE](datasets/usgs-landfire.md) | Fire-related Datasets | candidate | source candidate |
| [Fuelcast](datasets/fuelcast.md) | Fire-related Datasets | candidate | source candidate |
| [U.S. Census Bureau](datasets/u-s-census-bureau.md) | Socio-Cultural Data | candidate | source candidate |
| [Bureau of Indian Affairs (BIA) GIS](datasets/bureau-of-indian-affairs-bia-gis.md) | Socio-Cultural Data | candidate | source candidate |
| [Tribal and Cultural Lands](datasets/tribal-and-cultural-lands.md) | Socio-Cultural Data | candidate | local / governed resource |
| [NASA EarthData](datasets/nasa-earthdata.md) | Educational and Research Data | candidate | portal / resource |
| [Local Research Outputs (OLC)](datasets/local-research-outputs-olc.md) | Educational and Research Data | candidate | local / governed resource |
| [Student Projects](datasets/student-projects.md) | Educational and Research Data | candidate | local / governed resource |
| [USDA Cropland Data Layer (CDL)](datasets/cdl.md) | Agricultural Data | documented | product / product family |
| [SMAP soil moisture products](datasets/smap.md) | Hydrology | documented | product / product family |

## Scope and licensing

The MIT [license](LICENSE) covers repository-authored code and documentation. It does not relicense upstream datasets or grant access to governed Tribal data. Store downloaded data outside version control; preserve provider metadata and source-specific terms.
