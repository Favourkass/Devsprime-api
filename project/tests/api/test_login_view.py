from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token


class LoginViewTest(APITestCase):
    client = APIClient()

    def setUp(self):
        user = get_user_model().objects.create(
            email='tester@gmail.com', password='123456789')
        token, _ = Token.objects.get_or_create(user=user)

    def test_token_is_not_available_for_non_existing_user(self):
        url = reverse('login')
        payload = {'email': 'fakeuser@email.com', 'password': 'fakepassword'}
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)

    def test_token_exists_for_existing_user(self):
        user = get_user_model().objects.get(email='tester@gmail.com')
        token = Token.objects.get(user=user)
        self.assertTrue(token.key)

    def test_token_not_available_for_payload_with_blank_email_and_blank_password(self):
        url = reverse('login')
        payload = {'email': '', 'password': ''}
        response = self.client.post(url, payload)
        msg = {'message': "failure", 'data': 'null',
               'errors': {'email': 'This field cannot be blank', 'password': 'This field cannot be blank'}, }
        self.assertEqual(response.data, msg)
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)

    def test_token_not_available_for_payload_with_blank_email(self):
        url = reverse('login')
        payload = {'email': '', 'password': '123456789'}
        response = self.client.post(url, payload)
        msg = {'message': "failure", 'data': 'null',
               'errors': {'email': 'This field cannot be blank'}, }
        self.assertEqual(response.data, msg)
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)

    def test_token_not_available_for_payload_with_blank_password(self):
        url = reverse('login')
        payload = {'email': 'tester@gmail.com', 'password': ''}
        response = self.client.post(url, payload)
        msg = {'message': "failure", 'data': 'null',
               'errors': {'password': 'This field cannot be blank'}, }
        self.assertEqual(response.data, msg)
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)
