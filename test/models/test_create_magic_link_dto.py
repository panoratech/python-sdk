import unittest
from src.panorasdk.models.CreateMagicLinkDto import CreateMagicLinkDto


class TestCreateMagicLinkDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_magic_link_dto(self):
        # Create CreateMagicLinkDto class instance
        test_model = CreateMagicLinkDto(
            id_project="nobis",
            alias="sed",
            email="hic",
            linked_user_origin_id="molestias",
        )
        self.assertEqual(test_model.id_project, "nobis")
        self.assertEqual(test_model.alias, "sed")
        self.assertEqual(test_model.email, "hic")
        self.assertEqual(test_model.linked_user_origin_id, "molestias")

    def test_create_magic_link_dto_required_fields_missing(self):
        # Assert CreateMagicLinkDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateMagicLinkDto()


if __name__ == "__main__":
    unittest.main()
