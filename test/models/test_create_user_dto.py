import unittest
from src.panorasdk.models.CreateUserDto import CreateUserDto


class TestCreateUserDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_user_dto(self):
        # Create CreateUserDto class instance
        test_model = CreateUserDto(
            password_hash="modi",
            email="neque",
            last_name="inventore",
            first_name="nesciunt",
            id_organisation="placeat",
        )
        self.assertEqual(test_model.password_hash, "modi")
        self.assertEqual(test_model.email, "neque")
        self.assertEqual(test_model.last_name, "inventore")
        self.assertEqual(test_model.first_name, "nesciunt")
        self.assertEqual(test_model.id_organisation, "placeat")

    def test_create_user_dto_required_fields_missing(self):
        # Assert CreateUserDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateUserDto()


if __name__ == "__main__":
    unittest.main()
