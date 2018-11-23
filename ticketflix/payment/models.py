from django.db import models

from django.utils.translation import ugettext_lazy as _

from ticketflix.purchase.models import Purchase

class PaymentStrategy(models.Model):
    class Meta:
        verbose_name = _('Pagamento')
        verbose_name_plural = _('Pagamentos')
        abstract = True

    CARTAODECREDITO = 'Cartão de Crédito'
    BOLETOBANCARIO = 'Boleto Bancário'
    NA = 'NA'

    PAYMENT_CHOICES = (
        (CARTAODECREDITO, CARTAODECREDITO),
        (BOLETOBANCARIO, BOLETOBANCARIO),
        (NA, 'N/A'),
    )

    AGUARDANDO = 'Aguardando'
    CONFIRMADO = 'Confirmado'
    CANCELADO = 'Cancelado'

    STATUS_CHOICES = (
        (AGUARDANDO, AGUARDANDO),
        (CONFIRMADO, CONFIRMADO),
        (CANCELADO, CANCELADO),
    )

    _purchase = models.ForeignKey(
        Purchase, 
        on_delete=models.PROTECT,
    )

    _payment_type = models.CharField(
        verbose_name=_('Tipo de Pagamento'),
        help_text=_('Tipo de Pagamento'),
        max_length=20,
        choices=PAYMENT_CHOICES,
        default=NA,
    )

    statusPayment = models.CharField(
        verbose_name=_('Status'),
        help_text=_('Status do Pagamento'),
        max_length=20,
        choices=STATUS_CHOICES,
        default=AGUARDANDO,
    )

    def notifyStatus(self):
        purchase_instance = Purchase.objects.get(id=self.purchase.id)
        purchase_instance.updateStatusPayment(self.status_payment)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if(self.statusPayment != AGUARDANDO):
            self.notifyStatus()

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('payment:payment_detail', kwargs={'id': self.id})

class BankTicket(PaymentStrategy):
    class Meta:
        verbose_name = _('Boleto Bancário')
        verbose_name_plural = _('Boletos Bancários')

    _ownerName = models.CharField(
        verbose_name=_('Pagador do boleto'),
        help_text=_('Nome do pagador do boleto'),
        max_length=255,
        default = ''
    )

    _ownerCpf = models.BigIntegerField(
        verbose_name=_('CPF do pagador'),
        help_text=_('CPF do pagador do boleto'),
        default = 00000000000
    )

    _expirationDate = models.DateField(
        verbose_name=_('Data de vencimento'), 
        help_text=_('Data de vencimento do boleto'),
        auto_now=False,
        auto_now_add=False
    )

    _payment_type = models.CharField(
        verbose_name=_('Tipo de Pagamento'),
        help_text=_('Tipo de Pagamento'),
        max_length=20,
        default=PaymentStrategy.BOLETOBANCARIO,
        editable=False,
    )

class CreditCard(PaymentStrategy):
    class Meta:
        verbose_name = _('Cartão de Crédito')
        verbose_name_plural = _('Cartões de Crédito')

    _ownerName = models.CharField(
        verbose_name=_('Nome no cartão'),
        help_text=_('Nome do dono do cartão'),
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

    _payment_type = models.CharField(
        verbose_name=_('Tipo de Pagamento'),
        help_text=_('Tipo de Pagamento'),
        max_length=20,
        default=PaymentStrategy.CARTAODECREDITO,
        editable=False,
    )
