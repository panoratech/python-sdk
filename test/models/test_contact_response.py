import unittest
from src.panorasdk.models.ContactResponse import ContactResponse


class TestContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_contact_response(self):
        # Create ContactResponse class instance
        test_model = ContactResponse(
            remote_data={"doloremque": 9}, contacts=["error", "commodi"]
        )
        self.assertEqual(test_model.remote_data, {"doloremque": 9})
        self.assertEqual(test_model.contacts, ["error", "commodi"])

    def test_contact_response_required_fields_missing(self):
        # Assert ContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ContactResponse()


if __name__ == "__main__":
    unittest.main()
