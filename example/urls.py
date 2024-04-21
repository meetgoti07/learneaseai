# example/urls.py
from django.urls import path

from example.views import transcript_view


urlpatterns = [
    path('transcript/', transcript_view, name='transcript_view')
]