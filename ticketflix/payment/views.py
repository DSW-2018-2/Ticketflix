from django.shortcuts import render
from django.views.generic import CreateView, FormView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import PaymentSelectForm
from .models import PaymentStrategy, BankTicket, CreditCard
from ticketflix.purchase.models import Purchase


class PaymentSelectView(FormView):
    form_class = PaymentSelectForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        fk = kwargs['fk']
        purchase = Purchase.objects.get(id=fk)

        if form.is_valid():
            return self.form_valid(form, purchase)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, purchase):
        if(form.cleaned_data.get('choice') == 'bankTicket'):
            payment_instance = BankTicket.objects.create(purchase=purchase)
            payment_instance.save()
            success_url = reverse_lazy('payment:bank_ticket_create', kwargs={'id': payment_instance.id})
        
        elif(form.cleaned_data.get('choice') == 'creditCard'):
            payment_instance = CreditCard.objects.create(purchase=purchase)
            payment_instance.save()
            success_url = reverse_lazy('payment:credit_card_create', kwargs={'id': payment_instance.id})
        
        return HttpResponseRedirect(str(success_url))


class CreditCardCreateView(CreateView):
    model = CreditCard

    fields = [
        'ownerName',
        'cardNumber',
        'securityCode',
        'expireMonth',
        'expireYear'
    ]

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        payment_id = kwargs['id']

        if form.is_valid():
            return self.form_valid(form, payment_id)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, payment_id):

        payment = CreditCard.objects.get(id=payment_id)
        self.set_attributes(form, payment)

        return HttpResponseRedirect(self.get_success_url(payment_id))

    def set_attributes(self, form, payment):
        payment.ownerName = form.cleaned_data.get('ownerName')
        payment.cardNumber = form.cleaned_data.get('cardNumber')
        payment.securityCode = form.cleaned_data.get('securityCode')
        payment.expireMonth = form.cleaned_data.get('expireMonth')
        payment.expireYear = form.cleaned_data.get('expireYear')
        payment.save()


    def get_success_url(self, payment_id):
        success_url = reverse_lazy('payment:credit_card_detail', kwargs={'pk': payment_id})

        return str(success_url)

class BankTicketCreateView(CreateView):
    model = BankTicket

    fields = [
        'ownerName',
        'ownerCpf',
    ]

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        payment_id = kwargs['id']

        if form.is_valid():
            return self.form_valid(form, payment_id)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, payment_id):

        payment = BankTicket.objects.get(id=payment_id)
        self.set_attributes(form, payment)

        return HttpResponseRedirect(self.get_success_url(payment_id))

    def set_attributes(self, form, payment):
        payment.ownerName = form.cleaned_data.get('ownerName')
        payment.ownerCpf = form.cleaned_data.get('ownerCpf')
        payment.save()

    def get_success_url(self, payment_id):
        success_url = reverse_lazy('payment:bank_ticket_detail', kwargs={'pk': payment_id})

        return str(success_url)

class BankTicketDetail(DetailView):
    model = BankTicket

class CreditCardDetail(DetailView):
    model = CreditCard