from django.conf.urls.static import static
from django.urls import path

from sabaton import settings
from .views import main_page, about, participants, albums, songs, gallery, developers, album

urlpatterns = [
    path('', main_page, name='main_page'),
    path('about/', about, name='about'),
    path('participants/', participants, name='participants'),
    # path('participants/<int:pk>/', musician, name='musician'),
    path('albums/', albums, name='albums'),
    path('albums/<int:pk>/', album, name='album'),
    path('tracks/', songs, name='songs'),
    # path('tracks/<int:pk>', track, name='track'),
    path('gallery/', gallery, name='gallery'),
    path('developers/', developers, name='developers'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
