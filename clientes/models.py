from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_active_label(self):
        if self.status:
            return '<span class="label label-success">Ativo</span>'
        return '<span class="label label-danger">Inativo</span>'
