from django.urls import path
from .views import SportEventView

# URLConf
urlpatterns = [
    path('', SportEventView.as_view()),
]