import unittest
from src.panorasdk.models.AddContactResponse import AddContactResponse


class TestAddContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_contact_response(self):
        # Create AddContactResponse class instance
        test_model = AddContactResponse(
            statusCode=7, message="ad", error="cumque", data={"nobis": 2}
        )
        self.assertEqual(test_model.statusCode, 7)
        self.assertEqual(test_model.message, "ad")
        self.assertEqual(test_model.error, "cumque")
        self.assertEqual(test_model.data, {"nobis": 2})

    def test_add_contact_response_required_fields_missing(self):
        # Assert AddContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddContactResponse()


if __name__ == "__main__":
    unittest.main()
