from db.models.instructors import Instructor
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from db.models.learner import LearnerProfile
from db.models.course import Course
from db.models.course_payment import Order
from db.models.course_type import CourseType
from db.models.course_category import CourseCategory
from db.models.order_status import OrderStatus


class PaymentCardTest(APITestCase):
    def setUp(self):
        get_user_model().objects.create(
            fullname='testlearner', 
            email='test@admin.com', 
            password='admin1234x'
        )
        self.sample_user = get_user_model().objects.get(fullname='testlearner')
        LearnerProfile.objects.create(
            user_id=self.sample_user,
            account_name='John Doe',
            account_number='0119639776',
            bank_name='Guaranty Trust Bank')
        self.sample_learner = LearnerProfile.objects.get(user_id=self.sample_user) 
        course_type = CourseType.objects.create(name='Cloud Engineering')     
        course_cat = CourseCategory.objects.create(name="Tech")   
        instructor =  Instructor.objects.create(user_id=self.sample_user) 
        Course.objects.create(
            title='TeraForm Vs AWS',
            description='https://www.example.com',           
            course_url='https://www.example.com',
            overview='https://www.example.com',
            price=1000.00,
            instructor_id=instructor,
            type_id=course_type,
            category_id=course_cat
        )
        self.sample_course = Course.objects.get(title='TeraForm Vs AWS')        
        order_status = OrderStatus.objects.create(name="pending")    
        Order.objects.create(
            course_id=self.sample_course,
            learner_id=self.sample_learner ,
            order_status_id=order_status
        )
        self.sample_order = Order.objects.get(course_id=self.sample_course)
        self.payload={
            'course_id': self.sample_course.id,
            'paystack_id': "declined",
        }

    def test_course_payment(self):  
        self.client.force_authenticate(user=self.sample_user)
        res = self.client.post('/api/v1/pay/course/', self.payload)      
        self.assertEqual(res.status_code, 400)
        
    def tearDown(self):
        self.sample_user.delete()
        self.sample_learner.delete()
        self.sample_course.delete() 
        self.sample_order.delete()
