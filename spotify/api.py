from django.conf import settings
import requests
import json


class SpotifyToken:
    pass


class SpotifyAPI:
    def __init__(self, user):
        self.base_url = "https://api.spotify.com/v1"
        self.headers = {"Authorization": f"Bearer {user.profile.access_token}"}

    def get_tracks_and_features(self):
        tracks = self.get_tracks()
        features = self.get_features(tracks)

        return (tracks, features)

    def get_tracks(self):

        items = []

        next = f"{self.base_url}/me/tracks?limit=50"
        while next:
            response = requests.get(next, headers=self.headers).json()
            items += response["items"]
            next = response["next"]

        return [item["track"] for item in items]
        
    def get_features(self, tracks):
        ids = [track["id"] for track in tracks]

        features = []
        number_of_tracks = len(tracks)
        counter = 0
        while counter < number_of_tracks:
            if number_of_tracks - counter >= 100:
                chunk = ids[counter : counter + 100]
            else:
                chunk = ids[counter:]
            response = requests.get(
                f"https://api.spotify.com/v1/audio-features?ids={','.join(chunk)}",
                headers=self.headers,
            ).json()["audio_features"]
            features += response
            counter += 100
        
        return features
        
