import datetime

from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/participants")


class Photo(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    photo_id = models.IntegerField()


class Album(models.Model):
    title = models.CharField(max_length=50)
    tracks = models.IntegerField(default=0)
    release_date = models.DateField(default=datetime.date.today())
    photo = models.ImageField(upload_to="photos/albums")


class Track(models.Model):
    title = models.CharField(max_length=50)
    length = models.IntegerField()
    album = models.ForeignKey('Album', on_delete=models.PROTECT)
    audio_track = models.FileField(upload_to="songs/")
# Create your models here.
