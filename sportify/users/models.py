from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class User(models.Model):
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
