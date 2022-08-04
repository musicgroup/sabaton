from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def main_page(request):
    print(type(request))
    return HttpResponse('Главная страница приложения main')


# Create your views here.
