from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=500)
    fonte = models.CharField(max_length=200, blank=True)
    provincia = models.CharField(max_length=200, blank=True)
    comune = models.CharField(max_length=200, blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    paternidade = models.CharField(max_length=200, blank=True)
    conjuge = models.CharField(max_length=200, blank=True)
    data_casamento = models.DateField(blank=True, null=True)
    matrimonio = models.CharField(max_length=200, blank=True)
    chegada_ao_brasil = models.DateField(blank=True, null=True)
    local_de_chegada = models.CharField(max_length=200, blank=True)
    data_insercao = models.DateTimeField(default=datetime.now, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Mensagem(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField()

    def __str__(self):
        return self.email

