from django.db import models

class Krosovka(models.Model):
    SPORT = "SPORT"
    BAZM = "BAZM"
    PRODUCT_FILTER = [
        (SPORT, 'sport'),
        (BAZM, 'Bazm')
    ]

    brand = models.CharField(max_length=100)
    size = models.IntegerField(default=40)
    color = models.CharField(max_length=30)
    prise = models.IntegerField(default=40)
    turi = models.CharField(max_length=6, choices=PRODUCT_FILTER, default=SPORT)

    def __str__(self):
        return f"{self.brand} nomli Krosovka"

class Cars(models.Model):
    change = models.CharField(max_length=100)
    number = models.IntegerField(default=22)
  

    def __str__(self):
        return f"{self.number} number"

class products(models.Model):
    maxsulot_nomi = models.CharField(max_length=100)
    narxi = models.IntegerField(default=22)
  

    def __str__(self):
        return f"{self.narxi} summa"