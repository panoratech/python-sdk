import unittest
from src.panorasdk.models.GetContactResponse import GetContactResponse


class TestGetContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contact_response(self):
        # Create GetContactResponse class instance
        test_model = GetContactResponse(
            statusCode=3, message="recusandae", error="explicabo", data={"debitis": 9}
        )
        self.assertEqual(test_model.statusCode, 3)
        self.assertEqual(test_model.message, "recusandae")
        self.assertEqual(test_model.error, "explicabo")
        self.assertEqual(test_model.data, {"debitis": 9})

    def test_get_contact_response_required_fields_missing(self):
        # Assert GetContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactResponse()


if __name__ == "__main__":
    unittest.main()
