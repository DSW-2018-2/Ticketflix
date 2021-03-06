from django.db import models
from django.core import validators
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class ProductComponent(models.Model):
    """
    Abstract class that represents class 'Component' in Composite Pattern.
    """

    name = models.CharField(
        verbose_name=_("Nome"),
        help_text=_("Nome"),
        max_length=50,
        blank=False
    )

    description = models.TextField(
        verbose_name=_("Descrição"),
        help_text=_("Descrição"),
        max_length=200,
        blank=True,
        null=True
    )

    price = models.FloatField(
        verbose_name=_("Preço"),
        help_text=_("Preço"),
        validators=[validators.MinValueValidator(0)],
        blank=False
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'id': self.id})

    class Meta:
        abstract = True


class Product(ProductComponent):
    """
    Class that represents a Leaf in Composite Pattern.
    """

    class Meta:
        verbose_name = _("Produto")
        verbose_name_plural = _("Produtos")


class Combo(ProductComponent):
    """
    Class that represents the Composite in Composite Pattern.
    """

    products = models.ManyToManyField(
        Product,
        verbose_name=_("Produtos"),
        help_text=_("Produtos do Combo")    
    )

    class Meta:
        verbose_name = _("Combo")
        verbose_name_plural = _("Combos")


class ComboProductQuantity(models.Model):

    combo = models.ForeignKey(
        Combo,
        related_name="Combo",
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        related_name="Produto",
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(
        verbose_name=_("Quantidade"),
        help_text=_("Quantidade de Produtos no Combo"),
        validators=[validators.MinValueValidator(0)],
        default=1
    )
