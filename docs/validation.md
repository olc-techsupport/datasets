# Validation

## Daymet sample: passed on 2026-09-05

Executed `python examples/daymet_sample.py` with Python 3.11.15 against the public single-pixel endpoint. Retrieved January 1–31, 2020 at 43.03, -102.56; no authentication was needed. Returned citation: Daymet Version 4 R1, DOI https://doi.org/10.3334/ORNLDAAC/2129.

- Records: 31, with matching coordinates, dates, variables and finite non-missing values.
- Precipitation total: 9.88 mm; minimum temperature: -17.18 C; maximum temperature: 7.97 C.
- Retrieved UTC: 2026-09-05T16:43:14.399741+00:00.
- Response SHA-256: `178dc00af877e1cf618498a3eb3c85ceeafe0a7d730c668f29156a952c4b53b0`.
- Six offline tests passed with `python -m unittest discover -s tests`: valid response; service/version errors; missing/duplicate records and coordinates; missing/invalid values; request limits; leap-calendar handling.

Original CSV and provenance are stored in ignored local `data/daymet-sample/`. The source endpoint can revise data; this result establishes a dated sample, not continuous service availability. The supplied conda environment file was not installed during validation; the standard-library example ran in an existing Python environment.

## Documentation checks

51 unique catalog records; each has a dataset page and README entry. Local Markdown file links were checked. The five detailed ingestion records were reviewed against linked provider documentation on 2026-09-05. Other entries remain explicitly unverified candidates; there was no comprehensive external-link audit or live test of the other providers.
