from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
from django.db import models

from sportify.sports.constants import TIP_SPORT

sport_event = get_user_model()


class Sport(models.Model):
    sport_type = models.CharField(max_length=255, choices=TIP_SPORT,null=True)
    description = models.TextField()
