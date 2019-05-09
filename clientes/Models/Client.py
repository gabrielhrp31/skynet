
from django.db import models
from clientes.Models.Address import Address
from django.utils.timezone import now


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30, default='')
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.OneToOneField(Address, models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_border_color(self):
        if self.status:
            return '#00a65a'
        return '#dd4b39'

    def change_status(self):
        self.status = not self.status
        self.save()

    def full_name(self):
        return self.first_name+' '+self.last_name

    def get_active_label(self):
        if self.status:
            return '<span class="label label-success">Ativo</span>'
        return '<span class="label label-danger">Inativo</span>'

    def get_status(self):
        if self.status:
            return 'Ativo'
        return 'Inativo'
