# Daymet access example

Retrieve precipitation and minimum/maximum temperature for January 2020 at 43.03, -102.56, an illustrative point near Pine Ridge. This is a modeled grid-cell time series, not a station observation or reservation-wide summary.

Use Python 3.11 or newer. The script uses only the standard library; no packages or credentials are required for the tested public endpoint. Optionally create the provided environment:

```sh
conda env create -f environment.yml
conda activate olc-geospatial-data
python examples/daymet_sample.py
```

Run commands from the repository root. The default output is `data/daymet-sample/`, containing `daymet.csv` (unaltered provider response including metadata) and `provenance.json` (request, UTC retrieval time, citation/version, SHA-256 and summary). Data directories are ignored by Git. Existing output directories are never overwritten; choose a new path to rerun:

```sh
python examples/daymet_sample.py --lat 43.03 --lon -102.56 --start 2020-01-01 --end 2020-01-31 --output data/daymet-second-run
python -m unittest discover -s tests
```

Expected: 31 daily records with year, day-of-year, precipitation in mm/day and temperatures in degrees C. The initial validation returned 9.88 mm total precipitation, -17.18 C minimum and 7.97 C maximum. Provider revisions can change values; the saved checksum identifies the retrieved response, not a guarantee of immutable service data.

The example checks the V4 R1 citation, requested coordinates, dates, column names, missing values and basic value consistency before saving. It limits requests to 31 days within one year and responses to 2 MB. Daymet retains February 29 and omits December 31 in leap years; intervals including the omitted date are rejected. It does not implement bulk ingestion, retries or conversion to Zarr.

For timeouts, rate limits or service errors, wait and rerun with a new output path. A version/schema error requires reviewing the provider documentation before changing validation. For empty/missing values, inspect availability for the selected point rather than treating missing data as zero.

[Dataset record](../datasets/daymet.md) · [Provider tool and API example](https://daymet.ornl.gov/single-pixel/) · [Calendar and product description](https://daymet.ornl.gov/overview)
