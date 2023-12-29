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
        response = test_service.get_tickets("9247750119", "3318492077", True)
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
            test_service.get_tickets("2471905586", "1612092398", True)
        responses.reset()

    @responses.activate
    def test_add_ticket(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.add_ticket({}, "9603381990", "3207024687", True)
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
            test_service.add_ticket({}, "1034827672", "4376662207", True)
        responses.reset()

    @responses.activate
    def test_update_ticket(self):
        # Mock the API response
        responses.patch(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.update_ticket("7671679744")
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
            test_service.update_ticket("3929786810")
        responses.reset()

    @responses.activate
    def test_get_ticket(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/ticket/9558332861",
            json={},
            status=200,
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.get_ticket("9558332861", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_ticket_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/ticket/3294273248",
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
            "https://api-demo.panora.dev/ticketing/ticket/1956858552",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = TicketingTicket("testkey")
            test_service.get_ticket("1956858552", True)
        responses.reset()

    @responses.activate
    def test_add_tickets(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/ticket/batch", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.add_tickets({}, "3228489707", "9348005536", True)
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
            test_service.add_tickets({}, "3012540300", "6613077218", True)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
