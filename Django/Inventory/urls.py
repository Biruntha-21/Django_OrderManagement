from django.urls import path
from .views import *

urlpatterns = [
    path('products/add/',ProductsAdd),
    path('products/', AllProducts),
    path('products/delete/<int:id>/', DeleteProducts, name='product_delete'),
    path('products/update/<int:id>/', ProductUpdate, name='product_update')
]