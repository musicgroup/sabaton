from django.contrib import admin
from .models import Musician, Album, Track

admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Track)
# Register your models here.
