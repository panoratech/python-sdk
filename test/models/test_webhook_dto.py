import unittest
from src.panorasdk.models.WebhookDto import WebhookDto


class TestWebhookDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_webhook_dto(self):
        # Create WebhookDto class instance
        test_model = WebhookDto(
            scope=["totam", "assumenda"],
            id_project="unde",
            url="modi",
            description="natus",
        )
        self.assertEqual(test_model.scope, ["totam", "assumenda"])
        self.assertEqual(test_model.id_project, "unde")
        self.assertEqual(test_model.url, "modi")
        self.assertEqual(test_model.description, "natus")

    def test_webhook_dto_required_fields_missing(self):
        # Assert WebhookDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = WebhookDto()


if __name__ == "__main__":
    unittest.main()
