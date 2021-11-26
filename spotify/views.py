import requests
from django.conf import settings
from django.shortcuts import redirect
from base64 import b64encode
from django.http import HttpResponse

client_id = settings.SPOTIFY_CLIENT_ID
client_secret = settings.SPOTIFY_CLIENT_SECRET
response_type = "code"
redirect_uri = "http://localhost:8000/spotify/callback"
scopes = "user-library-read"

def authorize(request):
    return redirect(f"https://accounts.spotify.com/authorize?response_type={response_type}&client_id={client_id}&scope={scopes}&redirect_uri={redirect_uri}" )

def callback(request):
    code = request.GET["code"]
    authorization_string = b64encode(f"{client_id}:{client_secret}".encode())

    response = requests.post('https://accounts.spotify.com/api/token', data={
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":redirect_uri
    }, headers={
        "Authorization": f"Basic {authorization_string.decode()}",
    })

    return HttpResponse("Yahoo!")

