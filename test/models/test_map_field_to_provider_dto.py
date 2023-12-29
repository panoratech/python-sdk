import unittest
from src.panorasdk.models.MapFieldToProviderDto import MapFieldToProviderDto


class TestMapFieldToProviderDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_map_field_to_provider_dto(self):
        # Create MapFieldToProviderDto class instance
        test_model = MapFieldToProviderDto(
            linked_user_id="odio",
            source_provider="1775766837",
            source_custom_field_id="nulla",
            attributeId="nemo",
        )
        self.assertEqual(test_model.linked_user_id, "odio")
        self.assertEqual(test_model.source_provider, "1775766837")
        self.assertEqual(test_model.source_custom_field_id, "nulla")
        self.assertEqual(test_model.attributeId, "nemo")

    def test_map_field_to_provider_dto_required_fields_missing(self):
        # Assert MapFieldToProviderDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = MapFieldToProviderDto()


if __name__ == "__main__":
    unittest.main()
