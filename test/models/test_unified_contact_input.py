import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"laboriosam": 2},
            phone_numbers=["minus", "error"],
            email_addresses=["iste", "praesentium"],
            last_name="earum",
            first_name="voluptatem",
        )
        self.assertEqual(test_model.field_mappings, {"laboriosam": 2})
        self.assertEqual(test_model.phone_numbers, ["minus", "error"])
        self.assertEqual(test_model.email_addresses, ["iste", "praesentium"])
        self.assertEqual(test_model.last_name, "earum")
        self.assertEqual(test_model.first_name, "voluptatem")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
