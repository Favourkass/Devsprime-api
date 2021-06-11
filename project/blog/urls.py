from django.urls import path
from .views import home, blogs


urlpatterns = [
    path('home/', home.index),
    path('',  blogs.Blogs.as_view(), name='blogs')
]
