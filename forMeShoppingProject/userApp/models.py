from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    length = models.IntegerField(null=True, blank=True)
    shoulder = models.IntegerField(null=True, blank=True)
    chest = models.IntegerField(null=True, blank=True)
    sleeve = models.IntegerField(null=True, blank=True)
    waist = models.IntegerField(null=True, blank=True)
    rise = models.IntegerField(null=True, blank=True)
    hem = models.IntegerField(null=True, blank=True)
