from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from ticketflix.establishments.views import EstablishmentDetailView
from ticketflix.establishments.views import EstablishmentsListView
from ticketflix.establishments.views import EstablishmentUpdateView
from ticketflix.establishments.views import EstablishmentDeleteView

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include("ticketflix.users.urls", namespace="users"),
    ),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path('establishments/<slug:pk>', EstablishmentDetailView.as_view(template_name="establishment/establishment-detail.html"), name='establishment-detail'),
    path('establishments/', EstablishmentsListView.as_view(template_name="establishment/establishment_list.html"),name='establishment-list'),
    path('establishments/<slug:pk>/update', EstablishmentUpdateView.as_view(template_name="establishment/establishment_update.html"),name='establishment-update'),
    path('establishments/<slug:pk>/delete',EstablishmentDeleteView.as_view(template_name="establishment/establishment_delete.html"),name='establishment-delete')
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
