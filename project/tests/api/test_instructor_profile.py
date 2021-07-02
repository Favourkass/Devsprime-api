from db.models.user import User
from db.models.instructors import Instructor
from rest_framework.test import APITestCase
from rest_framework import status


class TestInstructorProfile(APITestCase):
    def setUp(self):
        User.objects.create(email='test@gmail.com',
                            fullname='Test User',
                            mobile_number='08012345678',
                            password='password1234')
        self.sample_user = User.objects.get(email='test@gmail.com')
        Instructor.objects.create(user_id=self.sample_user,
                                      avatar='Elias.jpg',
                                      facebook='https://www.facebook.com',
                                      twitter='https://www.twitter.com',
                                      instagram='https://www.instagram.com')
        self.sample_learner = Instructor.objects.get(
            user_id=self.sample_user)

    def test_get_instructor(self):
        self.client.force_authenticate(user=self.sample_user)
        response = self.client.get('/api/v1/instructor/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_instructor(self):
        self.client.force_authenticate(user=self.sample_user)
        payload = {'avatar': 'Johnson.jpeg',
                   'facebook': 'https://facebook.com',
                   'twitter': 'https://twitter.com',
                   'instagram': 'https://www.instagram.com'}
        response = self.client.put('/api/v1/instructor/', payload)                                                                                                    
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def teardown(self):
        self.sample_user.delete()
        self.sample_learner.delete()
