from django import forms

from .models import Product

class ProductSelectForm(forms.Form):

    def get_options():
        objects = Product.objects.all()
        objects_list = []

        for obj in objects:
            tup = (obj.id, obj.name)
            objects_list.append(tup)

        return objects_list

    OPTIONS = get_options()
    products = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=OPTIONS)