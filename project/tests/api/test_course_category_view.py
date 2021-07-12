from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from db.models.course_category import CourseCategory


class CourseCategoryViewTest(APITestCase):
    client = APIClient()
    url = reverse('course-categories')
    course_category_data = {
        "name": "Design",
    }

    def test_create_course_category(self):
        """
        Ensure we can create a new course category.
        """
        response = self.client.post(
            self.url,
            self.course_category_data,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_course_categories(self):
        """
        Ensure we can get all course categories.
        """
        response = self.client.get(
            self.url,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
