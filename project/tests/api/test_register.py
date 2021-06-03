from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from db.models.user import User


class CreateNewUserTest(APITestCase):
    """ Test module for creating a new user """

    def setUp(self):
        self.valid_payload = {
            'email': 'testuser@gmail.com',
            'fullname': 'Test User',
            'mobile_number': '08076543223',
            'password': 'test1234'
        }
        self.invalid_payload = {
            'email': '',
            'fullname': 'Test User',
            'mobile_number': '08076543223',
            'password': 'test1234'
        }
        self.invalid_fullname_payload = {
            'email': 'testuser1@gmail.com',
            'fullname': 'Test234567',
            'mobile_number': '08076543223',
            'password': 'test1234'
        }
        self.invalid_number_payload = {
            'email': 'testuser2@gmail.com',
            'fullname': 'Test User',
            'mobile_number': '0234567345eder',
            'password': 'test1234'
        }
        self.valid_number_payload = {
            'email': 'testuser2@gmail.com',
            'fullname': 'Test User',
            'mobile_number': '+02345673458',
            'password': 'test1234'
        }

        self.register_url = reverse('register')

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_user(self):
        res = self.client.post(
            self.register_url,
            self.valid_payload,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_create_invalid_user(self):
        res = self.client.post(
            self.register_url,
            self.invalid_payload,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_fullname(self):
        res = self.client.post(
            self.register_url,
            self.invalid_fullname_payload,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_number(self):
        res = self.client.post(
            self.register_url,
            self.invalid_number_payload,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_number(self):
        res = self.client.post(
            self.register_url,
            self.valid_number_payload,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
