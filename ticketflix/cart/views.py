from django.template import RequestContext
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import *
from ticketflix.ticket.models import Ticket
from ticketflix.session.models import Session
from .models import Cart


class SetTickets(FormView):

    form_class = SetTicketsForm

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        session_id = kwargs['pk_session']
        session = Session.objects.get(id=session_id)

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, session)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, session):
        """If the form is valid, redirect to the supplied URL."""
        
        half_tickets_quantity = form.cleaned_data.get('half_tickets_quantity')
        full_tickets_quantity = form.cleaned_data.get('full_tickets_quantity')

        tickets = []

        self.create_half_tickets(half_tickets_quantity, session, tickets)
        self.create_full_tickets(full_tickets_quantity, session, tickets)

        cart_id = self.create_cart(tickets)

        return HttpResponseRedirect(self.get_success_url(cart_id))

    def create_half_tickets(self, half_tickets, session, tickets):

        for i in range(1, half_tickets):
            ticket = Ticket.objects.create(ticket_type="Meia", session=session)
            ticket.save()
            tickets.append(ticket)


    def create_full_tickets(self, full_tickets, session, tickets):

        for i in range(1, full_tickets):
            ticket = Ticket.objects.create(ticket_type="Inteira", session=session)
            ticket.save()
            tickets.append(ticket)

    def create_cart(self, tickets):

        cart = Cart.objects.create()

        # TODO: terminar de criar carrinho, adicionar os objetos, e enviar o id      

    def get_success_url(self, tickets):
        """Return the URL to redirect to after processing a valid form."""
        
        self.success_url('cart:set_seats', kwargs={'tickets': tickets})

        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        return str(self.success_url)  # success_url may be lazy

# TODO: criar a url de setar assentos