from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about/', views.about, name='about'),
    path('participants/', views.participants, name='participants'),
    path('participants/<int:pk>/', views.musician, name='musician'),
    path('albums/', views.albums, name='albums'),
    path('albums/<int:pk>/', views.album, name='album'),
    path('tracks/', views.tracks, name='tracks'),
    path('tracks/<int:pk>', views.track, name='track'),
    path('photos/', views.gallery, name='gallery'),
]
