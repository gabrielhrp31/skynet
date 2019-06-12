from datetime import datetime
from django import forms
from django.forms import ModelForm
from services.models import Contract


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = ['client','service', 'extra_price', 'description', 'daily_hours', 'start_date','end_date']
        labels = {
            'client': 'Contratante',
            'service': 'Serviço',
            'extra_price': 'Valor Extra',
            'description': 'Descrição',
            'daily_hours': 'Horas por Dia',
            'start_date': 'Data de Ínicio',
            'end_date': 'Data de Término',
        }
