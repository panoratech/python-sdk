import unittest
from src.panorasdk.models.AddContactResponse import AddContactResponse


class TestAddContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_contact_response(self):
        # Create AddContactResponse class instance
        test_model = AddContactResponse(
            statusCode=2, message="quisquam", error="cum", data={"impedit": 9}
        )
        self.assertEqual(test_model.statusCode, 2)
        self.assertEqual(test_model.message, "quisquam")
        self.assertEqual(test_model.error, "cum")
        self.assertEqual(test_model.data, {"impedit": 9})

    def test_add_contact_response_required_fields_missing(self):
        # Assert AddContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddContactResponse()


if __name__ == "__main__":
    unittest.main()
