from django.urls import reverse
from db.models.user import User
from rest_framework import status 
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class TestSetup(APITestCase):
    def setUp(self):
        self.reset_password_url=reverse('reset-password')       
        self.otp_code='3456'
        self.no_otp={
        'email':'email@email.com',
        'otp_code': '',
        'password':'testing321',
        'confirm password':'testing321',
    }
        self.no_email={
        'email':'email@email.com',
        'password':'',
        'otp_code': '2345',
        'confirm password':'testing321',
    }
        self.no_password={
        'email':'email@email.com',
        'password':'',
        'otp_code': '2345',
        'confirm password':'testing321',
    }
        self.no_confirm_password={
        'email':'email@email.com',
        'password':'',
        'otp_code': '2345',
        'confirm password':'testing321',
    }
        
        return super().setUp()

    def test_insert_email_field(self):
        """Ensure users enter email field"""
        self.client=APIClient()
        response=self.client.put(self.reset_password_url,self.no_email)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
 
    def test_insert_otp_key_field(self):
        """Ensure users enter otp_key field"""
        self.client=APIClient()
        response=self.client.put(self.reset_password_url,self.no_otp)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_insert_password_field(self):
        """Ensure users enter password field"""
        self.client=APIClient()
        response=self.client.put(self.reset_password_url,self.no_password)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_insert_confirm_password_field(self):
        """Ensure users enter confirm password field"""
        self.client=APIClient()
        response=self.client.put(self.reset_password_url,self.no_confirm_password)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
 
    def test_reset_password(self):
        """
        Ensure user can  reset  new password.
        
        """
       
        User.objects.create(email='email@email.com',password='testing321',otp_code='')
        user=User.objects.get(email='email@email.com')
        user.otp_code=self.otp_code
        user.save()
        payload={
            'email':"email@email.com",
            'password':"admin321",
            'confirm_password':"admin321",
            "otp":'3456',
        }
        response = self.client.put(self.reset_password_url,payload,format='json')
        
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(payload['password'])
        
    def test_confirm_password(self):
        """
        Ensure user can  reset the  two passwords are the same.
        
        """
       
        User.objects.create(email='email@email.com',password='testing321',otp_code='')
        user=User.objects.get(email='email@email.com')
        user.otp_code=self.otp_code
        user.save()
        payload={
            'email':"email@email.com",
            'password':"admin321",
            'confirm_password':"admin",
            "otp_key":'3456',
        }
        response = self.client.put(self.reset_password_url,payload,format='json')
        
        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(payload['password'])
        

    
    def tearDown(self):
        return super().tearDown()
    
    
        
