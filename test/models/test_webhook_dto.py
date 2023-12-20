import unittest
from src.panorasdk.models.WebhookDto import WebhookDto


class TestWebhookDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_webhook_dto(self):
        # Create WebhookDto class instance
        test_model = WebhookDto(
            scope=["quisquam", "provident"],
            id_project="reprehenderit",
            url="voluptatum",
            description="expedita",
        )
        self.assertEqual(test_model.scope, ["quisquam", "provident"])
        self.assertEqual(test_model.id_project, "reprehenderit")
        self.assertEqual(test_model.url, "voluptatum")
        self.assertEqual(test_model.description, "expedita")

    def test_webhook_dto_required_fields_missing(self):
        # Assert WebhookDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = WebhookDto()


if __name__ == "__main__":
    unittest.main()
