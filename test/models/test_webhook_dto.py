import unittest
from src.panorasdk.models.WebhookDto import WebhookDto


class TestWebhookDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_webhook_dto(self):
        # Create WebhookDto class instance
        test_model = WebhookDto(
            scope=["cum", "ut"], id_project="magnam", url="dolorem", description="in"
        )
        self.assertEqual(test_model.scope, ["cum", "ut"])
        self.assertEqual(test_model.id_project, "magnam")
        self.assertEqual(test_model.url, "dolorem")
        self.assertEqual(test_model.description, "in")

    def test_webhook_dto_required_fields_missing(self):
        # Assert WebhookDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = WebhookDto()


if __name__ == "__main__":
    unittest.main()
