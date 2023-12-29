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
        response = test_service.get_contacts("8579930240", "1757268480", True)
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
            test_service.get_contacts("9147845128", "2805175959", True)
        responses.reset()

    @responses.activate
    def test_add_contact(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/crm/contact", json={}, status=200)
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.add_contact({}, "1182064380", "9335710309", True)
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
            test_service.add_contact({}, "2100482652", "6535198699", True)
        responses.reset()

    @responses.activate
    def test_update_contact(self):
        # Mock the API response
        responses.patch("https://api-demo.panora.dev/crm/contact", json={}, status=200)
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.update_contact("9225438594")
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
            test_service.update_contact("3219076321")
        responses.reset()

    @responses.activate
    def test_get_contact(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/9369452534", json={}, status=200
        )
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.get_contact("9369452534", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_contact_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/8476890414", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = CrmContact("testkey")
            test_service.get_contact()
        responses.reset(),

    @responses.activate
    def test_get_contact_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/1585229315", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = CrmContact("testkey")
            test_service.get_contact("1585229315", True)
        responses.reset()

    @responses.activate
    def test_add_contacts(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/crm/contact/batch", json={}, status=200
        )
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.add_contacts({}, "6742666154", "5287530226", True)
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
            test_service.add_contacts({}, "9574251443", "8823275732", True)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
