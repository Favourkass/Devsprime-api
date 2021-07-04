from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model
from django.urls import reverse

from db.models.learner import LearnerProfile
from db.models.course import Course, CourseType, CourseCategory
from db.models.instructors import Instructor
from db.models.cart import Cart
from db.serializers.instructor_course import CourseSerializer


class CartTest(APITestCase):
    '''create instances of instructor, course, category, type'''
    def setUp(self):
        # creating new learner
        get_user_model().objects.create(fullname='testlearner', email='testlearner@gmail.com'
                                        , password='testlearner')
        self.sample_user = get_user_model().objects.get(email='testlearner@gmail.com')
        self.sample_learner = LearnerProfile.objects.create(user_id=self.sample_user)
        
        # create new instructor, course, course
        get_user_model().objects.create(
            fullname='testinstructor', email = "testinstructor@gmail.com" , password = 'testinstructor')
        self.user =  get_user_model().objects.get(email='testinstructor@gmail.com')
        self.instructor = Instructor.objects.create(user_id=self.user)
        self.type = CourseType.objects.create(name='free')
        self.category = CourseCategory.objects.create(name='design')
        self.test_course = Course.objects.create(
            title='How To Test',description='make sure you test', cover_img='dfhsdflsj',
            course_url='dkfjslsfl', overview='sdfhslh', price=120,
            instructor_id= self.instructor, category_id=self.category, type_id=self.type
                        )
        
        #Get course id
        self.get_course = Course.objects.get(title='How To Test')
        courses_details = CourseSerializer(self.get_course)
        self.get_course_id = courses_details.data.get('id')
        
        #create a cart for a user
        self.test_cart = Cart.objects.create(course_id=self.get_course, 
                                            learner_id = self.sample_learner)
        self.cart_id = self.test_cart.id
        
        #url
        self.cart_url = reverse('cart')
        self.cart_detail_url = f'/api/v1/cart/{str(self.cart_id)}/'
        
        self.payload = {   
            'learner_id': str(self.sample_learner.id),
            'course_id': str(self.get_course_id)            
        }
        
        
    def test_get_courses_in_cart(self):
        self.client.force_authenticate(user=self.sample_user)
        res = self.client.get(self.cart_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_get_cart_item_by_id(self):
        self.client.force_authenticate(user=self.sample_user)
        res = self.client.get(self.cart_detail_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_get_cart_item_by_id(self):
        self.client.force_authenticate(user=self.sample_user)
        res = self.client.delete(self.cart_detail_url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)    
        