from django.db import models
from ticketflix.session.models import Session
from django.core import validators
from django.urls import reverse
from django.utils.translation import gettext as _

class Ticket(models.Model):
    """
    Class that represents Ticket 
    """

    ticket_type = models.CharField(
        verbose_name=_("Tipo"),
        help_text=_("Tipo"),
        max_length=50,
        blank=False
    )

    seat = models.CharField(
        verbose_name=_("Assento"),
        help_text=_("Assento"),
        max_length=50,
        blank=False
    )

    price = models.FloatField(
        verbose_name=_("Preço"),
        help_text=_("Preço"),
        validators=[validators.MinValueValidator(0)],
        blank=False
    )

    session = models.OneToOneField(
        Session,
        verbose_name=_("Sessão"),
        help_text=_("Sessão do Ticket"),
        on_delete=models.CASCADE,
        blank=False
    )

    class Meta:
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")


    def __str__(self):
        return self.ticket_type

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'id': self.id})
