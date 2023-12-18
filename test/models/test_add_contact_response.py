import unittest
from src.panorasdk.models.AddContactResponse import AddContactResponse


class TestAddContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_contact_response(self):
        # Create AddContactResponse class instance
        test_model = AddContactResponse(
            statusCode=4, message="blanditiis", error="accusamus", data={"officiis": 2}
        )
        self.assertEqual(test_model.statusCode, 4)
        self.assertEqual(test_model.message, "blanditiis")
        self.assertEqual(test_model.error, "accusamus")
        self.assertEqual(test_model.data, {"officiis": 2})

    def test_add_contact_response_required_fields_missing(self):
        # Assert AddContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddContactResponse()


if __name__ == "__main__":
    unittest.main()
