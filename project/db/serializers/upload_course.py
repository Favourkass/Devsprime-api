from rest_framework import serializers
from db.models.course import Course


class UploadCourseSerializer(serializers.ModelSerializer):
    cover_img = serializers.FileField()
    overview = serializers.FileField()
    course_url = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=True)
    )

    class Meta:
        model = Course
        fields = ('title', 'description', 'price',
                  'type_id', 'category_id', 'course_url','cover_img','overview')
