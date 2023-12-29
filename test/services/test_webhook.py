import unittest
import responses
from src.panorasdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.panorasdk.services.webhook import Webhook


class TestWebhook_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_webhooks_metadata(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/webhook", json={}, status=200)
        # call the method to test
        test_service = Webhook("testkey")
        response = test_service.get_webhooks_metadata()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_webhooks_metadata_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/webhook", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Webhook("testkey")
            test_service.get_webhooks_metadata()
        responses.reset()

    @responses.activate
    def test_create_webhook_metadata(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/webhook", json={}, status=200)
        # call the method to test
        test_service = Webhook("testkey")
        response = test_service.create_webhook_metadata({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_webhook_metadata_error_on_non_200(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/webhook", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Webhook("testkey")
            test_service.create_webhook_metadata({})
        responses.reset()

    @responses.activate
    def test_update_webhook_status(self):
        # Mock the API response
        responses.put(
            "https://api-demo.panora.dev/webhook/5882047801", json={}, status=200
        )
        # call the method to test
        test_service = Webhook("testkey")
        response = test_service.update_webhook_status("5882047801")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_webhook_status_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "https://api-demo.panora.dev/webhook/7644811787", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Webhook("testkey")
            test_service.update_webhook_status()
        responses.reset(),

    @responses.activate
    def test_update_webhook_status_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "https://api-demo.panora.dev/webhook/8180888774", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Webhook("testkey")
            test_service.update_webhook_status("8180888774")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
