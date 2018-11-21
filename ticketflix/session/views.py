from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Session


class SessionList(ListView):
    model = Session


class SessionView(DetailView):
    model = Session


class SessionCreate(CreateView):
    model = Session
    fields = [
        'place',
        'date',
        'time',
        'spectacle',
        'total_ticket_number',
        'available_ticket_number',
        'price'
    ]
    success_url = reverse_lazy('session:session_list')


class SessionUpdate(UpdateView):
    model = Session
    fields = [
        'place',
        'date',
        'time',
        'total_ticket_number',
        'available_ticket_number',
        'price'
    ]
    success_url = reverse_lazy('session:session_list')


class SessionDelete(DeleteView):
    model = Session
    success_url = reverse_lazy('session:session_list')
