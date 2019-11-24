import unittest
from datetime import datetime

import app.util.map_utils as sut


class TestMapUtils(unittest.TestCase):
    def test_convert_to_str(self):
        """
        Test that it converts data
        """
        res = sut.to_str(bytearray('byte_array', 'utf-8'))
        self.assertEqual(res, 'byte_array')

    def test_convert_time_to_str(self):
        """
        Test that it converts data
        """
        datetime_str = '2018-08-18 13:55:26'
        datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        res = sut.time_to_str(datetime_object)
        self.assertEqual(res, datetime_str)

    def test_convert_to_empty_if_no(self):
        """
        Test that it converts data
        """
        self.assertEqual(sut.time_to_str(None), '')
        self.assertEqual(sut.to_str(None), '')


if __name__ == '__main__':
    unittest.main()
