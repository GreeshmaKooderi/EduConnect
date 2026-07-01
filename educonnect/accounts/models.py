from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    USER_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_CHOICES
    )