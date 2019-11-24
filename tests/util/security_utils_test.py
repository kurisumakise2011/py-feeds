import unittest
import app.util.security_utils as sut


class TestSecurityUtils(unittest.TestCase):
    def test_check_passwords(self):
        """
        Test that it converts data
        """
        hash_value = '$2b$12$4AS6yQTrMzC/ug005pBlHeScMS3y8kgRT0U71bPt/vjJia0TCRsNS'
        res = sut.check_password_hash('610917', hash_value)
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
