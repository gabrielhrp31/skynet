from django.contrib import messages
from django.db import models
from clientes.models import Client


class Service(models.Model):
    name = models.CharField(max_length=60)
    avg_time = models.FloatField(blank=True, default=0.0)
    price = models.FloatField(null=False, blank=False, default=0.0)
    employees_available = models.IntegerField(null=False, default=0)
    status = models.BooleanField(default=False)
    contracts = models.ManyToManyField(Client, through='Contract')

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def change_status(self, request):
        if self.contracts.count()==0:
            messages.add_message(request, messages.SUCCESS, 'O status do serviço ' + self.name + ' foi alterado!',
                             extra_tags='status')
            self.status = not self.status
        else:
            messages.add_message(request, messages.ERROR, 'O status do serviço ' + self.name + ' não foi alterado pois o mesmo possui '+str(self.contracts.count())+' contrato(s) ativo(s)!',
                             extra_tags='status')
        self.save()

    def get_active_label(self):
        if self.status:
            return '<span class="label label-success">Ativo</span>'
        return '<span class="label label-danger">Inativo</span>'
