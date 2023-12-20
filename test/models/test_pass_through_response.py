import unittest
from src.panorasdk.models.PassThroughResponse import PassThroughResponse


class TestPassThroughResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_pass_through_response(self):
        # Create PassThroughResponse class instance
        test_model = PassThroughResponse(data={"ipsam": 9}, status=8, url="veritatis")
        self.assertEqual(test_model.data, {"ipsam": 9})
        self.assertEqual(test_model.status, 8)
        self.assertEqual(test_model.url, "veritatis")

    def test_pass_through_response_required_fields_missing(self):
        # Assert PassThroughResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = PassThroughResponse()


if __name__ == "__main__":
    unittest.main()
