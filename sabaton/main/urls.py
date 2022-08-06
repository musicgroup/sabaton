from django.urls import path
from .views import main_page, about

urlpatterns = [
    path('', main_page, name='main_page'),
    path('about/', about, name='about'),
    path('participants/', participants, name='participants'),
    path('participants/<int:pk>/', musician, name='musician'),
    path('albums/', albums, name='albums'),
    path('albums/<int:pk>/', album, name='album'),
    path('tracks/', tracks, name='tracks'),
    path('tracks/<int:pk>', track, name='track'),
    path('photos/', gallery, name='gallery'),
]
