from django.db import models

# Create your models here.
from django.db import models
from decimal import Decimal


class Product(models.Model):
    name = models.CharField("medicine name", max_length=200, blank=True, null=True)
    medicine_ID = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    supplier = models.CharField(max_length=200, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    quantity = models.DecimalField(max_digits=20, decimal_places=0, default=Decimal('0'))
    Date_in = models.CharField("Expired Date dd/mm/year ",max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Id:{0} Name:{1}'.format(self.id, self.name)
