import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"velit": 1},
            phone_numbers=["reprehenderit", "doloribus"],
            email_addresses=["laboriosam", "inventore"],
            last_name="eos",
            first_name="quo",
        )
        self.assertEqual(test_model.field_mappings, {"velit": 1})
        self.assertEqual(test_model.phone_numbers, ["reprehenderit", "doloribus"])
        self.assertEqual(test_model.email_addresses, ["laboriosam", "inventore"])
        self.assertEqual(test_model.last_name, "eos")
        self.assertEqual(test_model.first_name, "quo")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
