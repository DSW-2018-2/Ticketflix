from django.shortcuts import render
from django.views.generic import DetailView
from .models import Establishment

# Create your views here.

class EstablishmentDetailView(DetailView):
    model = Establishment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

