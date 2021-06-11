from django.db import models
import uuid
from django.conf import settings
from .user import User


class Blog(models.Model):
    DEFAULT_COVER_IMG_URL = 'https://res.cloudinary.com/devsprime/image/upload/v1623419362/Blogs/blog_ompj6m.jpg'

    id = models.UUIDField(unique=True, primary_key=True,
                          default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    cover_img = models.URLField(default=DEFAULT_COVER_IMG_URL)
    short_desc = models.TextField(blank=True)
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

