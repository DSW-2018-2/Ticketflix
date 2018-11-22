from django.db import models
from django.urls import reverse
from django.core import validators
from django.utils.translation import ugettext_lazy as _


class Room(models.Model):

    name = models.CharField(
        verbose_name=_("Nome"),
        help_text=_("Nome da Sala"),
        null=False,
        max_length=10
    )

    spare = models.BooleanField(
        verbose_name=_("Livre"),
        help_text=_("Assento Livre"),
        default=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Sala")
        verbose_name_plural = ("Salas")

class Seat(models.Model):

    row = models.CharField(
        verbose_name=_("Fileira"),
        help_text=_("Fileira do Assento"),
        null=False,
        max_length=1
    )

    number = models.IntegerField(
        verbose_name=_("Número"),
        help_text=_("Número do Assento"),
        validators=[validators.MinValueValidator(0)],
        blank=False,
        default=0
    )

    room = models.ForeignKey(
        Room,
        related_name='seats',
        related_query_name='seats',
        on_delete=models.CASCADE,
        null=False
    )

    spare = models.BooleanField(
        verbose_name=_("Livre"),
        help_text=_("Assento Livre"),
        default=True
    )

    def __str__(self):
        return ('Seat ' + str(self.id))

    class Meta:
        verbose_name = ("Assento")
        verbose_name_plural = ("Assentos")
        ordering = ['row']