from django.contrib import admin

from .models import Product

# Registrar os models no admin.

admin.site.register(Product) 
