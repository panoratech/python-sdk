import unittest
from src.panorasdk.models.LoginDto import LoginDto


class TestLoginDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_login_dto(self):
        # Create LoginDto class instance
        test_model = LoginDto(password_hash="iure", id_user="reiciendis", email="optio")
        self.assertEqual(test_model.password_hash, "iure")
        self.assertEqual(test_model.id_user, "reiciendis")
        self.assertEqual(test_model.email, "optio")

    def test_login_dto_required_fields_missing(self):
        # Assert LoginDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = LoginDto()


if __name__ == "__main__":
    unittest.main()
