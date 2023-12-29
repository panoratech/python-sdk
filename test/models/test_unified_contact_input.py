import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"repellat": 7},
            phone_numbers=["totam", "illum"],
            email_addresses=["facere", "itaque"],
            last_name="voluptatem",
            first_name="voluptatum",
        )
        self.assertEqual(test_model.field_mappings, {"repellat": 7})
        self.assertEqual(test_model.phone_numbers, ["totam", "illum"])
        self.assertEqual(test_model.email_addresses, ["facere", "itaque"])
        self.assertEqual(test_model.last_name, "voluptatem")
        self.assertEqual(test_model.first_name, "voluptatum")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
