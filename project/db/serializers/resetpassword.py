from rest_framework import serializers


class PasswordResetSerializer(serializers.Serializer):
    email=serializers.EmailField(min_length=2)
    otp=serializers.CharField(max_length=6)
    password=serializers.CharField(min_length=8)
    confirm_password=serializers.CharField(min_length=8)
    
    class Meta:
        fields=['email','otp','password','confirm_password']
        
        
        
        
        
