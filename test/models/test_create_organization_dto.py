import unittest
from src.panorasdk.models.CreateOrganizationDto import CreateOrganizationDto


class TestCreateOrganizationDtoModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_organization_dto(self):
        # Create CreateOrganizationDto class instance
        test_model = CreateOrganizationDto(stripe_customer_id="fugit", name="aliquam")
        self.assertEqual(test_model.stripe_customer_id, "fugit")
        self.assertEqual(test_model.name, "aliquam")

    def test_create_organization_dto_required_fields_missing(self):
        # Assert CreateOrganizationDto class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateOrganizationDto()


if __name__ == "__main__":
    unittest.main()
