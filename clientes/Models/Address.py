from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=60)
    district = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=2)
    number = models.IntegerField()

    def __str__(self):
        return self.street + ' ' + self.district

    def get_address(self):
        return self.street+', '+str(self.number)+', '+self.district+' - '+self.city+'/'+self.country