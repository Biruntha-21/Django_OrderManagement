from django.urls import path
from .views import *

urlpatterns = [
    path('customers/', AllCustomer),
    path('customers/add/', CustomerAdd),
    path('customers/delete/<int:id>/', CustomerDelete, name='customer_delete'),
    path('customers/update/<int:id>/', CustomerUpdate, name='customer_update'),
    
    path('orders/', OrdersList),
    path('orders/add/', OrdersAdd),
    path('orders/delete/<int:id>/ ', OrdersDelete, name='order_delete'),
    path('orders/update/<int:id>/ ', OrdersUpdate, name='order_update')
]
