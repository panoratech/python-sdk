import unittest
import responses
from src.panorasdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.panorasdk.services.projects import Projects


class TestProjects_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_projects(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/projects", json={}, status=200)
        # call the method to test
        test_service = Projects("testkey")
        response = test_service.get_projects()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_projects_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api-demo.panora.dev/projects", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Projects("testkey")
            test_service.get_projects()
        responses.reset()

    @responses.activate
    def test_create_project(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/projects/create", json={}, status=200
        )
        # call the method to test
        test_service = Projects("testkey")
        response = test_service.create_project({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_project_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api-demo.panora.dev/projects/create", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Projects("testkey")
            test_service.create_project({})
        responses.reset()


if __name__ == "__main__":
    unittest.main()
