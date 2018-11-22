from django.shortcuts import render
from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import PaymentSelectForm
from .models import PaymentStrategy

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
            print('================ ESCOLHEU O BOLETO')
            success_url = reverse_lazy('payment:payment_select')
        
        elif(form.cleaned_data.get('choice') == 'creditCard'):
            print('================ ESCOLHEU O CARTÃO DE CRÉDITO')
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