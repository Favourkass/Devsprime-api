from django.contrib.auth import get_user_model
from db.models.course import Course
from db.models.course_type import CourseType
from db.models.course_category import CourseCategory
from db.models.course_type import  CourseType
from db.models.course_category import  CourseCategory
from db.models.instructors import Instructor
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse


class TestInstructorCourseById(APITestCase):
    client = APIClient()

    def setUp(self):
        '''create instances of instructor, course, category, type'''
        get_user_model().objects.create(
            email = "nnabue@gmail.com" , password = '123456ddsbbbak!'
        )
        self.user =  get_user_model().objects.get(email='nnabue@gmail.com')
        self.instructor = Instructor.objects.create(user_id=self.user, avatar='thsijsfslfhs')
        self.type = CourseType.objects.create(name='free')
        self.category = CourseCategory.objects.create(name='design')
        self.course = Course.objects.create(
            title='testing',description='you are awesome',
            course_url=[{"para": "A meta-markup language, used to create markup languages such as DocBook."}],overview='http://youtube.com',price=20,
            instructor_id= self.instructor, category_id=self.category, type_id=self.type
                        )
        self.url = reverse('course-details', kwargs={'pk':self.course.pk})

        self.update_valid_payload = {
            Course.description: 'hello world',
            Course.overview: 'http://scrimba.com'
        }


    def test_get_course_with_auth(self):
        self.client.force_authenticate(user=self.instructor)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def update_course(self):
        self.force_authenticate(user=self.instructor)
        response = self.client.put( 
            self.url, 
            self.update_valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_206_PARTIAL_CONTENT)
