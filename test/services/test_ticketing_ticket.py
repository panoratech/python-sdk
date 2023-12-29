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
        response = test_service.get_tickets("2217803373", "5564804699", True)
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
            test_service.get_tickets("7312884636", "2851417223", True)
        responses.reset()

    @responses.activate
    def test_add_ticket(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.add_ticket({}, "7881064497", "8728666157", True)
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
            test_service.add_ticket({}, "8975085462", "7698362237", True)
        responses.reset()

    @responses.activate
    def test_update_ticket(self):
        # Mock the API response
        responses.patch(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.update_ticket("4608186126")
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
            test_service.update_ticket("5023008046")
        responses.reset()

    @responses.activate
    def test_get_ticket(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/ticket/3806532234",
            json={},
            status=200,
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.get_ticket("3806532234", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_ticket_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/ticket/7810303307",
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
            "https://api-demo.panora.dev/ticketing/ticket/6084810715",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = TicketingTicket("testkey")
            test_service.get_ticket("6084810715", True)
        responses.reset()

    @responses.activate
    def test_add_tickets(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/ticket/batch", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.add_tickets({}, "9168800178", "7295177257", True)
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
            test_service.add_tickets({}, "4140828487", "1492480731", True)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
