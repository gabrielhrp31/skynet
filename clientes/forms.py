from django import forms
from django.forms import ModelForm
from .models import Client
from .models import Address


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'occupation', 'age', 'salary', 'status']
        labels ={
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'occupation': 'Profissão',
            'age': 'Idade',
            'salary': 'Salário',
            'status': 'Ativo',
        }


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'number', 'district', 'city', 'country']
        labels ={
            'street': 'Rua',
            'number': 'Número',
            'district': 'Distrito',
            'city': 'Cidade',
            'country': 'Estado',
        }

