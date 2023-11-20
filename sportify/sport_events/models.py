from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
from django.db import models
from .constants import TIP_SPORT
sport_event = get_user_model()


class SportEvent(models.Model):
    sport_type = models.CharField(max_length=255, choices=TIP_SPORT, null=True)
    date = models.DateField(null=True)
    ora = models.TimeField(null=True)
    locatie = models.CharField(max_length=255, null=True)
    status = models.BooleanField(default=False, null=True)
    limit_capacity = models.IntegerField(null=True)