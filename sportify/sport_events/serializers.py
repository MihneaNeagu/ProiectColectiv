from rest_framework import serializers
from .models import SportEvent

class SportEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportEvent
        fields = ('id', 'sport_type', 'date', 'ora', 'locatie', 'status', 'limit_capacity')
