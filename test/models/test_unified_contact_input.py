import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"ducimus": 2},
            phone_numbers=["totam", "soluta"],
            email_addresses=["qui", "excepturi"],
            last_name="dolore",
            first_name="sunt",
        )
        self.assertEqual(test_model.field_mappings, {"ducimus": 2})
        self.assertEqual(test_model.phone_numbers, ["totam", "soluta"])
        self.assertEqual(test_model.email_addresses, ["qui", "excepturi"])
        self.assertEqual(test_model.last_name, "dolore")
        self.assertEqual(test_model.first_name, "sunt")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
