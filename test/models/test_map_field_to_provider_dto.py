import unittest
from src.panorasdk.models.MapFieldToProviderDto import MapFieldToProviderDto


class TestMapFieldToProviderDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_map_field_to_provider_dto(self):
        # Create MapFieldToProviderDto class instance
        test_model = MapFieldToProviderDto(
            linked_user_id="dicta",
            source_provider="8289467411",
            source_custom_field_id="pariatur",
            attributeId="commodi",
        )
        self.assertEqual(test_model.linked_user_id, "dicta")
        self.assertEqual(test_model.source_provider, "8289467411")
        self.assertEqual(test_model.source_custom_field_id, "pariatur")
        self.assertEqual(test_model.attributeId, "commodi")

    def test_map_field_to_provider_dto_required_fields_missing(self):
        # Assert MapFieldToProviderDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = MapFieldToProviderDto()


if __name__ == "__main__":
    unittest.main()
