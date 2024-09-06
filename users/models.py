from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=30, blank=True)
    surname = models.CharField(max_length=30, blank=True)
    username = models.CharField(unique=True, max_length=50, blank=True)
    email = models.EmailField(unique=True)
    address = models.TextField(null=True, blank=True)
