from django.db import models

# Create your models here.
class Session(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField( auto_now=False, auto_now_add=False)
    place = models.CharField( max_length=50)
    available_ticket_number = models.IntegerField()
    total_ticket_number = models.IntegerField()