from django.shortcuts import render
from django.views import generic
from .models import Products
# Create your views here.


class ProductList(generic.ListView):
    model = Products
