import random
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from db.serializers.register import RegisterSerializer
from api.utils import Util
from db.models.learner import LearnerProfile
from lib.response import Response



def generate_key(num_digit):
    """Generate key using user email and random str"""
    min_val = 10 ** (num_digit - 1)
    max_val = (10 ** num_digit) - 1
    otp = random.randint(min_val, max_val)
    return otp


class RegisterUserView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    """Create new user in the system"""
    serializer_class = RegisterSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        fullname = user_data.get('fullname', '')
        email = user_data.get('email', '')
        mobile_number = user_data.get('mobile_number', '')
        password = user_data.get('password', '')

        if not serializer.is_valid():
            return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = get_user_model().objects.create(fullname=fullname, email=email,
                                                   mobile_number=mobile_number, password=password)
            user.set_password(password)
            otp = generate_key(6)
            user.otp_code = otp
            user.is_learner = True

            EMAIL_VERFICATION_URL = 'http://localhost:18000/api/v1/otps/verify'
            email_text = 'Thank you for registering with us \n\n Please copy the code below to verify your email'
            email_body = f'Hi {fullname}\n {email_text} \n Click on this <a href="{EMAIL_VERFICATION_URL}' \
                         f'?otp={otp}&email={email}">link</a> to verify'
            data = {'email_body': email_body, 'to_email': [email], 'email_subject': 'Verify your email using this link'}
            Util.send_email(data)

            learner = LearnerProfile.objects.create(user_id=user)
            learner.save()
            user.save()

            return Response(data=dict(fullname=fullname, email=email, otp=otp), status=status.HTTP_201_CREATED)
        
