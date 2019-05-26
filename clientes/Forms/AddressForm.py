from django.forms import ModelForm
from clientes.models import Address


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'number', 'district', 'city', 'country']
        labels = {
            'street': 'Rua',
            'number': 'Número',
            'district': 'Bairro',
            'city': 'Cidade',
            'country': 'Estado',
        }

