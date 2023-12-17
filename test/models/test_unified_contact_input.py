import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"molestias": 4},
            phone_numbers=["fugit", "dolores"],
            email_addresses=["facere", "consequuntur"],
            last_name="debitis",
            first_name="accusamus",
        )
        self.assertEqual(test_model.field_mappings, {"molestias": 4})
        self.assertEqual(test_model.phone_numbers, ["fugit", "dolores"])
        self.assertEqual(test_model.email_addresses, ["facere", "consequuntur"])
        self.assertEqual(test_model.last_name, "debitis")
        self.assertEqual(test_model.first_name, "accusamus")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
