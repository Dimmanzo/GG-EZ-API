from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('default_user', 'Default User'),
        ('staff_user', 'Staff User'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='default_user')
