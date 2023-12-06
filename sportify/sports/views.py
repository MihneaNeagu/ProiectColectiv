from django.shortcuts import render
from rest_framework import generics
from .models import Sport
from .serializers import SportSerializer

# Create your views here.
class SportEventView(generics.CreateAPIView):
    def sport(request):
        sport = Sport.objects.all()
        return render(request, 'sportify/sports/templates/sports.html', {'sports': sport})
    serializer_class = SportSerializer

def sports(request):
    sports = Sport.objects.all()
    return render(request, 'sportsapp/sports.html', {'sports':sports})
