import unittest
from src.panorasdk.models.CreateUserDto import CreateUserDto


class TestCreateUserDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_user_dto(self):
        # Create CreateUserDto class instance
        test_model = CreateUserDto(
            password_hash="corrupti",
            email="quod",
            last_name="impedit",
            first_name="recusandae",
        )
        self.assertEqual(test_model.password_hash, "corrupti")
        self.assertEqual(test_model.email, "quod")
        self.assertEqual(test_model.last_name, "impedit")
        self.assertEqual(test_model.first_name, "recusandae")

    def test_create_user_dto_required_fields_missing(self):
        # Assert CreateUserDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateUserDto()


if __name__ == "__main__":
    unittest.main()
