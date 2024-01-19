from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.urls import reverse
import requests

from users.models import User

from sport_events.models import SportEvent

from .serializers import UserSerializer, UserAddSerializer, SportEventAddSerializer, SportEventSerializer

import logging

#User = get_user_model()


class UserListAPIView(generics.ListAPIView):
    """
    API view for listing users.
    It provides a list of User objects in response to GET requests.
    """
    #authentication_classes = [SessionAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific user.
    It allows clients to retrieve, update, and delete a single User object identified by its 'pk' (primary key).
    """
    #authentication_classes = [SessionAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


class GetUserAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific user by username.
    It allows clients to retrieve, update, and delete a single User object identified by its 'username'.
    """
    #authentication_classes = [SessionAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class AddUserAPI(generics.CreateAPIView):
    """
    API view for adding a new user.
    Allows clients to create a new User object.
    """
    #authentication_classes = [SessionAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserAddSerializer
    
class SportEventListAPIView(generics.ListAPIView):
    """
    API view for listing sport events.
    It provides a list of SportEvent objects in response to GET requests.
    """
    #authentication_classes = [SessionAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = SportEvent.objects.all()
    serializer_class = SportEventSerializer


class SportEventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific sport event.
    It allows clients to retrieve, update, and delete a single SportEvent object identified by its 'pk' (primary key).
    """
    #authentication_classes = [SessionAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = SportEvent.objects.all()
    serializer_class = SportEventSerializer
    lookup_field = 'pk'

class GetSportEventAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific sport event by username.
    It allows clients to retrieve, update, and delete a single SportEvent object identified by its 'host'.
    """
    #authentication_classes = [SessionAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = SportEvent.objects.all()
    serializer_class = SportEventSerializer
    lookup_field = 'host'


class AddSportEventAPI(generics.CreateAPIView):
    """
    API view for adding a new sport event.
    Allows clients to create a new SportEvent object.
    """
    #authentication_classes = [SessionAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = SportEvent.objects.all()
    serializer_class = SportEventAddSerializer

    def perform_create(self, serializer):
        # Get the username from the request data
        host = self.request.data.get('host', None)

        # Check if a user with the specified username exists
        user_url = reverse('GetUserAPI', kwargs={'username': host})
        user_response = requests.get(self.request.build_absolute_uri(user_url))

        if user_response.status_code != 200: 
            error_data = {'error': 'User with the specified username does not exist.', 'status_code': user_response.status_code}
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response({'success': 'SportEvent added successfully.'}, status=status.HTTP_201_CREATED)