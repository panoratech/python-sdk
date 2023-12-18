import unittest
from src.panorasdk.models.GetContactResponse import GetContactResponse


class TestGetContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contact_response(self):
        # Create GetContactResponse class instance
        test_model = GetContactResponse(
            statusCode=3, message="quia", error="magni", data={"facere": 8}
        )
        self.assertEqual(test_model.statusCode, 3)
        self.assertEqual(test_model.message, "quia")
        self.assertEqual(test_model.error, "magni")
        self.assertEqual(test_model.data, {"facere": 8})

    def test_get_contact_response_required_fields_missing(self):
        # Assert GetContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactResponse()


if __name__ == "__main__":
    unittest.main()
