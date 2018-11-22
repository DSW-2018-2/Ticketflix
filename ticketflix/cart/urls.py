from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView
from django.views import defaults as default_views

from .views import *

urlpatterns = [
    path("view/<int:pk>", CartView.as_view(template_name='cart/cart_view.html'), name='cart_view'),
    path("set_tickets/<int:pk_session>", SetTickets.as_view(template_name='cart/set_tickets.html'), name='set_tickets'),
    path("set_seats/<int:pk_cart>", SetSeats.as_view(template_name='cart/set_seats.html'), name='set_seats'),
    path("set_bomboniere_products/<int:pk_cart>", SetBomboniereProducts.as_view(template_name='cart/set_bomboniere_products.html'), name='set_bomboniere_products'),
]