from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=30, blank=False, default='')
    price = models.DecimalField(max_digits=20, decimal_places=1, blank=False)