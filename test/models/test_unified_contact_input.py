import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"expedita": 6},
            phone_numbers=["aliquam", "iste"],
            email_addresses=["autem", "laudantium"],
            last_name="nobis",
            first_name="pariatur",
        )
        self.assertEqual(test_model.field_mappings, {"expedita": 6})
        self.assertEqual(test_model.phone_numbers, ["aliquam", "iste"])
        self.assertEqual(test_model.email_addresses, ["autem", "laudantium"])
        self.assertEqual(test_model.last_name, "nobis")
        self.assertEqual(test_model.first_name, "pariatur")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
