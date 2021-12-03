from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("authorize", views.SpotifyAuthorize.as_view()),
    path("callback", views.SpotifyCallback.as_view()),
]
