from django.db import models
from django.urls import reverse

# Create your models here.
class Establishment(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    addressComplement = models.CharField(max_length=40)
    cep = models.CharField(max_length=8)
    city = models.CharField(max_length=40)
    phoneNumber = models.CharField(max_length=14)

    def get_absolute_url(self):
        return reverse("establishment-detail", args=[str(self.id)])
    