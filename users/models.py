from django.db import models


class Profile(models.Model):
    access_token = models.TextField()
    refresh_token = models.TextField()

