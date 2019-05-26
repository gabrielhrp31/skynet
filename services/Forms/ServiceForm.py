from django.forms import ModelForm
from services.models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'price', 'employees_available', 'status']
        labels = {
            'name': 'Nome do Serviço',
            'price': 'Preço',
            'employees_available': 'Funcionários Disponiveis',
            'status': 'Status'
        }
