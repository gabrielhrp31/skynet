from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Client
from .forms import ClientForm
# Create your views here.


def getCurrent(path):
    if path == '/clients/':
        return 'Todos'
    if path == '/clients/actives/':
        return 'Ativos'
    if path == '/clients/inactives/':
        return 'Inativos'
    return ''


@login_required
def list_clients_actives(request):
    persons = Client.objects.filter(status=True)
    return render(request, 'list.html', {'persons': persons, 'current': getCurrent(request.get_full_path())})


@login_required
def list_clients_inactives(request):
    persons = Client.objects.filter(status=False)
    return render(request, 'list.html', {'persons': persons, 'current': getCurrent(request.get_full_path())})


@login_required
def list_clients(request):
    persons = Client.objects.all()
    return render(request, 'list.html', {'persons': persons, 'current': getCurrent(request.get_full_path())})


@login_required
def new_client(request):
    form = ClientForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_clients')

    return render(request, 'new.html', {'form': form})


@login_required
def update_client(request, id):
    person = get_object_or_404(Client, pk=id)
    form = ClientForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('list_clients')
    return render(request, 'update.html', {'form': form})


@login_required
def delete_client(request, id):
    person = get_object_or_404(Client, pk=id)
    form = ClientForm(request.POST or None, request.FILES or None, instance=person)
    person.delete()
    return redirect('list_clients')


@login_required
def show_client(request, id):
    person = get_object_or_404(Client, pk=id)
    return render(request, 'show.html', {'person': person})


def logout_user(request):
    logout(request)
    return redirect('login')

