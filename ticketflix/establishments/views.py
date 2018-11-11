from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Establishment

# Create your views here.

class EstablishmentDetailView(DetailView):
    model = Establishment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EstablishmentsListView(ListView):
    model = Establishment
    
    paginate_by = 100  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EstablishmentUpdateView(UpdateView):
    model = Establishment

    fields = ['name', 'address', 'addressComplement', 'cep', 'city', 'phoneNumber']
    template_name_suffix = '_update_form'

class EstablishmentDeleteView(DeleteView):
    model = Establishment

    success_url = reverse_lazy('establishment-list')




