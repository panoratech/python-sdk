import unittest
from src.panorasdk.models.CreateMagicLinkDto import CreateMagicLinkDto


class TestCreateMagicLinkDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_magic_link_dto(self):
        # Create CreateMagicLinkDto class instance
        test_model = CreateMagicLinkDto(
            id_project="accusantium",
            alias="temporibus",
            email="nihil",
            linked_user_origin_id="est",
        )
        self.assertEqual(test_model.id_project, "accusantium")
        self.assertEqual(test_model.alias, "temporibus")
        self.assertEqual(test_model.email, "nihil")
        self.assertEqual(test_model.linked_user_origin_id, "est")

    def test_create_magic_link_dto_required_fields_missing(self):
        # Assert CreateMagicLinkDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateMagicLinkDto()


if __name__ == "__main__":
    unittest.main()
