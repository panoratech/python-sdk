import unittest
from src.panorasdk.models.MapFieldToProviderDto import MapFieldToProviderDto


class TestMapFieldToProviderDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_map_field_to_provider_dto(self):
        # Create MapFieldToProviderDto class instance
        test_model = MapFieldToProviderDto(
            linked_user_id="officiis",
            source_provider="1771562291",
            source_custom_field_id="ullam",
            attributeId="veniam",
        )
        self.assertEqual(test_model.linked_user_id, "officiis")
        self.assertEqual(test_model.source_provider, "1771562291")
        self.assertEqual(test_model.source_custom_field_id, "ullam")
        self.assertEqual(test_model.attributeId, "veniam")

    def test_map_field_to_provider_dto_required_fields_missing(self):
        # Assert MapFieldToProviderDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = MapFieldToProviderDto()


if __name__ == "__main__":
    unittest.main()
