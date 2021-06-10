import uuid
from django.db import models
from db.models.instructors import Instructor
from db.models.course_type import CourseType
from db.models.course_category import CourseCategory


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    avatar = models.CharField(max_length=255, blank=False)
    course_url = models.CharField(max_length=255, blank=False)
    overview = models.CharField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    instructor_id = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, blank=False)
    type_id = models.ForeignKey(
        CourseType, on_delete=models.CASCADE, blank=False)
    category_id = models.ForeignKey(
        CourseCategory, on_delete=models.CASCADE, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
