from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class ForgotPassordTest(APITestCase):

    def setUp(self):
        user = get_user_model().objects.create(fullname='ajibola',email='gurejea@gmail.com',
        mobile_number='08079105112', password='admin123')
        user.save()
        self.url =reverse('forgot-password')

        self.payload = {
            'email':'gurejea@gmail.com'
        }

        self.invalid_payload = {
            'email':'gurejea@gmail.com'
        }

    def test_empty_email(self):
        res = self.client.post(self.url)
        self.assertEqual(res.status_code, 404)

    def test_valid_email (self):
         res = self.client.post(self.payload, format='json')
         self.assertTrue(res.status_code, 200)

    def test_invalid_email (self):
         res = self.client.post(self.invalid_payload, format='json')
         self.assertTrue(res.status_code, 404)
        
