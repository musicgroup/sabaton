from django.contrib import admin
from . import models

# simple registration of models

admin.site.register(models.Musician)
admin.site.register(models.Track)
admin.site.register(models.Album)
admin.site.register(models.Photo)

