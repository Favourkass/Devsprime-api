from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from db.models.user import User



class TestOTPVerification(APITestCase):
    def setUp(self):
        self.verify_url = reverse('verify-otp')
        self.user_data = {
            'otp':'123456'
        }
        self.empty_data = {
            "otp":""
        }
    
    def test_empty_otp(self):
        res = self.client.post(self.verify_url, self.empty_data)
        self.assertEqual(res.status_code, 400)

    def test_invalid_otp(self):
        response = self.client.post(self.verify_url, self.user_data)
        self.assertEqual(response.status_code, 400)

    def test_otp_length(self):
        self.assertEqual(len(self.user_data['otp']), 6)
    
