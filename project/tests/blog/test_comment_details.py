from django.http import response
from django.contrib.auth import get_user_model
from db.models.blogs import Blog
from db.models.comment import  Comment
from db.models.reply import Reply
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse


class TestCommentDetails(APITestCase):
    client = APIClient()
    def setUp(self):

        get_user_model().objects.create(
            email = "ajibolagureje@gmail.com" , password = '123456'
        )
        self.user =  get_user_model().objects.get(email='ajibolagureje@gmail.com')
        self.blog = Blog.objects.create(user_id=self.user, cover_img='https://www.pexels.com/selfie',title='The way', short_desc ='Short description',detail ='The detail of the blog')
        self.comment = Comment.objects.create(user_id=self.user,blog_id=self.blog,comment='I like the blog')
        self.reply = Reply.objects.create(comment_id=self.comment, reply='You are right')
        self.url = reverse('comment-detail', kwargs={'pk':self.comment.pk})

    def test_get_comment_by_id(self):
        
        self.client.force_authenticate(user=self.user)
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_comment_by_id_with_auth(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_author_can_delete_a_comment(self):
        response = reverse('comment-detail', kwargs={'pk': self.comment.pk})
        comment = Comment.objects.get(id=self.comment.id )
        self.client.force_authenticate(user=None)
        res = self.client.delete(response)
        comment.delete()
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

