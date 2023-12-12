from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class User(models.Model):
    username = models.CharField(max_length=255, unique=True) 
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}, {self.username}, {self.password}"
