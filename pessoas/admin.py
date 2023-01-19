from django.contrib import admin
from .models import Pessoa, Mensagem

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'fonte', 'provincia', 'comune', 'chegada_ao_brasil', 'local_de_chegada', 'data_insercao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'fonte', 'provincia', 'comune', 'local_de_chegada')
    list_filter = ('id', 'nome', 'fonte', 'provincia', 'comune', 'chegada_ao_brasil', 'local_de_chegada', 'data_insercao')
    list_per_page = 20

class ListandoMensagens(admin.ModelAdmin):
    list_display = ('id', 'email', 'nome', 'assunto')
    list_display_links = ('id', 'email')
    search_fields = ('email', 'nome', 'assunto')
    list_filter = ('email', 'nome', 'assunto')
    list_per_page = 20

admin.site.register(Pessoa, ListandoPessoas)
admin.site.register(Mensagem, ListandoMensagens)
