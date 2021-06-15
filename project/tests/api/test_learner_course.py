from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from db.models.learner_course import LearnerCourse
from db.models.learner import LearnerProfile
from db.models.user import User
from db.models.course import Course
from db.models.course_category import CourseCategory
from db.models.course_type import CourseType
from db.models.instructors import Instructor


class TestLearnerCourseList(APITestCase):
    client = APIClient()

    def setUp(self):
        self.test_user = User.objects.create_user(email='testuser@gmail.com', password='testuser123.', fullname='testuser10')
        self.test_user1 = User.objects.create_user(email='testuser1@gmail.com', password='testuser1234.', fullname='testuser110')
        self.coursetype = CourseType.objects.create(name='premium')
        self.coursecategory = CourseCategory.objects.create(name='uiux')
        self.instructor1 = Instructor.objects.create(user_id=self.test_user1)
        self.testcourse1 = Course.objects.create(
                         title='physics', 
                         description='science',
                         price=100,
                         overview='physicscourse',
                         course_url='urlcourse',
                         cover_img='thumbnail',
                         category_id=self.coursecategory,
                         type_id=self.coursetype,
                         instructor_id=self.instructor1
                         )
        self.testcourse2 = Course.objects.create(
                         title='mathematics', 
                         description='science',
                         price=120,
                         overview='physicscourse',
                         course_url='urlcourse',
                         cover_img='thumbnail',
                         category_id=self.coursecategory,
                         type_id=self.coursetype,
                         instructor_id=self.instructor1
                         )
        self.learner = LearnerProfile.objects.create(user_id = self.test_user)
        self.learnercourse1 = LearnerCourse.objects.create(learner_id=self.learner, course_id=self.testcourse1)
        self.learnercourse2 = LearnerCourse.objects.create(learner_id=self.learner, course_id=self.testcourse2)

    def test_get_learnercourse_without_auth(self):
        "this tests unauthorized users"
        url = reverse('learner-course')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_learnercourse_with_auth(self):
        "this tests authorized users"
        url = reverse('learner-course')
        self.client.force_authenticate(user= self.test_user)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['message'], 'success')
        