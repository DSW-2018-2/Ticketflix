from django.contrib import admin

from .models import BankTicket, CreditCard

admin.site.register(BankTicket)
admin.site.register(CreditCard)
