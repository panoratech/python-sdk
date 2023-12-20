import unittest
from src.panorasdk.models.DefineTargetFieldDto import DefineTargetFieldDto


class TestDefineTargetFieldDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_define_target_field_dto(self):
        # Create DefineTargetFieldDto class instance
        test_model = DefineTargetFieldDto(
            data_type="quod",
            description="cumque",
            name="tempore",
            object_type_owner="vitae",
        )
        self.assertEqual(test_model.data_type, "quod")
        self.assertEqual(test_model.description, "cumque")
        self.assertEqual(test_model.name, "tempore")
        self.assertEqual(test_model.object_type_owner, "vitae")

    def test_define_target_field_dto_required_fields_missing(self):
        # Assert DefineTargetFieldDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = DefineTargetFieldDto()


if __name__ == "__main__":
    unittest.main()
