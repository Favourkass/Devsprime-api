import uuid
from django.db import models
from .course import Course
from .learner import LearnerProfile



class Cart(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    course_id = models.ForeignKey(Course, blank=False, on_delete=models.CASCADE, related_name='course')
    learner_id = models.ForeignKey(LearnerProfile, on_delete=models.CASCADE, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['learner_id', '-created_at']
    
    def __str__(self):
        return f'{self.learner_id}'