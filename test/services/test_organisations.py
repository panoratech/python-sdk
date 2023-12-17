import unittest
import responses
from src.panorasdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.panorasdk.services.organisations import Organisations


class TestOrganisations_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_organisations(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/organisations", json={}, status=200)
        # call the method to test
        test_service = Organisations("testkey")
        response = test_service.get_organisations()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_organisations_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/organisations", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Organisations("testkey")
            test_service.get_organisations()
        responses.reset()

    @responses.activate
    def test_create_organisation(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/organisations/create", json={}, status=200
        )
        # call the method to test
        test_service = Organisations("testkey")
        response = test_service.create_organisation({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_organisation_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/organisations/create", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Organisations("testkey")
            test_service.create_organisation({})
        responses.reset()


if __name__ == "__main__":
    unittest.main()
