from django.shortcuts import render
from django.http import HttpResponse


def participants(request):
    return HttpResponse('Здесь представлены все музыканты: ')


# Create your views here.
