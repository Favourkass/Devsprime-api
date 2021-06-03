from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with an email is successful"""
        email = 'test@testing.com'
        fullname = 'Test User'
        password = 'testpasss321'
        user = get_user_model().objects.create_user(
            email=email, password=password, fullname=fullname
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.fullname, fullname)
        self.assertTrue(user.check_password(password))

