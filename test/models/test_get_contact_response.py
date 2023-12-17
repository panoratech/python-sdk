import unittest
from src.panorasdk.models.GetContactResponse import GetContactResponse


class TestGetContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contact_response(self):
        # Create GetContactResponse class instance
        test_model = GetContactResponse(
            statusCode=2, message="deleniti", error="quis", data={"commodi": 7}
        )
        self.assertEqual(test_model.statusCode, 2)
        self.assertEqual(test_model.message, "deleniti")
        self.assertEqual(test_model.error, "quis")
        self.assertEqual(test_model.data, {"commodi": 7})

    def test_get_contact_response_required_fields_missing(self):
        # Assert GetContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactResponse()


if __name__ == "__main__":
    unittest.main()
