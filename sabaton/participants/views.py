from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Musician


def participants(request):
    posts = Musician.objects.all()
    return render(request, 'participants/list_of_part.html', {'posts': posts, 'title': 'Текущие участники группы'})


def musician(request, pk):
    if pk >= len(Musician.objects.all()):
        return HttpResponseNotFound('<h1>Такого участника в группе нет ):</h1>')
    mus = Musician.objects.filter(pk=pk)
    return render(request, 'participants/musician.html', {'mus': mus[0]})

# Create your views here.
