from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return redirect('login')


def hello(request):
    return HttpResponse('Olá mundo')


def helloName(request, name=''):
    return render(request, 'pessoa.html', {'name': name})
