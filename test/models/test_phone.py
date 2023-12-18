import unittest
from src.panorasdk.models.Phone import Phone


class TestPhoneModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_phone(self):
        # Create Phone class instance
        test_model = Phone(
            phone_type="inventore", phone_number="perspiciatis", owner_type="nam"
        )
        self.assertEqual(test_model.phone_type, "inventore")
        self.assertEqual(test_model.phone_number, "perspiciatis")
        self.assertEqual(test_model.owner_type, "nam")

    def test_phone_required_fields_missing(self):
        # Assert Phone class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = Phone()


if __name__ == "__main__":
    unittest.main()
