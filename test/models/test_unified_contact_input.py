import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"voluptates": 6},
            phone_numbers=["aspernatur", "odio"],
            email_addresses=["enim", "dolorum"],
            last_name="hic",
            first_name="eos",
        )
        self.assertEqual(test_model.field_mappings, {"voluptates": 6})
        self.assertEqual(test_model.phone_numbers, ["aspernatur", "odio"])
        self.assertEqual(test_model.email_addresses, ["enim", "dolorum"])
        self.assertEqual(test_model.last_name, "hic")
        self.assertEqual(test_model.first_name, "eos")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
