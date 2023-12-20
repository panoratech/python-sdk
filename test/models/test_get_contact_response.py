import unittest
from src.panorasdk.models.GetContactResponse import GetContactResponse


class TestGetContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_contact_response(self):
        # Create GetContactResponse class instance
        test_model = GetContactResponse(
            statusCode=4, message="rem", error="distinctio", data={"ipsam": 8}
        )
        self.assertEqual(test_model.statusCode, 4)
        self.assertEqual(test_model.message, "rem")
        self.assertEqual(test_model.error, "distinctio")
        self.assertEqual(test_model.data, {"ipsam": 8})

    def test_get_contact_response_required_fields_missing(self):
        # Assert GetContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GetContactResponse()


if __name__ == "__main__":
    unittest.main()
