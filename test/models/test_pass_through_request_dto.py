import unittest
from src.panorasdk.models.PassThroughRequestDto import PassThroughRequestDto


class TestPassThroughRequestDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_pass_through_request_dto(self):
        # Create PassThroughRequestDto class instance
        test_model = PassThroughRequestDto(
            path="nostrum", method="GET", data={"molestias": 7}, headers_={"eum": 2}
        )
        self.assertEqual(test_model.path, "nostrum")
        self.assertEqual(test_model.method, "GET")
        self.assertEqual(test_model.data, {"molestias": 7})
        self.assertEqual(test_model.headers_, {"eum": 2})

    def test_pass_through_request_dto_required_fields_missing(self):
        # Assert PassThroughRequestDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = PassThroughRequestDto()


if __name__ == "__main__":
    unittest.main()
