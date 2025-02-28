#from django.http import HttpResponse

from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Hello world!")
    nome = "Rodrigo"
    pessoa = {
        'nome': 'Maria',
        'idade': 30,
        'cidade': 'São Paulo'
    }
    return render(request, 'home.html',  {'nome': nome, 'pessoa': pessoa})

def about(request):
    #return HttpResponse("about me")
    frutas = ['maça', 'Banana', 'Laranja', 'Uva']
    return render(request, 'about.html', {'frutas': frutas})