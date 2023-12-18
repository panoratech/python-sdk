import unittest
from src.panorasdk.models.GetContactsResponse import GetContactsResponse


class TestGetContactsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contacts_response(self):
        # Create GetContactsResponse class instance
        test_model = GetContactsResponse(
            statusCode=6, message="perferendis", error="quis", data={"sed": 9}
        )
        self.assertEqual(test_model.statusCode, 6)
        self.assertEqual(test_model.message, "perferendis")
        self.assertEqual(test_model.error, "quis")
        self.assertEqual(test_model.data, {"sed": 9})

    def test_get_contacts_response_required_fields_missing(self):
        # Assert GetContactsResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactsResponse()


if __name__ == "__main__":
    unittest.main()
