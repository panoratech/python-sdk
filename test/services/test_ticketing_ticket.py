import unittest
import responses
from src.panorasdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.panorasdk.services.ticketing_ticket import TicketingTicket


class TestTicketingTicket_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_tickets(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.get_tickets("6012849729", "1521093979", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_tickets_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = TicketingTicket("testkey")
            test_service.get_tickets()
        responses.reset(),

    @responses.activate
    def test_get_tickets_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = TicketingTicket("testkey")
            test_service.get_tickets("3383844426", "3471650219", True)
        responses.reset()

    @responses.activate
    def test_add_ticket(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.add_ticket({}, "7830589339", "1734222817", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_ticket_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = TicketingTicket("testkey")
            test_service.add_ticket()
        responses.reset(),

    @responses.activate
    def test_add_ticket_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = TicketingTicket("testkey")
            test_service.add_ticket({}, "7427273688", "8514403287", True)
        responses.reset()

    @responses.activate
    def test_update_ticket(self):
        # Mock the API response
        responses.patch(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.update_ticket("6889155330")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_ticket_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = TicketingTicket("testkey")
            test_service.update_ticket()
        responses.reset(),

    @responses.activate
    def test_update_ticket_error_on_non_200(self):
        # Mock the API response
        responses.patch(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = TicketingTicket("testkey")
            test_service.update_ticket("2111635972")
        responses.reset()

    @responses.activate
    def test_get_ticket(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/ticket/2753396880",
            json={},
            status=200,
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.get_ticket("2753396880", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_ticket_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/ticket/9269548435",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = TicketingTicket("testkey")
            test_service.get_ticket()
        responses.reset(),

    @responses.activate
    def test_get_ticket_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/ticket/8731841120",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = TicketingTicket("testkey")
            test_service.get_ticket("8731841120", True)
        responses.reset()

    @responses.activate
    def test_add_tickets(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/ticket/batch", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.add_tickets({}, "7183829874", "8177459608", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_tickets_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/ticket/batch", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = TicketingTicket("testkey")
            test_service.add_tickets()
        responses.reset(),

    @responses.activate
    def test_add_tickets_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/ticket/batch", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = TicketingTicket("testkey")
            test_service.add_tickets({}, "1439906084", "1374335121", True)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
