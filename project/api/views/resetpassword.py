from rest_framework.response import Response
from rest_framework import generics

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from db.models.user import User 

from db.serializers.resetpassword import PasswordResetSerializer


class PasswordReset(generics.GenericAPIView):
    """This class should return success if the user already exist and enters
    a valid otp_code that was sent to their mail"""
    
    serializer_class=PasswordResetSerializer
    def put(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        otp = serializer.data.get('otp')
        password = request.data.get('password')
        confirm_password =request.data.get('confirm_password')
        try:
            user = User.objects.get(email=email)
            
        except ObjectDoesNotExist:
            return Response({"message":"User does not exist"}, status=404)
        
        if password == confirm_password:
            
            keygen=user.otp_code
            OTP=keygen
            if otp != OTP:  
                return Response({
                "message": "Failure",
                "data": None,
                "errors": {
                    'otp_code': "Does not match or expired"
                }
            }, status=400)
            
            
            user.set_password(password)
            user.save()
            return Response({
                "message": "success",
                "data": {
                    "otp": None
                },
                "errors": None
            }, status=200)
        
        else:
            return Response({"message":"Failure","data":None,"errors":{
                "passwords": "The two Passwords must be the same"
            }},status=400)
            
        
