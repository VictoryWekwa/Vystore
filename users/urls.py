""" This is the urls for the users app"""
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # adding django default auth
    path('', include('django.contrib.auth.urls')),
    # registration views
    path('register/', views.register, name='register'),

]
