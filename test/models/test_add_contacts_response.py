import unittest
from src.panorasdk.models.AddContactsResponse import AddContactsResponse


class TestAddContactsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_contacts_response(self):
        # Create AddContactsResponse class instance
        test_model = AddContactsResponse(
            statusCode=5, message="dolor", error="ullam", data={"optio": 5}
        )
        self.assertEqual(test_model.statusCode, 5)
        self.assertEqual(test_model.message, "dolor")
        self.assertEqual(test_model.error, "ullam")
        self.assertEqual(test_model.data, {"optio": 5})

    def test_add_contacts_response_required_fields_missing(self):
        # Assert AddContactsResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddContactsResponse()


if __name__ == "__main__":
    unittest.main()
