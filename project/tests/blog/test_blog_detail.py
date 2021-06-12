from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status 
from rest_framework.authtoken.models import Token

from db.models.blogs import Blog
from db.models.user import User






class TestSetup(APITestCase):
    
    def setUp(self): 
        self.user = User.objects.create(email='email@email.com',password='testing321',)
        self.user_id = User.objects.get(id=self.user.id)
        self.token = Token.objects.create(user=self.user)
    
        self.blog= Blog.objects.create(user_id=self.user_id,title='first one',
                            short_desc='first short descripion',detail='first detail view')
        self.blog.save()
        
    def test_get_blog_details(self):
        """Ensure a user can get a particular blog"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('blog-details', kwargs={'uuid': self.blog.id}))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
      
    def test_delete_a_blog(self):
        """Ensure only the author can delete a blog """
        url = reverse('blog-details', kwargs={'uuid': self.blog.id})
        blog = Blog.objects.get(id=self.blog.id )
        self.client.force_authenticate(user=self.user, token=self.token.key)
        res=self.client.delete(url)
        blog.delete()
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)     
       
    def test_only_author_can_delete_a_blog(self):
        """Ensure only author can delete a particular blog"""

        response = reverse('blog-details', kwargs={'uuid': self.blog.id})
        blog = Blog.objects.get(id=self.blog.id )
        self.client.force_authenticate(user=None)
        res = self.client.delete(response)
        blog.delete()
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    
    def test_edit_a_blog_by_unauthourized_user(self):
        """Ensure only unauthourized user cannot edit a blog"""
        
        self.client.force_authenticate(user=None)
        response = reverse('blog-details', kwargs={'uuid': self.blog.id})
        blog = Blog.objects.get(id=self.blog.id )
        payload = {
            "user_id": "",
            "title": " title",
            "short_desc": "description",
            "detail": " details"
        }
        response = self.client.put(response, payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        