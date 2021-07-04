from rest_framework import serializers

from db.models.instructors import Instructor


class InstructorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'twitter', 'facebook', 'instagram']
