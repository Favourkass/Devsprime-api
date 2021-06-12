import math, random
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from db.serializers.forgot_serializers import ForgotPasswordSerializer


def generateOTP() :
        digits = "0123456789"
        OTP = ""
        for i in range(6) :
            OTP += digits[math.floor(random.random() * 10)]
        return OTP

class ForgotPasswordView(APIView):
    """ Checks for if user exists and generate OTP for reseting password after email has been inserted"""
    serializer_class = ForgotPasswordSerializer
    
    def post(self, request):
        email = request.data.get('email')
        try:
            user = get_user_model().objects.get(email=email)
        
        except ObjectDoesNotExist:
            return Response({"message":"User does not exist"}, status=404)
        
        
        OTP=generateOTP()
        user.otp_code = OTP
        user.save()
        if user.is_active == True:  
            send_mail(
                subject ='Here is the OTP for resetting your password. ',
                message =f'Your OTP is {OTP} \n Kindly click on this link to proceed http://localhost:18000/api/v1/passwords/reset',
                from_email = 'DevsPrime',
                recipient_list = [str(email),]
            )
            return Response({
                "message": "success",
                "data": {
                    "otp": str(OTP)
                },
                "errors": None
            }, status=200)
        
        
