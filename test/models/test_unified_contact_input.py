import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"iusto": 1},
            phone_numbers=["tempora", "similique"],
            email_addresses=["dignissimos", "molestias"],
            last_name="molestias",
            first_name="sequi",
        )
        self.assertEqual(test_model.field_mappings, {"iusto": 1})
        self.assertEqual(test_model.phone_numbers, ["tempora", "similique"])
        self.assertEqual(test_model.email_addresses, ["dignissimos", "molestias"])
        self.assertEqual(test_model.last_name, "molestias")
        self.assertEqual(test_model.first_name, "sequi")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
