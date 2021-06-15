from rest_framework import serializers
from db.models.learner_course import LearnerCourse


class LearnerCourseSerializer(serializers.ModelSerializer):
      class Meta:
        model = LearnerCourse
        fields = '__all__'
        