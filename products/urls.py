"""Defines the urls for products app.
"""
from django.contrib import admin
from . import views
from django.urls import path, include

app_name = 'products'
urlpatterns = [
    # Homepage
    path('', views.home, name='home'),
    # page that shows all products
    path('products/', views.index, name='index'),
    # detail page for a single product
    path('products/<int:product_id>/', views.product, name='product'),
    ]