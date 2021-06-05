from django.db import models
import uuid
from django.conf import settings


class Instructor(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.CharField(null=True, blank=True, max_length=200)
    facebook = models.CharField(null=True, blank=True, max_length=200)
    twitter = models.CharField(null=True, blank=True, max_length=200)
    instagram = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return f'{self.user_id}'
    
