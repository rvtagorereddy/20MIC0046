from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.CharField(max_length=100)
    rating = models.FloatField()
    discount = models.FloatField()
    product_id = models.CharField(max_length=100, unique=True)