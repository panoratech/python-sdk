import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"voluptatum": 8},
            phone_numbers=["id", "officia"],
            email_addresses=["nemo", "suscipit"],
            last_name="nisi",
            first_name="dolores",
        )
        self.assertEqual(test_model.field_mappings, {"voluptatum": 8})
        self.assertEqual(test_model.phone_numbers, ["id", "officia"])
        self.assertEqual(test_model.email_addresses, ["nemo", "suscipit"])
        self.assertEqual(test_model.last_name, "nisi")
        self.assertEqual(test_model.first_name, "dolores")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
