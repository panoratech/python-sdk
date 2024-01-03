import unittest
from src.panorasdk.models.Phone import Phone


class TestPhoneModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_phone(self):
        # Create Phone class instance
        test_model = Phone(phone_type="ut", phone_number="dolore", owner_type="optio")
        self.assertEqual(test_model.phone_type, "ut")
        self.assertEqual(test_model.phone_number, "dolore")
        self.assertEqual(test_model.owner_type, "optio")

    def test_phone_required_fields_missing(self):
        # Assert Phone class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = Phone()


if __name__ == "__main__":
    unittest.main()
