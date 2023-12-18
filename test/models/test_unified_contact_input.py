import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"reiciendis": 1},
            phone_numbers=["quidem", "ducimus"],
            email_addresses=["officia", "necessitatibus"],
            last_name="quaerat",
            first_name="quibusdam",
        )
        self.assertEqual(test_model.field_mappings, {"reiciendis": 1})
        self.assertEqual(test_model.phone_numbers, ["quidem", "ducimus"])
        self.assertEqual(test_model.email_addresses, ["officia", "necessitatibus"])
        self.assertEqual(test_model.last_name, "quaerat")
        self.assertEqual(test_model.first_name, "quibusdam")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
