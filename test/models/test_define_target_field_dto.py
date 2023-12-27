import unittest
from src.panorasdk.models.DefineTargetFieldDto import DefineTargetFieldDto


class TestDefineTargetFieldDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_define_target_field_dto(self):
        # Create DefineTargetFieldDto class instance
        test_model = DefineTargetFieldDto(
            data_type="inventore",
            description="delectus",
            name="consectetur",
            object_type_owner="eum",
        )
        self.assertEqual(test_model.data_type, "inventore")
        self.assertEqual(test_model.description, "delectus")
        self.assertEqual(test_model.name, "consectetur")
        self.assertEqual(test_model.object_type_owner, "eum")

    def test_define_target_field_dto_required_fields_missing(self):
        # Assert DefineTargetFieldDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = DefineTargetFieldDto()


if __name__ == "__main__":
    unittest.main()
