from datetime import timedelta, datetime, timezone

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from clientes.models import Client
from skynet.forms import UpdateProfile


@login_required
def index(request):
    #Conta a quantidade de clientes cadastrados
    all = Client.objects.all()
    all = all.count()

    # Calcula a porcentagem de clientes cadastrados
    all_recents=Client.objects.filter(created_at__lte=datetime.now()-timedelta(30))
    all_recents = all_recents.count()
    if all_recents>0:
        all_recents=((all-all_recents)/all)*100

    # Pega a quantidade de clientes ativos e calcula a porcentagem em relação ao total
    list_actives = Client.objects.filter(status=True)
    list_actives = list_actives.count()
    if list_actives>0:
        actives = {'amount': list_actives, 'percentual': ((list_actives/all)*100)}
    else:
        actives = {'amount': 0, 'percentual': 0}

    # Pega a quantidade de clientes inativos e calcula a porcentagem em relação ao total
    list_inactives = Client.objects.filter(status=False)
    list_inactives = list_inactives.count()
    if list_inactives>0:
        inactives = {'amount': list_inactives, 'percentual': ((list_inactives/all)*100)}
    else:
        inactives = {'amount': 0, 'percentual': 0}
    return render(request, 'dashboard/views/index.html', {'all': all, 'all_recents': all_recents, 'actives': actives, 'inactives': inactives})


@login_required
def update_profile(request):
    form = UpdateProfile(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'dashboard/views/edit_profile.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'dashboard/views/profile.html')

