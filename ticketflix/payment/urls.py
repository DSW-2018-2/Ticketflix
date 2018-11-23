from django.conf import settings
from django.urls import include, path
from django.views import defaults as default_views

from .views import PaymentSelectView
from .views import BankTicketCreateView
from .views import CreditCardCreateView
from .views import BankTicketDetail
from .views import CreditCardDetail

urlpatterns = [
    path(
        'select/<int:fk>', 
        PaymentSelectView.as_view(template_name='payment/payment_select.html'), 
        name='payment_select'
    ),
    path(
        "bank_ticket/create/<int:id>",
        BankTicketCreateView.as_view(template_name="payment/bank_ticket_create.html"),
        name="bank_ticket_create"
    ),
    path(
        "credit_card/create/<int:id>",
        CreditCardCreateView.as_view(template_name="payment/credit_card_create.html"),
        name="credit_card_create"
    ),
    path(
        "bank_ticket/detail/<int:pk>",
        BankTicketDetail.as_view(template_name="payment/bank_ticket_detail.html"),
        name="bank_ticket_detail"
    ),
    path(
        "credit_card/detail/<int:pk>",
        CreditCardDetail.as_view(template_name="payment/credit_card_detail.html"),
        name="credit_card_detail"
    )
]
