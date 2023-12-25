import unittest
import responses
from src.panorasdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.panorasdk.services.protected import Protected


class TestProtected_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_app_controller_get_hello2(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/protected", json={}, status=200)
        # call the method to test
        test_service = Protected("testkey")
        response = test_service.app_controller_get_hello2()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_app_controller_get_hello2_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/protected", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Protected("testkey")
            test_service.app_controller_get_hello2()
        responses.reset()


if __name__ == "__main__":
    unittest.main()
