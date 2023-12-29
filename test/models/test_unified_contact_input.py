import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"accusantium": 4},
            phone_numbers=["iusto", "odit"],
            email_addresses=["mollitia", "repellendus"],
            last_name="saepe",
            first_name="officia",
        )
        self.assertEqual(test_model.field_mappings, {"accusantium": 4})
        self.assertEqual(test_model.phone_numbers, ["iusto", "odit"])
        self.assertEqual(test_model.email_addresses, ["mollitia", "repellendus"])
        self.assertEqual(test_model.last_name, "saepe")
        self.assertEqual(test_model.first_name, "officia")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
