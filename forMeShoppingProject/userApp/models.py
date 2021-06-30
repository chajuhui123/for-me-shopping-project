from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
