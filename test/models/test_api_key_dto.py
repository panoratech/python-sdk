import unittest
from src.panorasdk.models.ApiKeyDto import ApiKeyDto


class TestApiKeyDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_api_key_dto(self):
        # Create ApiKeyDto class instance
        test_model = ApiKeyDto(
            userId="voluptatum", projectId="optio", keyName="recusandae"
        )
        self.assertEqual(test_model.userId, "voluptatum")
        self.assertEqual(test_model.projectId, "optio")
        self.assertEqual(test_model.keyName, "recusandae")

    def test_api_key_dto_required_fields_missing(self):
        # Assert ApiKeyDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ApiKeyDto()


if __name__ == "__main__":
    unittest.main()
