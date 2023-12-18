import unittest
from src.panorasdk.models.WebhookDto import WebhookDto


class TestWebhookDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_webhook_dto(self):
        # Create WebhookDto class instance
        test_model = WebhookDto(
            scope="quidem", id_project="voluptate", url="quis", description="esse"
        )
        self.assertEqual(test_model.scope, "quidem")
        self.assertEqual(test_model.id_project, "voluptate")
        self.assertEqual(test_model.url, "quis")
        self.assertEqual(test_model.description, "esse")

    def test_webhook_dto_required_fields_missing(self):
        # Assert WebhookDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = WebhookDto()


if __name__ == "__main__":
    unittest.main()
