from django.shortcuts import render

from django.views.generic import DetailView
# Create your views here.

from .models import Session

class SessionDetailView(DetailView):
    model = Session

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
