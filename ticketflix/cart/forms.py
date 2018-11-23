from django import forms
from django.core import validators

from django.core.exceptions import ValidationError

from ticketflix.bomboniere.models import Product, Combo
from ticketflix.room.models import *
from .models import Cart


class SetTicketsForm(forms.Form):

    half_tickets_quantity = forms.IntegerField(
        validators=[validators.MinValueValidator(0)],
        required=True,
        initial=0
    )

    full_tickets_quantity = forms.IntegerField(
        validators=[validators.MinValueValidator(0)],
        required=True,
        initial=0
    )
    
    def clean(self):
      data = self.cleaned_data
      half_tickets_quantity = data.get('half_tickets_quantity')
      full_tickets_quantity = data.get('full_tickets_quantity')
      quantity = half_tickets_quantity + full_tickets_quantity
      if quantity < 1:
        raise ValidationError('Escolha ao menos um ingresso')
      return data


class SetSeatsForm(forms.Form):

    def __init__(self, *args, **kwargs):

        initial = kwargs['initial']
        cart_id = initial.pop('pk_cart')

        super(SetSeatsForm, self).__init__(*args, **kwargs)

        self.fields['cart_pk'] = forms.IntegerField(widget=forms.HiddenInput(), initial=cart_id)
        self.fields['seats'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
                                                         choices=self.get_choices(cart_id),
                                                         required=False)

    def get_choices(self, cart_id):
        cart = Cart.objects.get(id=cart_id)

        ticket = cart.tickets.all()[0]
        session = ticket.session
        room = session.room
        seats = Seat.objects.filter(room=room, spare=True)

        choices = []

        for seat in seats.all():
            tup = (seat.id, seat.row + "-" + str(seat.number))
            choices.append(tup)

        return choices

    def clean(self):

        data = self.cleaned_data

        cart_id = data.get('cart_pk')
        cart = Cart.objects.get(id=cart_id)

        seats = data.get('seats')

        tickets_quantity = len(cart.tickets.all())

        if(len(seats) != tickets_quantity):
            data = data
            raise ValidationError("Você precisa escolher " + str(tickets_quantity) + " assentos.")

        return data


class SetBomboniereProductsForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(SetBomboniereProductsForm, self).__init__(*args, **kwargs)

        self.fields['products'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
                                                            choices=self.get_products_choices(),
                                                            required=False)

        self.fields['combos'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
                                                          choices=self.get_combos_choices(),
                                                          required=False)

    def get_products_choices(self):
        products_choices = []

        if Product.objects.all().exists():
            products = Product.objects.all()

            for product in products:
                tup = (product.id, product.name + "-" + product.description)
                products_choices.append(tup)

        return products_choices

    def get_combos_choices(self):
        combos_choices = []

        if Combo.objects.all().exists():
            combos = Combo.objects.all()

            for combo in combos:
                tup = (combo.id, combo.name + "-" + combo.description)
                combos_choices.append(tup)

        return combos_choices
