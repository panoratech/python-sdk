import unittest
from src.panorasdk.models.AddContactResponse import AddContactResponse


class TestAddContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_contact_response(self):
        # Create AddContactResponse class instance
        test_model = AddContactResponse(
            statusCode=8, message="eius", error="nam", data={"amet": 2}
        )
        self.assertEqual(test_model.statusCode, 8)
        self.assertEqual(test_model.message, "eius")
        self.assertEqual(test_model.error, "nam")
        self.assertEqual(test_model.data, {"amet": 2})

    def test_add_contact_response_required_fields_missing(self):
        # Assert AddContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddContactResponse()


if __name__ == "__main__":
    unittest.main()
