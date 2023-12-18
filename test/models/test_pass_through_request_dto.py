import unittest
from src.panorasdk.models.PassThroughRequestDto import PassThroughRequestDto


class TestPassThroughRequestDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_pass_through_request_dto(self):
        # Create PassThroughRequestDto class instance
        test_model = PassThroughRequestDto(
            path="quam", method="GET", data={"ullam": 9}, headers_={"nihil": 3}
        )
        self.assertEqual(test_model.path, "quam")
        self.assertEqual(test_model.method, "GET")
        self.assertEqual(test_model.data, {"ullam": 9})
        self.assertEqual(test_model.headers_, {"nihil": 3})

    def test_pass_through_request_dto_required_fields_missing(self):
        # Assert PassThroughRequestDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = PassThroughRequestDto()


if __name__ == "__main__":
    unittest.main()
