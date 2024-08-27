from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name="Phone")
    city = models.CharField(max_length=100, verbose_name="City")
    image = models.ImageField(upload_to="users/", null=True, verbose_name="Image")
