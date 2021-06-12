from db.models.user import User
from db.models.blogs import Blog
from db.models.comment import Comment
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse


class TestLearnerProfile(APITestCase):
    client = APIClient()

    def setUp(self):
        User.objects.create(email='test@gmail.com',
                            fullname='Test User',
                            mobile_number='08012345678',
                            password='password1234'
                            )

        self.sample_user = User.objects.get(email='test@gmail.com')

        self.blog = Blog.objects.create(user_id=self.sample_user,
                                        title='title',
                                        cover_img='Elias',
                                        short_desc='it',
                                        detail='He leads me'
                                        )
        self.sample_blog = Blog.objects.get(title='title')

        self.comment = Comment.objects.create(user_id=self.sample_user,
                                              blog_id=self.sample_blog,
                                              comment='Test comment'
                                              )
        self.sample_comment = Comment.objects.get(comment='Test comment')

    def test_get_comment(self) :
        self.client.force_authenticate(user=self.sample_user)
        response = self.client.get(
            reverse('comments', kwargs={'pk': self.blog.pk}))
        self.assertEqual(response.data.get('message'), 'success')

    def test_valid_post_comment(self):
        self.client.force_authenticate(user=self.sample_user)
        self.sample_user.is_learner = True
        self.sample_user.is_verified = True
        payload = {'user_id': self.sample_user,
                   'blog_id': self.sample_blog,
                   'comment': 'Help me God'}
        url = reverse('comments', kwargs={'pk': self.sample_blog.pk})
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def teardown(self):
        self.sample_user.delete()
        self.sample_blog.delete()
        self.sample_comment.delete()
