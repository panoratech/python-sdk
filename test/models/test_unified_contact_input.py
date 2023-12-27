import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"iste": 8},
            phone_numbers=["blanditiis", "dolorem"],
            email_addresses=["excepturi", "enim"],
            last_name="ex",
            first_name="autem",
        )
        self.assertEqual(test_model.field_mappings, {"iste": 8})
        self.assertEqual(test_model.phone_numbers, ["blanditiis", "dolorem"])
        self.assertEqual(test_model.email_addresses, ["excepturi", "enim"])
        self.assertEqual(test_model.last_name, "ex")
        self.assertEqual(test_model.first_name, "autem")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
