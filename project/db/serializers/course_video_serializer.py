from db.models.course_video import CourseVideo
from rest_framework import serializers


class CourseVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseVideo
        fields = '__all__'


class UploadCourseVideoSerializer(serializers.ModelSerializer):
    video_urls = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=True)
    )

    class Meta:
        model = CourseVideo
        fields = ['id', 'video_urls', 'course_id']
