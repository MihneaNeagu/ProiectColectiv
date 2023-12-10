from django.urls import path
from .views import UserListAPIView, UserDetailAPIView, GetUserAPI
from . import views


urlpatterns = [
    path('users', UserListAPIView.as_view()),
    path('users', views.allUsers),
    path('create-users', UserDetailAPIView.as_view()),
    path('get-users', GetUserAPI.as_view())
]
