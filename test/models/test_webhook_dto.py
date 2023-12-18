import unittest
from src.panorasdk.models.WebhookDto import WebhookDto


class TestWebhookDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_webhook_dto(self):
        # Create WebhookDto class instance
        test_model = WebhookDto(
            scope="accusamus",
            id_project="molestiae",
            url="tenetur",
            description="minima",
        )
        self.assertEqual(test_model.scope, "accusamus")
        self.assertEqual(test_model.id_project, "molestiae")
        self.assertEqual(test_model.url, "tenetur")
        self.assertEqual(test_model.description, "minima")

    def test_webhook_dto_required_fields_missing(self):
        # Assert WebhookDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = WebhookDto()


if __name__ == "__main__":
    unittest.main()
