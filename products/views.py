from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Product


def home(request):
    """The home page for products app ."""
    return render(request, 'products/home.html')


def index(request):
    products = Product.objects.order_by('date_added')
    return render(request, 'products/index.html', {'products': products})


@login_required
def product(request, product_id):
    """ The page for each product"""
    product = Product.objects.get(id=product_id)
    discount = product.discount_set.order_by('date_added')
    return render(request, 'products/product.html', {'product': product, 'discount': discount})

