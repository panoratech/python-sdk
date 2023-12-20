import unittest
from src.panorasdk.models.LoginDto import LoginDto


class TestLoginDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_login_dto(self):
        # Create LoginDto class instance
        test_model = LoginDto(
            password_hash="totam", id_user="nisi", email="exercitationem"
        )
        self.assertEqual(test_model.password_hash, "totam")
        self.assertEqual(test_model.id_user, "nisi")
        self.assertEqual(test_model.email, "exercitationem")

    def test_login_dto_required_fields_missing(self):
        # Assert LoginDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = LoginDto()


if __name__ == "__main__":
    unittest.main()
