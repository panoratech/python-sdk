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
        response = test_service.get_comments("5008335197", "6584292575", True)
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
            test_service.get_comments("5898155544", "9207086452", True)
        responses.reset()

    @responses.activate
    def test_add_comment(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/comment", json={}, status=200
        )
        # call the method to test
        test_service = TicketingComment("testkey")
        response = test_service.add_comment({}, "1480562057", "2866932178", True)
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
            test_service.add_comment({}, "3981098500", "1646717714", True)
        responses.reset()

    @responses.activate
    def test_update_comment(self):
        # Mock the API response
        responses.patch(
            "https://api-demo.panora.dev/ticketing/comment", json={}, status=200
        )
        # call the method to test
        test_service = TicketingComment("testkey")
        response = test_service.update_comment("6341695416")
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
            test_service.update_comment("8256135808")
        responses.reset()

    @responses.activate
    def test_get_comment(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/comment/1201981309",
            json={},
            status=200,
        )
        # call the method to test
        test_service = TicketingComment("testkey")
        response = test_service.get_comment("1201981309", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_comment_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/comment/3130054856",
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
            "https://api-demo.panora.dev/ticketing/comment/7952828841",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = TicketingComment("testkey")
            test_service.get_comment("7952828841", True)
        responses.reset()

    @responses.activate
    def test_add_comments(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/comment/batch", json={}, status=200
        )
        # call the method to test
        test_service = TicketingComment("testkey")
        response = test_service.add_comments({}, "8063797698", "6700329062", True)
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
            test_service.add_comments({}, "3717508517", "8049421739", True)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
