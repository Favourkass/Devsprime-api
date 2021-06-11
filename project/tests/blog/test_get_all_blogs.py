from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from db.models.user import User


class TestBlogs(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            fullname='Tester Tesing', email='tester@gmail.com',  mobile_number='09099900099', password='testpassword123_')
        self.user.set_password('testpassword123_')
        self.user.email_verified = True
        self.user.is_active = True
        self.user.save()

        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        self.blog_url = reverse('blogs')
        self.login_url = reversed('login')

    def test_get_all_blogs(self):
        response = self.client.get(self.blog_url)
        self.assertEqual(response.status_code, 200)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)

    def test_unathorized_user_cannot_post_blog(self):
        """
        Test anonymous users cannot post a blog
        """
        self.client.force_authenticate(user=None)
        payload = {
            "user_id": "",
            "title": "Test title",
            "cover_img": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Lemgo_-_Marktplatz_mit_Rathaus.jpg",
            "short_desc": "Test description",
            "detail": "Test details"
        }
        response = self.client.post(self.blog_url, payload)
        self.assertEqual(response.status_code, 401)

   