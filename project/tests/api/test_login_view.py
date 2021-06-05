from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token


class LoginViewTest(APITestCase):
    client = APIClient()
    url = reverse('login')

    def setUp(self):
        user = get_user_model().objects.create(
            fullname='Tester John', email='tester@gmail.com',  mobile_number='08093005000', password='testpassword123_')
        user.set_password('testpassword123_')
        user.email_verified = True
        user.is_active = True
        user.save()

    def test_token_returned_to_authenticated_user(self):
        payload = {'email':'tester@gmail.com', 'password': 'testpassword123_'}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

    def test_token_not_available_for_non_existing_user(self):
        payload = {'email': 'fakeuser@email.com', 'password': 'fakepassword'}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_token_not_available_for_unauthenticated_user(self):
        user = get_user_model().objects.get(email='tester@gmail.com')
        user.email_verified = False
        user.save()
        payload = {'email':'tester@gmail.com', 'password': 'testpassword123_'}   
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_token_not_available_for_payload_with_blank_email_and_blank_password(self):
        payload = {'email': '', 'password': ''}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_token_not_available_for_payload_with_blank_email(self):
        payload = {'email': '', 'password': 'testpassword123'}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_token_not_available_for_payload_with_blank_password(self):
        payload = {'email': 'tester@gmail.com', 'password': ''}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)