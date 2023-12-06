from django.urls import path
from .views import SportEventView
from . import views

# URLConf
urlpatterns = [
    path('', SportEventView.as_view()),
    path('sport_events/', views.sport_events),
]
