from django import forms
from .models import Spectacle, Movie, Show, Play


class SpectacleForm(forms.ModelForm):
    class Meta:
        model = Spectacle
        fields = '__all__'

    def clean(self):
        # import ipdb; ipdb.set_trace()

        return False
