import unittest
import responses
from src.panorasdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.panorasdk.services.linked_users import LinkedUsers


class TestLinkedUsers_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_add_linked_user(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/linked-users/create", json={}, status=200
        )
        # call the method to test
        test_service = LinkedUsers("testkey")
        response = test_service.add_linked_user({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_linked_user_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/linked-users/create", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LinkedUsers("testkey")
            test_service.add_linked_user({})
        responses.reset()

    @responses.activate
    def test_get_linked_users(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/linked-users", json={}, status=200)
        # call the method to test
        test_service = LinkedUsers("testkey")
        response = test_service.get_linked_users()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_linked_users_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/linked-users", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = LinkedUsers("testkey")
            test_service.get_linked_users()
        responses.reset()

    @responses.activate
    def test_get_linked_user(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/linked-users/single", json={}, status=200
        )
        # call the method to test
        test_service = LinkedUsers("testkey")
        response = test_service.get_linked_user("2413505756")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_linked_user_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/linked-users/single", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LinkedUsers("testkey")
            test_service.get_linked_user()
        responses.reset(),

    @responses.activate
    def test_get_linked_user_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/linked-users/single", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LinkedUsers("testkey")
            test_service.get_linked_user("7972063877")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
