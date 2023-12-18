import unittest
from src.panorasdk.models.AddContactsResponse import AddContactsResponse


class TestAddContactsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_contacts_response(self):
        # Create AddContactsResponse class instance
        test_model = AddContactsResponse(
            statusCode=1, message="consequatur", error="labore", data={"illum": 5}
        )
        self.assertEqual(test_model.statusCode, 1)
        self.assertEqual(test_model.message, "consequatur")
        self.assertEqual(test_model.error, "labore")
        self.assertEqual(test_model.data, {"illum": 5})

    def test_add_contacts_response_required_fields_missing(self):
        # Assert AddContactsResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddContactsResponse()


if __name__ == "__main__":
    unittest.main()
