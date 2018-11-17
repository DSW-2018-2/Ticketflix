from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from .models import Spectacle, Movie, Play, Show


class SpectacleDetailView(DetailView):
    model = Spectacle
    template_name = 'spectacle/detail.html'

    def get_object(self, queryset=None):
        spectacle = Spectacle.objects.get(
            id=self.kwargs.get('id')
        )
        return spectacle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        spectacle = context['object']

        if spectacle.spectacle_type == 'FILME':
            objects = Movie.objects.get_related_object(spectacle)
        elif spectacle.spectacle_type == 'PECA':
            objects = Peca.objects.get_related_object(spectacle)
        elif spectacle.spectacle_type == 'SHOW':
            objects = Show.object.get_related_object(spectacle)
        else:
            objects = None 

        context['decorator'] = objects
        return context


class SpectacleListView(ListView):
    model = Spectacle
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SpectacleCreateView(CreateView):
    model = Spectacle
    template_name = 'spectacle/form.html'
    fields = '__all__'

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


class MovieCreateView(CreateView):
    model = Movie
    template_name = 'spectacle/movie_form.html'
    fields = [
        'synopsis',
        'diretor',
        'cast',
        'producer',
        'writer',
        'gender',
        'trailer',
        'spectacle',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        spectacles = Spectacle.objects.all()
        objects = []
        for spectacle in spectacles:
            related = Spectacle.objects.get_related_object(spectacle)
            if related is None:
                objects.append(spectacle)

        context['spectacles'] = objects
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list'
    )


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'spectacle/movie_form.html'
    fields = [
        'synopsis',
        'diretor',
        'cast',
        'producer',
        'writer',
        'gender',
        'trailer',
        'spectacle',
    ]

    def get_object(self, queryset=None):
        spectacle = Movie.objects.get(
            id=self.kwargs.get('id')
        )
        return spectacle

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list'
    )


class MovieDeleteView(DeleteView):
    model = Movie

    def get_object(self, queryset=None):
        spectacle = Movie.objects.get(
            id=self.kwargs.get('id')
        )
        return spectacle

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list',
    )


class PlayCreateView(CreateView):
    model = Play
    template_name = 'spectacle/play_form.html'
    fields = [
        'spectacle',
        'synopsis',
        'diretor',
        'cast',
        'writer',
        'producer',
        'gender',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        spectacles = Spectacle.objects.all()
        objects = []
        for spectacle in spectacles:
            related = Spectacle.objects.get_related_object(spectacle)
            if related is None:
                objects.append(spectacle)

        context['spectacles'] = objects
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list'
    )


class PlayUpdateView(UpdateView):
    model = Play
    template_name = 'spectacle/play_form.html'
    fields = [
        'spectacle',
        'synopsis',
        'diretor',
        'cast',
        'writer',
        'producer',
        'gender',
    ]

    def get_object(self, queryset=None):
        spectacle = Play.objects.get(
            id=self.kwargs.get('id')
        )
        return spectacle

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list',
    )


class PlayDeleteView(DeleteView):
    model = Play

    def get_object(self, queryset=None):
        spectacle = Play.objects.get(
            id=self.kwargs.get('id')
        )
        return spectacle

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list',
    )


class ShowCreateView(CreateView):
    model = Show
    template_name = 'spectacle/play_form.html'
    fields = [
        'spectacle',
        'band',
        'tour',
        'description',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        spectacles = Spectacle.objects.all()
        objects = []
        for spectacle in spectacles:
            related = Spectacle.objects.get_related_object(spectacle)
            if related is None:
                objects.append(spectacle)

        context['spectacles'] = objects
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list'
    )


class ShowUpdateView(UpdateView):
    model = Show
    template_name = 'spectacle/play_form.html'
    fields = [
        'spectacle',
        'band',
        'tour',
        'description',
    ]

    def get_object(self, queryset=None):
        spectacle = Show.objects.get(
            id=self.kwargs.get('id')
        )
        return spectacle

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list',
    )


class ShowDeleteView(DeleteView):
    model = Show

    def get_object(self, queryset=None):
        spectacle = Show.objects.get(
            id=self.kwargs.get('id')
        )
        return spectacle

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list',
    )
