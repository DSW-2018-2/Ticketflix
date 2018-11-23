from django.urls import path
from .views import SpectacleCreateView, SpectacleDeleteView
from .views import SpectacleListView, SpectacleUpdateView
from .views import SpectacleDetailView
from .views import MovieCreateView, MovieDeleteView
from .views import MovieUpdateView
from .views import PlayCreateView, PlayDeleteView
from .views import PlayUpdateView
from .views import ShowCreateView, ShowDeleteView
from .views import ShowUpdateView


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
    path(
        "movie/<int:id>/update",
        MovieUpdateView.as_view(template_name="spectacle/movie_form.html"),
        name="movie-update"
    ),
    path(
        "movie/<int:id>/delete/",
        MovieDeleteView.as_view(template_name="spectacle/delete.html"),
        name="movie-delete"
    ),
    path(
        "play/create/",
        PlayCreateView.as_view(template_name="spectacle/play_form.html"),
        name="play-create"
    ),
    path(
        "play/<int:id>/update",
        PlayUpdateView.as_view(template_name="spectacle/play_form.html"),
        name="play-update"
    ),
    path(
        "play/<int:id>/delete/",
        PlayDeleteView.as_view(template_name="spectacle/delete.html"),
        name="play-delete"
    ),
    path(
        "show/create/",
        ShowCreateView.as_view(template_name="spectacle/show_form.html"),
        name="show-create"
    ),
    path(
        "show/<int:id>/update",
        ShowUpdateView.as_view(template_name="spectacle/show_form.html"),
        name="show-update"
    ),
    path(
        "show/<int:id>/delete/",
        ShowDeleteView.as_view(template_name="spectacle/delete.html"),
        name="show-delete"
    ),
]
