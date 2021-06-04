from rest_framework import serializers


class OTPFormSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6)
    email = serializers.EmailField(max_length=200)
    