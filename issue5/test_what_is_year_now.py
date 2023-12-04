import json
from unittest import TestCase, mock
import urllib.request

from what_is_year_now import what_is_year_now


class TestWhatIsYearNow(TestCase):

    @mock.patch('urllib.request.urlopen')
    def test_what_is_year_now_ymd_format(self, mock_urlopen):
        mock_resp = mock.Mock()
        mock_resp.__enter__.return_value.read.return_value = json.dumps({'currentDateTime': '2023-12-05'})
        mock_urlopen.return_value = mock_resp

        year = what_is_year_now()
        self.assertEqual(year, 2023)

    @mock.patch('urllib.request.urlopen')
    def test_what_is_year_now_dmy_format(self, mock_urlopen):
        mock_resp = mock.Mock()
        mock_resp.__enter__.return_value.read.return_value = json.dumps({'currentDateTime': '05.12.2023'})
        mock_urlopen.return_value = mock_resp

        year = what_is_year_now()
        self.assertEqual(year, 2023)

    @mock.patch('urllib.request.urlopen')
    def test_what_is_year_now_invalid_format(self, mock_urlopen):
        mock_resp = mock.Mock()
        mock_resp.__enter__.return_value.read.return_value = json.dumps({'currentDateTime': '2023/12/05'})
        mock_urlopen.return_value = mock_resp

        with self.assertRaises(ValueError, msg='Invalid format'):
            what_is_year_now()


if __name__ == '__main__':
    import pytest

    pytest.main(['-v', '--cov=your_module_name', '--cov-report=html'])
