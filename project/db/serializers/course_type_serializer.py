from rest_framework import serializers
from db.models.course_type import CourseType

class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = ['id', 'name']