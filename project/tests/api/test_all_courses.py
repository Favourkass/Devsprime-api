from rest_framework.test import APITestCase, APIClient
from rest_framework import status



class TestAllCourses(APITestCase):
    client = APIClient()

    def test_get_all_courses(self):
        response = self.client.get('/api/v1/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
