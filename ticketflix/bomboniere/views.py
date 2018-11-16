
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Product


class ProductList(ListView):
    model = Product


class ProductView(DetailView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    fields = [
        'name',
        'description',
        'price',
        'quantity'
    ]
    success_url = reverse_lazy('bomboniere:product:product_list')


class ProductUpdate(UpdateView):
    model = Product
    fields = [
        'name',
        'description',
        'price',
        'quantity'
    ]
    success_url = reverse_lazy('bomboniere:product:product_list')


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('bomboniere:product:product_list')