from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """CustomUserModel to be used for my api project"""
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
