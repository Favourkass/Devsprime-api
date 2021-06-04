from rest_framework import generics, status
from rest_framework.response import Response
from db.models.user import User
from db.serializers.otp_form_serializer import OTPFormSerializer


class VerifyOtp(generics.GenericAPIView):
    serializer_class = OTPFormSerializer

    def post(self, request):
        user = request.data
        serializer = OTPFormSerializer(data = user)

        if serializer.is_valid():
            user_otp = serializer.data['otp']
            user_email = serializer.data['email']

            user_details = {user.email:user.otp_code for user in User.objects.all()}
            user_model = User.objects.get(email = user_email)
            if user_details[user_email] == user_otp:
                
                user_model.email_verified = True
                user_model.is_active = True
                user_model.is_learner = True
                user_model.save()

                return Response({
                    'message':'success',
                    'data':'null',
                    'errors':'null'
                })
                
            return Response({'message':"verification failed"})
            
        message='Please input valid data'
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
