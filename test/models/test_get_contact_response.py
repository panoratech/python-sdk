import unittest
from src.panorasdk.models.GetContactResponse import GetContactResponse


class TestGetContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contact_response(self):
        # Create GetContactResponse class instance
        test_model = GetContactResponse(
            statusCode=8, message="neque", error="beatae", data={"perspiciatis": 1}
        )
        self.assertEqual(test_model.statusCode, 8)
        self.assertEqual(test_model.message, "neque")
        self.assertEqual(test_model.error, "beatae")
        self.assertEqual(test_model.data, {"perspiciatis": 1})

    def test_get_contact_response_required_fields_missing(self):
        # Assert GetContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactResponse()


if __name__ == "__main__":
    unittest.main()
