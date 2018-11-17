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

combo_urls = [
    path('', ComboList.as_view(template_name='bomboniere/combo_list.html'), name='combo_list'),
    path('view/<int:pk>', ComboView.as_view(template_name='bomboniere/combo_view.html'), name='combo_view'),
    path('new', ComboCreate.as_view(template_name='bomboniere/combo_form.html'), name='combo_new'),
    path('edit/<int:pk>', ComboUpdate.as_view(template_name='bomboniere/combo_form.html'), name='combo_edit'),
    path('delete/<int:pk>', ComboDelete.as_view(template_name='bomboniere/combo_delete.html'), name='combo_delete'),
]

urlpatterns = [
    path(
        "product/",
        include((product_urls, "product"), namespace="product")
    ),
    path(
        "combo/",
        include((combo_urls, "combo"), namespace="combo")
    )
]