from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from . import views


urlpatterns = [
    path('query', views.query, name='query'),
    path('transcribe', views.transcribe, name='transcribe'),
    path('random', views.random_sentence, name='random')
]
