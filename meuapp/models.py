from django.db import models

class Carro(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    
    