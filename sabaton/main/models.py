import datetime

from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    photo_id = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


class Track(models.Model):
    length = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


class Album(models.Model):
    title = models.CharField(max_length=50, default="album")
    tracks = models.IntegerField(default=0)
    release_date = models.DateField(default=datetime.date.today())
    photo = models.ImageField(upload_to="photos/albums", default=0)
# Create your models here.
