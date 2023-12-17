import unittest
from src.panorasdk.models.UnifiedContactInput import UnifiedContactInput


class TestUnifiedContactInputModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unified_contact_input(self):
        # Create UnifiedContactInput class instance
        test_model = UnifiedContactInput(
            field_mappings={"pariatur": 5},
            phone_numbers=["tempora", "magni"],
            email_addresses=["itaque", "optio"],
            last_name="exercitationem",
            first_name="expedita",
        )
        self.assertEqual(test_model.field_mappings, {"pariatur": 5})
        self.assertEqual(test_model.phone_numbers, ["tempora", "magni"])
        self.assertEqual(test_model.email_addresses, ["itaque", "optio"])
        self.assertEqual(test_model.last_name, "exercitationem")
        self.assertEqual(test_model.first_name, "expedita")

    def test_unified_contact_input_required_fields_missing(self):
        # Assert UnifiedContactInput class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnifiedContactInput()


if __name__ == "__main__":
    unittest.main()
