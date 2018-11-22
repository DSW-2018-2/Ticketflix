from django.db import models

from django.utils.translation import ugettext_lazy as _

# these are temporary class that must be exterminated when the real is implemented
class Customer(models.Model):
    def __init__(self):
        self.firstName = 'Valdir'
        self.lastName = 'das Couves'


class Purchase(models.Model):
    totalPrice = 42.00
    customer = Customer()


class PaymentStrategy(models.Model):
    class Meta:
        verbose_name = _('Pagamento')
        verbose_name_plural = _('Pagamentos')
        abstract = True

    purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT)


class BankTicket(PaymentStrategy):
    class Meta:
        verbose_name = _('Boleto Bancário')
        verbose_name_plural = _('Boletos Bancários')

    ownerName = models.CharField(
        verbose_name=_('Pagador do boleto'),
        help_text=_('Nome do pagador do boleto'),
        max_length=255,
        default = ''
    )

    ownerCpf = models.BigIntegerField(
        verbose_name=_('CPF do pagador'),
        help_text=_('CPF do pagador do boleto'),
        default = 00000000000
    )

    expirationDate = models.DateField(
        verbose_name=_('Data de vencimento'), 
        help_text=_('Data de vencimento do boleto'),
        auto_now=False,
        auto_now_add=False
    )


class CreditCard(PaymentStrategy):
    class Meta:
        verbose_name = _('Cartão de Crédito')
        verbose_name_plural = _('Cartões de Crédito')

    _ownerName = models.CharField(
        verbose_name=_('Pagador do boleto'),
        help_text=_('Nome do pagador do boleto'),
        max_length=255,
        default = ''
    )

    _cardNumber = models.CharField(
        verbose_name=_('Número do cartão'),
        help_text=_('Número do cartão de crédito'),
        max_length=16,
        default = ''
    )

    _securityCode = models.IntegerField(
        verbose_name=_('Código de segurança'),
        help_text=_('Código de segurança do cartão de crédito'),
        default = 000
    )

    _expireMonth = models.IntegerField(
        verbose_name=_('Mês de vencimento'),
        help_text=_('Mês de vencimento do cartão de crédito'),
        default = 00
    )

    _expireYear = models.IntegerField(
        verbose_name=_('Ano de vencimento'),
        help_text=_('Ano de vencimento do cartão de crédito'),
        default = 00
    )

    _installmentNumber = models.IntegerField(
        verbose_name=_('Parcelas'),
        help_text=_('Quantidade de parcelas do pagamento'),
        default = 1
    )