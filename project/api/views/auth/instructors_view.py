import random

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import generics, status, permissions

from db.serializers.registerserializer import RegisterInstructorSerializer
from api.utils import Util
from db.models.instructors import Instructor
from lib.response import Response


def generate_key(num_digit):
    """Generate key using user email and random str"""
    min_val = 10 ** (num_digit - 1)
    max_val = (10 ** num_digit) - 1
    otp = random.randint(min_val, max_val)
    return otp


class RegisterInstructorView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    """Create new Instructor in the system"""
    serializer_class = RegisterInstructorSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        valid_sirializer = serializer.is_valid()
        if not valid_sirializer:
            return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = request.data.get('email')
        fullname = request.data.get('fullname')
        password = request.data.get('password')
        phone = request.data.get('mobile_number')
        otp = generate_key(6)

        # Generate Email Message
        EMAIL_VERIFICATION_URL = settings.EMAIL_VERIFICATION_URL
        email_text = f'Thank you for registering with us \n\n Please click the link below to authenticate your account'
        email_body = f'Hi {fullname}\n {email_text} \n click on this <a href="{EMAIL_VERIFICATION_URL}/?otp={otp}&email={email}">link</a> to verify your account '
        data = {'email_body': email_body, 'to_email': [
            email], 'email_subject': 'Verify your email using this link'}

        # Send Mail
        is_email_sent = Util.send_email(data)
        if not is_email_sent:
            return Response(
                errors=dict(
                    email_error='Email service is unavailable, please try later'),
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        # create User
        user = get_user_model().objects.create(email=email, password=password,
                                               fullname=fullname, mobile_number=phone, otp_code=otp, is_instructor=True)

        user.set_password(password)
        user.save()

        create_instructor = Instructor.objects.create(user_id=user)
        create_instructor.save()
        return Response(data=dict(fullname=fullname, email=email, otp=otp, mobile_number=phone), status=status.HTTP_201_CREATED)
