from django.urls import path
from .views import home, blogs
from .views.blog_details import BlogDetail


urlpatterns = [
    path('home/', home.index),
    path('',  blogs.Blogs.as_view(), name='blogs'),
    path('<uuid>/', BlogDetail.as_view(),name='blog-details'),
    
]
