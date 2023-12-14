from django.urls import path
from .views import UserListAPIView, UserDetailAPIView, GetUserAPI, AddUserAPI
from . import views

urlpatterns = [
    path('users', UserListAPIView.as_view()),
    path('users/<int:pk>', UserDetailAPIView.as_view()),
    path('users/<str:username>', GetUserAPI.as_view()),
    path('usersAdd', AddUserAPI.as_view(), name='add_user')
]
