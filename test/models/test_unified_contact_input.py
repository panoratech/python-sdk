import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"nostrum": 9},
            phone_numbers=["rerum", "ea"],
            email_addresses=["voluptatibus", "voluptatem"],
            last_name="eum",
            first_name="soluta",
        )
        self.assertEqual(test_model.field_mappings, {"nostrum": 9})
        self.assertEqual(test_model.phone_numbers, ["rerum", "ea"])
        self.assertEqual(test_model.email_addresses, ["voluptatibus", "voluptatem"])
        self.assertEqual(test_model.last_name, "eum")
        self.assertEqual(test_model.first_name, "soluta")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
