import unittest
from src.panorasdk.models.GetContactResponse import GetContactResponse


class TestGetContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contact_response(self):
        # Create GetContactResponse class instance
        test_model = GetContactResponse(
            statusCode=7, message="dolore", error="a", data={"dolores": 8}
        )
        self.assertEqual(test_model.statusCode, 7)
        self.assertEqual(test_model.message, "dolore")
        self.assertEqual(test_model.error, "a")
        self.assertEqual(test_model.data, {"dolores": 8})

    def test_get_contact_response_required_fields_missing(self):
        # Assert GetContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactResponse()


if __name__ == "__main__":
    unittest.main()
