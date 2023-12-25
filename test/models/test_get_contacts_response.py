import unittest
from src.panorasdk.models.GetContactsResponse import GetContactsResponse


class TestGetContactsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contacts_response(self):
        # Create GetContactsResponse class instance
        test_model = GetContactsResponse(
            statusCode=1, message="cumque", error="hic", data={"saepe": 7}
        )
        self.assertEqual(test_model.statusCode, 1)
        self.assertEqual(test_model.message, "cumque")
        self.assertEqual(test_model.error, "hic")
        self.assertEqual(test_model.data, {"saepe": 7})

    def test_get_contacts_response_required_fields_missing(self):
        # Assert GetContactsResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactsResponse()


if __name__ == "__main__":
    unittest.main()
