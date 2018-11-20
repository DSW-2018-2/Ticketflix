from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Purchase


class PurchaseList(ListView):
    model = Purchase


class PurchaseView(DetailView):
    model = Purchase


class PurchaseCreate(CreateView):
    model = Purchase
    fields = [
        'total_price',
        'rate',
        'statusPayment',
        'customer',
        'cart'
    ]
    success_url = reverse_lazy('purchase:purchase_list')


class PurchaseUpdate(UpdateView):
    model = Purchase
    fields = [
        'total_price',
        'rate',
        'statusPayment',
        'customer',
        'cart'
    ]
    success_url = reverse_lazy('purchase:purchase_list')


class PurchaseDelete(DeleteView):
    model = Purchase
    success_url = reverse_lazy('purchase:purchase_list')
