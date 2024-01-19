from django.urls import path
from .views import UserListAPIView, UserDetailAPIView, GetUserAPI, AddUserAPI, SportEventListAPIView, GetSportEventAPI, SportEventDetailAPIView, AddSportEventAPI

from . import views

urlpatterns = [
    path('users', UserListAPIView.as_view()),
    path('users/<int:pk>', UserDetailAPIView.as_view()),
    path('users/<str:username>', GetUserAPI.as_view(), name='GetUserAPI'),
    path('usersAdd', AddUserAPI.as_view(), name='add_user'),
    path('sport_events', SportEventListAPIView.as_view()),
    path('sport_events/<int:pk>', SportEventDetailAPIView.as_view()),
    path('sport_events/<str:username>', GetSportEventAPI.as_view()),
    path('sportEventAdd', AddSportEventAPI.as_view(), name='add_sport_event')
]
