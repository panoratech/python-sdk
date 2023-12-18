import unittest
from src.panorasdk.models.GetContactResponse import GetContactResponse


class TestGetContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contact_response(self):
        # Create GetContactResponse class instance
        test_model = GetContactResponse(
            statusCode=9, message="totam", error="minima", data={"reiciendis": 4}
        )
        self.assertEqual(test_model.statusCode, 9)
        self.assertEqual(test_model.message, "totam")
        self.assertEqual(test_model.error, "minima")
        self.assertEqual(test_model.data, {"reiciendis": 4})

    def test_get_contact_response_required_fields_missing(self):
        # Assert GetContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactResponse()


if __name__ == "__main__":
    unittest.main()
