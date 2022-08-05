from django.urls import path
from .views import main_page, about

urlpatterns = [
    path('', main_page, name='main_page'),
    path('about/', about, name='about'),
]
