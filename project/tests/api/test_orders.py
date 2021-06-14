from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from db.models.orders import Order
from db.models.order_status import OrderStatus
from db.models.learner import LearnerProfile
from db.models.user import User
from db.models.course import Course
from db.models.course_type import CourseType
from db.models.course_category import CourseCategory
from db.models.instructors import Instructor


class TestOrderViewList(APITestCase):
    client = APIClient()

    def setUp(self):
        self.test_user = User.objects.create_user(email='testuser@gmail.com', password='testuser123.', fullname='testuser10')
        self.test_user1 = User.objects.create_user(email='testuser1@gmail.com', password='testuser1234.', fullname='testuser110')
        self.coursetype = CourseType.objects.create(name='premium')
        self.coursecategory = CourseCategory.objects.create(name='uiux')
        self.orderstatus1= OrderStatus.objects.create(name="success")
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
        self.order1 = Order.objects.create(course_id=self.testcourse1,learner_id=self.learner,order_status_id=self.orderstatus1)

    def test_get_orders_without_auth(self):
        "this tests unauthorized users"
        url = reverse('order')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_orders_with_auth(self):
        "this tests authorized users"
        url = reverse('order')
        self.client.force_authenticate(user= self.test_user)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['message'], 'success')
        self.assertEqual(res.data['data']['courses'][0]['title'], 'physics')
        
