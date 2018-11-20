from django.db import models
from django.utils.translation import gettext as _
from django.core import validators
from ticketflix.users.models import User
from ticketflix.cart.models import Cart

class Purchase(models.Model):
    total_price = models.FloatField(
        verbose_name=_("Preço Total"),
        help_text=_("Preço Total"),
        validators=[validators.MinValueValidator(0)],
        blank=False
    )

    rate = models.FloatField(
        verbose_name=_("Taxa"),
        help_text=_("Taxa"),
        blank=False
    )

    statusPayment = models.BooleanField(
        default=False
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT
    )

    def update_status_payment(self):
        self.statusPayment = True
        self.save()
