import unittest
from src.panorasdk.models.CreateUserDto import CreateUserDto


class TestCreateUserDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_user_dto(self):
        # Create CreateUserDto class instance
        test_model = CreateUserDto(
            password_hash="occaecati",
            email="dolores",
            last_name="perferendis",
            first_name="molestias",
            id_organisation="provident",
        )
        self.assertEqual(test_model.password_hash, "occaecati")
        self.assertEqual(test_model.email, "dolores")
        self.assertEqual(test_model.last_name, "perferendis")
        self.assertEqual(test_model.first_name, "molestias")
        self.assertEqual(test_model.id_organisation, "provident")

    def test_create_user_dto_required_fields_missing(self):
        # Assert CreateUserDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateUserDto()


if __name__ == "__main__":
    unittest.main()
