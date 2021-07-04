from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
import uuid


class Manager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    DEFAULT_AVATAR = 'https://res.cloudinary.com/devsprime/image/upload/v1625394926/Icons%20and%20Logo/user_ooaqks.png'

    username = None
    id = models.UUIDField(unique=True, primary_key=True,
                          default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    mobile_number = models.CharField(max_length=50)
    avatar = models.URLField(default=DEFAULT_AVATAR)
    otp_code = models.CharField(max_length=100, null=True)
    email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_learner = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = Manager()

    def __str__(self):
        return self.email
