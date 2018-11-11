from django.shortcuts import render
from django.views.generic import ListView
from .models import Spectacle, Movie, Play, Show


class SpectacleListView(ListView):
	model = Spectacle 
	paginate_by = 10 

	def get_context_data(self, **kwargs):
		context = super(SpectacleListView, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk') 
		return context

	
