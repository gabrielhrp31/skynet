from datetime import timedelta, datetime, timezone

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from clientes.models import Client


@login_required
def index(request):
    #Conta a quantidade de clientes cadastrados
    all = Client.objects.all()
    all = all.count()

    # Calcula a porcentagem de clientes cadastrados
    all_recents=Client.objects.filter(created_at__lte=datetime.now(tz=timezone.utc)-timedelta(30))
    all_recents = all_recents.count()
    all_recents=((all-all_recents)/all)*100

    # Pega a quantidade de clientes ativos e calcula a porcentagem em relação ao total
    list_actives = Client.objects.filter(status=True)
    list_actives = list_actives.count()
    actives = {'amount': list_actives, 'percentual': ((list_actives/all)*100)}

    # Pega a quantidade de clientes inativos e calcula a porcentagem em relação ao total
    list_inactives = Client.objects.filter(status=False)
    list_inactives = list_inactives.count()
    inactives = {'amount': list_inactives, 'percentual': ((list_inactives/all)*100)}
    return render(request, 'dashboard/index.html', {'all': all, 'all_recents': all_recents, 'actives': actives, 'inactives': inactives})
