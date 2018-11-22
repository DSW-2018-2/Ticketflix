from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView
from django.views import defaults as default_views

from .views import *

urlpatterns = [
    path('select', PaymentSelect.as_view(template_name='payment/payment_select.html'), name='payment_select'),
]
