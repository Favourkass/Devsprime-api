from django.urls import reverse
from db.models.user import User
from rest_framework.test import APITestCase
from rest_framework import status


class TestLearnerProfile(APITestCase):
    def setUp(self) :
        User.objects.create(email='test@gmail.com',
                            fullname='Test User',
                            mobile_number='08012345678',
                            password='password1234')
        self.sample_user = User.objects.get(email='test@gmail.com')

    def test_get_learner(self):
        url = reverse('learners')
        self.client.force_authenticate(user=self.sample_user)
        self.sample_user.email_verified=True
        self.sample_user.is_learner=True
        self.sample_user.save()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_update_learner(self):
        self.client.force_authenticate(user=self.sample_user)
        payload = {'fullname' : 'Johnson',
                   'mobile_number' : '123345623',}
        response = self.client.put(reverse('learners'), payload)
        data = response.data.get('message')
        user_data = response.data.get('data')
        self.assertEqual(user_data['fullname'], 'Johnson')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, 'success')

    def teardown(self):
        self.sample_user.delete()
        self.sample_learner.delete()
