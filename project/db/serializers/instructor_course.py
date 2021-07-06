from db.models.course import Course
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    type_id = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Course
