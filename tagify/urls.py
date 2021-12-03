from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("spotify/", include("spotify.urls")),
    path("users/", include("users.urls")),
    url(r"^auth/", include("djoser.urls")),
    url(r"^auth/", include("djoser.urls.authtoken")),
]
