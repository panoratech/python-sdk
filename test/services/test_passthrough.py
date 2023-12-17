import unittest
import responses
from src.panorasdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.panorasdk.services.passthrough import Passthrough


class TestPassthrough_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_passthrough_request(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/passthrough", json={}, status=200)
        # call the method to test
        test_service = Passthrough("testkey")
        response = test_service.passthrough_request({}, "4795202315", "8707347482")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_passthrough_request_required_fields_missing(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/passthrough", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Passthrough("testkey")
            test_service.passthrough_request()
        responses.reset(),

    @responses.activate
    def test_passthrough_request_error_on_non_200(self):
        # Mock the API response
        responses.post("https://api-demo.panora.dev/passthrough", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Passthrough("testkey")
            test_service.passthrough_request({}, "9511016251", "2910341040")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
