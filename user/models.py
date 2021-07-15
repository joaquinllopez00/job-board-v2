from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, blank=False)
    bio = models.TextField(null=True, blank=True)
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
