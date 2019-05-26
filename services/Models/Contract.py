from django.db import models

from clientes.models import Client
from services.Models.Service import Service


class Contract(models.Model):
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    description = models.TextField(default='')
    daily_hours = models.FloatField(default=0.0)
    extra_price = models.FloatField(default=0.0)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    
    def __str__(self):
        return 'Contrato de '+self.service.name

    def get_contract_title(self):
        return 'Contrato de '+self.service.name