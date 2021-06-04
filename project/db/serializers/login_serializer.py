from rest_framework import serializers
from django.contrib.auth import get_user_model


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=8, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
