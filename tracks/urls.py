from django.urls import path
from . import views

urlpatterns = [
    path("", views.TracksList.as_view()),
]
