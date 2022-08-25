from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Musician, Album

menu = [{'title': 'Основная информация',
         'url_name': "about"},
        {'title': 'Участники группы',
         'url_name': "participants"},
        {'title': 'Альбомы',
         'url_name': "albums"},
        {'title': 'Треки',
         'url_name': "songs"},
        {'title': 'Галерея',
         'url_name': "gallery"},
        {'title': 'Разработчики сайта',
         'url_name': "developers"}
        ]


def main_page(request):
    # print(posts)
    # return HttpResponse('Главная страница приложения main')
    return render(request, 'main\index.html', {'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'main\\about.html', {'menu': menu, 'title': 'О сайте', 'header': 'Страница about'})

def participants(request):
    return render(request, 'main\\temp.html', {'menu': menu, 'title': 'Участники', 'header': 'Страница participants'})

def albums(request):
    albums = Album.objects.all().order_by("release_date")
    return render(request, 'main\\albums.html', {'menu': menu, 'title': 'Альбомы', 'header': 'Страница albums', 'albums': albums})

def songs(request):
    return render(request, 'main\\temp.html', {'menu': menu, 'title': 'Треки', 'header': 'Страница songs'})

def gallery(request):
    return render(request, 'main\\temp.html', {'menu': menu, 'title': 'Галерея', 'header': 'Страница gallery'})

def developers(request):
    return render(request, 'main\\temp.html', {'menu': menu, 'title': 'Разработчики', 'header': 'Страница developers'})

