from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.products_list, name="list"), #acessar: products:List
    path('<slug:slug>', views.product_page, name="page") #acessar: products:Page

]
