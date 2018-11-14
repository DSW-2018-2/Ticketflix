from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView
from django.views import defaults as default_views

from .views import *

product_urls = [
    path('', ProductList.as_view(template_name='bomboniere/product_list.html'), name='product_list'),
    path('view/<int:pk>', ProductView.as_view(template_name='bomboniere/product_view.html'), name='product_view'),
    path('new', ProductCreate.as_view(template_name='bomboniere/product_form.html'), name='product_new'),
    path('edit/<int:pk>', ProductUpdate.as_view(template_name='bomboniere/product_form.html'), name='product_edit'),
    path('delete/<int:pk>', ProductDelete.as_view(template_name='bomboniere/product_delete.html'), name='product_delete'),
]

urlpatterns = [
    path(
        "product/",
        include((product_urls, "product"), namespace="product")
    )
]