from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Participant, Album, Track

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
                  {'menu': menu, 'title': 'Участники', 'header': 'Страница participants',
                   'participants': all_participants})


def participant(request, pk):
    current_participant = Participant.objects.get(pk=pk)
    return render(request, 'main\\participant.html',
                  {'menu': menu, 'title': 'Участники', 'header': 'Страница participants',
                   'participant': current_participant})


def albums(request):
    all_albums = Album.objects.all().order_by("release_date")
    return render(request, 'main\\albums.html',
                  {'menu': menu, 'title': 'Альбомы', 'header': 'Страница albums', 'albums': all_albums})


def album(request, pk):
    current_album = Album.objects.get(pk=pk)
    tracks = Track.objects.filter(album_id=pk)
    return render(request, 'main\\album.html',
                  {'menu': menu, 'title': current_album.title, 'header': 'Страница albums', 'tracks': tracks,
                   'album': current_album})


def about(request):
    band_info = Participant.objects.filter(name='Sabaton').first()
    print(band_info.name)
    return render(request, 'main\\about.html',
                  {'menu': menu, 'title': "О группе", 'header': "О группе", 'band': band_info})

def gallery(request):
    return render(request, 'main\\temp.html', {'menu': menu, 'title': 'Галерея', 'header': 'Страница gallery'})
