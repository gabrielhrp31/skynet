from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'dashboard/index.html')


def hello(request):
    return HttpResponse('Olá mundo')


def helloName(request, name=''):
    return render(request, 'pessoa.html', {'name': name})
