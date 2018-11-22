from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView, ListView, DetailView

from .models import Purchase
from ticketflix.cart.models import Cart

class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase


class PurchaseView(LoginRequiredMixin, DetailView):
    model = Purchase

class FinalizePurchase(LoginRequiredMixin, RedirectView):
    url = "http://localhost:8000/" # Apagar essa linha quando a url do pagamento for setada

    def get(self, request, *args, **kwargs):
        
        cart = Cart.objects.get(id=kwargs['pk_cart'])

        purchase = Purchase.objects.create(customer=request.user, cart=cart)
        purchase.set_total_price()
        purchase.save()

        # Colocar aqui a url do pagamento (com a pk da compra)
        # self.url = reverse_lazy('payment:payment_url', kwargs={'pk_purchase': purchase.id})

        return super(FinalizePurchase, self).get(request, *args, **kwargs)