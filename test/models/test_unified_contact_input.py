import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"incidunt": 4},
            phone_numbers=["consectetur", "itaque"],
            email_addresses=["ex", "voluptates"],
            last_name="temporibus",
            first_name="aperiam",
        )
        self.assertEqual(test_model.field_mappings, {"incidunt": 4})
        self.assertEqual(test_model.phone_numbers, ["consectetur", "itaque"])
        self.assertEqual(test_model.email_addresses, ["ex", "voluptates"])
        self.assertEqual(test_model.last_name, "temporibus")
        self.assertEqual(test_model.first_name, "aperiam")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
