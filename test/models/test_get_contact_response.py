import unittest
from src.panorasdk.models.GetContactResponse import GetContactResponse


class TestGetContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contact_response(self):
        # Create GetContactResponse class instance
        test_model = GetContactResponse(
            statusCode=7, message="ex", error="nesciunt", data={"expedita": 6}
        )
        self.assertEqual(test_model.statusCode, 7)
        self.assertEqual(test_model.message, "ex")
        self.assertEqual(test_model.error, "nesciunt")
        self.assertEqual(test_model.data, {"expedita": 6})

    def test_get_contact_response_required_fields_missing(self):
        # Assert GetContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactResponse()


if __name__ == "__main__":
    unittest.main()
