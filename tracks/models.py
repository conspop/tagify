from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spotify_id = models.TextField()
    title = models.TextField()
    artist = models.TextField()
    album = models.TextField()
    album_image = models.TextField()
    popularity = models.IntegerField()
    danceability = models.DecimalField(max_digits=10,decimal_places=3)
    energy = models.DecimalField(max_digits=10,decimal_places=3)
    key = models.IntegerField()
    loudness = models.DecimalField(max_digits=10,decimal_places=3)
    mode = models.IntegerField()
    speechiness = models.DecimalField(max_digits=10,decimal_places=3)
    acousticness = models.DecimalField(max_digits=10,decimal_places=3)
    instrumentalness = models.DecimalField(max_digits=10,decimal_places=3)
    liveness = models.DecimalField(max_digits=10,decimal_places=3)
    valence = models.DecimalField(max_digits=10,decimal_places=3)
    tempo = models.DecimalField(max_digits=10,decimal_places=3)
    duration_ms_y = models.IntegerField()
    time_signature = models.IntegerField()
