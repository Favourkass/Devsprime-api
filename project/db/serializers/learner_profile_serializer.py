from rest_framework import serializers
from db.models.learner import LearnerProfile
from db.models.user import User


class LearnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','fullname','mobile_number']
        