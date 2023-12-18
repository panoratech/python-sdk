import unittest
import responses
from src.panorasdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.panorasdk.services.crm_contact import CrmContact


class TestCrmContact_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_contacts(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/crm/contact", json={}, status=200)
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.get_contacts("5679626054", "6958112869", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_contacts_required_fields_missing(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/crm/contact", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = CrmContact("testkey")
            test_service.get_contacts()
        responses.reset(),

    @responses.activate
    def test_get_contacts_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/crm/contact", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = CrmContact("testkey")
            test_service.get_contacts("5754715464", "6556507517", True)
        responses.reset()

    @responses.activate
    def test_add_contact(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/crm/contact", json={}, status=200)
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.add_contact({}, "8139024743", "1565135832", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_contact_required_fields_missing(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/crm/contact", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = CrmContact("testkey")
            test_service.add_contact()
        responses.reset(),

    @responses.activate
    def test_add_contact_error_on_non_200(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/crm/contact", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = CrmContact("testkey")
            test_service.add_contact({}, "9004244884", "3287277192", True)
        responses.reset()

    @responses.activate
    def test_update_contact(self):
        # Mock the API response
        responses.patch("https://api-demo.panora.dev/crm/contact", json={}, status=200)
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.update_contact("6113846530")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_contact_required_fields_missing(self):
        # Mock the API response
        responses.patch("https://api-demo.panora.dev/crm/contact", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = CrmContact("testkey")
            test_service.update_contact()
        responses.reset(),

    @responses.activate
    def test_update_contact_error_on_non_200(self):
        # Mock the API response
        responses.patch("https://api-demo.panora.dev/crm/contact", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = CrmContact("testkey")
            test_service.update_contact("7998119638")
        responses.reset()

    @responses.activate
    def test_get_contact(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/1078820591", json={}, status=200
        )
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.get_contact("1078820591", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_contact_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/1344252530", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = CrmContact("testkey")
            test_service.get_contact()
        responses.reset(),

    @responses.activate
    def test_get_contact_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/5720974989", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = CrmContact("testkey")
            test_service.get_contact("5720974989", True)
        responses.reset()

    @responses.activate
    def test_add_contacts(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/crm/contact/batch", json={}, status=200
        )
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.add_contacts({}, "5178872203", "2940403198", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_contacts_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/crm/contact/batch", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = CrmContact("testkey")
            test_service.add_contacts()
        responses.reset(),

    @responses.activate
    def test_add_contacts_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/crm/contact/batch", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = CrmContact("testkey")
            test_service.add_contacts({}, "3466253071", "3849756547", True)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
