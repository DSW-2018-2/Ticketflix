from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from .models import Establishment

# Create your views here.

class EstablishmentDetailView(DetailView):
    model = Establishment
    template_name = 'establishment/detail.html'

    def get_object(self, queryset=None):
        establishment = Establishment.objects.get(
            id=self.kwargs.get('id')
        )
        return establishment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EstablishmentListView(ListView):
    model = Establishment
    paginate_by = 100  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EstablishmentUpdateView(UpdateView):
    model = Establishment
    template_name = 'spectacle/form.html'
    fields = [
        'name', 
        'address', 
        'addressComplement', 
        'cep', 
        'city', 
        'phoneNumber'
    ]
    
    def get_object(self, queryset=None):
        establishment = Establishment.objects.get(
            id=self.kwargs.get('id')
        )
        return establishment

    success_url = reverse_lazy(
        viewname='establishment:establishment-list'
    )

class EstablishmentDeleteView(DeleteView):
    model = Establishment

    def get_object(self, queryset=None):
        establishment = Establishment.objects.get(
            id=self.kwargs.get('id')
        )
        return establishment

    success_url = reverse_lazy(
        viewname='establishment:establishment-list'
    )

class EstablishmentCreateView(CreateView):
    model = Establishment
    template_name = 'establishment/form.html'
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

    success_url = reverse_lazy(
        viewname='establishment:establishment-list'
    )




