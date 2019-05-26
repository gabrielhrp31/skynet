from django.forms import ModelForm
from clientes.models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'occupation', 'age', 'salary', 'status']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'occupation': 'Profissão',
            'age': 'Idade',
            'salary': 'Salário',
            'status': 'Ativo',
        }
