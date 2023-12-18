import unittest
from src.panorasdk.models.CreateMagicLinkDto import CreateMagicLinkDto


class TestCreateMagicLinkDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_magic_link_dto(self):
        # Create CreateMagicLinkDto class instance
        test_model = CreateMagicLinkDto(
            id_project="harum", alias="ea", email="dicta", linked_user_origin_id="quo"
        )
        self.assertEqual(test_model.id_project, "harum")
        self.assertEqual(test_model.alias, "ea")
        self.assertEqual(test_model.email, "dicta")
        self.assertEqual(test_model.linked_user_origin_id, "quo")

    def test_create_magic_link_dto_required_fields_missing(self):
        # Assert CreateMagicLinkDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateMagicLinkDto()


if __name__ == "__main__":
    unittest.main()
