import unittest
from src.panorasdk.models.Phone import Phone


class TestPhoneModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_phone(self):
        # Create Phone class instance
        test_model = Phone(phone_type="cumque", phone_number="culpa", owner_type="quod")
        self.assertEqual(test_model.phone_type, "cumque")
        self.assertEqual(test_model.phone_number, "culpa")
        self.assertEqual(test_model.owner_type, "quod")

    def test_phone_required_fields_missing(self):
        # Assert Phone class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = Phone()


if __name__ == "__main__":
    unittest.main()
