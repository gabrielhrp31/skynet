from django.forms import ModelForm
from django.contrib.auth.models import User


class UpdateProfile(ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = (
            {
                'first_name': 'Nome',
                'last_name': 'Sobrenome'
            }
        )
