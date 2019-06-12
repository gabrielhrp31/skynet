from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from services.forms import ContractForm
from .forms import ServiceForm
from .models import Service
from .models import Contract


def get_current(path):
    if path == '/services/':
        return 'Todos'
    if path == '/services/actives/':
        return 'Ativos'
    if path == '/services/inactives/':
        return 'Inativos'
    return ''


def get_current_contracts(path):
    if path == '/services/contracts/':
        return 'Todos'
    if path == '/services/contracts/in_progress/':
        return 'Em Progresso'
    if path == '/services/contracts/finished/':
        return 'Finalizados'
    return ''


@login_required()
def list_contracts(request):
    contracts = Contract.objects.all()
    return render(request, 'contracts/list.html', {'contracts': contracts, 'current': get_current_contracts(request.get_full_path())})


@login_required()
def list_contracts_in_progress(request):
    contracts = Contract.objects.filter(end_date__gte=datetime.now(), start_date__lte=datetime.now())
    return render(request, 'contracts/list.html', {'contracts': contracts, 'current': get_current_contracts(request.get_full_path())})


@login_required()
def list_contracts_finished(request):
    contracts = Contract.objects.filter(end_date__lte=datetime.now())
    return render(request, 'contracts/list.html', {'contracts': contracts, 'current': get_current_contracts(request.get_full_path())})


@login_required()
def new_contract(request):
    form = ContractForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        contract = form.save()
        messages.add_message(request, messages.SUCCESS, 'Um '+contract.get_contract_title()+' foi resgitrado com sucesso!', extra_tags='registred')
        return redirect('list_contracts')
    return render(request, 'contracts/new.html', {'form': form})


@login_required
def show_contract(request, id):
    contract = Contract.objects.get(pk=id)
    contracts_finished = Contract.objects.filter(end_date__lte=datetime.now())
    renewable = False
    if contract.end_date.__lt__(datetime.utcnow()):
        renewable = True
    if request.method == 'POST' and renewable:
        renew_for = request.POST['renew_for']
        if renew_for != '':
            renew_for = int(renew_for)
            renew_type = request.POST['renew_type']
            renew_types = {'Meses': 30, 'Dias': 1, 'Anos': 365}
            renew_total = renew_for * renew_types[renew_type]
            contract.renew(renew_total, request)
            messages.add_message(request, messages.SUCCESS, 'Contrato renovado com sucesso para '+str(renew_for) + ' ' + renew_type + '!', extra_tags='renewed')
        else:
            messages.add_message(request, messages.ERROR, 'Erro ao renovar contrato! Digite uma quantidade', extra_tags='renewed')
        redirect('show_contract', 2)
    return render(request, 'contracts/show.html', {'contract': contract, 'renewable': renewable})


@login_required
def update_contract(request, id):
    contract = Contract.objects.get(pk=id)
    form = ContractForm(request.POST or None, request.FILES or None, instance=contract)

    if form.is_valid():
        contract = form.save()
        messages.add_message(request, messages.SUCCESS, 'Um ' + contract.get_contract_title() + ' foi atualizado com sucesso!', extra_tags='updated')
        return redirect('list_contracts')

    return render(request, 'contracts/update.html', {'form': form})


@login_required
def delete_contract(request, id):
    contract = get_object_or_404(Contract, pk=id)
    contract.delete()
    messages.add_message(request, messages.SUCCESS, 'Um '+contract.get_contract_title()+' foi deletado com sucesso!', extra_tags='deleted')
    return redirect('list_contracts')


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
        messages.add_message(request, messages.SUCCESS, 'O Serviço ' + service.get_name() + ' foi atualizado com sucesso!', extra_tags='updated')
        return redirect('list_services')

    return render(request, 'services/update.html', {'form': form})


@login_required
def change_status(request, id):
    service = get_object_or_404(Service, pk=id)
    service.change_status(request)
    return redirect('list_services')


@login_required
def delete_service(request, id):
    service = get_object_or_404(Service, pk=id)
    service.delete()
    messages.add_message(request, messages.SUCCESS, 'O serviço '+service.name+' foi deletado com sucesso!', extra_tags='deleted')
    return redirect('list_services')
