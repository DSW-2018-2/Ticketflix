from django.conf import settings
from django.urls import include, path
from django.views import defaults as default_views

from .views import *

urlpatterns = [
    path(
        'select/<int:fk>', 
        PaymentSelectView.as_view(template_name='payment/payment_select.html'), 
        name='payment_select'
    ),
    path(
        "detail/<int:fk>/<int:id>",
        PaymentDetailView.as_view(template_name="payment/detail.html"),
        name="payment_detail"
    ),
    path(
        "bank_ticket/create/<int:id>",
        BankTicketCreateView.as_view(template_name="payment/bank_ticket_create.html"),
        name="bank_ticket_create"
    ),
    path(
        "credit_card/create/<int:id>",
        BankTicketCreateView.as_view(template_name="payment/credit_card_create.html"),
        name="credit_card_create"
    ),
]
