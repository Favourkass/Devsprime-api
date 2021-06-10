from rest_framework import serializers
from django.contrib.auth import get_user_model
import re


class RegisterInstructorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True,
        style={'input_type': 'password'}, trim_whitespace=True, max_length=68, min_length=8,)
    fullname = serializers.CharField(write_only = True, trim_whitespace=True, min_length = 8)
    mobile_number = serializers.CharField(min_length = 11)
    
    class Meta:
        model = get_user_model()
        fields = ['email', 'fullname', 'mobile_number', 'password']
        
    def validate_fullname(self,fullname):
        regex=re.compile(r'^[A-Za-z\s]+$')
        if regex.match(fullname):
            return fullname
        raise serializers.ValidationError("Enter a valid fullname, no numbers allowed")

    def validate_mobile_number(self, mobile_number):
        regex = re.compile(r'^\+?[0-9]+$')
        if regex.match(mobile_number):
            return mobile_number
        raise serializers.ValidationError("Enter a valid phone number")
        