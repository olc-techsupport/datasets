import importlib.util
from pathlib import Path
from datetime import date
import unittest

spec = importlib.util.spec_from_file_location('daymet', Path(__file__).resolve().parents[1] / 'examples/daymet_sample.py')
daymet = importlib.util.module_from_spec(spec)
spec.loader.exec_module(daymet)

class SampleValidation(unittest.TestCase):
    def setUp(self):
        self.start = date(2020, 1, 1)
        self.end = date(2020, 1, 2)
        self.raw = ('Latitude: 43.03  Longitude: -102.56\nCitation: ' + daymet.DOI + '\n' + ','.join(daymet.COLUMNS) + '\n2020,1,0,2,-1\n2020,2,1,3,-2\n').encode()

    def parse(self, raw):
        return daymet.parse_response(raw, 43.03, -102.56, self.start, self.end)

    def test_valid_sample(self):
        self.assertEqual(len(self.parse(self.raw)[0]), 2)

    def test_reject_service_error_and_version_change(self):
        for raw in [b'<html>Service unavailable</html>', self.raw.replace(daymet.DOI.encode(), b'new-version')]:
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                self.parse(raw)

    def test_reject_missing_duplicate_and_wrong_location(self):
        for raw in [self.raw.replace(b'2020,2', b'2020,1'), self.raw.split(b'2020,2')[0], self.raw.replace(b'43.03', b'44.03')]:
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                self.parse(raw)

    def test_reject_nodata_and_invalid_values(self):
        for token in [b'-9999', b'nan', b'-1']:
            with self.subTest(token=token), self.assertRaises(ValueError):
                self.parse(self.raw.replace(b'2020,1,0,', b'2020,1,'+token+b','))

    def test_bound_request_and_calendar(self):
        for lat, end in [(float('nan'), self.end), (43.03, date(2021,1,1)), (43.03, date(2020,12,31))]:
            with self.subTest(lat=lat,end=end), self.assertRaises(ValueError):
                daymet.validate_request(lat, -102.56, self.start, end)

    def test_leap_day_allowed_but_leap_december_31_absent(self):
        daymet.validate_request(43.03, -102.56, date(2020,2,28), date(2020,2,29))
        with self.assertRaises(ValueError):
            daymet.validate_request(43.03, -102.56, date(2020,12,30), date(2020,12,31))

if __name__ == '__main__':
    unittest.main()
