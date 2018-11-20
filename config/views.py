from django.views.generic import ListView
from ticketflix.spectacle.models import Spectacle

class ScheduleView(ListView):
    model = Spectacle
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context