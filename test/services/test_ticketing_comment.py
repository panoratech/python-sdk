import unittest
import responses
from src.panorasdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.panorasdk.services.ticketing_comment import TicketingComment


class TestTicketingComment_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_comments(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/comment", json={}, status=200
        )
        # call the method to test
        test_service = TicketingComment("testkey")
        response = test_service.get_comments("9518231580", "3969066995", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_comments_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/comment", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = TicketingComment("testkey")
            test_service.get_comments()
        responses.reset(),

    @responses.activate
    def test_get_comments_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/comment", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = TicketingComment("testkey")
            test_service.get_comments("9476261644", "4764274379", True)
        responses.reset()

    @responses.activate
    def test_add_comment(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/comment", json={}, status=200
        )
        # call the method to test
        test_service = TicketingComment("testkey")
        response = test_service.add_comment({}, "4486870817", "9345583028", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_comment_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/comment", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = TicketingComment("testkey")
            test_service.add_comment()
        responses.reset(),

    @responses.activate
    def test_add_comment_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/comment", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = TicketingComment("testkey")
            test_service.add_comment({}, "9321585980", "3941076987", True)
        responses.reset()

    @responses.activate
    def test_update_comment(self):
        # Mock the API response
        responses.patch(
            "https://api-demo.panora.dev/ticketing/comment", json={}, status=200
        )
        # call the method to test
        test_service = TicketingComment("testkey")
        response = test_service.update_comment("4366997208")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_comment_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api-demo.panora.dev/ticketing/comment", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = TicketingComment("testkey")
            test_service.update_comment()
        responses.reset(),

    @responses.activate
    def test_update_comment_error_on_non_200(self):
        # Mock the API response
        responses.patch(
            "https://api-demo.panora.dev/ticketing/comment", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = TicketingComment("testkey")
            test_service.update_comment("2934397432")
        responses.reset()

    @responses.activate
    def test_get_comment(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/comment/2025024734",
            json={},
            status=200,
        )
        # call the method to test
        test_service = TicketingComment("testkey")
        response = test_service.get_comment("2025024734", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_comment_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/comment/3238006924",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = TicketingComment("testkey")
            test_service.get_comment()
        responses.reset(),

    @responses.activate
    def test_get_comment_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/comment/5945756865",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = TicketingComment("testkey")
            test_service.get_comment("5945756865", True)
        responses.reset()

    @responses.activate
    def test_add_comments(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/comment/batch", json={}, status=200
        )
        # call the method to test
        test_service = TicketingComment("testkey")
        response = test_service.add_comments({}, "8796324099", "8813738829", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_comments_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/comment/batch", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = TicketingComment("testkey")
            test_service.add_comments()
        responses.reset(),

    @responses.activate
    def test_add_comments_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/comment/batch", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = TicketingComment("testkey")
            test_service.add_comments({}, "8907113134", "1792255974", True)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
