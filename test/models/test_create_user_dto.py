import unittest
from src.panorasdk.models.CreateUserDto import CreateUserDto


class TestCreateUserDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_user_dto(self):
        # Create CreateUserDto class instance
        test_model = CreateUserDto(
            password_hash="commodi",
            email="laboriosam",
            last_name="natus",
            first_name="dignissimos",
            id_organisation="cumque",
        )
        self.assertEqual(test_model.password_hash, "commodi")
        self.assertEqual(test_model.email, "laboriosam")
        self.assertEqual(test_model.last_name, "natus")
        self.assertEqual(test_model.first_name, "dignissimos")
        self.assertEqual(test_model.id_organisation, "cumque")

    def test_create_user_dto_required_fields_missing(self):
        # Assert CreateUserDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateUserDto()


if __name__ == "__main__":
    unittest.main()
