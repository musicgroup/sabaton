from django.conf.urls.static import static
from django.urls import path

from sabaton import settings
from .views import main_page,participants, albums, gallery, album, participant, about, photo

urlpatterns = [
    path('', main_page, name='main_page'),
    path('participants/', participants, name='participants'),
    path('participants/<int:pk>/', participant, name='participant'),
    path('albums/', albums, name='albums'),
    path('albums/<int:pk>/', album, name='album'),
    path('gallery/', gallery, name='gallery'),
    path('about/', about, name='about'),
    path('gallery/<int:pk>', photo, name='photo')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
