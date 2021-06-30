import uuid
from django.db import models
from .course import Course
from .learner import LearnerProfile
from .orders import Order


class CoursePayment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    learner_id = models.ForeignKey(LearnerProfile, on_delete=models.CASCADE) 
    order_id  = models.ForeignKey(Order, on_delete=models.CASCADE) 
    paystack_id = models.TextField(blank=True, null=True)
    amount = models.DecimalField(default=0.0, max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.learner_id.account_name}'
