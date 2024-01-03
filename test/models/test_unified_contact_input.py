import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"doloribus": 3},
            phone_numbers=["non", "magni"],
            email_addresses=["soluta", "architecto"],
            last_name="adipisci",
            first_name="perferendis",
        )
        self.assertEqual(test_model.field_mappings, {"doloribus": 3})
        self.assertEqual(test_model.phone_numbers, ["non", "magni"])
        self.assertEqual(test_model.email_addresses, ["soluta", "architecto"])
        self.assertEqual(test_model.last_name, "adipisci")
        self.assertEqual(test_model.first_name, "perferendis")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
