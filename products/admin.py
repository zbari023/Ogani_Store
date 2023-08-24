from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','flag']
    list_filter = ['name', 'price']
    search_fields = ['name', 'price']

admin.site.register(Products, ProductAdmin)