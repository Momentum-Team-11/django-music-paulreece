from django.db import models
from datetime import datetime


class Artist(models.Model):
    artist = models.CharField(max_length=200)


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=datetime.now)
    favorite = models.CharField(max_length=1, null=True, blank=True)
    the_artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, null=True, related_name="albums")
