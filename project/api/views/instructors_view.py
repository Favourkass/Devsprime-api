from django.contrib.auth import get_user_model
import random
from decouple import config
from rest_framework import generics,status,permissions
from db.serializers.registerserializer import RegisterInstructorSerializer
from ..utils import Util
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
            return Response(errors=serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        else:
            email = request.data.get('email')
            fullname = request.data.get('fullname')
            password = request.data.get('password')
            phone = request.data.get('mobile_number')
            EMAIL_VERIFICATION_URL=config('EMAIL_VERIFICATION_URL')
            otp = generate_key(6)
            is_instructor = True
            user = get_user_model().objects.create(email=email, password=password, fullname=fullname, mobile_number = phone,otp_code =otp,is_instructor=is_instructor )
            email_text = f'Thank you for registering with us \n\n Please click the link below to authenticate your account'
            email_body = f'Hi {fullname}\n {email_text} \n click on this link <a href="{EMAIL_VERIFICATION_URL}/?otp={otp}&email={email}" to verify your account '
            data = {'email_body': email_body, 'to_email': [email], 'email_subject': 'Verify your email using this link'}
            Util.send_email(data)
            user.save()
            create_instructor = Instructor.objects.create(user_id = user)
            create_instructor.save()
            return Response(data=serializer.data, status = status.HTTP_201_CREATED)
        