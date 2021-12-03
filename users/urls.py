from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views as auth_views
from . import views

urlpatterns = [
    path("api-token-auth/", auth_views.obtain_auth_token),
    path("refresh-songs/", views.RefreshSongs.as_view()),
]
