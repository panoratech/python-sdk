import unittest
from src.panorasdk.models.CreateUserDto import CreateUserDto


class TestCreateUserDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_user_dto(self):
        # Create CreateUserDto class instance
        test_model = CreateUserDto(
            password_hash="temporibus",
            email="ex",
            last_name="possimus",
            first_name="deleniti",
        )
        self.assertEqual(test_model.password_hash, "temporibus")
        self.assertEqual(test_model.email, "ex")
        self.assertEqual(test_model.last_name, "possimus")
        self.assertEqual(test_model.first_name, "deleniti")

    def test_create_user_dto_required_fields_missing(self):
        # Assert CreateUserDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateUserDto()


if __name__ == "__main__":
    unittest.main()
