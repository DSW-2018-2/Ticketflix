from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView
from django.views import defaults as default_views

from .views import *

urlpatterns = [
#    path(
#        '<slug:pk>', 
#        SessionDetailView.as_view(template_name="session/session-detail.html"),
#         name="session-datail"
#    ),
#    path(
#        '',
#        SessionListView.as_view(template_name="session/session-list.html"),
#        name="session-list"
#    ),
    path('', SessionList.as_view(template_name='session/session_list.html'), name='session_list'),
    path('view/<int:pk>', SessionView.as_view(template_name='session/session_view.html'), name='session_view'),
    path('new', SessionCreate.as_view(template_name='session/session_form.html'), name='session_new'),
    path('edit/<int:pk>', SessionUpdate.as_view(template_name='session/session_form.html'), name='session_edit'),
    path('delete/<int:pk>', SessionDelete.as_view(template_name='session/session_delete.html'), name='session_delete'),
]