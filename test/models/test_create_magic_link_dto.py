import unittest
from src.panorasdk.models.CreateMagicLinkDto import CreateMagicLinkDto


class TestCreateMagicLinkDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_magic_link_dto(self):
        # Create CreateMagicLinkDto class instance
        test_model = CreateMagicLinkDto(
            id_project="nam", alias="et", email="dicta", linked_user_origin_id="quod"
        )
        self.assertEqual(test_model.id_project, "nam")
        self.assertEqual(test_model.alias, "et")
        self.assertEqual(test_model.email, "dicta")
        self.assertEqual(test_model.linked_user_origin_id, "quod")

    def test_create_magic_link_dto_required_fields_missing(self):
        # Assert CreateMagicLinkDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateMagicLinkDto()


if __name__ == "__main__":
    unittest.main()
