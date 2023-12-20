import unittest
from src.panorasdk.models.DefineTargetFieldDto import DefineTargetFieldDto


class TestDefineTargetFieldDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_define_target_field_dto(self):
        # Create DefineTargetFieldDto class instance
        test_model = DefineTargetFieldDto(
            data_type="aperiam",
            description="harum",
            name="explicabo",
            object_type_owner="debitis",
        )
        self.assertEqual(test_model.data_type, "aperiam")
        self.assertEqual(test_model.description, "harum")
        self.assertEqual(test_model.name, "explicabo")
        self.assertEqual(test_model.object_type_owner, "debitis")

    def test_define_target_field_dto_required_fields_missing(self):
        # Assert DefineTargetFieldDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = DefineTargetFieldDto()


if __name__ == "__main__":
    unittest.main()
