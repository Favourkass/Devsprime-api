from django.db import models
import uuid
from .blogs import Blog

class Comment(models.Model):
    id = models.UUIDField(unique=True, primary_key=True,
                          default=uuid.uuid4, editable=False)
    blog_id = models.ForeignKey(
        Blog, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
