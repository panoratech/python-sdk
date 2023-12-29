import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"nam": 2},
            phone_numbers=["suscipit", "itaque"],
            email_addresses=["laborum", "nostrum"],
            last_name="dolorem",
            first_name="illum",
        )
        self.assertEqual(test_model.field_mappings, {"nam": 2})
        self.assertEqual(test_model.phone_numbers, ["suscipit", "itaque"])
        self.assertEqual(test_model.email_addresses, ["laborum", "nostrum"])
        self.assertEqual(test_model.last_name, "dolorem")
        self.assertEqual(test_model.first_name, "illum")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
