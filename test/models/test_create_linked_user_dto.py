import unittest
from src.panorasdk.models.CreateLinkedUserDto import CreateLinkedUserDto


class TestCreateLinkedUserDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_linked_user_dto(self):
        # Create CreateLinkedUserDto class instance
        test_model = CreateLinkedUserDto(
            id_project="aspernatur", alias="doloribus", linked_user_origin_id="incidunt"
        )
        self.assertEqual(test_model.id_project, "aspernatur")
        self.assertEqual(test_model.alias, "doloribus")
        self.assertEqual(test_model.linked_user_origin_id, "incidunt")

    def test_create_linked_user_dto_required_fields_missing(self):
        # Assert CreateLinkedUserDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateLinkedUserDto()


if __name__ == "__main__":
    unittest.main()
