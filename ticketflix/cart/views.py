from django.template import RequestContext
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import *
from ticketflix.ticket.models import Ticket
from ticketflix.session.models import Session
from .models import Cart

class CartView(DetailView):
    model = Cart

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

        for i in range(1, half_tickets + 1):
            ticket = Ticket.objects.create(ticket_type="Meia", 
                                           session=session,
                                           price=(session.price)/2.0)
            ticket.save()
            tickets.append(ticket)


    def create_full_tickets(self, full_tickets, session, tickets):

        for i in range(1, full_tickets + 1):
            ticket = Ticket.objects.create(ticket_type="Inteira", 
                                           session=session, 
                                           price=session.price)
            ticket.save()
            tickets.append(ticket)

    def create_cart(self, tickets):
        cart = Cart.objects.create()
        cart.save()

        for ticket in tickets:
            cart.tickets.add(ticket)

        cart.update_parcial_price()
        cart.save()

        return cart.id

    def get_success_url(self, cart_id):
        """Return the URL to redirect to after processing a valid form."""
        
        self.success_url = reverse_lazy('cart:set_seats', kwargs={'pk_cart': cart_id})

        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        return str(self.success_url)  # success_url may be lazy


class SetSeats(FormView):

    form_class = SetSeatsForm

    def get_initial(self):
        initials = super(SetSeats, self).get_initial()
        initials['pk_cart'] = self.kwargs['pk_cart']
        return initials

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""

        cart = self.get_cart()
        tickets_quantity = len(cart.tickets.all())

        kwargs['tickets_quantity'] = tickets_quantity

        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super().get_context_data(**kwargs)

    def form_valid(self, form, **kwargs):

        seats = form.cleaned_data.get('seats')
        cart = self.get_cart()

        for ticket in cart.tickets.all():
            seat_id = seats.pop()
            ticket.seat = Seat.objects.get(id=seat_id)

        cart.save()

        return HttpResponseRedirect(self.get_success_url(cart.id))

    def get_cart(self):
        cart_id = self.kwargs.get('pk_cart')
        cart = Cart.objects.get(id=cart_id)

        return cart

    def get_success_url(self, cart_id):
        """Return the URL to redirect to after processing a valid form."""
        
        self.success_url = reverse_lazy('cart:set_bomboniere_products', kwargs={'pk_cart': cart_id})

        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        return str(self.success_url)  # success_url may be lazy


class SetBomboniereProducts(FormView):

    form_class = SetBomboniereProductsForm

    def form_valid(self, form, **kwargs):

        products = form.cleaned_data.get('products')
        combos = form.cleaned_data.get('combos')
        
        cart = self.get_cart()
        
        self.add_products(cart, products)
        self.add_combos(cart, combos)

        cart.update_parcial_price()
        cart.save()

        return HttpResponseRedirect(self.get_success_url(cart.id))

    def get_cart(self):
        cart_id = self.kwargs.get('pk_cart')
        cart = Cart.objects.get(id=cart_id)

        return cart

    def add_products(self, cart, products):
        self.reset_products(cart)

        for product_id in products:
            product = Product.objects.get(id=product_id)
            cart.products.add(product)
        
        cart.save()

    def reset_products(self, cart):

        for product in cart.products.all():
            cart.products.remove(product)
        
        cart.save()

    def add_combos(self, cart, combos):
        self.reset_combos(cart)
        
        for combo_id in combos:
            combo = Combo.objects.get(id=combo_id)
            cart.combos.add(combo)
        
        cart.save()

    def reset_combos(self, cart):
        for combo in cart.combos.all():
            cart.combos.remove(combo)
        
        cart.save()

    def get_success_url(self, cart_id):
        """Return the URL to redirect to after processing a valid form."""
        
        self.success_url = reverse_lazy('cart:cart_view', kwargs={'pk': cart_id})

        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        return str(self.success_url)  # success_url may be lazy
