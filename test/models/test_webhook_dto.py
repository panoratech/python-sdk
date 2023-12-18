import unittest
from src.panorasdk.models.WebhookDto import WebhookDto


class TestWebhookDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_webhook_dto(self):
        # Create WebhookDto class instance
        test_model = WebhookDto(
            scope="tenetur",
            id_project="sequi",
            url="repudiandae",
            description="aspernatur",
        )
        self.assertEqual(test_model.scope, "tenetur")
        self.assertEqual(test_model.id_project, "sequi")
        self.assertEqual(test_model.url, "repudiandae")
        self.assertEqual(test_model.description, "aspernatur")

    def test_webhook_dto_required_fields_missing(self):
        # Assert WebhookDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = WebhookDto()


if __name__ == "__main__":
    unittest.main()
