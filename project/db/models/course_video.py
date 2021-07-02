import uuid
from django.db import models
from db.models.course import Course


class CourseVideo(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    course_id = models.ForeignKey(
        Course, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=255, blank=False)
    video_url = models.URLField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
