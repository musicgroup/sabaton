from django.urls import path
from .views import *

urlpatterns = [
    path('', participants, name='participants'),
]