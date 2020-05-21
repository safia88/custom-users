from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


class Customuser(AbstractUser):
    Homepage = models.URLField(null=True)
    Display_name = models.CharField(max_length=100, null=True)
    Age = models.IntegerField(null=True)
