from django.db import models
from django.urls import reverse
from ticketflix.spectacle.models import Spectacle

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

    def __str__(self):
        return ('Session ' + str(self.id))

    class Meta:
        verbose_name = ("Sessão")
        verbose_name_plural = ("Sessões")
