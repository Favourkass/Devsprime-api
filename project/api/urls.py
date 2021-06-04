from django.urls import path
from api.views.register_view import RegisterUserView
from api.views.verify_otp import VerifyOtp


urlpatterns = [
    path('auth/register/', RegisterUserView.as_view(), name='register'),
    path('otps/verify', VerifyOtp.as_view(), name='verify-otp')
]
