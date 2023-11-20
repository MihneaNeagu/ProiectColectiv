from django.urls import path
from .views import UserListView

# URLConf
urlpatterns = [
    path('', UserListView.as_view())
]