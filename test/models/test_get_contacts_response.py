import unittest
from src.panorasdk.models.GetContactsResponse import GetContactsResponse


class TestGetContactsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contacts_response(self):
        # Create GetContactsResponse class instance
        test_model = GetContactsResponse(
            statusCode=7, message="amet", error="cupiditate", data={"praesentium": 4}
        )
        self.assertEqual(test_model.statusCode, 7)
        self.assertEqual(test_model.message, "amet")
        self.assertEqual(test_model.error, "cupiditate")
        self.assertEqual(test_model.data, {"praesentium": 4})

    def test_get_contacts_response_required_fields_missing(self):
        # Assert GetContactsResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactsResponse()


if __name__ == "__main__":
    unittest.main()
