from django import forms
from django.core import validators

class SetTicketsForm(forms.Form):

    half_tickets_quantity = forms.IntegerField(
        validators=[validators.MinValueValidator(0)],
        required=True,
        initial=0
    )

    full_tickets_quantity = forms.IntegerField(
        validators=[validators.MinValueValidator(0)],
        required=True,
        initial=0
    )