import unittest
from src.panorasdk.models.GetContactsResponse import GetContactsResponse


class TestGetContactsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contacts_response(self):
        # Create GetContactsResponse class instance
        test_model = GetContactsResponse(
            statusCode=6, message="error", error="voluptatem", data={"fugiat": 5}
        )
        self.assertEqual(test_model.statusCode, 6)
        self.assertEqual(test_model.message, "error")
        self.assertEqual(test_model.error, "voluptatem")
        self.assertEqual(test_model.data, {"fugiat": 5})

    def test_get_contacts_response_required_fields_missing(self):
        # Assert GetContactsResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactsResponse()


if __name__ == "__main__":
    unittest.main()
