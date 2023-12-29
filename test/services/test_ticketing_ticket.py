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
        response = test_service.get_tickets("4513538677", "5074159513", True)
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
            test_service.get_tickets("5589579768", "8091548404", True)
        responses.reset()

    @responses.activate
    def test_add_ticket(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.add_ticket({}, "4335565017", "7755350365", True)
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
            test_service.add_ticket({}, "9333168940", "9297433385", True)
        responses.reset()

    @responses.activate
    def test_update_ticket(self):
        # Mock the API response
        responses.patch(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.update_ticket("6922524356")
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
            test_service.update_ticket("4599639261")
        responses.reset()

    @responses.activate
    def test_get_ticket(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/ticket/5124553693",
            json={},
            status=200,
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.get_ticket("5124553693", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_ticket_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/ticket/3874763810",
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
            "https://api-demo.panora.dev/ticketing/ticket/9616627898",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = TicketingTicket("testkey")
            test_service.get_ticket("9616627898", True)
        responses.reset()

    @responses.activate
    def test_add_tickets(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/ticket/batch", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.add_tickets({}, "3923434661", "4793059611", True)
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
            test_service.add_tickets({}, "3419677747", "7624939313", True)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
