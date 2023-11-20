from django.shortcuts import render
from rest_framework import generics
from .models import SportEvent
from .serializers import SportEventSerializer

# Create your views here.

class SportEventView(generics.CreateAPIView):
    queryset = SportEvent.objects.all
    serializer_class = SportEventSerializer
