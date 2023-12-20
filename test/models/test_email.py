import unittest
from src.panorasdk.models.Email import Email


class TestEmailModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_email(self):
        # Create Email class instance
        test_model = Email(
            email_address_type="ipsam", email_address="sequi", owner_type="nisi"
        )
        self.assertEqual(test_model.email_address_type, "ipsam")
        self.assertEqual(test_model.email_address, "sequi")
        self.assertEqual(test_model.owner_type, "nisi")

    def test_email_required_fields_missing(self):
        # Assert Email class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = Email()


if __name__ == "__main__":
    unittest.main()
