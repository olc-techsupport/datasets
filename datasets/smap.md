# SMAP soil moisture products

| Field | Value |
| --- | --- |
| Status | documented |
| Product | SMAP SPL4SMGP Version 8: L4 surface and root-zone soil moisture |
| Coverage and scale | Global; 9 km EASE-Grid, three-hourly, mission era beginning in 2015; verify exact granule availability. |
| Source / output formats | HDF5 source granules. NetCDF/Zarr would be derived outputs, not downloads implemented here. |
| Proposed series and purpose | Soil moisture and drought (proposed). |
| Project selection | Example settings only where supplied; production extent and period unconfirmed. |
| Documentation reviewed | 2026-09-05; see linked provider sources. |
| Access last tested | Not tested unless a validation record is linked below. |

## Access

Open the exact NSIDC product page, review its user guide, and use the listed Earthdata access options to select a small date interval and region. Earthdata authentication may be required. L4 includes modeled/assimilated surface and root-zone estimates; do not describe it as a 3 km surface-only observation. Other L3/L4 products require separate records.

[Provider/access documentation](https://nsidc.org/data/spl4smgp/versions/8) · [Citation/product reference](https://nsidc.org/data/spl4smgp/versions/8)

## Reproducibility and use

Record the exact release, variables, units, dates, geographic selection, retrieval time and source citation. Retain original quality flags and metadata. Follow [data governance](../docs/governance.md); source terms apply independently of this repository's MIT license.
