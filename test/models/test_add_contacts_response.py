import unittest
from src.panorasdk.models.AddContactsResponse import AddContactsResponse


class TestAddContactsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_contacts_response(self):
        # Create AddContactsResponse class instance
        test_model = AddContactsResponse(
            statusCode=9, message="voluptate", error="laudantium", data={"nihil": 4}
        )
        self.assertEqual(test_model.statusCode, 9)
        self.assertEqual(test_model.message, "voluptate")
        self.assertEqual(test_model.error, "laudantium")
        self.assertEqual(test_model.data, {"nihil": 4})

    def test_add_contacts_response_required_fields_missing(self):
        # Assert AddContactsResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddContactsResponse()


if __name__ == "__main__":
    unittest.main()
