from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('busca', busca, name='busca'),
    path('contato', contato, name='contato'),
    path('servicos', servicos, name='servicos'),
    path('sobre', sobre, name='sobre'),
]