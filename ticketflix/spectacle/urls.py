from django.urls import path
from .views import SpectacleCreateView, SpectacleDeleteView
from .views import SpectacleListView, SpectacleUpdateView
from .views import SpectacleDetailView


urlpatterns = [
    path(
        "",
        SpectacleListView.as_view(template_name="spectacle/list.html"),
        name="spectacle-list"
    ),
    path(
        "<int:id>",
        SpectacleDetailView.as_view(template_name="spectacle/detail.html"),
        name="spectacle-detail"
    ),
    path(
        "create/",
        SpectacleCreateView.as_view(template_name="spectacle/form.html"),
        name="spectacle-create"
    ),
    path(
        "<int:id>/update/",
        SpectacleUpdateView.as_view(template_name="spectacle/form.html"),
        name="spectacle-update"
    ),
    path(
        "<int:id>/delete",
        SpectacleDeleteView.as_view(template_name="spectacle/delete.html"),
        name="spectacle-delete"
    )
]
