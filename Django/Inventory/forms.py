#from django.forms import ModelForm
from django import forms
from .models import *

class Product_Form(forms.ModelForm):

    class Meta:

        model = Product
        fields = '__all__'

        widgets = {
            'product_name' : forms.TextInput(attrs={'class':"form-control"}),
            'product_code' : forms.TextInput(attrs={'class':"form-control"}),
            'price' : forms.NumberInput(attrs={'class':"form-control"}),
            'gst' : forms.NumberInput(attrs={'class':"form-control"}),
            
            
        }