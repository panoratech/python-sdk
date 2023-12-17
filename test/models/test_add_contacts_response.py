import unittest
from src.panorasdk.models.AddContactsResponse import AddContactsResponse


class TestAddContactsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_contacts_response(self):
        # Create AddContactsResponse class instance
        test_model = AddContactsResponse(
            statusCode=1, message="molestias", error="voluptate", data={"quaerat": 3}
        )
        self.assertEqual(test_model.statusCode, 1)
        self.assertEqual(test_model.message, "molestias")
        self.assertEqual(test_model.error, "voluptate")
        self.assertEqual(test_model.data, {"quaerat": 3})

    def test_add_contacts_response_required_fields_missing(self):
        # Assert AddContactsResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddContactsResponse()


if __name__ == "__main__":
    unittest.main()
