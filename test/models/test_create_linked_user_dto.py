import unittest
from src.panorasdk.models.CreateLinkedUserDto import CreateLinkedUserDto


class TestCreateLinkedUserDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_linked_user_dto(self):
        # Create CreateLinkedUserDto class instance
        test_model = CreateLinkedUserDto(
            id_project="illo", alias="repellendus", linked_user_origin_id="temporibus"
        )
        self.assertEqual(test_model.id_project, "illo")
        self.assertEqual(test_model.alias, "repellendus")
        self.assertEqual(test_model.linked_user_origin_id, "temporibus")

    def test_create_linked_user_dto_required_fields_missing(self):
        # Assert CreateLinkedUserDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateLinkedUserDto()


if __name__ == "__main__":
    unittest.main()
