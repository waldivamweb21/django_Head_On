from django.shortcuts import render
from .models import Product
from django.http import HttpResponse


#Views vai mostrar os model e apresentar na tela.

def products_list(request):
    products = Product.objects.all().order_by('created_at')
    return render(request, 'products/products_list.html', {'products':products})

def product_page(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, "products/product_page.html", {'product':product})






