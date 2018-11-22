from django.conf import settings
from django.urls import include, path
from django.views import defaults as default_views

from .views import *

urlpatterns = [
    path(
        'select', 
        PaymentSelectView.as_view(template_name='payment/payment_select.html'), 
        name='payment_select'
    ),
    path(
        "<int:id>/",
        PaymentDetailView.as_view(template_name="payment/detail.html"),
        name="payment_detail"
    ),
]
