from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from .models import Spectacle, Movie, Play, Show
from django.urls import reverse_lazy


class SpectacleDetailView(DetailView):
    model = Spectacle
    template_name = 'spectacle/detail.html'

    def get_object(self, queryset=None):
        spectacle = Spectacle.objects.get(
            id=self.kwargs.get('id')
        )
        return spectacle


class SpectacleListView(ListView):
    model = Spectacle
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SpectacleCreateView(CreateView):
    model = Spectacle
    template_name = 'spectacle/form.html'
    fields = [
        'name',
        'spectacle_type',
        'status',
        'duration',
        'poster',
        'classification',
    ]

    def form_valid(self, form):
        return super().form_valid(form)

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list'
    )


class SpectacleDeleteView(DeleteView):
    model = Spectacle

    def get_object(self, queryset=None):
        spectacle = Spectacle.objects.get(
            id=self.kwargs.get('id')
        )
        return spectacle

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list',
    )


class SpectacleUpdateView(UpdateView):
    model = Spectacle
    template_name = 'spectacle/form.html'
    fields = [
        'name',
        'spectacle_type',
        'status',
        'duration',
        'poster',
        'classification',
    ]

    def get_object(self, queryset=None):
        spectacle = Spectacle.objects.get(
            id=self.kwargs.get('id')
        )
        return spectacle

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list'
    )

