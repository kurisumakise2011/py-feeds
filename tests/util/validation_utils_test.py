import unittest

import app.util.validation_utils as sut


class TestValidationUtils(unittest.TestCase):
    def test_should_validate_if_is_number(self):
        res = sut.is_int_number('2121')
        self.assertTrue(res)

    def test_is_not_valid_number(self):
        res = sut.is_int_number('1212s')
        self.assertFalse(res)

    def test_is_valid_str(self):
        res = sut.is_str_in_length('sadsa', 1, 128)
        self.assertTrue(res)

    def test_is_invalid_str(self):
        res = sut.is_str_in_length('222222222222222', 1, 5)
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
