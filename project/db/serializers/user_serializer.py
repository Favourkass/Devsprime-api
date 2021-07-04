from rest_framework import serializers

from db.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fullname', 'mobile_number',
                  'avatar', 'is_learner', 'is_instructor', 'is_admin']
