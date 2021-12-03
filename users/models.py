from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from spotify.api import SpotifyAPI
from tracks.models import Track

from .helpers import merge_tracks_and_features

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    access_token = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    expires_in = models.IntegerField(blank=True, null=True)

    def refresh_tracks(self):
        tracks, features = SpotifyAPI(self.user).get_tracks_and_features()
        current_tracks = merge_tracks_and_features(tracks, features)

        current_track_ids = set([track["id"] for track in current_tracks])

        saved_tracks = Track.objects.filter(user=self.user)
        saved_track_ids = set([track.spotify_id for track in saved_tracks])

        added_tracks = current_track_ids.difference(saved_track_ids)
        removed_tracks = saved_track_ids.difference(current_track_ids)

        self.add_tracks_by_id(added_tracks, current_tracks)
        self.remove_tracks_by_id(removed_tracks)
    
    def add_tracks_by_id(self, track_ids, current_tracks):

        tracks_to_add = []

        for track in current_tracks:
            if track["id"] in track_ids:
                tracks_to_add.append(Track(
                    user = self.user,
                    spotify_id = track["id"],
                    title = track["name"],
                    artist = track["artist"],
                    album = track["album_name"],
                    album_image = track["album_image"],
                    popularity = track["popularity"],
                    danceability = track["danceability"],
                    energy = track["energy"],
                    key = track["key"],
                    loudness = track["loudness"],
                    mode = track["mode"],
                    speechiness = track["speechiness"],
                    acousticness = track["acousticness"],
                    instrumentalness = track["instrumentalness"],
                    liveness = track["liveness"],
                    valence = track["valence"],
                    tempo = track["tempo"],
                    duration_ms_y = track["duration_ms_y"],
                    time_signature = track["time_signature"],
                ))
        print(f"adding {len(tracks_to_add)}")
        Track.objects.bulk_create(tracks_to_add)


    def remove_tracks_by_id(self, track_ids):
        tracks_to_remove = Track.objects.filter(user=self.user, spotify_id__in=track_ids)
        print(f"removing {len(tracks_to_remove)}")
        tracks_to_remove.delete()




    


        


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
