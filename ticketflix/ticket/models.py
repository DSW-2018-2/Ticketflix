from django.db import models

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

    class Meta:
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'id': self.id})
