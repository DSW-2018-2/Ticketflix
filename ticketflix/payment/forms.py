from django.forms import Form, ChoiceField, RadioSelect

class PaymentSelectForm(Form):
    CHOICES=[('bankTicket','Boleto bancário'),
             ('creditCard','Cartão de crédito')]

    choice = ChoiceField(choices=CHOICES, widget=RadioSelect())