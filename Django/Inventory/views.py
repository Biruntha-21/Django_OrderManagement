from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def ProductsAdd(request):
     context = {
          'product_form' : Product_Form()
     }
     if request.method == "POST":
          product_form = Product_Form(request.POST, request.FILES)
          if product_form.is_valid():
               product_form.save()
               return redirect('/inventory/products/')
     return render(request, "products_add.html", context)
     

@login_required(login_url='/')
def AllProducts(request):
      all_products = Product.objects.all()
      return render(request, 'products.html', {'all_products' : all_products})

@login_required(login_url='/')
def DeleteProducts(request, id):
     selected_product = Product.objects.get(id = id)
     selected_product.delete()
     return redirect('/inventory/products/')

@login_required(login_url='/')
def ProductUpdate(request, id):
     selected_product = Product.objects.get(id = id)
     context ={
          "product_form" : Product_Form(instance=selected_product)
     } 
     if request.method == 'POST':
          product_form = Product_Form(request.POST, instance=selected_product)
          if product_form.is_valid():
               product_form.save()
               return redirect('/inventory/products/')
     return render(request, "products_add.html", context)


