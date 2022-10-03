from email.policy import default
from django.db import models

class Krosovka(models.Model):
    brand = models.CharField(max_length=100)
    size = models.IntegerField(default=40)
    color = models.CharField(max_length=30)
    prise = models.IntegerField(default=40)

    def __str__(self):
        return f"{self.brand} nomli Krosovka"

class Cars(models.Model):
    change = models.CharField(max_length=100)
    number = models.IntegerField(default=22)
  

    def __str__(self):
        return f"{self.number} number"