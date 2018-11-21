from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Ticket


class TicketList(ListView):
    model = Ticket


class TicketView(DetailView):
    model = Ticket


class TicketCreate(CreateView):
    model = Ticket
    fields = [
        'ticket_type',
        'seat',
        'price',
        'session',
    ]
    success_url = reverse_lazy('ticket:ticket_list')


class TicketUpdate(UpdateView):
    model = Ticket
    fields = [
        'ticket_type',
        'seat',
        'price',
        'session',
    ]
    success_url = reverse_lazy('ticket:ticket_list')


class TicketDelete(DeleteView):
    model = Ticket
    success_url = reverse_lazy('ticket:ticket_list')
