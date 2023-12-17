import unittest
from src.panorasdk.models.AddContactResponse import AddContactResponse


class TestAddContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_contact_response(self):
        # Create AddContactResponse class instance
        test_model = AddContactResponse(
            statusCode=6, message="perferendis", error="libero", data={"saepe": 2}
        )
        self.assertEqual(test_model.statusCode, 6)
        self.assertEqual(test_model.message, "perferendis")
        self.assertEqual(test_model.error, "libero")
        self.assertEqual(test_model.data, {"saepe": 2})

    def test_add_contact_response_required_fields_missing(self):
        # Assert AddContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddContactResponse()


if __name__ == "__main__":
    unittest.main()
