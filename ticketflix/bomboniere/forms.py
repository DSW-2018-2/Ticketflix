from django import forms

from .models import Product, Combo

class ProductSelectForm(forms.Form):

    def __init__(self, *args, **kwargs):
        
        initial = kwargs['initial']
        products_in_combo = self.get_products_in_combo(initial.pop('pk'))

        super(ProductSelectForm, self).__init__(*args, **kwargs)
        
        self.fields['combo_products'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'checked': True}),
                                                                  choices=self.get_selected_choices(products_in_combo),
                                                                  required=False)

        self.fields['products'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                            choices=self.get_choices(products_in_combo),
                                                            required=False)
    
    def get_products_in_combo(self, pk):
        
        combo = Combo.objects.get(pk=pk)
        
        return combo.products.all()
    

    def get_choices(self, products_in_combo):

        if Product.objects.exists():
            objects = Product.objects.all()
        else:
            return []
        
        objects_list = []

        for obj in objects:
            if obj not in products_in_combo:
                tup = (obj.id, obj.name)
                objects_list.append(tup)
    
        return objects_list

                                    
    def get_selected_choices(self, products_in_combo):

        objects_list = []

        for obj in products_in_combo:
            tup = (obj.id, obj.name)
            objects_list.append(tup)

        return objects_list

        
