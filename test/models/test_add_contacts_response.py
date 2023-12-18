import unittest
from src.panorasdk.models.AddContactsResponse import AddContactsResponse


class TestAddContactsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_contacts_response(self):
        # Create AddContactsResponse class instance
        test_model = AddContactsResponse(
            statusCode=2, message="quo", error="ex", data={"voluptates": 7}
        )
        self.assertEqual(test_model.statusCode, 2)
        self.assertEqual(test_model.message, "quo")
        self.assertEqual(test_model.error, "ex")
        self.assertEqual(test_model.data, {"voluptates": 7})

    def test_add_contacts_response_required_fields_missing(self):
        # Assert AddContactsResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddContactsResponse()


if __name__ == "__main__":
    unittest.main()
