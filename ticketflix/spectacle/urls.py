from django.urls import path
from .views import SpectacleCreateView, SpectacleDeleteView
from .views import SpectacleListView, SpectacleUpdateView
from .views import SpectacleDetailView
from .views import MovieCreateView


urlpatterns = [
    path(
        "",
        SpectacleListView.as_view(template_name="spectacle/list.html"),
        name="spectacle-list"
    ),
    path(
        "<int:id>/",
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
        "<int:id>/delete/",
        SpectacleDeleteView.as_view(template_name="spectacle/delete.html"),
        name="spectacle-delete"
    ),
    path(
        "movie/create/",
        MovieCreateView.as_view(template_name="spectacle/movie_form.html"),
        name="movie-create"
    ),
    # path(
    #     "<int:id>/movie/<int:id>/update"
    # ),
    # path(
    #     "<int:id>/movie/<int:id>/delete/"
    # ),
    # path(
    #     "<int:id>/play/create/"
    # ),
    # path(
    #     "<int:id>/play/<int:id>/update"
    # ),
    # path(
    #     "<int:id>/play/<int:id>/delete/"
    # ),
    # path(
    #     "<int:id>/show/create/"
    # ),
    # path(
    #     "<int:id>/show/<int:id>/update"
    # ),
    # path(
    #     "<int:id>/show/<int:id>/delete/"
    # ),
]
