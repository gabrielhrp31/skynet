from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ServiceForm
from .models import Service


def get_current(path):
    if path == '/services/':
        return 'Todos'
    if path == '/services/actives/':
        return 'Ativos'
    if path == '/services/inactives/':
        return 'Inativos'
    return ''


@login_required()
def list_contracts(request):
    return render(request, 'contracts/list.html', {'current': get_current(request.get_full_path())})


@login_required
def list_services(request):
    services = Service.objects.all()
    return render(request, 'services/list.html', {'services': services, 'current': get_current(request.get_full_path())})


@login_required
def list_services_actives(request):
    services = Service.objects.filter(status=True)
    return render(request, 'services/list.html', {'services': services, 'current': get_current(request.get_full_path())})

@login_required
def list_services_inactives(request):
    services = Service.objects.filter(status=False)
    return render(request, 'services/list.html', {'services': services, 'current': get_current(request.get_full_path())})


@login_required
def show_service(request, id):
    service = Service.objects.get(pk=id)
    return render(request, 'services/show.html', {'service': service})


@login_required
def new_service(request):
    form = ServiceForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        service = form.save()
        messages.add_message(request, messages.SUCCESS, 'O Serviço ' + service.get_name() + ' foi cadastrado com sucesso!', extra_tags='registred')

        return redirect('list_services')

    return render(request, 'services/new.html', {'form': form})


@login_required
def update_service(request, id):
    service = Service.objects.get(pk=id)
    form = ServiceForm(request.POST or None, request.FILES or None, instance=service)

    if form.is_valid():
        service = form.save()
        messages.add_message(request, messages.SUCCESS, 'O Serviço ' + service.get_name() + ' foi cadastrado com sucesso!', extra_tags='registred')
        return redirect('list_services')

    return render(request, 'services/update.html', {'form': form})


@login_required
def change_status(request, id):
    service = get_object_or_404(Service, pk=id)
    service.change_status()
    messages.add_message(request, messages.INFO, 'O status do serviço '+service.name+' foi alterado!', extra_tags='status')
    return redirect('list_services')


@login_required
def delete_service(request, id):
    service = get_object_or_404(Service, pk=id)
    service.delete()
    messages.add_message(request, messages.SUCCESS, 'O serviço '+service.name+' foi deletado com sucesso!', extra_tags='deleted')
    return redirect('list_services')
