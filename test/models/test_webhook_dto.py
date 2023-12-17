import unittest
from src.panorasdk.models.WebhookDto import WebhookDto


class TestWebhookDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_webhook_dto(self):
        # Create WebhookDto class instance
        test_model = WebhookDto(
            scope="esse", id_project="atque", url="ratione", description="nisi"
        )
        self.assertEqual(test_model.scope, "esse")
        self.assertEqual(test_model.id_project, "atque")
        self.assertEqual(test_model.url, "ratione")
        self.assertEqual(test_model.description, "nisi")

    def test_webhook_dto_required_fields_missing(self):
        # Assert WebhookDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = WebhookDto()


if __name__ == "__main__":
    unittest.main()
