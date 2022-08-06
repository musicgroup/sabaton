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

# Create your models here.
