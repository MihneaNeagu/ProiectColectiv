from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from users.models import User

from .serializers import UserSerializer, UserAddSerializer

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
