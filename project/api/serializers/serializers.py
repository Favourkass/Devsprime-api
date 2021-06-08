from rest_framework import serializers
from db.models.learner import LearnerProfile


class LearnerCardSerializer(serializers.ModelSerializer):    

    class Meta:
        model = LearnerProfile
        fields = ('account_name', 'account_number', 'bank_name')
