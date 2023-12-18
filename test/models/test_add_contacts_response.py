import unittest
from src.panorasdk.models.AddContactsResponse import AddContactsResponse


class TestAddContactsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_contacts_response(self):
        # Create AddContactsResponse class instance
        test_model = AddContactsResponse(
            statusCode=8, message="voluptatem", error="omnis", data={"quod": 9}
        )
        self.assertEqual(test_model.statusCode, 8)
        self.assertEqual(test_model.message, "voluptatem")
        self.assertEqual(test_model.error, "omnis")
        self.assertEqual(test_model.data, {"quod": 9})

    def test_add_contacts_response_required_fields_missing(self):
        # Assert AddContactsResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddContactsResponse()


if __name__ == "__main__":
    unittest.main()
