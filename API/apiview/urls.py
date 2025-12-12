from django.urls import path
from .views import get_users


urlpatterns = [
    path('GET/',get_users, name= 'users')
]