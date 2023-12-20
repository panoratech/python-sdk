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
        response = test_service.get_contacts("2253849784", "5071343980", True)
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
            test_service.get_contacts("1371905993", "3229956870", True)
        responses.reset()

    @responses.activate
    def test_add_contact(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/crm/contact", json={}, status=200)
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.add_contact({}, "2742664761", "1494486446", True)
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
            test_service.add_contact({}, "5356214078", "3829124384", True)
        responses.reset()

    @responses.activate
    def test_update_contact(self):
        # Mock the API response
        responses.patch("https://api-demo.panora.dev/crm/contact", json={}, status=200)
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.update_contact("3934834278")
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
            test_service.update_contact("2647849315")
        responses.reset()

    @responses.activate
    def test_get_contact(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/6439569818", json={}, status=200
        )
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.get_contact("6439569818", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_contact_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/9122091495", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = CrmContact("testkey")
            test_service.get_contact()
        responses.reset(),

    @responses.activate
    def test_get_contact_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/6673994179", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = CrmContact("testkey")
            test_service.get_contact("6673994179", True)
        responses.reset()

    @responses.activate
    def test_add_contacts(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/crm/contact/batch", json={}, status=200
        )
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.add_contacts({}, "3262289248", "5911510653", True)
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
            test_service.add_contacts({}, "9103909918", "1315981471", True)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
