import datetime

from django.db import models


class Musician(models.Model):
    """Class, which is representing member of music band"""
    class Meta:
        verbose_name = "Музыкант"
        verbose_name_plural = "Музыканты"

    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    """Class, which is representing one photo from Gallery chapter on a site"""

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    height = models.IntegerField()
    width = models.IntegerField()
    photo_id = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


class Track(models.Model):
    """Class, representing one Song - part of Album"""
    class Meta:
        verbose_name = "Трэк"
        verbose_name_plural = "Трэки"

    length = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


class Album(models.Model):
    """Class, representing one album from Album's page on a site"""

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    title = models.CharField(max_length=50, default="album")
    tracks = models.IntegerField(default=0)
    release_date = models.DateField(default=datetime.date.today())
    photo = models.ImageField(upload_to="photos/albums", default=0)
