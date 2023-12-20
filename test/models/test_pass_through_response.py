import unittest
from src.panorasdk.models.PassThroughResponse import PassThroughResponse


class TestPassThroughResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_pass_through_response(self):
        # Create PassThroughResponse class instance
        test_model = PassThroughResponse(data={"hic": 2}, status=4, url="quas")
        self.assertEqual(test_model.data, {"hic": 2})
        self.assertEqual(test_model.status, 4)
        self.assertEqual(test_model.url, "quas")

    def test_pass_through_response_required_fields_missing(self):
        # Assert PassThroughResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = PassThroughResponse()


if __name__ == "__main__":
    unittest.main()
