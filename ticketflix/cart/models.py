from django.db import models
from django.utils.translation import gettext as _
from django.core import validators
from django.urls import reverse

from ticketflix.ticket.models import Ticket
from ticketflix.bomboniere.models import Product, Combo

class Cart(models.Model):

    parcial_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    tickets = models.ManyToManyField(
        Ticket,
        verbose_name=_("Ticket"),
        help_text=_("Tickets do Carrinho")   
    )

    products = models.ManyToManyField(
        Product,
        verbose_name=_("Produtos"),
        help_text=_("Produtos do Carrinho")   
    )

    combos = models.ManyToManyField(
        Combo,
        verbose_name=_("Combos"),
        help_text=_("Combos do Carrinho")   
    )


    class Meta:
        verbose_name = _("Carrinho")
        verbose_name_plural = _("Carrinhos")


    def get_absolute_url(self):
        return reverse('cart-detail', kwargs={'id': self.id})

    def update_parcial_price(self):
        parcial_price = 0

        for ticket in self.tickets.all():
            parcial_price += ticket.price

        for product in self.products.all():
            parcial_price += product.price
            
        for combo in self.combos.all():
            parcial_price += combo.price

        self.parcial_price = parcial_price
        self.save()

    # def add_cart_items(self, item):
    #     if isinstance(item, Ticket):
    #         self.tickets.add(item)
    #     self.save()
    #     self.update_parcial_price()

    # def remove_cart_items(self, item):
    #     if isinstance(item, Ticket):
    #         self.tickets.remove(item)
    #     self.save()
    #     self.update_parcial_price()