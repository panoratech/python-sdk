import unittest
from src.panorasdk.models.AddContactResponse import AddContactResponse


class TestAddContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_contact_response(self):
        # Create AddContactResponse class instance
        test_model = AddContactResponse(
            statusCode=9, message="aut", error="hic", data={"voluptatum": 1}
        )
        self.assertEqual(test_model.statusCode, 9)
        self.assertEqual(test_model.message, "aut")
        self.assertEqual(test_model.error, "hic")
        self.assertEqual(test_model.data, {"voluptatum": 1})

    def test_add_contact_response_required_fields_missing(self):
        # Assert AddContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddContactResponse()


if __name__ == "__main__":
    unittest.main()
