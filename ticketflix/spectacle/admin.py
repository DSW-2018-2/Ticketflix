from django.contrib import admin

from .models import Spectacle, Movie, Play, Show

admin.site.register(Spectacle)
admin.site.register(Movie)
admin.site.register(Play)
admin.site.register(Show)