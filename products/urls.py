from django.urls import path
from .view import ProductList



urlpatterns = [
    path('', ProductList.as_view(),name='product_list'),
]