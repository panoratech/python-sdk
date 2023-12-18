import unittest
from src.panorasdk.models.PassThroughResponse import PassThroughResponse


class TestPassThroughResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_pass_through_response(self):
        # Create PassThroughResponse class instance
        test_model = PassThroughResponse(
            data={"recusandae": 9}, status=7, url="aperiam"
        )
        self.assertEqual(test_model.data, {"recusandae": 9})
        self.assertEqual(test_model.status, 7)
        self.assertEqual(test_model.url, "aperiam")

    def test_pass_through_response_required_fields_missing(self):
        # Assert PassThroughResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = PassThroughResponse()


if __name__ == "__main__":
    unittest.main()
