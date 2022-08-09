from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Musician
menu = ['Основная информация', 'Участники группы', 'Альбомы', 'Треки', 'Галерея', 'Разработчики сайта']


def main_page(request):

    # print(posts)
    # return HttpResponse('Главная страница приложения main')
    return render(request, 'main\index.html', {'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'main\\about.html', {'title': 'О сайте', 'header': 'Страница about'})


def participants(request):
    posts = Musician.objects.all()
    return render(request, 'participants/list_of_part.html', {'posts': posts, 'title': 'Текущие участники группы'})


def musician(request, pk):
    if pk >= len(Musician.objects.all()):
        return HttpResponseNotFound('<h1>Такого участника в группе нет ):</h1>')
    mus = Musician.objects.filter(pk=pk)
    return render(request, 'participants/musician.html', {'mus': mus[0]})


def albums(request):
    return HttpResponse('<h1>Страница с альбомами</h1>')


def album(request, pk):
    return HttpResponse(f'<h1>Альбом: {pk}</h1>')


def tracks(request):
    return HttpResponse('<h1>Страница с трэками</h1>')


def track(request, pk):
    return HttpResponse(f'<h1>Трэк: {pk}</h1>')


def gallery(request):
    return HttpResponse('<h1>Фотографии</h1>')
