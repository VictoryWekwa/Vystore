from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image_url = models.CharField(max_length=2083)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    discount = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        verbose_name_plural = 'discounts'

    def __str__(self):
        return str(self.product)
