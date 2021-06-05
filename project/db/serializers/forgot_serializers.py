from django.contrib.auth import get_user_model
from rest_framework import serializers


class ForgotPasswordSerializer(serializers.ModelSerializer):
    """Serializer to Generate OTP"""
    email = serializers.EmailField()

    class Meta:
        model = get_user_model()
        fields = ('email',)
        
        
