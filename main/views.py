from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Participant, Album, Track, Photo

menu = [{'title': 'Участники группы',
         'url_name': "participants"},
        {'title': 'Альбомы',
         'url_name': "albums"},
        {'title': 'Галерея',
         'url_name': "gallery"},
        {'title': 'О группе',
         'url_name': 'about'}
        ]


def main_page(request):
    # print(posts)
    # return HttpResponse('Главная страница приложения main')
    return render(request, 'main\index.html', {'menu': menu, 'title': 'Главная страница'})


def participants(request):
    all_participants = Participant.objects.all().exclude(name='Sabaton')
    return render(request, 'main\\participants.html',
                  {'menu': menu, 'title': 'Участники',
                   'participants': all_participants})


def participant(request, pk):
    current_participant = Participant.objects.get(pk=pk)
    return render(request, 'main\\participant.html',
                  {'menu': menu, 'title': 'Участники',
                   'participant': current_participant})


def albums(request):
    all_albums = Album.objects.all().order_by("release_date")
    return render(request, 'main\\albums.html',
                  {'menu': menu, 'title': 'Альбомы', 'albums': all_albums})


def album(request, pk):
    current_album = Album.objects.get(pk=pk)
    tracks = Track.objects.filter(album_id=pk)
    return render(request, 'main\\album.html',
                  {'menu': menu, 'title': current_album.title, 'tracks': tracks,
                   'album': current_album})


def about(request):
    band_info = Participant.objects.filter(name='Sabaton').first()
    print(band_info.name)
    return render(request, 'main\\about.html',
                  {'menu': menu, 'title': "О группе", 'band': band_info})


def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'main\\gallery.html', {'menu': menu, 'title': 'Галерея', 'photos': photos})


def photo(request, pk):
    current_photo = Photo.objects.get(pk=pk)
    print(current_photo.photo_name)
    return render(request, 'main\\photo.html',
                  {'menu': menu, 'title': current_photo.photo_name, 'photo': current_photo})
