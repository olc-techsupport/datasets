# SMAP soil moisture products

| Field | Value |
| --- | --- |
| Status | documented |
| Selection | candidate |
| Implementation | not implemented; none recorded |
| Entry type | product / product family |
| Topics / series | Soil moisture and drought (proposed). |
| Product / version | SPL4SMGP Version 8, surface and root-zone soil moisture |
| Geographic coverage | Global |
| Available time coverage | Mission era from 2015; exact first/last available granules not checked |
| Project time coverage | Series-specific dates not recorded |
| Temporal interval | Three-hourly |
| Native spatial resolution / scale | 9 km EASE-Grid |
| Project output resolution | Not recorded; retain separately from source resolution |
| Source format | Product/access-route dependent |
| Project output format | Not recorded |
| Latest observation confirmed | Not checked |
| Documentation reviewed | 2026-09-05; linked provider reference and existing documented specifications |
| Access last tested | Not tested unless a validation record is linked below. |

## Product and series details

L4 modeled/assimilated surface and root-zone estimates. HDF5 source; preserve grid and layer/depth. Earlier provider review retained; no new download.

Format details: HDF5 source granules. NetCDF/Zarr would be derived outputs, not downloads implemented here.

[Provider specification](https://nsidc.org/data/spl4smgp/versions/8)

[Field definitions and review scope](../docs/metadata.md)

## Access

Open the exact NSIDC product page, review its user guide, and use the listed Earthdata access options to select a small date interval and region. Earthdata authentication may be required. L4 includes modeled/assimilated surface and root-zone estimates; do not describe it as a 3 km surface-only observation. Other L3/L4 products require separate records.

[Provider/access documentation](https://nsidc.org/data/spl4smgp/versions/8) · [Citation/product reference](https://nsidc.org/data/spl4smgp/versions/8)

## Reproducibility and use

Record the exact release, variables, units, dates, geographic selection, retrieval time and source citation. Retain original quality flags and metadata. Follow [data governance](../docs/governance.md); source terms apply independently of this repository's MIT license.
