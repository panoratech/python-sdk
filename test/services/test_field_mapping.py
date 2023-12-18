import unittest
import responses
from src.panorasdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.panorasdk.services.field_mapping import FieldMapping


class TestFieldMapping_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_field_mappings_entities(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/field-mapping/entities", json={}, status=200
        )
        # call the method to test
        test_service = FieldMapping("testkey")
        response = test_service.get_field_mappings_entities()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_field_mappings_entities_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/field-mapping/entities", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = FieldMapping("testkey")
            test_service.get_field_mappings_entities()
        responses.reset()

    @responses.activate
    def test_get_field_mappings(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/field-mapping/attribute", json={}, status=200
        )
        # call the method to test
        test_service = FieldMapping("testkey")
        response = test_service.get_field_mappings()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_field_mappings_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/field-mapping/attribute", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = FieldMapping("testkey")
            test_service.get_field_mappings()
        responses.reset()

    @responses.activate
    def test_get_field_mapping_values(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/field-mapping/value", json={}, status=200
        )
        # call the method to test
        test_service = FieldMapping("testkey")
        response = test_service.get_field_mapping_values()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_field_mapping_values_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/field-mapping/value", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = FieldMapping("testkey")
            test_service.get_field_mapping_values()
        responses.reset()

    @responses.activate
    def test_define_target_field(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/field-mapping/define", json={}, status=200
        )
        # call the method to test
        test_service = FieldMapping("testkey")
        response = test_service.define_target_field({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_define_target_field_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/field-mapping/define", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = FieldMapping("testkey")
            test_service.define_target_field({})
        responses.reset()

    @responses.activate
    def test_map_field(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/field-mapping/map", json={}, status=200
        )
        # call the method to test
        test_service = FieldMapping("testkey")
        response = test_service.map_field({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_map_field_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/field-mapping/map", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = FieldMapping("testkey")
            test_service.map_field({})
        responses.reset()

    @responses.activate
    def test_get_custom_provider_properties(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/field-mapping/properties", json={}, status=200
        )
        # call the method to test
        test_service = FieldMapping("testkey")
        response = test_service.get_custom_provider_properties(
            "5299239222", "7943454957"
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_custom_provider_properties_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/field-mapping/properties", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = FieldMapping("testkey")
            test_service.get_custom_provider_properties()
        responses.reset(),

    @responses.activate
    def test_get_custom_provider_properties_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api-demo.panora.dev/field-mapping/properties", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = FieldMapping("testkey")
            test_service.get_custom_provider_properties("7123397545", "4042063649")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
