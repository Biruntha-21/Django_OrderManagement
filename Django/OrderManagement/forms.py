#from django.forms import ModelForm
from django import forms
from .models import *

class Customer_Form(forms.ModelForm):

    class Meta:
        
        model = Customer
        fields = '__all__'

        widgets = {
            'customer_name' : forms.TextInput(attrs={'class':"form-control"}),
            'customer_since' : forms.DateInput(attrs={'class':"form-control"})
        }

class Orders_Form(forms.ModelForm):

    class Meta:

        model = Orders
        fields = ['customer_reference','product_reference','order_number','order_date','quantity']

        widgets = {
            #'customer_reference' : forms.TextInput(attrs={'class':"form-control"}),
            #'product_reference' : forms.TextInput(attrs={'class':"form-control"}),
            'order_number' : forms.NumberInput(attrs={'class':"form-control"}),
            'order_date' : forms.DateInput(attrs={'class':"form-control"}),
            'quantity' : forms.DateInput(attrs={'class':"form-control"})
        }