"""Download and validate a bounded Daymet V4 R1 single-pixel sample."""
import argparse
import calendar
import csv
from datetime import date, datetime, timezone
import hashlib
import io
import json
import math
from pathlib import Path
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ENDPOINT = 'https://daymet.ornl.gov/single-pixel/api/data'
DOI = 'https://doi.org/10.3334/ORNLDAAC/2129'
COLUMNS = ['year', 'yday', 'prcp (mm/day)', 'tmax (deg c)', 'tmin (deg c)']

def validate_request(lat, lon, start, end):
    if not (math.isfinite(lat) and math.isfinite(lon) and -90 <= lat <= 90 and -180 <= lon <= 180):
        raise ValueError('Coordinates must be finite latitude/longitude in decimal degrees.')
    if start.year < 1980 or end < start or (end-start).days > 30:
        raise ValueError('Choose an ordered interval of at most 31 days starting in 1980 or later.')
    if start.year != end.year or (calendar.isleap(end.year) and end.month == 12 and end.day == 31):
        raise ValueError('Choose dates within one year, excluding December 31 in leap years (absent in Daymet).')

def parse_response(raw, lat, lon, start, end):
    text = raw.decode('utf-8-sig')
    lines = text.splitlines()
    header = next((i for i, line in enumerate(lines) if line.startswith('year,yday,')), None)
    if header is None or DOI not in '\n'.join(lines[:header]):
        raise ValueError('Missing Daymet CSV header or expected V4 R1 citation; review the service response/version.')
    import re
    location = re.search(r'Latitude:\s*([-\d.]+)\s+Longitude:\s*([-\d.]+)', text)
    if not location or abs(float(location[1])-lat) > 0.0001 or abs(float(location[2])-lon) > 0.0001:
        raise ValueError('Response coordinates do not match the requested point.')
    reader = csv.DictReader(io.StringIO('\n'.join(lines[header:])))
    if reader.fieldnames != COLUMNS:
        raise ValueError(f'Unexpected columns: {reader.fieldnames}')
    rows = list(reader)
    expected = list(range(start.timetuple().tm_yday, end.timetuple().tm_yday+1))
    if [(int(r['year']), int(r['yday'])) for r in rows] != [(start.year, d) for d in expected]:
        raise ValueError('Missing, duplicate, unordered or out-of-range daily records.')
    for row in rows:
        values = [float(row[k]) for k in COLUMNS[2:]]
        if any(not math.isfinite(v) or v == -9999 for v in values):
            raise ValueError('Missing/non-finite values in this sample; inspect source data before analysis.')
        if values[0] < 0 or values[1] < values[2]:
            raise ValueError('Invalid precipitation or temperature ordering.')
    return rows, '\n'.join(lines[:header])

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lat', type=float, default=43.03)
    parser.add_argument('--lon', type=float, default=-102.56)
    parser.add_argument('--start', type=date.fromisoformat, default=date(2020, 1, 1))
    parser.add_argument('--end', type=date.fromisoformat, default=date(2020, 1, 31))
    parser.add_argument('--output', type=Path, default=Path('data/daymet-sample'))
    args = parser.parse_args()
    validate_request(args.lat, args.lon, args.start, args.end)
    if args.output.exists():
        raise ValueError('Output directory already exists; choose a new --output path to preserve prior results.')
    params = dict(lat=args.lat, lon=args.lon, vars='prcp,tmax,tmin', start=args.start.isoformat(), end=args.end.isoformat())
    url = ENDPOINT + '?' + urlencode(params)
    request = Request(url, headers={'User-Agent': 'OLC-NIFA-dataset-example/1.0'})
    with urlopen(request, timeout=45) as response:
        raw = response.read(2_000_001)
        if len(raw) > 2_000_000:
            raise ValueError('Response exceeds the 2 MB sample limit.')
    rows, preamble = parse_response(raw, args.lat, args.lon, args.start, args.end)
    summary = dict(records=len(rows), precipitation_total_mm=round(sum(float(r[COLUMNS[2]]) for r in rows), 2),
                   minimum_temperature_deg_c=min(float(r[COLUMNS[4]]) for r in rows),
                   maximum_temperature_deg_c=max(float(r[COLUMNS[3]]) for r in rows))
    manifest = dict(dataset='Daymet Version 4 R1', citation_doi=DOI, request_url=url,
                    retrieved_utc=datetime.now(timezone.utc).isoformat(), parameters=params,
                    response_sha256=hashlib.sha256(raw).hexdigest(), source_metadata=preamble,
                    python_version=sys.version, summary=summary,
                    transformations='Original CSV retained; summary only. No reprojection, interpolation or conversion.')
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output/'daymet.csv').write_bytes(raw)
    (args.output/'provenance.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))
    print(f'Saved source CSV and provenance to {args.output.resolve()}')

if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as exc:
        raise SystemExit(f'Daymet sample failed: {exc}')
