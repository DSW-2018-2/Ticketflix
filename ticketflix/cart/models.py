from django.db import models
from ticketflix.ticket.models import Ticket


class Cart(models.Model):

    parcial_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    tickets = models.ManyToManyField(Ticket, on_delete=models.SET_NULL, null=True)

