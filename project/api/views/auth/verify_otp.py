from rest_framework import generics, status

from db.models.user import User
from db.serializers.otp_form_serializer import OTPFormSerializer
from lib.response import Response


class VerifyOtp(generics.GenericAPIView):
    serializer_class = OTPFormSerializer

    def post(self, request):
        data = request.data
        otp = data.get('otp', '')
        email = data.get('email', '')

        if otp is None or email is None:
            return Response(errors=dict(invalid_input="Please provide both otp and email"), status=status.HTTP_400_BAD_REQUEST)

        get_user = User.objects.filter(email=email)

        if not get_user.exists():
            return Response(errors=dict(invalid_email = "please provide a valid registered email"), status=status.HTTP_400_BAD_REQUEST )
        
        user = get_user[0] 

        if user.otp_code != otp:
            return Response(errors=dict(invalid_otp = "please provide a valid otp code"), status=status.HTTP_400_BAD_REQUEST)
        
        user.email_verified = True
        user.is_active = True
        user.save()
        
        return Response(data={
                "verified status":"Your account has been successfully verified"
            }, status=status.HTTP_200_OK)
                