import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"sequi": 1},
            phone_numbers=["pariatur", "accusantium"],
            email_addresses=["autem", "magni"],
            last_name="tempore",
            first_name="ipsa",
        )
        self.assertEqual(test_model.field_mappings, {"sequi": 1})
        self.assertEqual(test_model.phone_numbers, ["pariatur", "accusantium"])
        self.assertEqual(test_model.email_addresses, ["autem", "magni"])
        self.assertEqual(test_model.last_name, "tempore")
        self.assertEqual(test_model.first_name, "ipsa")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
