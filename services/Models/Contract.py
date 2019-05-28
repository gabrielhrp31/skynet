from datetime import date, timedelta

from django.core.exceptions import ValidationError
from django.db import models

from clientes.models import Client
from services.Models.Service import Service


class Contract(models.Model):
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, limit_choices_to={'status': True})
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, limit_choices_to={'status': True})
    description = models.TextField(default='')
    daily_hours = models.FloatField(default=0.0)
    extra_price = models.FloatField(default=0.0)
    start_date = models.DateField(null=False, default=date.today())
    end_date = models.DateField(null=False, default=date.today())
    
    def __str__(self):
        return 'Contrato de '+self.service.name

    def clean(self):
        # run the base validation
        super(Contract, self).clean()

        # Don't allow dates older than now.
        if self.end_date.__lt__(self.start_date):
            raise ValidationError('A data de Inicio deve ser Maior que a de termino')

    def get_contract_title(self):
        return 'Contrato de '+self.service.name

    def get_duration(self):
        return self.end_date-self.start_date + timedelta(days=1)
