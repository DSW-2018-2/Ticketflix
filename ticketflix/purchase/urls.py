from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView
from django.views import defaults as default_views

from .views import *

urlpatterns = [
    path('', PurchaseList.as_view(template_name='purchase/purchase_list.html'), name='purchase_list'),
    path('view/<int:pk>', PurchaseView.as_view(template_name='purchase/purchase_view.html'), name='purchase_view'),
    path('finalize_purchase/<int:pk_cart>', FinalizePurchase.as_view(), name="finalize_purchase")

]