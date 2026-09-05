# Maintaining the catalog

1. Add one record in `datasets/` for a specific product or clearly label a discovery portal/resource. Update `catalog.json` and the README table together.
2. Record status, proposed/confirmed series, product/version, coverage, resolution, time interval, source formats, intended outputs, access instructions, authentication, citation and terms. Use explicit “not verified” values instead of guessing.
3. Promote to documented after reviewing provider documentation. Add a small access example only when needed for evaluation or a series; include dependencies, expected output, bounded scope and provenance.
4. Promote to access tested only after a successful live run, recording date, command, product version and outcome in `docs/validation.md`. Check offline validation with `python -m unittest discover -s tests`.
5. Before a teaching/research release, rerun the used examples and check those product links. Record failures and review changed schemas, endpoints or versions. Retire superseded entries with replacement links.

Keep examples small; do not add full-region downloads by default. Never commit data or secrets. Preserve source quality flags, units and metadata. Do not claim streaming where the provider only offers full downloads. Link full series pipelines instead of duplicating them.


## Coverage and implementation metadata

Keep the dataset table and its `catalog.json` metadata synchronized. Separate provider coverage from requested project dates and actual returned dates. Record source grid spacing/mapping scale separately from output grids; resampling does not improve source information resolution. Use event dates and positional uncertainty for occurrences, survey depths/versions for soils, and publication/vintage dates for maps. A portal has no universal time coverage or resolution.

Store selection and implementation status independently of live access validation. Preserve project-owner implementation reports, and add repository/file links and a reviewed commit when code is available. Do not assign a collection version from a sensor name alone. Record latest observations only after checking returned data or provider availability metadata, with the check date. Keep historical projections, observations and climate normals distinct.
