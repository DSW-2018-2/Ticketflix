from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView
from django.views import defaults as default_views

from .views import *

urlpatterns = [
    path('', TicketList.as_view(template_name='ticket/ticket_list.html'), name='ticket_list'),
    path('view/<int:pk>', TicketView.as_view(template_name='ticket/ticket_view.html'), name='ticket_view'),
    path('new', TicketCreate.as_view(template_name='ticket/ticket_form.html'), name='ticket_new'),
]