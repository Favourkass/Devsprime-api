from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from db.models.course_type import CourseType


class CourseTypeViewTest(APITestCase):
    client = APIClient()
    url = reverse('course-types')
    course_type_data = {
        "name": "Premium",
    }

    def test_create_course_type(self):
        """
        Ensure we can create a new course type.
        """
        response = self.client.post(
            self.url,
            self.course_type_data,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_course_types(self):
        """
        Ensure we can get all course types.
        """
        response = self.client.get(
            self.url,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
