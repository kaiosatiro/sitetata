from django.shortcuts import render, redirect
from .models import Mensagem, Pessoa
from django.contrib import messages


def index(request):
    contexto = {
        'segmento': 'index'
    }
    return render(request, 'index.html', contexto)


def busca(request):
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar'].strip()
        if nome_a_buscar == '':
            return redirect('busca')

        lista = Pessoa.objects.filter(nome__icontains=nome_a_buscar).order_by('-nome')

        contexto = {
        'segmento': 'busca',
        'pessoas': lista,
        'total': lista.count(),
        'indice': 1
        }
        return render(request, 'busca.html', contexto)

    else:
        contexto = {
        'segmento': 'busca',
    }
        return render(request, 'busca.html', contexto)


def contato(request):
    contexto = {
        'segmento': 'contato'
    }
    if request.method == 'POST':
        n = request.POST['nome']
        e = request.POST['email']
        a = request.POST['assunto']
        m = request.POST['mensagem']
        
        obj = Mensagem.objects.create(nome=n, email=e, assunto=a, mensagem=m)
        obj.save()
        messages.success(request, 'Mensagem enviada')
        return redirect('contato')
    else:    
        return render(request, 'contato.html', contexto)


def servicos(request):
    contexto = {
        'segmento': 'servicos'
    }
    return render(request, 'servicos.html', contexto)


def sobre(request):
    contexto = {
        'segmento': 'sobre'
    }
    return render(request, 'sobre.html', contexto)