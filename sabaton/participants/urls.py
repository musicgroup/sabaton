from django.urls import path
from .views import *

urlpatterns = [
    path('', participants, name='participants'),
    path('<int:pk>/', musician, name='musician')
]