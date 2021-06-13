from django.urls import path
from .views import home, blogs
from .views.blog_details import BlogDetail
from .views import comment
from .views.comment_details import  CommentDetails


urlpatterns = [
    path('home/', home.index),
    path('',  blogs.Blogs.as_view(), name='blogs'),
    path('<uuid>/', BlogDetail.as_view(),name='blog-details'),
    path('<uuid:pk>/comments/', comment.CommentView.as_view(), name='comments'),
    path('comments/<uuid:pk>/',  CommentDetails.as_view(), name='comment-detail'),
]
