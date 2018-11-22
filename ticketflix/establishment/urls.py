from django.urls import path

from .views import EstablishmentListView
from .views import EstablishmentDetailView
from .views import EstablishmentUpdateView
from .views import EstablishmentDeleteView
from .views import EstablishmentCreateView


urlpatterns = [
    path(
        '',
        EstablishmentListView.as_view(template_name='establishment/list.html'),
        name='establishment-list'
    ),
    path(
        '<int:id>/',
        EstablishmentDetailView.as_view(template_name='establishment/detail.html'),
        name='establishment-detail'
    ),
    path(
        'create/',
        EstablishmentCreateView.as_view(template_name='establishment/form.html'),
        name='establishment-create'
    ),
    path(
        '<int:id>/update/',
        EstablishmentUpdateView.as_view(template_name='establishment/form.html'),
        name='establishment-update'
    ),
    path(
        '<int:id>/delete/',
        EstablishmentDeleteView.as_view(template_name='establishment/delete.html'),
        name='establishment-delete'
    ),
]