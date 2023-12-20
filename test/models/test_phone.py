import unittest
from src.panorasdk.models.Phone import Phone


class TestPhoneModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_phone(self):
        # Create Phone class instance
        test_model = Phone(
            phone_type="occaecati", phone_number="eum", owner_type="ipsa"
        )
        self.assertEqual(test_model.phone_type, "occaecati")
        self.assertEqual(test_model.phone_number, "eum")
        self.assertEqual(test_model.owner_type, "ipsa")

    def test_phone_required_fields_missing(self):
        # Assert Phone class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = Phone()


if __name__ == "__main__":
    unittest.main()
