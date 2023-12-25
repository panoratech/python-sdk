import unittest
from src.panorasdk.models.MapFieldToProviderDto import MapFieldToProviderDto


class TestMapFieldToProviderDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_map_field_to_provider_dto(self):
        # Create MapFieldToProviderDto class instance
        test_model = MapFieldToProviderDto(
            linked_user_id="officia",
            source_provider="7801438354",
            source_custom_field_id="vel",
            attributeId="omnis",
        )
        self.assertEqual(test_model.linked_user_id, "officia")
        self.assertEqual(test_model.source_provider, "7801438354")
        self.assertEqual(test_model.source_custom_field_id, "vel")
        self.assertEqual(test_model.attributeId, "omnis")

    def test_map_field_to_provider_dto_required_fields_missing(self):
        # Assert MapFieldToProviderDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = MapFieldToProviderDto()


if __name__ == "__main__":
    unittest.main()
