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
        response = test_service.get_contacts("2724544517", "6143823911", True)
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
            test_service.get_contacts("8176369457", "5199452467", True)
        responses.reset()

    @responses.activate
    def test_add_contact(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/crm/contact", json={}, status=200)
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.add_contact({}, "4917322662", "4985285854", True)
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
            test_service.add_contact({}, "3521783180", "2275482674", True)
        responses.reset()

    @responses.activate
    def test_update_contact(self):
        # Mock the API response
        responses.patch("https://api-demo.panora.dev/crm/contact", json={}, status=200)
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.update_contact("9577966437")
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
            test_service.update_contact("6694847882")
        responses.reset()

    @responses.activate
    def test_get_contact(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/4938577808", json={}, status=200
        )
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.get_contact("4938577808", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_contact_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/2232381837", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = CrmContact("testkey")
            test_service.get_contact()
        responses.reset(),

    @responses.activate
    def test_get_contact_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/crm/contact/3308667123", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = CrmContact("testkey")
            test_service.get_contact("3308667123", True)
        responses.reset()

    @responses.activate
    def test_add_contacts(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/crm/contact/batch", json={}, status=200
        )
        # call the method to test
        test_service = CrmContact("testkey")
        response = test_service.add_contacts({}, "8397476850", "7359739636", True)
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
            test_service.add_contacts({}, "2257644807", "7785945666", True)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
