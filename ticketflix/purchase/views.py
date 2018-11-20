from django.shortcuts import render
from django.http import HttpResponse

from .models import Purchase
from ticketflix.cart.models import Cart

# class PurchaseList(ListView):
#     model = Purchase


# class PurchaseView(DetailView):
#     model = Purchase


# class PurchaseCreate(CreateView):
#     model = Purchase
#     fields = [
#         'total_price',
#         'rate',
#         'statusPayment',
#         'customer',
#         'cart'
#     ]
#     success_url = reverse_lazy('purchase:purchase_list')


# class PurchaseUpdate(UpdateView):
#     model = Purchase
#     fields = [
#         'total_price',
#         'rate',
#         'statusPayment',
#         'customer',
#         'cart'
#     ]
#     success_url = reverse_lazy('purchase:purchase_list')


# class PurchaseDelete(DeleteView):
#     model = Purchase
#     success_url = reverse_lazy('purchase:purchase_list')
