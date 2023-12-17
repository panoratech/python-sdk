import unittest
import responses
from src.panorasdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.panorasdk.services.connections import Connections


class TestConnections_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_handle_o_auth_callback(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/connections/oauth/callback",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Connections("testkey")
        response = test_service.handle_o_auth_callback("necessitatibus", "id", "ut")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_handle_o_auth_callback_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/connections/oauth/callback",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Connections("testkey")
            test_service.handle_o_auth_callback()
        responses.reset(),

    @responses.activate
    def test_handle_o_auth_callback_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/connections/oauth/callback",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Connections("testkey")
            test_service.handle_o_auth_callback("officia", "velit", "reiciendis")
        responses.reset()

    @responses.activate
    def test_get_connections(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/connections", json={}, status=200)
        # call the method to test
        test_service = Connections("testkey")
        response = test_service.get_connections()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_connections_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/connections", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Connections("testkey")
            test_service.get_connections()
        responses.reset()


if __name__ == "__main__":
    unittest.main()
