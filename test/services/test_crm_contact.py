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
        response = test_service.get_contacts("2241877202", "1770425295", True)
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
            test_service.get_contacts("5598213724", "7384727901", True)
        responses.reset()

    @responses.activate
    def test_add_contact(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/crm/contact", json={}, status=200)
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.add_contact({}, "7626513163", "6598149033", True)
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
            test_service.add_contact({}, "7618969502", "1944829398", True)
        responses.reset()

    @responses.activate
    def test_update_contact(self):
        # Mock the API response
        responses.patch("https://api-demo.panora.dev/crm/contact", json={}, status=200)
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.update_contact("5790093099")
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
            test_service.update_contact("7833735344")
        responses.reset()

    @responses.activate
    def test_get_contact(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/2216478440", json={}, status=200
        )
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.get_contact("2216478440", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_contact_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/9498468248", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = CrmContact("testkey")
            test_service.get_contact()
        responses.reset(),

    @responses.activate
    def test_get_contact_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/5548356892", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = CrmContact("testkey")
            test_service.get_contact("5548356892", True)
        responses.reset()

    @responses.activate
    def test_add_contacts(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/crm/contact/batch", json={}, status=200
        )
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.add_contacts({}, "4773880403", "8555346736", True)
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
            test_service.add_contacts({}, "4526343382", "2331110812", True)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
