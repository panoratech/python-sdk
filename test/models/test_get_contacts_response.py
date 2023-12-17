import unittest
from src.panorasdk.models.GetContactsResponse import GetContactsResponse


class TestGetContactsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contacts_response(self):
        # Create GetContactsResponse class instance
        test_model = GetContactsResponse(
            statusCode=9, message="in", error="porro", data={"consequuntur": 5}
        )
        self.assertEqual(test_model.statusCode, 9)
        self.assertEqual(test_model.message, "in")
        self.assertEqual(test_model.error, "porro")
        self.assertEqual(test_model.data, {"consequuntur": 5})

    def test_get_contacts_response_required_fields_missing(self):
        # Assert GetContactsResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactsResponse()


if __name__ == "__main__":
    unittest.main()
