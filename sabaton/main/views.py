from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from participants.models import Musician
menu = ['Основная информация', 'Участники группы', 'Альбомы', 'Треки', 'Галерея', 'Разработчики сайта']


def main_page(request):

    # print(posts)
    # return HttpResponse('Главная страница приложения main')
    return render(request, 'main\index.html', {'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'main\\about.html', {'title': 'О сайте', 'header': 'Страница about'})
# Create your views here.
