from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ErrorDetail

from db.models.course import Course
from db.models.course_category import CourseCategory
from db.models.course_type import CourseType
from db.models.instructors import Instructor

class UploadCourseViewTest(APITestCase):
    client = APIClient()
    url = reverse('upload-course')
    
    def setUp(self):
        course_type = CourseType.objects.create(name='Premium')
        course_category = CourseCategory.objects.create(name='DevOps')
        self.user = get_user_model().objects.create(fullname='John Doe', email='jdoe@gmail.com',
                                           mobile_number='08093005000', password='testpassword123')

        self.user.set_password('testpassword123')
        self.user.email_verified = True
        self.user.is_active = True
        self.user.save()

        self.payload = {'title': 'Testing Django', 'description': 'Introduction to Testing Django', 'price': 129.00, 'category_id': course_category.id,
               'type_id': course_type.id, 'course_url': 'course_sample.mp4', 'overview': 'course_overview.mp4', 'cover_img': 'cover.png'}

    def test_non_authenticated_learner_cannot_access_view(self):
        self.user.is_learner = True
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.post(self.url, self.payload, user=self.user)
        error_message = ErrorDetail(string='Authentication credentials were not provided.', code='not_authenticated')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], error_message)

    def test_authenticated_learner_cannot_access_view(self):
        self.user.is_learner = True
        token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(self.url, self.payload, user=self.user)
        error_message = ErrorDetail(string='You do not have permission to perform this action.', code='permission_denied')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], error_message)

    def test_non_authenticated_instructor_cannot_upload_course(self):
        self.user.is_instructor = True
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.post(self.url, self.payload, user=self.user)
        error_message = ErrorDetail(string='Authentication credentials were not provided.', code='not_authenticated')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], error_message)

    def test_authenticated_instructor_cannot_create_course_with_incomplete_payload(self):
        self.user.is_instructor = True
        instructor = Instructor.objects.create(user_id=self.user)
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, self.payload, user=instructor)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)