from django.urls import path
from api.views.register_view import RegisterUserView


urlpatterns = [
    path('auth/register/', RegisterUserView.as_view(), name='register'),
]
