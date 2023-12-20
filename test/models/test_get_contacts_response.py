import unittest
from src.panorasdk.models.GetContactsResponse import GetContactsResponse


class TestGetContactsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contacts_response(self):
        # Create GetContactsResponse class instance
        test_model = GetContactsResponse(
            statusCode=3, message="ipsam", error="ad", data={"quas": 2}
        )
        self.assertEqual(test_model.statusCode, 3)
        self.assertEqual(test_model.message, "ipsam")
        self.assertEqual(test_model.error, "ad")
        self.assertEqual(test_model.data, {"quas": 2})

    def test_get_contacts_response_required_fields_missing(self):
        # Assert GetContactsResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactsResponse()


if __name__ == "__main__":
    unittest.main()
