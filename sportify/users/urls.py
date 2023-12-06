from django.urls import path
#from .views import UserListView
from . import views

# URLConf
urlpatterns = [
    #path('', UserListView.as_view()),
    path('user/', views.allUsers)
]