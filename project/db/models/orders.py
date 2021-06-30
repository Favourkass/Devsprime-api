from django.db import models
from .course import Course
from .learner import LearnerProfile
from .order_status import OrderStatus
import uuid


class Order(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    learner_id = models.ForeignKey(LearnerProfile, on_delete=models.CASCADE)
    order_status_id = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.course_id.title}'
