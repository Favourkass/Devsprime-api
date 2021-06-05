# from db.models.users import User
# from db.models.instructors import Instructor
# from rest_framework.test import APIClient,APITestCase
# from django.contrib.auth import get_user_model
# from django.urls import reverse
# from rest_framework.views import status
# from django.test import TestCase, Client
# from django.contrib.auth import get_user_model


# class InstructorList(APITestCase):
#     client = APIClient()
#     def setUp(self):
#         favour = get_user_model().objects.create(email = 'favour@gmail.com', 
#                                     password = 'favour@19', 
#                                     mobile_number='08165306674',
#                                     fullname='Nnabue Chukwuemeka',
#                                     is_instructor=True)
#         create_instructor = Instructor.objects.create(user_id = favour)

#     def get_instructors(self):
#         url = reverse('registerinstructor')
#         res = self.client.get(url)
#         self.assertEquals(res.status_code, status.HTTP_200_OK)
#         self.assertEqual(User.is_instructor,True)
#         self.assertEqual(Instructor.user_id, 'favour@gmail.com')





