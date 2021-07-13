from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, blank=False)
    bio = models.TextField(null=True, blank=True)
    # fave_jobs = models.ManyToManyField('self', symmetrical=False)
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name + self.email
