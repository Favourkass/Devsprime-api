from api.views.payment_card_views import LearnerCardView
from django.urls import path, include
from api.views.login import LoginView
from api.views.resetpassword import PasswordReset 
from api.views.login import LoginView
from api.views.register_view import RegisterUserView
from api.views.instructors_view import RegisterInstructorView
from api.views.verify_otp import VerifyOtp
from api.views.forgot_password import ForgotPasswordView
from api.views.resetpassword import PasswordReset 
from api.views.register_view import RegisterUserView
from api.views.instructor_profile import InstructorProfile
from api.views.instructor_course import CourseList
from api.views.learner_profile import LearnerProfile
from api.views.all_courses import AllCourses
from api.views.upload_course import UploadCourseView
from api.views.course_details import CourseDetails
from api.views.orders import OrderListView
from api.views.learner_course import LearnerCourseList
from api.views.cart_list import CartItemList
from api.views.cart_details import CartDetail


urlpatterns = [
    path('learners/', LearnerProfile.as_view(), name='learners'),
    path('auth/register/', RegisterUserView.as_view(), name='register'),
    path('auth/register/instructor/', RegisterInstructorView.as_view(), name='registerinstructor'),
    path('otps/verify/', VerifyOtp.as_view(), name='verify-otp'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('passwords/forgot/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('passwords/reset/',PasswordReset.as_view(), name='reset-password'),
    path('learner/card/', LearnerCardView.as_view(), name='learn-card-detail'),
    path('instructor/', InstructorProfile.as_view(), name='instructor-profile'),
    path('blogs/', include('blog.urls')),
    path('instructors/courses/<instructor_id>/',CourseList.as_view(), name='instructor-courses'),   
    path('courses/', AllCourses.as_view(), name='all_courses'),
    path('courses/upload/', UploadCourseView.as_view(), name='upload-course'),
    path('courses/<uuid:pk>/',CourseDetails.as_view(), name='course-details'),
    path('orders/', OrderListView.as_view(),name='order'),
    path('learner/courses/', LearnerCourseList.as_view(),name='learner-course'),
    path('cart/', CartItemList.as_view(),name='cart'),
    path('cart/<uuid:pk>/', CartDetail.as_view(),name='cart-detail'),
]
