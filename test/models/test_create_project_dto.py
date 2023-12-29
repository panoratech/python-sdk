import unittest
from src.panorasdk.models.CreateProjectDto import CreateProjectDto


class TestCreateProjectDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_project_dto(self):
        # Create CreateProjectDto class instance
        test_model = CreateProjectDto(id_organization="rem", name="error")
        self.assertEqual(test_model.id_organization, "rem")
        self.assertEqual(test_model.name, "error")

    def test_create_project_dto_required_fields_missing(self):
        # Assert CreateProjectDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateProjectDto()


if __name__ == "__main__":
    unittest.main()
