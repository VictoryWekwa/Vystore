from django.contrib import admin
from .models import Product, Discount


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('description', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'quantity')


admin.site.register(Product, ProductAdmin)
admin.site.register(Discount, DiscountAdmin)
