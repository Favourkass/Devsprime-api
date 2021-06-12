from django.db import models
import uuid
from .comment import Comment


class Reply(models.Model):
    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'

    id = models.UUIDField(unique=True, primary_key=True,
                          default=uuid.uuid4, editable=False)
    comment_id = models.ForeignKey(
        Comment, related_name='replies', on_delete=models.CASCADE)
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reply
