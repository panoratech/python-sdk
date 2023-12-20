import unittest
from src.panorasdk.models.AddContactResponse import AddContactResponse


class TestAddContactResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_contact_response(self):
        # Create AddContactResponse class instance
        test_model = AddContactResponse(
            statusCode=1, message="dolorem", error="ipsam", data={"maiores": 6}
        )
        self.assertEqual(test_model.statusCode, 1)
        self.assertEqual(test_model.message, "dolorem")
        self.assertEqual(test_model.error, "ipsam")
        self.assertEqual(test_model.data, {"maiores": 6})

    def test_add_contact_response_required_fields_missing(self):
        # Assert AddContactResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddContactResponse()


if __name__ == "__main__":
    unittest.main()
