from django.db import models
from .user import User
from django.utils.translation import ugettext_lazy as _
import uuid


class LearnerProfile(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    account_name = models.CharField(_('account name'), max_length=225, null=True)
    account_number = models.CharField(_('account number'), max_length=225, null=True)
    bank_name = models.CharField(_('bank name'), max_length=225, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id
