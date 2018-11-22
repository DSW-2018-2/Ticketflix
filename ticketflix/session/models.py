from django.db import models
from django.urls import reverse
from django.core import validators
from django.utils.translation import ugettext_lazy as _

from ticketflix.spectacle.models import Spectacle
from ticketflix.room.models import Room

class Session(models.Model):

    date = models.DateField(
        auto_now=False,
        auto_now_add=False
    )

    time = models.TimeField(
        auto_now=False,
        auto_now_add=False
    )

    place = models.CharField(
        max_length=50
    )

    available_ticket_number = models.IntegerField()

    total_ticket_number = models.IntegerField()

    spectacle = models.ForeignKey(
        Spectacle,
        related_name='sessions',
        related_query_name='session',
        on_delete=models.CASCADE,
        null=True
    )

    price = models.FloatField(
        verbose_name=_("Preço"),
        help_text=_("Preço"),
        validators=[validators.MinValueValidator(0)],
        blank=False,
        default=0
    )

    room = models.ForeignKey(
        Room,
        related_name='sessions',
        related_query_name='sessions',
        on_delete=models.CASCADE,
        blank=False,
        default=None
    )

    def __str__(self):
        return ('Session ' + str(self.id))

    class Meta:
        verbose_name = ("Sessão")
        verbose_name_plural = ("Sessões")
