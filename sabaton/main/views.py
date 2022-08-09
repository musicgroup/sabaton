from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Musician

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
    return render(request, 'main\\temp.html', {'menu': menu, 'title': 'Альбомы', 'header': 'Страница albums'})

def songs(request):
    return render(request, 'main\\temp.html', {'menu': menu, 'title': 'Треки', 'header': 'Страница songs'})

def gallery(request):
    return render(request, 'main\\temp.html', {'menu': menu, 'title': 'Галерея', 'header': 'Страница gallery'})

def developers(request):
    return render(request, 'main\\temp.html', {'menu': menu, 'title': 'Разработчики', 'header': 'Страница developers'})



# def participants(request):
#     posts = Musician.objects.all()
#     return render(request, 'participants/list_of_part.html', {'posts': posts, 'title': 'Текущие участники группы'})
#
#
# def musician(request, pk):
#     if pk >= len(Musician.objects.all()):
#         return HttpResponseNotFound('<h1>Такого участника в группе нет ):</h1>')
#     mus = Musician.objects.filter(pk=pk)
#     return render(request, 'participants/musician.html', {'mus': mus[0]})
