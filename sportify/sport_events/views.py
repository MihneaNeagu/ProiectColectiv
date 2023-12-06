from django.shortcuts import render
from rest_framework import generics
from .models import SportEvent
from .serializers import SportEventSerializer

# Create your views here.


def sport_events(request):
    # users = User.objects.all()
    context = {
        "sport_events": SportEvent.objects.all()
    }
    return render(request, "sport_events.html", context)


class SportEventView(generics.CreateAPIView):
    serializer_class = SportEventSerializer
