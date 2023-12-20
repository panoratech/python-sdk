import unittest
from src.panorasdk.models.ContactResponse import ContactResponse


class TestContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_contact_response(self):
        # Create ContactResponse class instance
        test_model = ContactResponse(
            remote_data={"placeat": 6}, contacts=["magnam", "eius"]
        )
        self.assertEqual(test_model.remote_data, {"placeat": 6})
        self.assertEqual(test_model.contacts, ["magnam", "eius"])

    def test_contact_response_required_fields_missing(self):
        # Assert ContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ContactResponse()


if __name__ == "__main__":
    unittest.main()
