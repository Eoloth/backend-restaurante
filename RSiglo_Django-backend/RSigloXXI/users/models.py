from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    category = models.CharField(max_length=20, default='no_profile')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    