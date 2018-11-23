from django.shortcuts import render
from django.views.generic import CreateView, FormView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import PaymentSelectForm
from .models import PaymentStrategy, BankTicket, CreditCard


class PaymentSelectView(FormView):
    form_class = PaymentSelectForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form, request, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, request, **kwargs):
        if(form.cleaned_data.get('choice') == 'bankTicket'):
            success_url = reverse_lazy('payment:payment_detail')
        
        elif(form.cleaned_data.get('choice') == 'creditCard'):
            success_url = reverse_lazy('payment:payment_select')
        
        return HttpResponseRedirect(success_url)


class PaymentDetailView(DetailView):
    model = PaymentStrategy
    template_name = 'payment/detail.html'

    def get_object(self, queryset=None):
        payment = PaymentStrategy.objects.get(
            id=self.kwargs.get('id')
        )
        return payment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        payment = context['object']
        return context


class BankTicketCreateView(CreateView):
    model = BankTicket
    template_name = 'payment/bank_ticket_create.html'

    fields = [
        '_ownerName',
        '_cardNumber',
        '_securityCode',
        '_explireMonth',
        '_expireYear'
    ]

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form, request, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, request, **kwargs):
        return HttpResponseRedirect(self.get_success_url(kwargs['id']))

    def get_success_url(self, id_payment):
        success_url = reverse_lazy('payment:credit_card:detail', kwargs={'id': payment_id})

        return str(success_url)

class CreditCardCreateView(CreateView):
    model = CreditCard
    template_name = 'payment/bank_ticket_create.html'

    fields = [
        '_ownerName',
        '_ownerCpf',
    ]

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form, request, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, request, **kwargs):
        return HttpResponseRedirect(self.get_success_url(kwargs['id']))

    def get_success_url(self, id_payment):
        success_url = reverse_lazy('payment:credit_card:detail', kwargs={'id': payment_id})

        return str(success_url)