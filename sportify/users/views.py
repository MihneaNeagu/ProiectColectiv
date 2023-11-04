from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

#Base model

class User(models.Model):
    username = models.CharField(max_length=255)

# Create your views here.
