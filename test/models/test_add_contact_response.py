import unittest
from src.panorasdk.models.AddContactResponse import AddContactResponse


class TestAddContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_contact_response(self):
        # Create AddContactResponse class instance
        test_model = AddContactResponse(
            statusCode=4, message="excepturi", error="minima", data={"nihil": 8}
        )
        self.assertEqual(test_model.statusCode, 4)
        self.assertEqual(test_model.message, "excepturi")
        self.assertEqual(test_model.error, "minima")
        self.assertEqual(test_model.data, {"nihil": 8})

    def test_add_contact_response_required_fields_missing(self):
        # Assert AddContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddContactResponse()


if __name__ == "__main__":
    unittest.main()
