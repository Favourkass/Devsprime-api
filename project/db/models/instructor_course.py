import uuid
from django.db import models
from django.db.models.deletion import CASCADE
from db.models.instructors import Instructor


class CourseCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CourseType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(max_length=500, blank=False)
    avatar = models.CharField(max_length=255, blank=False)
    course_url = models.CharField(max_length=255, blank=False)
    overview = models.CharField(max_length=200, blank=False)
    price = models.IntegerField(blank=False)
    instructor_id = models.ForeignKey(Instructor, on_delete=CASCADE, blank=False)
    type_id = models.ForeignKey(CourseType, on_delete=CASCADE, blank=False)
    category_id = models.ForeignKey(CourseCategory, on_delete=CASCADE, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
