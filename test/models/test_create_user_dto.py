import unittest
from src.panorasdk.models.CreateUserDto import CreateUserDto


class TestCreateUserDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_user_dto(self):
        # Create CreateUserDto class instance
        test_model = CreateUserDto(
            password_hash="adipisci",
            email="nesciunt",
            last_name="iure",
            first_name="non",
            id_organisation="molestiae",
        )
        self.assertEqual(test_model.password_hash, "adipisci")
        self.assertEqual(test_model.email, "nesciunt")
        self.assertEqual(test_model.last_name, "iure")
        self.assertEqual(test_model.first_name, "non")
        self.assertEqual(test_model.id_organisation, "molestiae")

    def test_create_user_dto_required_fields_missing(self):
        # Assert CreateUserDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateUserDto()


if __name__ == "__main__":
    unittest.main()
