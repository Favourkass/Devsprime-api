import _uuid
from django.test import TestCase, client
from django.contrib.auth import get_user_model
from db.models.instructor_course import Course, CourseType, CourseCategory
from db.models.instructors import Instructor
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class TestInstructorCourse(APITestCase):
    client = APIClient()

    def setUp(self):
        '''create instances of instructor, course, category, type'''
        get_user_model().objects.create(
            email = "samson@gmail.com" , password = '123456ddsbbbak!'
        )
        self.user =  get_user_model().objects.get(email='samson@gmail.com')
        self.instructor = Instructor.objects.create(user_id=self.user, avatar='thsijsfslfhs')
        self.type = CourseType.objects.create(name='free')
        self.category = CourseCategory.objects.create(name='design')
        self.testing = Course.objects.create(
            title='testing',description='you are awesome',avatar='dfhsdflsj',
            course_url='dkfjslsfl',overview='sdfhslh',price=20,
            instructor_id= self.instructor, category_id=self.category, type_id=self.type
                        )
        self.url = f'/api/v1/instructors/courses/{str(self.instructor.id)}/'


    def test_get_instructor_courses_with_auth(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_instructor_courses_without_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

 

   
