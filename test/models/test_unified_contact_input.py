import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"fuga": 8},
            phone_numbers=["exercitationem", "ratione"],
            email_addresses=["nobis", "cupiditate"],
            last_name="facilis",
            first_name="tempora",
        )
        self.assertEqual(test_model.field_mappings, {"fuga": 8})
        self.assertEqual(test_model.phone_numbers, ["exercitationem", "ratione"])
        self.assertEqual(test_model.email_addresses, ["nobis", "cupiditate"])
        self.assertEqual(test_model.last_name, "facilis")
        self.assertEqual(test_model.first_name, "tempora")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
