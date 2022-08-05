from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician


def participants(request):
    posts = Musician.objects.all()
    return render(request, 'participants/list_of_part.html', {'posts': posts, 'title': 'Текущие участники группы'})


# Create your views here.
