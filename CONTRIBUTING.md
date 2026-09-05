# Maintaining the catalog

1. Add one record in `datasets/` for a specific product or clearly label a discovery portal/resource. Update `catalog.json` and the README table together.
2. Record status, proposed/confirmed series, product/version, coverage, resolution, time interval, source formats, intended outputs, access instructions, authentication, citation and terms. Use explicit “not verified” values instead of guessing.
3. Promote to documented after reviewing provider documentation. Add a small access example only when needed for evaluation or a series; include dependencies, expected output, bounded scope and provenance.
4. Promote to access tested only after a successful live run, recording date, command, product version and outcome in `docs/validation.md`. Check offline validation with `python -m unittest discover -s tests`.
5. Before a teaching/research release, rerun the used examples and check those product links. Record failures and review changed schemas, endpoints or versions. Retire superseded entries with replacement links.

Keep examples small; do not add full-region downloads by default. Never commit data or secrets. Preserve source quality flags, units and metadata. Do not claim streaming where the provider only offers full downloads. Link full series pipelines instead of duplicating them.
