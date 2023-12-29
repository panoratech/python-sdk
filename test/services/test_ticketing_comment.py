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
        response = test_service.get_comments("5766531292", "8471985993", True)
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
            test_service.get_comments("1911981381", "7780774613", True)
        responses.reset()

    @responses.activate
    def test_add_comment(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/comment", json={}, status=200
        )
        # call the method to test
        test_service = TicketingComment("testkey")
        response = test_service.add_comment({}, "9358905195", "6511932972", True)
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
            test_service.add_comment({}, "9678711356", "5441249215", True)
        responses.reset()

    @responses.activate
    def test_update_comment(self):
        # Mock the API response
        responses.patch(
            "https://api-demo.panora.dev/ticketing/comment", json={}, status=200
        )
        # call the method to test
        test_service = TicketingComment("testkey")
        response = test_service.update_comment("2293915984")
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
            test_service.update_comment("7214744693")
        responses.reset()

    @responses.activate
    def test_get_comment(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/comment/8342519740",
            json={},
            status=200,
        )
        # call the method to test
        test_service = TicketingComment("testkey")
        response = test_service.get_comment("8342519740", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_comment_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/comment/1207802331",
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
            "https://api-demo.panora.dev/ticketing/comment/1019691993",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = TicketingComment("testkey")
            test_service.get_comment("1019691993", True)
        responses.reset()

    @responses.activate
    def test_add_comments(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/comment/batch", json={}, status=200
        )
        # call the method to test
        test_service = TicketingComment("testkey")
        response = test_service.add_comments({}, "9718134309", "5359889251", True)
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
            test_service.add_comments({}, "6221412099", "2878647817", True)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
