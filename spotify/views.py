import requests
from django.conf import settings
from django.shortcuts import redirect
from base64 import b64encode
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
import webbrowser
from rest_framework.response import Response
from rest_framework import status
import json

client_id = settings.SPOTIFY_CLIENT_ID
client_secret = settings.SPOTIFY_CLIENT_SECRET
response_type = "code"
redirect_uri = "http://localhost:8000/spotify/callback"
scopes = "user-library-read"


class SpotifyAuthorize(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        state = request.query_params["token"]
        url = (
            f"https://accounts.spotify.com/authorize?response_type={response_type}&client_id={client_id}&scope={scopes}&redirect_uri={redirect_uri}&state={state}",
        )
        return Response(url, status=status.HTTP_200_OK)


class SpotifyCallback(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        code = request.GET["code"]

        authorization_string = b64encode(f"{client_id}:{client_secret}".encode())

        response = requests.post(
            "https://accounts.spotify.com/api/token",
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": redirect_uri,
            },
            headers={
                "Authorization": f"Basic {authorization_string.decode()}",
            },
        )

        data = json.loads(response.content)

        token = request.GET["state"]
        user = Token.objects.get(key=token).user

        user.profile.access_token = data["access_token"]
        user.profile.refresh_token = data["refresh_token"]
        user.profile.expires_in = data["expires_in"]
        user.profile.save()

        return redirect("http://localhost:3000/")
