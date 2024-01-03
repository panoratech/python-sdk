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
        response = test_service.get_tickets("2168756695", "8980805743", True)
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
            test_service.get_tickets("9744939126", "4549326996", True)
        responses.reset()

    @responses.activate
    def test_add_ticket(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.add_ticket({}, "6196644696", "3656675486", True)
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
            test_service.add_ticket({}, "9592085511", "1332793848", True)
        responses.reset()

    @responses.activate
    def test_update_ticket(self):
        # Mock the API response
        responses.patch(
            "https://api-demo.panora.dev/ticketing/ticket", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.update_ticket("5390795256")
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
            test_service.update_ticket("7110262290")
        responses.reset()

    @responses.activate
    def test_get_ticket(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/ticket/9077887713",
            json={},
            status=200,
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.get_ticket("9077887713", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_ticket_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/ticketing/ticket/3712375370",
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
            "https://api-demo.panora.dev/ticketing/ticket/6373366929",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = TicketingTicket("testkey")
            test_service.get_ticket("6373366929", True)
        responses.reset()

    @responses.activate
    def test_add_tickets(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/ticketing/ticket/batch", json={}, status=200
        )
        # call the method to test
        test_service = TicketingTicket("testkey")
        response = test_service.add_tickets({}, "1083210503", "6195460486", True)
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
            test_service.add_tickets({}, "8204044029", "1561597251", True)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
