import unittest
from src.panorasdk.models.Email import Email


class TestEmailModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_email(self):
        # Create Email class instance
        test_model = Email(
            email_address_type="aperiam", email_address="labore", owner_type="officiis"
        )
        self.assertEqual(test_model.email_address_type, "aperiam")
        self.assertEqual(test_model.email_address, "labore")
        self.assertEqual(test_model.owner_type, "officiis")

    def test_email_required_fields_missing(self):
        # Assert Email class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = Email()


if __name__ == "__main__":
    unittest.main()
