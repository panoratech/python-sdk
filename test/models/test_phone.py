import unittest
from src.panorasdk.models.Phone import Phone


class TestPhoneModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_phone(self):
        # Create Phone class instance
        test_model = Phone(phone_type="veniam", phone_number="nihil", owner_type="odit")
        self.assertEqual(test_model.phone_type, "veniam")
        self.assertEqual(test_model.phone_number, "nihil")
        self.assertEqual(test_model.owner_type, "odit")

    def test_phone_required_fields_missing(self):
        # Assert Phone class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = Phone()


if __name__ == "__main__":
    unittest.main()
