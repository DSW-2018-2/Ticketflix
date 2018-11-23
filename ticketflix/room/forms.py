from django import forms
from django.core import validators

class AddSeatRowForm(forms.Form):

    row = forms.CharField(
        required=True,
        max_length=10
    )

    seats_quantity = forms.IntegerField(
        validators=[validators.MinValueValidator(0)],
        required=True,
        initial=0
    )