from django.db import models
from django.utils.translation import gettext as _
from django.core import validators
from django.urls import reverse

from ticketflix.ticket.models import Ticket

class Cart(models.Model):

    parcial_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    tickets = models.ManyToManyField(
        Ticket,
        verbose_name=_("Ticket"),
        help_text=_("Tickets do Carrinho")   
    )

    class Meta:
        verbose_name = _("Carrinho")
        verbose_name_plural = _("Carrinhos")


    def get_absolute_url(self):
        return reverse('cart-detail', kwargs={'id': self.id})

