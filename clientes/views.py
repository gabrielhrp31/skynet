from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

from .models import Client
from .forms import ClientForm
from .forms import AddressForm


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
    form_client = ClientForm(request.POST or None, request.FILES or None)
    form_address = AddressForm(request.POST or None, request.FILES or None)

    if form_client.is_valid() and form_address.is_valid():
        client = form_client.save()
        address = form_address.save()
        client.address_id = address.id
        client.save()
        messages.add_message(request, messages.SUCCESS, 'O usuário ' + client.full_name() + ' foi cadastrado com sucesso!', extra_tags='registred')

        return redirect('list_clients')

    return render(request, 'new.html', {'form': form_client, 'form_adress': form_address})


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
    deleted = person
    person.delete()
    messages.add_message(request, messages.SUCCESS, 'O usuário '+deleted.full_name()+' não será mais listado nas relações de clientes!', extra_tags='deleted')
    return redirect('list_clients')


@login_required
def change_status(request, id):
    person = get_object_or_404(Client, pk=id)
    person.change_status()
    messages.add_message(request, messages.INFO, 'O status do usuário '+person.full_name()+' foi alterado!', extra_tags='status')
    return redirect('list_clients')


@login_required
def show_client(request, id):
    person = get_object_or_404(Client, pk=id)
    return render(request, 'show.html', {'person': person})


def logout_user(request):
    logout(request)
    return redirect('login')

