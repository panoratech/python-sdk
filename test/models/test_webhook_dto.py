import unittest
from src.panorasdk.models.WebhookDto import WebhookDto


class TestWebhookDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_webhook_dto(self):
        # Create WebhookDto class instance
        test_model = WebhookDto(
            scope="sed", id_project="magni", url="repellendus", description="placeat"
        )
        self.assertEqual(test_model.scope, "sed")
        self.assertEqual(test_model.id_project, "magni")
        self.assertEqual(test_model.url, "repellendus")
        self.assertEqual(test_model.description, "placeat")

    def test_webhook_dto_required_fields_missing(self):
        # Assert WebhookDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = WebhookDto()


if __name__ == "__main__":
    unittest.main()
