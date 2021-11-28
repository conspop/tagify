from django.conf import settings
from django.shortcuts import redirect

client_id = settings.SPOTIFY_CLIENT_ID
response_type = "code"
redirect_uri = "http://localhost:8000/spotify/callback"
scopes = "user-library-read"


def authorize_user():
    payload = {
        "response_type": response_type,
        "client_id": client_id,
        "scope": scopes,
        "redirect_uri": redirect_uri,
    }
    redirect("https://accounts.spotify.com/authorize?", **payload)
