import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"amet": 9},
            phone_numbers=["neque", "eveniet"],
            email_addresses=["temporibus", "architecto"],
            last_name="dolorum",
            first_name="natus",
        )
        self.assertEqual(test_model.field_mappings, {"amet": 9})
        self.assertEqual(test_model.phone_numbers, ["neque", "eveniet"])
        self.assertEqual(test_model.email_addresses, ["temporibus", "architecto"])
        self.assertEqual(test_model.last_name, "dolorum")
        self.assertEqual(test_model.first_name, "natus")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
