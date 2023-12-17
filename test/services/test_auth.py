import unittest
import responses
from src.panorasdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.panorasdk.services.auth import Auth


class TestAuth_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_sign_up(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/auth/register", json={}, status=200)
        # call the method to test
        test_service = Auth("testkey")
        response = test_service.sign_up({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_sign_up_error_on_non_200(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/auth/register", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Auth("testkey")
            test_service.sign_up({})
        responses.reset()

    @responses.activate
    def test_sign_in(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/auth/login", json={}, status=200)
        # call the method to test
        test_service = Auth("testkey")
        response = test_service.sign_in({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_sign_in_error_on_non_200(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/auth/login", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Auth("testkey")
            test_service.sign_in({})
        responses.reset()

    @responses.activate
    def test_get_users(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/auth/users", json={}, status=200)
        # call the method to test
        test_service = Auth("testkey")
        response = test_service.get_users()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_users_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/auth/users", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Auth("testkey")
            test_service.get_users()
        responses.reset()

    @responses.activate
    def test_get_api_keys(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/auth/api-keys", json={}, status=200)
        # call the method to test
        test_service = Auth("testkey")
        response = test_service.get_api_keys()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_api_keys_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/auth/api-keys", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Auth("testkey")
            test_service.get_api_keys()
        responses.reset()

    @responses.activate
    def test_generate_api_key(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/auth/generate-apikey", json={}, status=200
        )
        # call the method to test
        test_service = Auth("testkey")
        response = test_service.generate_api_key({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_generate_api_key_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/auth/generate-apikey", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Auth("testkey")
            test_service.generate_api_key({})
        responses.reset()


if __name__ == "__main__":
    unittest.main()
