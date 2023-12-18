import unittest
from src.panorasdk.models.DefineTargetFieldDto import DefineTargetFieldDto


class TestDefineTargetFieldDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_define_target_field_dto(self):
        # Create DefineTargetFieldDto class instance
        test_model = DefineTargetFieldDto(
            data_type="culpa",
            description="dolore",
            name="amet",
            object_type_owner="occaecati",
        )
        self.assertEqual(test_model.data_type, "culpa")
        self.assertEqual(test_model.description, "dolore")
        self.assertEqual(test_model.name, "amet")
        self.assertEqual(test_model.object_type_owner, "occaecati")

    def test_define_target_field_dto_required_fields_missing(self):
        # Assert DefineTargetFieldDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = DefineTargetFieldDto()


if __name__ == "__main__":
    unittest.main()
