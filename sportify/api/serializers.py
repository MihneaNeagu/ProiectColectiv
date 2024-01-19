from rest_framework import serializers

from users.models import User
from sport_events.models import SportEvent

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'phoneNumber')

class UserAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'phoneNumber')
        
class SportEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportEvent
        fields = ('id', 'host', 'sport_type', 'date', 'ora', 'locatie', 'status', 'limit_capacity')


class SportEventAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportEvent
        fields = ('host', 'sport_type', 'date', 'ora', 'locatie', 'status', 'limit_capacity')
