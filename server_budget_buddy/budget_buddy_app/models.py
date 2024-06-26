from django.db import models
from django.contrib.auth.models import AbstractUser


# Overwride the Djangos default model and added abstration of newly added fields
class User(AbstractUser):
    # name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
