import unittest
from src.panorasdk.models.GetContactsResponse import GetContactsResponse


class TestGetContactsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contacts_response(self):
        # Create GetContactsResponse class instance
        test_model = GetContactsResponse(
            statusCode=9, message="vero", error="molestias", data={"veniam": 3}
        )
        self.assertEqual(test_model.statusCode, 9)
        self.assertEqual(test_model.message, "vero")
        self.assertEqual(test_model.error, "molestias")
        self.assertEqual(test_model.data, {"veniam": 3})

    def test_get_contacts_response_required_fields_missing(self):
        # Assert GetContactsResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactsResponse()


if __name__ == "__main__":
    unittest.main()
