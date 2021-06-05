from django.urls import path
from api.views.login import LoginView
from api.views.register_view import RegisterUserView
from api.views.instructors_view import RegisterInstructorView
from api.views.verify_otp import VerifyOtp
from api.views.forgot_password import ForgotPasswordView


urlpatterns = [
    path('auth/register/', RegisterUserView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('otps/verify', VerifyOtp.as_view(), name='verify-otp'),
    path('passwords/forgot/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('auth/register/instructor', RegisterInstructorView.as_view(), name='registerinstructor'),
]
